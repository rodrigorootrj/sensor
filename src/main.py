from lib.config import Values
from lib.objeto import Artefto
from lib.localmods.rand import Randomic
from lib.pusher import Pusher
'''
autor: Rodrigo da Silva Cunha.
email: rodrigo.root.rj@gmail.com
class: snack
cat: A51, PW-VC
'''

def run():
    import time
    local = Randomic.main_02()
    artefato = Artefto.nugget(local=local)
    Pusher().pusher(artefato)
    print(artefato)
    time.sleep(10)

if __name__ == '__main__':
    while True:
        run()