
import time
import sys
import os

def ola():
    time.sleep(1)  
    print('Repetição')
    time.sleep(1)



var = ''
log_ = ['','.','..','...']
log = ['','.','..','...']
ola()
while True:
    for i in log_:
        os.system('cls')
        print('Repetição')
        var = i
        print(str(var))
        time.sleep(1)
        var = ''


    # for i in log:
    #     # print(".", end="", flush=True)
    #     sys.stdout.write("\r{}".format(i))
    #     sys.stdout.flush()
    #     time.sleep(1)
