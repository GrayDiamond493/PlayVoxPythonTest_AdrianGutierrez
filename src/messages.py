import os
import mysql.connector
import boto3

# Environment Variables
user = os.environ('PLAYVOX_USER')
password = os.environ('PLAYVOX_PASSWORD')
aws_key_id = os.environ('PLAYVOX_AWS_ACCESS_KEY_ID')
aws_secret = os.environ('PLAYVOX_AWS_SECRET_ACCESS_KEY')

# AWS SNS Client
client = boto3.client(
    "sns",
    aws_access_key_id=aws_key_id,
    aws_secret_access_key=aws_secret,
    region_name="us-east-1"
)

# MySQL Connection
cnx = mysql.connector.connect(user=user, password=password,
                              host='127.0.0.1',
                              database='users')

# Publish Message to AWS SNS


def send_message(message, number):
    client.publish(
        phone_number=number,
        message=message
    )

# Assemble Message from database user information


def build_message(user_subscription, user_profile):
    query = "select * from users where profile ="+user_profile
    cursor = cnx.cursor()
    cursor.execute(query)
    db_records = cursor.fetchall()

    for row in db_records:
        for number in row['phone_number']:
            send_message("Hey "+row['first_name']+" "+row['last_name'] + " we have some information about your "+user_subscription+" account, please go to " + row['service_link']
                         + " to get more details", number)

# Check membership class and build message accordingly


def check_subscription(user_info):
    user_subscription = user_info[0].split(' ')[1]
    user_profile = user_info[1]
    build_message(user_subscription, user_profile)

# Read text file with profile info


def read_file():
    file = open("src/profileDB_id.txt", "r")
    lines = file.readlines()
    for line in lines:
        user_info = line.split(";")
        check_subscription(user_info)
