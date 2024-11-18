from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address)

# 生成公钥
def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [
        OP_DUP, # 复制栈顶元素
        OP_HASH160, # 对栈顶元素进行哈希处理
        address, # 水龙头地址的哈希值入栈
        OP_EQUALVERIFY, # 弹出栈顶的两个元素，比较它们是否相等。如果相等，继续执行；否则，脚本失败。
        OP_CHECKSIG, # 弹出栈顶的两个元素（公钥和签名），检查是否匹配。如果匹配，将 `True` 压入栈顶；否则，将 `False` 压入栈顶。
    ]
    ######################################################################

# 生成签名
def P2PKH_scriptSig(txin, txout, txin_scriptPubKey):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction. You may need to use variables
    # that are globally defined.
    return [signature, my_public_key]
    ######################################################################

# 发送 P2PKH 交易
def send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index,txout_scriptPubKey):
    txout = create_txout(amount_to_send, txout_scriptPubKey) # 交易输出
    txin_scriptPubKey = P2PKH_scriptPubKey(my_address) # 前一笔交易输出的锁定脚本
    txin = create_txin(txid_to_spend, utxo_index) # 当前交易输入（引用前一笔交易的 UTXO）
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey) # 当前交易输入的解锁脚本
    # 在 `create_signed_transaction` 函数中，通过 `VerifyScript` 函数验证数字签名，证明我有权花费该UTXO
    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,txin_scriptSig)

    return broadcast_transaction(new_tx)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000099
    txid_to_spend = (
        '387f1017c5f92552d1104c57a923bd932db5f03729aba5609394c2296ed5c6d0')
    utxo_index = 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
