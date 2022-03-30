import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MMSAlert:
    def __init__(self):
        from config import config

        self.email = config['email']
        self.pas = config['pas']
        self.sms_gateway = config['sms_gateway']
        self.smtp = config['smtp']
        self.port = int(config['port'])

        self.server = None


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