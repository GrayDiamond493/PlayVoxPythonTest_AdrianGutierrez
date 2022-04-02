import os #security
import mysql.connector
import boto3

'''
Environment variables created for security, so keys, passwords and other info 
are not visible from repo. As this is an academic exercise, all variables will
be set in a separate file so they can be seen.
'''
user=os.environ('PLAYVOX_USER')
password=os.environ('PLAYVOX_PASSWORD')
aws_key_id=os.environ('PLAYVOX_AWS_ACCESS_KEY_ID')
aws_secret=os.environ('PLAYVOX_AWS_SECRET_ACCESS_KEY')

client = boto3.client(
    "sns",
    aws_access_key_id=aws_key_id,
    aws_secret_access_key=aws_secret,
    region_name="us-east-1"
)

cnx = mysql.connector.connect(user=user, password=password,
                              host='127.0.0.1',
                              database='users')


def send_message(message, number):
    client.publish(
        phone_number=number, #variable name changed to snake for consistency
        message=message  #variable name changed to snake for consistency
    )

#functions func03 to func06 were replaced by 'build_message' to make it easier to understand what it does and save lines of code
'''
The previous implementation was highly redundant. It used 4 functions with the exact same code, differing only
in the user subscription level (Gold, Silver...), which was hardcoded as a String. To solve this, a new parameter
'user_subscription' was added in order to be sent within the message.
'''
def build_message(user_subscription,user_profile):
    query = "select * from users where profile ="+user_profile
    cursor = cnx.cursor()
    cursor.execute(query)
    db_records = cursor.fetchall() #To make iterations easier than they were
    
    for row in db_records: #only iterating through rows in the database, instead of columns
        #iterate through phone numbers in record
        for number in row['phone_number']:
            '''
            Since every individual phone number is already accounted for in the loop, it was
            considered redundant to make a new query and store it in a dictionary with only
            one key, since the only thing sent to the send_message function is a single value
            '''
            send_message("Hey "+row['first_name']+" "+row['last_name'] +" we have some information about your "+user_subscription+" account, please go to "+ row['service_link']
                    + " to get more details", number)
                        


#function func02 was renamed 'check_subscription' to make it easier to understand what it does
'''
The if statement was replaced by adding the user subscription as a parameter to be used
by a single function, in contrast with the previous 4 that did the exact same thing with
only the subscription (formerly hard-coded) as a difference.
'''
def check_subscription(user_info): #parameter 'x' was renamed 'user_info' to make it easier to understand what it does
    #variable 'y' was renamed 'user_subscription' to make it easier to understand what it does
    user_subscription = user_info[0].split(' ')[1]
    #variable 'user_profile' was created to favour readability
    user_profile = user_info[1]
    #func03 - 06 were replaced by 'build_message()'
    build_message(user_subscription,user_profile)

#function func01 was renamed 'read_file' to make it easier to understand what it does
def read_file():
    #variable 'f' was renamed 'file' to make it easier to understand what it does
    file = open("src/profileDB_id.txt", "r")#';' was removed due to it being inconsistent with the rest of the code's writting style
    lines = file.readlines() #initial was changed to lowercase for consistency

    #There were both iteration and tail recursion being implemented. Only the iteration was kept.
    '''
    Iteration was kept due to it being much faster and space efficient than recursion
    For this particular case, it's simple enough to be easily understood through iteratitions
    '''
    for line in lines:
        #variable 'x' was renamed to 'user_info' to make it easier to understand what it does
        user_info = line.split(";") # ';' was removed due to it being inconsistent with the rest of the code's writting style
        check_subscription(user_info)