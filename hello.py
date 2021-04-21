import os
import datetime
os.system('clear')
now = datetime.datetime.now()
timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))
flog = open("run_logs/status.log."+timestamp,"a")
ferror = open("error_logs/error.log"+timestamp,"a")
a=3
if a == 1:
    flog.write('hello john and ciciliya')
elif a == 2:
    flog.write('hello ciciliya')
else:
    flog.write ('hello john')
flog.write("Passed")
try:
    
    b=1/0
except ZeroDivisionError as e:
    #print('error occured')
    ferror.write(str(e))