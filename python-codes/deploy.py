from config import PWD
from solcx import compile_standard

import os
import json


if not os.path.isdir(PWD + "/artifacts"):
    os.mkdir(PWD + "/artifacts")

artifacts_dir = PWD + "/artifacts/"

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
