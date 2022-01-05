import os
import json

from config import PWD, chain_id, my_address, my_pk, rpc_port
from solcx import compile_standard
from web3 import Web3


if not os.path.isdir(PWD + "/artifacts-py"):
    os.mkdir(PWD + "/artifacts-py")

artifacts_dir = PWD + "/artifacts-py/"

simple_storage_path = PWD + "/contracts/storage/SimpleStorage.sol"

with open(simple_storage_path, "r") as file:
    simple_storage_file = file.read()


## compile solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.0",
)

with open(artifacts_dir + "simple_storage.json", "w") as file:
    json.dump(compiled_sol, file)


# get bytecode
byte_code = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# web3 provider setup ganache
w3 = Web3(Web3.HTTPProvider(f"http://127.0.0.1:{rpc_port}"))

# create contract
SimpleStorage = w3.eth.contract(abi=abi, bytecode=byte_code)

# get nonce from address transaction count
nonce = w3.eth.getTransactionCount(my_address)
gasPrice = 445051

## Build and deploy contract
# build transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce, "gasPrice": gasPrice}
)

# sign transaction
signed_tx = w3.eth.account.sign_transaction(transaction, private_key=my_pk)

# send transaction
