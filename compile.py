###############################################################################
# MMSOverseer compiler script
###############################################################################
# Michael Fisher, 2022
###############################################################################
# Unless you are very familiar with the behaviour of PyInstaller, do not modify
# this program. Messing with this file can lead to anomolous behaviour with 
# compiling and may lead to the program breaking. 
# 
# Modify at your own risk
###############################################################################


import subprocess
import shutil
import os
import getpass

def config_SMTP() -> None:
    with open('config.py', 'w') as config:

        print('=' * 80)
        print('| Configure SMTP for text message notify')
        print('=' * 80)

        email       = input("| Email: ")
        pas         = getpass.getpass("| Passw: ")
        sms_gateway = input('| Phone Number: ').replace('-', '') + '@' + input('| MMS Gateway: ')
        smtp        = input("| SMTP: ")
        port        = int(input("| Port: "))
        print('=' * 80)


        config.writelines(
            [
                'config = {',
                '"email" : "{0}",'.format(email),
                '"pas" : "{0}",'.format(pas),
                '"sms_gateway" : "{0}",'.format(sms_gateway),
                '"smtp" : "{0}",'.format(smtp),
                '"port" : "{0}"'.format(port),
                '}'
                ]
            )

def pycompile() -> None:

    print('=' * 80)
    print('| Compiling...')
    print('=' * 80)

    PyInstaller.__main__.run([
    'MMSOverseer.py',
    '--onefile',
    '--console',
    ])

    print()

def clean_up() -> None:
    print('=' * 80)
    print('| Tidying up...')
    print('=' * 80)

    os.chdir('./dist')
    for f in os.listdir('.'):
        if os.access(f, os.X_OK):
            shutil.move(f, './../' + f)

    os.chdir('./..')
    shutil.rmtree('./dist')
    shutil.rmtree('./build')
    shutil.rmtree('./__pycache__')

    os.remove('./MMSOverseer.spec')
    os.remove('./config.py')

    print()




print('=' * 80)
print('| MMSOverseer setup Phase')
print('| We will:')
print('| - Install any missing packages')
print('| - Ask you a few questions about your email account to set up SMTP')
print('| - Generate a single executable that you can use with any program')
print('|')
print('| Press any Key to continue')
print('=' * 80)
input()


print('=' * 80)
try:
    import PyInstaller.__main__

    print('| Packages already installed, continuing')
    print('=' * 80)


except ImportError as e:
    print('| Missing Packages, Installing...')
    print('=' * 80)

    # print(e + '\n')

    subprocess.run("python -m pip install pyinstaller", shell=True)

    import PyInstaller.__main__

print()


config_SMTP()
pycompile()
clean_up()

print('Finished!')

    







