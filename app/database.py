import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
ORACLE_HOST = os.getenv("ORACLE_HOST")
ORACLE_PORT = int(os.getenv("ORACLE_PORT", "1521"))
ORACLE_SERVICE = os.getenv("ORACLE_SERVICE")


# def get_connection():
#     return oracledb.connect(
#         user=ORACLE_USER,
#         password=ORACLE_PASSWORD,
#         host=ORACLE_HOST,
#         port=ORACLE_PORT,
#         service_name=ORACLE_SERVICE
#     )

def get_connection():

    connection = oracledb.connect(
        user=ORACLE_USER,
        password=ORACLE_PASSWORD,
        host=ORACLE_HOST,
        port=ORACLE_PORT,
        service_name=ORACLE_SERVICE
    )

    print("Connected User:", connection.username)

    return connection