from time import sleep
print('Repetição')
while True:
    for i in range(4):
        print('.'*i, end='')
        sleep(0.3)
        print('   ', end='\r')