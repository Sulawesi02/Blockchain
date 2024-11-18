from bitcoin.core.script import *

######################################################################
# This function will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret 
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
# 
# TODO: Fill this in to create a script that is redeemable by both
#       of the above conditions.
# 
# See this page for opcode: https://en.bitcoin.it/wiki/Script
#
#

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [
        OP_IF, # 如果栈顶是"真"值（即接收方提供秘密x和签名）                       
            OP_HASH160, # 对栈顶元素进行哈希处理
            hash_of_secret, # 秘密 x 的哈希值
            OP_EQUALVERIFY, # 弹出栈顶的两个元素，比较它们是否相等。如果相等，继续执行；否则，脚本失败
            public_key_recipient, # 接收方的公钥（Bob 的公钥）
            OP_CHECKSIG, # 弹出栈顶的两个元素（公钥和签名），检查是否匹配。如果匹配，将 `True` 压入栈顶；否则，将 `False` 压入栈顶。
        OP_ELSE, # 如果栈顶是"假"值（即双方提供签名）                         
            public_key_recipient, # 接收方的公钥（Bob 的公钥）
            OP_CHECKSIGVERIFY, # 弹出栈顶的两个元素（公钥和签名），检查是否匹配。如果匹配，继续执行；否则，脚本失败。
            public_key_sender, # 发送方的公钥（Alice 的公钥）
            OP_CHECKSIG, # 弹出栈顶的两个元素（公钥和签名），检查是否匹配。如果匹配，将 `True` 压入栈顶；否则，将 `False` 压入栈顶。
        OP_ENDIF
    ]

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [
        sig_recipient, # 接收方的签名（Bob 的签名）
        secret, # 秘密 x
        OP_TRUE
    ]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [
        sig_sender, # 发送方的签名（Alice 的签名）
        sig_recipient, # 接收方的签名（Bob 的签名）
        OP_FALSE
    ]

#
#
######################################################################

