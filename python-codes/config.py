import os
from dotenv import load_dotenv

PWD = "c:/Users/PANOPTICON/Desktop/job-work/personal/solidity-python-course/python-codes"
load_dotenv(PWD + "/.env.rinkeby")

chain_id = int(os.getenv("CHAIN_ID"))
my_address = os.getenv("MY_ADDRESS")
my_pk = os.getenv("MY_PK")
rpc_provider = os.getenv("RPC_PROVIDER")
