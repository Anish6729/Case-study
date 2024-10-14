import configparser

class PropertyUtil:

    @staticmethod
    def getPropertyString():
        # config = configparser.ConfigParser()
        # config.read('db.properties')
        host = "LAPTOP-AT863VNS\SQLEXPRESS"
        dbname = "Project_Management_System"
        # username = config['DATABASE']['username']
        # password = config['DATABASE']['password']
        # port = config['DATABASE']['port']
        
        # return f'DRIVER={{SQL Server}};SERVER={host};DATABASE={dbname};UID={username};PWD={password};PORT={port}'
        return f'DRIVER={{SQL Server}};SERVER={host};DATABASE={dbname};Trusted_Connection=yes;'


# 'Driver={SQL Server};'
#                     'Server=LAPTOP-AT863VNS\SQLEXPRESS;'
#                     'Database=Order_Management_System;'
#                     'Trusted_Connection=yes;'