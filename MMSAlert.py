import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MMSAlert:
    def __init__(self):
        if 'CONFIG' not in os.listdir():
            self.init()
        else:
            file  = open('CONFIG', 'r')
            self.email = file.readline().strip('\n')
            self.pas = file.readline().strip('\n')
            self.sms_gateway = file.readline().strip('\n')
            self.smtp = file.readline().strip('\n')
            self.port = int(file.readline().strip('\n'))
        self.server = None

    def init(self):
        self.email       = input("Email: ")
        self.pas         = input("Passw: ")
        self.sms_gateway = input('Phone Number: ') + '@' + input('MMS Gateway: ')
        self.smtp        = input("SMTP: ")
        self.port        = int(input("Port: "))

        file = open('CONFIG', 'w')
        file.write(self.email + '\n')
        file.write(self.pas + '\n')
        file.write(self.sms_gateway + '\n')
        file.write(self.smtp + '\n')
        file.write(str(self.port) + '\n')
        file.close()

    def start(self):
        self.server = smtplib.SMTP(self.smtp, self.port)
        self.server.starttls()
        self.server.login(self.email, self.pas)
    
    def stop(self):
        self.server.quit()

    def send_message(self, message, subject=None):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        sms = msg.as_string()
        self.server.sendmail(self.email, self.sms_gateway, sms)

def ErrorNotify(error, writelog=True, errorlog='ErrorLog.txt'):
    if writelog:
        file = open(errorlog, 'a')
        file.writelines(str(error))

    alert = MMSAlert()
    alert.start()
    alert.send_message(str(error), 'Error')
    alert.stop()

def TerminateNotify(sendlog=True):
    log = ''
    if 'Output_log.txt' in os.listdir():
        file = open('Output_lot.txt', 'r')
        for line in file.readlines():
            log += line
    msg = "Program terminated sucessfully\n" + log
    alert = MMSAlert()
    alert.start()
    alert.send_message(msg, 'Terminate Program')
    alert.stop()