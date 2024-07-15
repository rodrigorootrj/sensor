import mysql.connector
from lib.config import Values
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


