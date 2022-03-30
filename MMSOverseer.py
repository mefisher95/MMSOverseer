import subprocess 
from sys import argv
import traceback
import MMSAlert as MMSAlert

process = subprocess.Popen(' '.join(argv[1:]))

while process.poll() is None: pass
print(process.poll()) 

if process.poll() == 1: MMSAlert.ErrorNotify(traceback.format_exc())
else: MMSAlert.TerminateNotify()