from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cPWj8567uEcuRE1Ac66EGhXHWM7gGjGa9pZvdQCZzxgw5fFmM7Lh')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cV1wuvFe4sEVhLJZB1qeniMGddURrKLt1Lc3XCH93EN7VFFycubT')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cUfuUESnzdpjEsUFDwRN637bepy8UQzibNjaBUjyxNjNJNk7ofHn')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

ex2a_txout_scriptPubKey = [
    my_public_key,
    OP_CHECKSIGVERIFY, # 弹出栈顶的两个元素（公钥和签名），检查是否匹配。如果匹配，继续执行；否则，脚本失败。
    OP_1,
    cust1_public_key,
    cust2_public_key,
    cust3_public_key,
    OP_3,
    OP_CHECKMULTISIG # 检查三个客户签名是否至少有一个与公钥签名匹配。如果匹配，消耗顶部的 3 和 3 个公钥消耗顶部的 `3` 和3个公钥（`cust3_public_key`, `cust2_public_key`, `cust1_public_key`）和 `1` 和 `cust1_sig` 和一个额外的 `0`；否则，脚本失败。
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000050
    txid_to_spend = (
        '387f1017c5f92552d1104c57a923bd932db5f03729aba5609394c2296ed5c6d0')
    utxo_index = 2
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
