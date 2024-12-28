// Please paste your contract's solidity code here
// Note that writing a contract here WILL NOT deploy it and allow you to access it from your client
// You should write and develop your contract in Remix and then, before submitting, copy and paste it here
pragma solidity >=0.4.22 <0.6.0;

contract BlockchainSplitwise {
    // 债务结构，记录债务金额。最大债务为2^32 ~= 40亿。
    // 合约中会检查溢出。
    struct Debt {
        uint32 amount;
    }
    
    // 跟踪债务关系的映射。从债务人debtor到债权人creditor及其债务。
    // 例如，debts[Alice][Bob] = 10 表示Alice欠Bob 10。
    mapping(address => mapping(address => Debt)) internal all_debts;
    
    // 查询债务人欠债权人的总债务额。
    function lookup(address debtor, address creditor) public view returns (uint32 ret) {
        ret = all_debts[debtor][creditor].amount;
    }
    
    // 添加债务，记录msg.sender欠债权人更多金额。path 可能是从债权人到msg.sender的现有路径，表示通过添加此IOU将创建一个循环。
    // 'min_on_cycle' 是提议的循环中最小金额，将从所有债务中减去（包括正在添加的债务）。
    // 函数验证以下内容：
    // 如果给出路径，它确实存在并连接债权人和债务人。
    // 参数 min_on_cycle 是路径上的最小债务金额，用于清除循环中的债务。
    function add_IOU(address creditor, uint32 amount, address[] memory path, uint32 min_on_cycle) public {
        address debtor = msg.sender;
        // 不能是自己。
        require(debtor != creditor);
        // 金额必须为正数
        require(amount > 0);
        // 获取当前债务记录
        Debt storage iou = all_debts[debtor][creditor];
        
        // 检查溢出。
        if (min_on_cycle == 0) {
            iou.amount = add(iou.amount, amount);
            return;
        }
        require(min_on_cycle <= (iou.amount + amount));
        require(verify_and_fix_path(creditor, debtor, path, min_on_cycle));
        
        iou.amount = add(iou.amount, (amount - min_on_cycle));
    }
    
    // 验证并修复路径。如果路径部分固定，调用者负责撤销部分固定的路径。使用require()能够回滚交易。
    function verify_and_fix_path(address start, address end, address[] memory path, uint32 min_on_cycle) private returns (bool ret) {
        if (start != path[0] || end != path[path.length - 1]) {
            return false;
        }
        //防止路径过长高gas
        if (path.length > 12) {
            return false;
        }
        for (uint i = 1; i < path.length; i++) {
            Debt storage iou = all_debts[path[i - 1]][path[i]];
            if (iou.amount == 0 || iou.amount < min_on_cycle) {
                return false;
            } else {
                iou.amount -= min_on_cycle;
            }
        }
        return true;
    }
    
    // 带溢出检查的添加.
    function add(uint32 a, uint32 b) internal pure returns (uint32) {
        uint32 c = a + b;
        require(c >= a);
        return c;
    }
}