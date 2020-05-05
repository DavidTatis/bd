#!/usr/bin/env bash

sudo apt-get update
sudo apt install python3-pip -y
sudo apt-get install libpq-dev python-dev -y
pip3 install flask
pip3 install psycopg2
export user="aiunwldnhkbunn"
export passwd="be170b23bc334c15599357ead52561d762890d7fd8acdc35e2d9c6051cff70d7"
export dbname="d2ueo0t924r3q"
export host="ec2-52-6-143-153.compute-1.amazonaws.com"
export port=5432
source ~/.bashrc
