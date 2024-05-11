#!/bin/bash
sudo apt update
sudo apt upgrade
sudo apt install -y python3-pip
pip3 install flask 
pip3 install boto3
pip3 install pymysql
git clone https://github.com/raviyadav1907/Assignment-AWS-NAGP.git
cd Assignment-AWS-NAGP
python3 app.py
