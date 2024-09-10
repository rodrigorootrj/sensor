from lib.config import Values
from lib.objeto import Artefto
from lib.pusher import Pusher
'''
autor: Rodrigo da Silva Cunha.
email: rodrigo.root.rj@gmail.com
class: snack
cat: A51, PW-VC
'''

def run():
    import time
    ## Info
    artefato = Artefto.windly()
    Pusher().pusher_exporter(artefato) 

    time.sleep(600)

if __name__ == '__main__':
    while True:
        run()