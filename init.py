import time
import random
import webbrowser

Trigger = False
t0 = time.time()
current = time.strftime('%H:%M:%S', time.localtime(t0))
print("⏰ Çalar Saat Uygulamasına Hoşgeldiniz!\nŞuan Saat: {0} ⏰  ".format(current))

def sounds():
    with open('alarms.txt','r') as f:
        alarms = f.readlines()
        alarms = [i.strip() for i in alarms]
        z = random.randrange(0,len(alarms))
        webbrowser.open(alarms[z])


def alarm(saat):
    if gun == True:
        print("⏰ Çalar saat {0} gün {1} saat sonra {2}'da çalacak⏰".format(int(girdi / 1440),int((girdi % 1440)/60), ayar))
    else:
        print("⏰ Çalar saat bugün saat {0}'da Çalacak ⏰".format(ayar))
    while True:
        t3 = time.time()
        zaat = time.strftime('%H:%M:%S', time.localtime(saat))
        current = time.strftime('%H:%M:%S', time.localtime(t3))
        if zaat < current:
            print('Gelecek bir tarih girmelisiniz değer yanlış kapatılıyor!')
            break
        elif zaat == current:
            print("⏰⏰⏰ Saat {} alarm çalıyor.⏰⏰⏰".format(zaat))
            time.sleep(3)
            sounds()
            break
        else:
            print("Şuan saat {0} Kurulmuş Alarm: {1}".format(current,zaat))
            time.sleep(5)

while Trigger == False:

    try:
        girdi = int(input("Lütfen alarmın kaç dakika sonra çalması gerektiğini yazın:\n"))
        if isinstance(girdi,int) == True:
            if girdi < 60:
                print("⏰ Çalar Saat {} dakika sonra çalması için ayarlandı.⏰".format(girdi))
                gun = False
            elif girdi >= 1440:
                print("⏰ Çalar Saat {0} gün {1} saat sonra çalması için ayarlandı.⏰".format(int(girdi / 1440), int((girdi % 1440)/60)))
                gun = True
            elif girdi >= 60:
                print("⏰ Çalar Saat {0} saat {1} dakika sonra çalması için ayarlandı.⏰".format(int(girdi / 60), int(girdi % 60)))
                gun = False
            time.sleep(1)
            t0 = time.time()
            t1 = t0 + (girdi/60 * 60) * 60
            ayar = time.strftime('%H:%M:%S', time.localtime(t1))
            alarm(t1)
            Trigger = True
    except ValueError:
        print("Lütfen bir sayı değeri girin.")
        break