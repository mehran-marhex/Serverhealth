from os_data_storage.views import os_data_storage
import threading

def startProject():
    with open('counter.txt', 'r') as f:
        counter = f.read()[0]
        if counter == "0":
            t = threading.Thread(target=os_data_storage)
            t.start()
            
            with open('counter.txt', 'w') as f:
                f.write('1')


def endProject():
    with open('counter.txt', 'w') as f:
        f.write('0')
