import os
import sys
sys.path.append("..")
import configparser
config = configparser.ConfigParser()
config.read('etcd/app.config')
##
token = config.get('default', 'token')
url = config.get('default', 'url')
###
##
host = config.get('mysql', 'host')
user = config.get('mysql', 'user')
passwd = config.get('mysql', 'pass')
base = config.get('mysql', 'base')

class Values:
    def values():
        artefato = {
            'host' : host,
            'user' : user,
            'passwd' : passwd,
            'base' : base        
        }        
        return artefato
    def deploy():
        artefato = {
            'TOKEN' : os.environ.get('TOKEN'), 
            'USER' : os.environ.get('USER'),            
        }        
        return artefato
