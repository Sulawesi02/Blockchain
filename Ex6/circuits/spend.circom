include "./mimc.circom";

/*
 * IfThenElse sets `out` to `true_value` if `condition` is 1 and `out` to
 * `false_value` if `condition` is 0.
 *
 * It enforces that `condition` is 0 or 1.
 *
 */
template IfThenElse() {
    signal input condition;
    signal input true_value;
    signal input false_value;
    signal output out;

    // TODO
    // Hint: You will need a helper signal...
    condition * (1 - condition) === 0;  //确保 condition 为 0 或 1

    if(condition == 1){
        out <== true_value;
    }else{
        out <== false_value;
    }
}

/*
 * SelectiveSwitch takes two data inputs (`in0`, `in1`) and produces two ouputs.
 * If the "select" (`s`) input is 1, then it inverts the order of the inputs
 * in the ouput. If `s` is 0, then it preserves the order.
 *
 * It enforces that `s` is 0 or 1.
 */
template SelectiveSwitch() {
    signal input in0;
    signal input in1;
    signal input s;
    signal output out0;
    signal output out1;

    s * (1 - s) === 0;  //确保 s 为0/1

    // TODO
    if(s == 1){
        out0 <== in1;
        out1 <== in0;
    }else{
        out0 <== in0;
        out1 <== in1;
    }
}

/*
 * Verifies the presence of H(`nullifier`, `nonce`) in the tree of depth
 * `depth`, summarized by `digest`.
 * This presence is witnessed by a Merle proof provided as
 * the additional inputs `sibling` and `direction`, 
 * which have the following meaning:
 *   sibling[i]: the sibling of the node on the path to this coin
 *               at the i'th level from the bottom.
 *   direction[i]: "0" or "1" indicating whether that sibling is on the left.
 *       The "sibling" hashes correspond directly to the siblings in the
 *       SparseMerkleTree path.
 *       The "direction" keys the boolean directions from the SparseMerkleTree
 *       path, casted to string-represented integers ("0" or "1").
 */
template Spend(depth) {
    
    signal input digest;
    signal input nullifier;
    signal private input nonce;
    signal private input sibling[depth];
    signal private input direction[depth];

    // TODO
    // 计算叶节点的哈希值
    component leafHasher = Mimc2();
    leafHasher.in0 <== nullifier;
    leafHasher.in1 <== nonce;
    
    component mimc[depth];// 计算路径的哈希值
    signal tmp[depth+1];// 存储路径的哈希值
    tmp[0] <== leafHasher.out;
    component selectiveSwitch[depth];// 选择路径的节点
    signal left[depth];// 存储路径的左节点
    signal right[depth];// 存储路径的右节点
    
    // 计算从叶节点到根节点的路径
    for(var i = 0; i < depth; i++) {
        selectiveSwitch[i] = SelectiveSwitch();
        selectiveSwitch[i].in0 <== tmp[i];
        selectiveSwitch[i].in1 <== sibling[i];
        selectiveSwitch[i].s <== direction[i];
        
        // 获取左右子节点
        left[i] <== selectiveSwitch[i].out0;
        right[i] <== selectiveSwitch[i].out1;
        
        // 计算父节点的哈希值
        mimc[i] = Mimc2();
        mimc[i].in0 <== left[i];
        mimc[i].in1 <== right[i];
        tmp[i+1] <== mimc[i].out;
    }
    
    // 验证计算出的根哈希值与输入的 digest 相等
    tmp[depth] === digest;
}

