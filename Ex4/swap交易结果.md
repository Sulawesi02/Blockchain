Alice swap tx (BTC) created successfully!
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "179aeec771a9c6bfd8833a7508fc17a3960970f2289fda5d4682619419042d2f",
    "addresses": [
      "mzHSnW6dKgKkWnefjuDRSKgu7aHR8UecyZ"
    ],
    "total": 9,
    "fees": 1191,
    "size": 298,
    "vsize": 298,
    "preference": "low",
    "relayed_by": "60.29.153.4",
    "received": "2024-11-11T11:42:21.766441799Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "52e4e8d41d0e64e129e1537973846241047d1422cbcf63b3ef56d57b77d136b0",
        "output_index": 0,
        "script": "4830450221009ee63665e6bad84e4f04a1156109e657ae2a44c95c67e60c4aac909b8db5b78202207798d9bf3cc48b3f31aa233e7df9b5349fbb398caa56b90abed9799597d802da0121026181bc2be94b6a2f630db348557782028813b8df99b8430aede7687380f66df6",
        "output_value": 1200,
        "sequence": 4294967295,
        "addresses": [
          "mzHSnW6dKgKkWnefjuDRSKgu7aHR8UecyZ"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 0
      }
    ],
    "outputs": [
      {
        "value": 9,
        "script": "63a914853b775079232503df966e626618e1d388a957208821023131a4b61b38561e25e7dc66beb3c93383a6a638148fadbd79ba6fa97a1b9528ac6721023131a4b61b38561e25e7dc66beb3c93383a6a638148fadbd79ba6fa97a1b9528ad21026181bc2be94b6a2f630db348557782028813b8df99b8430aede7687380f66df6ac68",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
}
Bob swap tx (BCY) created successfully!
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "b3a83f825b1cdf3ef3f8d55a231e39cd2d094a2a1246c4453ed6bb04577df8a2",
    "addresses": [
      "CAFQph1mS4h2ciwcPgEVMt8vqcSNxiYffg"
    ],
    "total": 999999,
    "fees": 1,
    "size": 297,
    "vsize": 297,
    "preference": "low",
    "relayed_by": "60.29.153.4",
    "received": "2024-11-11T11:42:22.746608417Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "72364f5f7a5cf83c118a1ccc9ff97548c33e36b1908fbbe01b023734de2277e7",
        "output_index": 0,
        "script": "47304402201541ea1a879c188e77506101191e273b0f45bc86387887e36e32761c5a32102e02206c30102d71170bcf872a2799866c5de914abb351d2a8a8f66b75dd228ee8786d012103a84808b962faf7aad486688f99f8adf6862d41f038e1e219a6955461f2b61e21",
        "output_value": 1000000,
        "sequence": 4294967295,
        "addresses": [
          "CAFQph1mS4h2ciwcPgEVMt8vqcSNxiYffg"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 1586093
      }
    ],
    "outputs": [
      {
        "value": 999999,
        "script": "63a914853b775079232503df966e626618e1d388a957208821031d60feee079e6f210cd10f2163b13174fab56bd68e0a4e8f13c50800463a105cac6721031d60feee079e6f210cd10f2163b13174fab56bd68e0a4e8f13c50800463a105cad2103a84808b962faf7aad486688f99f8adf6862d41f038e1e219a6955461f2b61e21ac68",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
}
Sleeping for 20 minutes to let transactions confirm...
Alice redeem from swap tx (BCY) created successfully!
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "9f543ec3f2fec8e710931be0be7cd2b9be706dd62dad7e27ee5669c23e5dfaed",
    "addresses": [
      "C8PNMBEqQ5GgoF2kEgeubZk4z4ogqo35V7"
    ],
    "total": 999998,
    "fees": 1,
    "size": 184,
    "vsize": 184,
    "preference": "low",
    "relayed_by": "60.29.153.4",
    "received": "2024-11-11T12:02:24.150709263Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "b3a83f825b1cdf3ef3f8d55a231e39cd2d094a2a1246c4453ed6bb04577df8a2",
        "output_index": 0,
        "script": "483045022100c8d6d7e92273b67ebb227ba933c9aceb77c61c729d526e3c27af5b5de1f5196c022033ca875e9377f151f8db060bde5026f2586014af26483cf83e00acd67574fcfe01187468697349734153656372657450617373776f726431323351",
        "output_value": 999999,
        "sequence": 4294967295,
        "script_type": "unknown",
        "age": 1586106
      }
    ],
    "outputs": [
      {
        "value": 999998,
        "script": "76a914a7641a1cc269ab7dd7f61999e43d0d62639d870488ac",
        "addresses": [
          "C8PNMBEqQ5GgoF2kEgeubZk4z4ogqo35V7"
        ],
        "script_type": "pay-to-pubkey-hash"
      }
    ]
  }
}
Bob redeem from swap tx (BTC) created successfully!
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "1e960f3fbe164a6d14fa4f8cd701e6c87dbaec8ec6786df26e743afb78960c2d",
    "addresses": [
      "moZ7a2TCTTE62ZBwYfpWSYfga6KXc5D33G"
    ],
    "total": 8,
    "fees": 1,
    "size": 184,
    "vsize": 184,
    "preference": "low",
    "relayed_by": "221.238.245.27",
    "received": "2024-11-11T12:02:25.555559332Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "179aeec771a9c6bfd8833a7508fc17a3960970f2289fda5d4682619419042d2f",
        "output_index": 0,
        "script": "483045022100ebf4b2b1d1c7fedfb98b70b06fdf406a6ce2d66cf5e371992e81fc3b1e99e1060220141a2d8cbe10402cd2ee030a5bee462f17aedf2108cc8fa5088ed4f4fe9c4a0701187468697349734153656372657450617373776f726431323351",
        "output_value": 9,
        "sequence": 4294967295,
        "script_type": "unknown",
        "age": 0
      }
    ],
    "outputs": [
      {
        "value": 8,
        "script": "76a914582994b51384839fc0f061bd5d096ec291c8f5bd88ac",
        "addresses": [
          "moZ7a2TCTTE62ZBwYfpWSYfga6KXc5D33G"
        ],
        "script_type": "pay-to-pubkey-hash"
      }
    ]
  }
}