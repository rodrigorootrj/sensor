import mysql.connector
from lib.config import Values
from lib.localmods.time import TimerFormat
class Pusher:
    def __init__(self):
        artefato = Values.values()
        mydb = mysql.connector.connect(
        host=artefato['host'],
        user=artefato['user'],
        password=artefato['passwd'],
        database=artefato['base']
        )
        self.mycursor = mydb.cursor()
        self.mydb = mydb
        self.table = artefato['table']

        pass
    def pusher(self,artefato):
        mycursor = self.mycursor
        mydb = self.mydb
        artefato_stamp = Office.office(artefato)
        data = artefato_stamp['data']
        temperatura = artefato_stamp['temperatura']
        local = artefato_stamp['local']

        mycursor.execute("INSERT INTO temperatura (data,temperatura,local) VALUES ('{}','{}','{}')".format(data,temperatura,local))
        retorno = mydb.commit()
        mydb.close()
        return retorno
    ## nerverland names
    def pusher_exporter(self,artefato):
        mycursor = self.mycursor
        mydb = self.mydb
        table = self.table
        
        artefato_stamp = artefato
        print(artefato_stamp)
        data = artefato_stamp['data']
        temperatura = artefato_stamp['temperatura']
        umidade =  artefato_stamp['umidade']
        localidade = artefato_stamp['local']
        data_from = TimerFormat.main(artefato_stamp['ts_from_api'])['iso']
        print(umidade,temperatura)
        mycursor.execute("INSERT INTO {} (data,data_from,temperatura,umidade,localidade) VALUES ('{}','{}','{}','{}','{}')".format(table,data,data_from,temperatura,umidade,localidade))
        retorno = mydb.commit()
        mydb.close()
        return retorno

class Office:
    def stamp(artefato):        
        return all(valor is not None for valor in artefato.values())
    def office(artefato):
        check = Office.stamp(artefato)
        if check == True:
            return artefato
        else:
            print("#"*75)
            print("ERRO NO ARTEFATO")
            print("#"*75)


