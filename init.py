import time
import random
import webbrowser

Trigger = False
t0 = time.time()
current = time.strftime('%H:%M:%S', time.localtime(t0))
print("⏰ Welcome to The Youtube Alarm Clock!\nCurrent Time is: {0} ⏰  ".format(current))

def sounds():
    with open('alarms.txt','r') as f:
        alarms = f.readlines()
        alarms = [i.strip() for i in alarms]
        z = random.randrange(0,len(alarms))
        webbrowser.open(alarms[z])


def alarm(saat):
    if gun == True:
        print("⏰ Alarm clock is going to ring {0} day {1} hour later at {2} ⏰".format(int(girdi / 1440),int((girdi % 1440)/60), ayar))
    else:
        print("⏰ Alarm clock is going to ring at {0} ⏰".format(ayar))
    while True:
        t3 = time.time()
        zaat = time.strftime('%H:%M:%S', time.localtime(saat))
        current = time.strftime('%H:%M:%S', time.localtime(t3))
        if zaat < current:
            print('You should enter a valid future date program is closing!')
            break
        elif zaat == current:
            print("⏰⏰⏰ The clock is {} alarm is ringing.⏰⏰⏰".format(zaat))
            time.sleep(3)
            sounds()
            break
        else:
            print("The current time is {0} Alarm will ring at: {1}".format(current,zaat))
            time.sleep(5)

while Trigger == False:

    try:
        girdi = int(input("Please enter how much minutes later the Alarm Clock should ring:\n"))
        if isinstance(girdi,int) == True:
            if girdi < 60:
                print("⏰ Alarm Clock is set to ring {} minutes later.⏰".format(girdi))
                gun = False
            elif girdi >= 1440:
                print("⏰ Alarm Clock is set to ring {0} day {1} hour later.⏰".format(int(girdi / 1440), int((girdi % 1440)/60)))
                gun = True
            elif girdi >= 60:
                print("⏰ Alarm Clock is set to ring {0} hour {1} minutes later.⏰".format(int(girdi / 60), int(girdi % 60)))
                gun = False
            time.sleep(1)
            t0 = time.time()
            t1 = t0 + (girdi/60 * 60) * 60
            ayar = time.strftime('%H:%M:%S', time.localtime(t1))
            alarm(t1)
            Trigger = True
    except ValueError:
        print("Please enter a valid numerical value.")
        break