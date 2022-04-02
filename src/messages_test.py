import os
#Simulation to check if my thinking is correct
#doesn't take user profile into account
def build_message(user_subscription,user_profile):

    #simulated records
    row1 = {
        'first_name':'Gray',
        'last_name':'Diamond',
        'phone_number':[1234567890, 4589032468, 5749037485],
        'service_link':'something.com',
        'user_profile':'1'
        }
    row2 = {
        'first_name':'Simon',
        'last_name':'Florez',
        'phone_number':[5783028954,  3222424580],
        'service_link':'something.net',
        'user_profile':'2'
        }
    row3 = {
        'first_name':'Adrian',
        'last_name':'Gutierrez',
        'phone_number':[3052260924],
        'service_link':'something.org',
        'user_profile':'3'
        }
    db_records=[row1,row2,row3]
    
    for row in db_records:
        if (row['user_profile']==user_profile):
            print('done')
            for number in row['phone_number']:
                #To show correctly built message. The rest depends on third-party libraries
                print("Hey "+row['first_name']+" "+row['last_name'] +" we have some information about your "+user_subscription+" account, please go to "+ row['service_link']
                            + " to get more details", number) 
                        

def check_subscription(user_info):
    user_subscription = user_info[0].split(' ')[1]
    user_profile = user_info[1].strip() #only for my particular test case
    build_message(user_subscription,user_profile)

def read_file():
    file = open("src/profileDB_id.txt", "r")
    lines = file.readlines()
 
    for line in lines:
        user_info = line.split(";")
        check_subscription(user_info)

if __name__ == "__main__":
    read_file()
