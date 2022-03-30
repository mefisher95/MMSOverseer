###############################################################################
# MMSOverseer Driver Code
###############################################################################
# Michael Fisher, 2022
###############################################################################
# Driver code for MMSOverseer, to be compiled down into an executable. 
# The generated exectuable will take in any program exectuable with its args
# and run it in a subproccess shell. When the program terminates, the 
# exe will send a message via SMTP, detailing the termination
###############################################################################
# Program can be modified freely to tailor to use case, but will need to be 
# recompiled after each change. 
# To compile, simply run python compile.py.
# Do not change the name of this file. compile.py is trained on this filename
###############################################################################



# Imports
import subprocess 
from sys import argv
import MMSAlert as MMSAlert

# takes in args from the command line, joins them, and feeds them into a 
# subprocess. 
process = subprocess.Popen(' '.join(argv[1:]), stdout=subprocess.PIPE)

# wait on standby for the program to terminate. 
while process.poll() is None: pass 


# when program terminates, it will return a termination code. 
# 0 is defined as healthy termination
# 1 is defined as termination due to error
# user can define how the script responds to exits by defining for
# each termination code 

if process.poll() == 1:
    MMSAlert.ErrorNotify("Program Terminated Unexpectedly")
else: MMSAlert.TerminateNotify()