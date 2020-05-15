#!/usr/bin/env bash

sudo apt-get update
sudo apt install python3-pip -y
sudo apt-get install libpq-dev python-dev -y
pip3 install flask
pip3 install psycopg2
