import os
from dotenv import load_dotenv

PWD = "c:/Users/PANOPTICON/Desktop/job-work/personal/solidity-python-course"
load_dotenv(PWD + "/.env")

chain_id = int(os.getenv("CHAIN_ID"))
my_address = os.getenv("MY_ADDRESS")
my_pk = os.getenv("MY_PK")
rpc_port = os.getenv("RPC_PORT")
