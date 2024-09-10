import requests
from lib.config import Values, local
import json
from lib.localmods.time import Timer

class Windy:
    def caller(pay,url,extra):
        pay = pay
        url = url
        req = requests.post(url,json=pay)
        req_json = req.json()
        def media(valor):
            size = len(valor)
            b = 0
            for x in range(0,size):
                b = valor[x] + b
            data_media = b/size
            return data_media
        #print(req_json)
        temperatura = float('{:.2f}'.format(media(req_json['temp-surface']) - 273.15))
        umidade = float('{:.2f}'.format(media(req_json['rh-surface'])))
        artefatoLocal = {        
        'temperatura': temperatura,
        'umidade':umidade,
        'local':extra['localizacao'],
        'data':extra['data'],
        'ts_from_api':req_json['ts'][0],
        }
        return artefatoLocal

    def worker():
        token = Values.values()['api']['token']
        url = Values.values()['api']['host']
        localiza = local['data'][0]    
        _objeto = {
            "lat": localiza['latitude'],
            "lon": localiza['longitude'],
            "model": "gfs",
            "parameters": ["temp","rh"],
            "key": token,
        }
        _objetoExtra = {
            'localizacao':localiza['cidade'],
            'data':Timer.data_iso()['iso'],
        }   
        artefato = Windy.caller(_objeto,url,_objetoExtra)    
        print(artefato)
        return artefato
#MOC
    def moc():
        artefatoLocal = {        
        'temperatura': 24.50,
        'umidade':70,
        'local':'Rio de Janeiro',
        'data':Timer.data_iso()['iso'],
        'ts_from_api':42000,
        }
        return  artefatoLocal
       