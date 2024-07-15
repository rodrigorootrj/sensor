from lib.localmods.time import Timer
from lib.localmods.rand import Randomic
from asset.data import Local as Data
class Artefto:
    def artefato():
        artefato = {
            'data':Timer.data_iso(),
            'temperatura':Randomic.main_1845()
        }
        return artefato
    def nugget(local):
        '''
        **
        '''

        artefato_127 = {
            'data':Artefto.artefato()['data']['iso'],
            'temperatura':Artefto.artefato()['temperatura'],
            'local': Data(local)             
        }
        return artefato_127        