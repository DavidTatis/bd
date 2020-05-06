#Databse configuration information
from os.path import join, dirname
from os import environ
dotenv_path = join(dirname(__file__), '.env')


pg_config = {
    'user' : environ.get("user"),
    'passwd' : environ.get("passwd"),
    'dbname' : environ.get("dbname"),
    'host':environ.get("host"),
    'port':environ.get("port")
}