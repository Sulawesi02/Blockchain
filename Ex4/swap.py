import time
import alice
import bob


#                                                                   
#              Written by: Max Spero                                 
#
# In this assignment we will implement a cross-chain atomic swap
# between two parties, Alice and Bob.
#
# Alice has bitcoin on BTC Testnet3 (the standard bitcoin testnet).
# Bob has bitcoin on BCY Testnet (Blockcypher's Bitcoin testnet).
# They want to trade ownership of their respective coins securely,
# something that can't be done with a simple transaction because
# they are on different blockchains.
#
# This method also works between other cryptocurrencies and altcoins,
# for example trading n Bitcoin for m Litecoin.
# 
# The idea here is to set up transactions around a secret x, that
# only one party (Alice) knows. In these transactions only H(x) 
# will be published, leaving x secret. 
# 
# Transactions will be set up in such a way that once x is revealed,
# both parties can redeem the coins sent by the other party.
#
# If x is never revealed, both parties will be able to retrieve their
# original coins safely, without help from the other.
#
#
#
######################################################################
#                           BTC Testnet3                             #     
######################################################################
#
# Alice ----> UTXO ----> Bob (with x)
#               |
#               |
#               V
#             Alice (after 48 hours)
#
######################################################################
#                            BCY Testnet                             #
######################################################################
#
#   Bob ----> UTXO ----> Alice (with x)
#               |
#               |
#               V
#              Bob (after 24 hours)
#
######################################################################

######################################################################
#
# Configured for your addresses
# 
# TODO: Fill in all of these fields
#

alice_txid_to_spend     = "52e4e8d41d0e64e129e1537973846241047d1422cbcf63b3ef56d57b77d136b0" 
alice_utxo_index        = 0
alice_amount_to_send    = 0.0000001

bob_txid_to_spend       = "72364f5f7a5cf83c118a1ccc9ff97548c33e36b1908fbbe01b023734de2277e7"
bob_utxo_index          = 0
bob_amount_to_send      = 0.01

# Get current block height (for locktime) in 'height' parameter for each blockchain (and put it into swap.py):
#  curl https://live.blockcypher.com/btc-testnet/
btc_test3_chain_height  = 3254861

#  curl https://live.blockcypher.com/bcy/
bcy_test_chain_height   = 1586104

# Parameter for how long Alice/Bob should have to wait before they can take back their coins
## alice_locktime MUST be > bob_locktime
alice_locktime = 5
bob_locktime = 3

tx_fee = 0.00000001

broadcast_transactions = True
alice_redeems = True

#
#
######################################################################


######################################################################
#
# Read the following function.
# 
# There's nothing to implement here, but it outlines the structure
# of how Alice and Bob will communicate to perform this cross-
# chain atomic swap.
#
# You will run swap.py to test your code.
#
######################################################################

def atomic_swap(broadcast_transactions=False, alice_redeems=True):
    # Alice选择一个秘密`x`，计算其哈希值
    hash_of_secret = alice.hash_of_secret()

    # Alice创建一个交易，Bob可以用x和签名赎回，或者Alice和Bob共同签名赎回
    alice_swap_tx, alice_swap_scriptPubKey = alice.alice_swap_tx(
        alice_txid_to_spend,
        alice_utxo_index,
        alice_amount_to_send - tx_fee,
    )

    # Alice创建一个时间锁定交易，以在一定时间后取回自己的比特币
    alice_return_coins_tx = alice.return_coins_tx(
        alice_amount_to_send - (2 * tx_fee), # 减去交易费用后，剩余要返还的比特币数量
        alice_swap_tx, # 上面创建的交换交易
        btc_test3_chain_height + alice_locktime,  # 设置锁定时间为当前区块高度 + Alice 的锁定时间
        alice_swap_scriptPubKey, # 上面创建的交换交易的锁定脚本
    )

    # Alice请求Bob签名她的时间锁定交易
    bob_signature_BTC = bob.sign_BTC(alice_return_coins_tx, alice_swap_scriptPubKey)

    # Alice 仅在 Bob 签署此交易后才广播她的第一笔交易
    if broadcast_transactions:
        alice.broadcast_BTC(alice_swap_tx)

    # 发生同样的情况，角色颠倒
    bob_swap_tx, bob_swap_scriptPubKey = bob.bob_swap_tx(
        bob_txid_to_spend,
        bob_utxo_index,
        bob_amount_to_send - tx_fee,
        hash_of_secret,
    )
    bob_return_coins_tx = bob.return_coins_tx(
        bob_amount_to_send - (2 * tx_fee),
        bob_swap_tx,
        bcy_test_chain_height + bob_locktime,
    )

    alice_signature_BCY = alice.sign_BCY(bob_return_coins_tx, bob_swap_scriptPubKey)

    if broadcast_transactions:
        bob.broadcast_BCY(bob_swap_tx)

    if broadcast_transactions:
        print('Sleeping for 20 minutes to let transactions confirm...')
        time.sleep(60 * 20)

    if alice_redeems:
        # Alice 赎回她的硬币，公开展示 x（它现在在区块链上）
        alice_redeem_tx, alice_secret_x = alice.redeem_swap(
            bob_amount_to_send - (2 * tx_fee),
            bob_swap_tx,
            bob_swap_scriptPubKey,
        )
        if broadcast_transactions:
            alice.broadcast_BCY(alice_redeem_tx)

        # 一旦 x 被揭开，Bob 也可以赎回他的硬币
        bob_redeem_tx = bob.redeem_swap(
            alice_amount_to_send - (2 * tx_fee),
            alice_swap_tx,
            alice_swap_scriptPubKey,
            alice_secret_x,
        )
        if broadcast_transactions:
            bob.broadcast_BTC(bob_redeem_tx)
    else:
        
        # Bob 和 Alice 可以在指定时间后取回他们原来的硬币
        completed_bob_return_tx = bob.complete_return_tx(
            bob_return_coins_tx,
            bob_swap_scriptPubKey,
            alice_signature_BCY,
        )
        completed_alice_return_tx = alice.complete_return_tx(
            alice_return_coins_tx,
            alice_swap_scriptPubKey,
            bob_signature_BTC,
        )
        if broadcast_transactions:
            print('Sleeping for bob_locktime blocks to pass locktime...')
            time.sleep(10 * 60 * bob_locktime)
            bob.broadcast_BCY(completed_bob_return_tx)

            print('Sleeping for alice_locktime blocks to pass locktime...')
            time.sleep(10 * 60 * max(alice_locktime - bob_locktime, 0))
            alice.broadcast_BTC(completed_alice_return_tx)

if __name__ == '__main__':
    atomic_swap(broadcast_transactions, alice_redeems)
