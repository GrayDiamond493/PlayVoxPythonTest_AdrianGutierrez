import mysql.connector
import boto3

client = boto3.client(
    "sns",
    aws_access_key_id="jhw76321ihdsjbd879213nkjnsd32",
    aws_secret_access_key="dkjhdsd0i324987ldkhfkjq7q61398u9",
    region_name="us-east-1"
)

dic = {}

cnx = mysql.connector.connect(user='admin', password='A3djbai$095ndpo#"2',
                              host='127.0.0.1',
                              database='users')


def sendMesagge(message, number):
    client.publish(
        PhoneNumber=number,
        Message=message
    )


def func03(user_profile):
    query = "select * from users where profile ="+user_profile
    cursor = cnx.cursor()
    cursor.execute(query)
    for (first_name, last_name, phone_numbers, service_link) in cursor:
        for number in phone_numbers:
            query2 = "select number from phone_number where phone_id="+number
            cursor.execute(query)
            dic['table'] = cursor.fetchall()
            sendMesagge("Hey "+first_name+" "+last_name + " we have some information about your platinum account, please go to " + service_link
                        + "to get more details", dic['table'][0])


def func04(user_profile):
    query = "select * from users where profile ="+user_profile
    cursor = cnx.cursor()
    cursor.execute(query)
    for (first_name, last_name, phone_numbers, service_link) in cursor:
        for number in phone_numbers:
            query2 = "select number from phone_number where phone_id="+number
            cursor.execute(query)
            dic['table'] = cursor.fetchall()
            sendMesagge("Hey "+first_name+" "+last_name + " we have some information about your gold account, please go to " + service_link
                        + "to get more details", dic['table'][0])


def func05(user_profile):
    query = "select * from users where profile ="+user_profile
    cursor = cnx.cursor()
    cursor.execute(query)
    for (first_name, last_name, phone_numbers, service_link) in cursor:
        for number in phone_numbers:
            query2 = "select number from phone_number where phone_id="+number
            cursor.execute(query)
            dic['table'] = cursor.fetchall()
            sendMesagge("Hey "+first_name+" "+last_name +" we have some information about your silver account, please go to "+ service_link
                        + "to get more details", dic['table'][0])


def func06(user_profile):
    query = "select * from users where profile ="+user_profile
    cursor = cnx.cursor()
    cursor.execute(query)
    for (first_name, last_name, phone_numbers, service_link) in cursor:
        for number in phone_numbers:
            query2 = "select number from phone_number where phone_id="+number
            cursor.execute(query)
            dic['table'] = cursor.fetchall()
            sendMesagge("Hey "+first_name+" "+last_name +" we have some information about your bronze account, please go to "+ service_link
                        + "to get more details", dic['table'][0])


def func02(x):
    y = x[0]
    if y == "user platinum":
        func03(x[1])
    elif y == "user gold":
        func04(x[1])
    elif y == "user silver":
        func05(x[1])
    elif y == "user bronze":
        func06(x[1])

def func01(line):
    x = line.split(";")
    func02(x)
    f = open("profileDB_id.txt", "r")
    Lines = f.readlines()

    for line in Lines:
        func01(line)
