###############################################################################
# MMSAlert
###############################################################################
# Michael Fisher, 2022
###############################################################################
# Modification of my MMSAlert script, which can be found at: 
# https://github.com/mefisher95/MMSAlert
# This script has been modified to directly pull information a compiled config
# file and is not suited to being modified. If you wish to use the more general
# version, please refer to the version linked above. 
#
###############################################################################
# two common functions have been defined below, TerminateNotify
# and ErrorNotify. These are used to notify the user when the program has ended
# and when an error has occured, respectively. If the user wants to send custom
# messages during run time, they can do so by using the start, send_message,
# and stop methods, in that order. 
# 
# start() -> None: starts the SMTP server
# sendmessage(message, subject) -> None: sends a message with a provided subject
#       to the defined SMTP account
# stop() -> None: terminates the SMTP server
#
# Any message can be used with these methods, and the user cand define any fun
# they wish around them
###############################################################################

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MMSAlert:
    def __init__(self) -> None:
        from config import config

        self.email = config['email']
        self.pas = config['pas']
        self.sms_gateway = config['sms_gateway']
        self.smtp = config['smtp']
        self.port = int(config['port'])

        self.server = None

        return None

    def start(self) -> None:
        self.server = smtplib.SMTP(self.smtp, self.port)
        self.server.starttls()
        self.server.login(self.email, self.pas)
    
        return None

    def stop(self) -> None:
        self.server.quit()

        return None

    def send_message(self, message, subject=None) -> None:
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        sms = msg.as_string()
        self.server.sendmail(self.email, self.sms_gateway, sms)

        return None

def ErrorNotify(error, writelog=False, errorlog='ErrorLog.txt') -> None:
    if writelog:
        file = open(errorlog, 'a')
        file.writelines(str(error))

    alert = MMSAlert()
    alert.start()
    alert.send_message(str(error), 'Error')
    alert.stop()

    return None

def TerminateNotify(sendlog=False) -> None:
    log = ''
    if 'Output_log.txt' in os.listdir() and sendlog:
        file = open('Output_lot.txt', 'r')
        for line in file.readlines():
            log += line
    msg = "Program terminated sucessfully\n" + log
    alert = MMSAlert()
    alert.start()
    alert.send_message(msg, 'Terminate Program')
    alert.stop()

    return None