#Databse configuration information
from os.path import join, dirname
from os import environ
dotenv_path = join(dirname(__file__), '.env')


pg_config = {
    'user' : "aiunwldnhkbunn",
    'passwd' : "be170b23bc334c15599357ead52561d762890d7fd8acdc35e2d9c6051cff70d7",
    'dbname' : "d2ueo0t924r3q",
    'host':"ec2-52-6-143-153.compute-1.amazonaws.com",
    'port':5432
}