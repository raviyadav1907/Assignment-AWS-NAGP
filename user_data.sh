#!/bin/bash
sudo apt update
sudo apt upgrade
sudo apt install -y python3-pip
pip3 install flask boto3 pymysql
git clone https://github.com/raviyadav1907/Assignment-AWS-NAGP.git
Assignment-AWS-NAGP
python3 app.py