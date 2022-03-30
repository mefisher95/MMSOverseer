import email
import subprocess
import shutil
import os
import sys

try:
    import PyInstaller.__main__
except ImportError as e:
    print(e + '\n')

    subprocess.run("python -m pip install pyinstaller", shell=True)

    import PyInstaller.__main__

def config_SMTP() -> None:
    with open('config.py', 'w') as config:
        print('Configure SMTP for text message notify:\n')
        email       = input("Email: ")
        pas         = input("Passw: ")
        sms_gateway = input('Phone Number: ') + '@' + input('MMS Gateway: ')
        smtp        = input("SMTP: ")
        port        = int(input("Port: "))

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
    PyInstaller.__main__.run([
    'MMSOverseer.py',
    '--onefile',
    '--console'
    ])

def clean_up() -> None:
    shutil.move('./dist/MMSOverseer.exe', './MMSOverseer.exe')
    shutil.rmtree('./dist')
    shutil.rmtree('./build')
    shutil.rmtree('./__pycache__')

    os.remove('./MMSOverseer.spec')
    os.remove('./config.py')

def main() -> None:

    config_SMTP()
    pycompile()
    clean_up()

if __name__ == "__main__":
    main()


