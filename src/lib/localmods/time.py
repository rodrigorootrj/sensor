import time
import datetime
from datetime import date

class Timer:
    def main():        
        data = date.today()
        return data
    def data_ts():        
        data = time.time()
        data_fromts = datetime.datetime.fromtimestamp(data).isoformat(timespec='minutes') 
        return data_fromts
    def data_iso():        
        data_fromts = datetime.datetime.now().isoformat(timespec='seconds') 
        iso = datetime.datetime.fromisoformat(data_fromts)
        artefato = {
            'data_fromts': data_fromts,
            'iso' : iso.strftime("%Y-%m-%d %H:%M:%S")
        }
        return artefato
class TimerFormat:
    def main(data_fromts):
        data = data_fromts/1000
        data_fromts = datetime.datetime.fromtimestamp(data).isoformat(timespec='milliseconds') 
        iso = datetime.datetime.fromisoformat(data_fromts)
        print(iso)
        iso = datetime.datetime.fromisoformat(data_fromts)
        artefato = {
           'data_fromts': data_fromts,
           'iso' : iso.strftime("%Y-%m-%d %H:%M:%S")
        }
        return artefato