from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3
ex3a_txout_scriptPubKey = [
    OP_2DUP, # 复制栈顶的两个元素
    OP_ADD, # 将栈顶的两个元素相加
    2213, 
    OP_EQUALVERIFY, # 弹出栈顶的两个元素，比较它们是否相等。如果相等，继续执行；否则，脚本失败
    OP_SUB, # 计算栈顶的第二个元素减去栈顶的第一个元素
    409, 
    OP_EQUAL # 弹出栈顶的两个元素，比较它们是否相等。如果相等，将 `True` 压入栈顶；否则，将 `False` 压入栈顶
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000050
    txid_to_spend = (
        '387f1017c5f92552d1104c57a923bd932db5f03729aba5609394c2296ed5c6d0')
    utxo_index = 3
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex3a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
