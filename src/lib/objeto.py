from lib.localmods.time import Timer
from lib.localmods.rand import Randomic
from lib.asset.data import Windy as Data
class Artefto:
    def artefato():
        artefato = {
            'data':Timer.data_iso(),
            'temperatura':Randomic.main_1845()
        }
        return artefato
    def nugget():
        '''
        **
        '''    
        artefato_127 = {
            'data':Data.moc()['data'],
            'temperatura':Data.moc()['temperatura'],
            'umidade':Data.moc()['umidade'],
            'local': Data.moc()['local'],
            'ts_from_api': Data.moc()['ts_from_api'],        
        }
        return artefato_127  
    def windly():
            print(Data.worker())
            artefato_127 = {
            'data':Data.worker()['data'],
            'temperatura':Data.worker()['temperatura'],
            'umidade':Data.worker()['umidade'],
            'local': Data.worker()['local'],
            'ts_from_api': Data.worker()['ts_from_api'],        
            }
            #print(artefato_127)
            return artefato_127