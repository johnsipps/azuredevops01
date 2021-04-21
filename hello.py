import os
import logging
os.system('clear')
a=3
if a == 1:
    print('hello john and ciciliya')
elif a == 2:
    print('hello ciciliya')
else:
    print ('hello john')

try:
    b=1/0
except ZeroDivisionError as e:
    os.system('echo first:'+str(e)+'>error.log')
    #print('error occured')
    logging.exception("Error occured while printing GeeksforGeeks") 
    f = open("error.log","a")
    f.write("second:Error occured while printing GeeksforGeeks")