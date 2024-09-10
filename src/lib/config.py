import os
import sys
sys.path.append("..")
import configparser
config = configparser.ConfigParser()
config.read('etcd/app.config')
##
token = config.get('api', 'token')
url = config.get('api', 'url')
###
##
host = config.get('mysql', 'host')
user = config.get('mysql', 'user')
passwd = config.get('mysql', 'pass')
base = config.get('mysql', 'base')
table = config.get('mysql', 'table')
##
class Values:
    def values():
        artefato = {
            'host' : host,
            'user' : user,
            'passwd' : passwd,
            'base' : base,
            'table': table,
            'api':{
                'host':url,
                'token':token,
            }       
        }        
        return artefato
    def deploy():
        artefato = {
            'TOKEN' : os.environ.get('TOKEN'), 
            'USER' : os.environ.get('USER'),            
        }        
        return artefato
##
local = {'data':[
{'cidade':'Rio de Janeiro','latitude':-22.9068,'longitude':-43.1729,'tag':'g_temperatura_rio_de_janeiro'},
]}