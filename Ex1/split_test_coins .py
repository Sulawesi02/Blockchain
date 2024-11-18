from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address)


def split_coins(amount_to_send, txid_to_spend, utxo_index, n):
    txin_scriptPubKey = my_address.to_scriptPubKey() # 前一笔交易输出的锁定脚本
    txin = create_txin(txid_to_spend, utxo_index) # 当前交易输入（引用前一笔交易的 UTXO）
    txout_scriptPubKey = my_address.to_scriptPubKey() # 当前交易输出的锁定脚本
    txout = create_txout(amount_to_send / n, txout_scriptPubKey) # 交易输出
    tx = CMutableTransaction([txin], [txout]*n) # 创建交易
    sighash = SignatureHash(txin_scriptPubKey, tx, # 计算签名哈希
                            0, SIGHASH_ALL)
    txin.scriptSig = CScript([my_private_key.sign(sighash) + bytes([SIGHASH_ALL]), # 当前交易输入的解锁脚本
                              my_public_key])
    VerifyScript(txin.scriptSig, txin_scriptPubKey, # 验证数字签名，证明是否有权花费该UTXO
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    response = broadcast_transaction(tx) # 通过网络广播
    print(response.status_code, response.reason)
    print(response.text)

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00001 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '58b551cdb6e3d6c08a9e707622fbc979806337909e1fc19c5e8b2d7c3e470799')
    utxo_index = 1
    n=10 # number of outputs to split the input into
    ######################################################################

    split_coins(amount_to_send, txid_to_spend, utxo_index, n)
