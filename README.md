# MMSOverseer
Script that can encapsulate programs and report on their termination

This program uses an modified version of MMSAlert, which can be found at:

https://github.com/mefisher95/MMSAlert

## Setup:

### Modify MMSOverseer.py to suit your needs
- This script is meant to be a boiler plate for a user to tailor for their usecase. 
- This script will be compiled down into an executable and will process any program fed into it.
- After any modification, this script will need to be recompiled for the changes to take effect.
- Do not change the name of this file. ```compile.py``` is trained specifically to this filename
- Any modules that need to be imported should be in this scripts import path (as seen in the beginning with ```MMSAlert.py```

### Run ```python compile.py``` and follow the instructions
- This script will:
  - Install any missing packages
  - Ask you some questions for configuring SMTP for communication
  - Convert MMSOverseer.py into an Executable
  - Clean up anything created during the config phase

### For configuration of SMTP
  - Less secue app access
	  - can be found in the Google Account Security tab. Enable to
	    allow SMTP to access your Gmail  
  - Enter your Email Address
  - Enter your Email Password
  - Enter your phone number, followed by your MMS Gateway code
	  - This unique to your cell phone provider, and can ve found 
	  online
	  - Ex: AT&T = mms.att.net
  - Enter your Email's SMTP address
	  - This is unique for each email provider, and can be found online
	  - Ex: Gmail's = smtp.gmail.com
  - Enter your Email accounts SMTP Port Number
	  - This is unqiue for each email provider, and can be found online
	  - Ex: Gmail has 3: 25, 465, or 587
	  - Try each until one works

## Use
### To Use, run ```MMSObserver.exe [program name with arguments]```
- Ex: ```MMSObserver.exe python example.py arg1 arg2```
- Ex: ```MMSObserver.exe cpp_program.exe```
- Ex: ```MMSObserver.exe firefox```
- Ex: ```MMSObserver.exe python```
