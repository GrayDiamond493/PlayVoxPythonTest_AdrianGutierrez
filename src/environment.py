import os

def check():
    print(os.environ['PLAYVOX_USER'])
    print(os.environ['PLAYVOX_PASSWORD'])
    print(os.environ['PLAYVOX_AWS_ACCESS_KEY_ID'])
    print(os.environ['PLAYVOX_AWS_SECRET_ACCESS_KEY'])


if __name__ == "__main__":
    os.environ['PLAYVOX_USER'] = 'admin'
    os.environ['PLAYVOX_PASSWORD'] = 'A3djbai$095ndpo#"2'
    os.environ['PLAYVOX_AWS_ACCESS_KEY_ID'] = 'jhw76321ihdsjbd879213nkjnsd32'
    os.environ['PLAYVOX_AWS_SECRET_ACCESS_KEY'] = 'dkjhdsd0i324987ldkhfkjq7q61398u9'

    check()
