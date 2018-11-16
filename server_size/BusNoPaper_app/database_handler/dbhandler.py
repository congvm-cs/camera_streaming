#!/usr/bin/python

import pymysql
import pandas as pd
import numpy as np
from random import choice
import string


class BusNoPaperDB(object):
    def __init__(self):
        self.hostname = 'localhost'
        self.username = 'root'
        self.password = ''
        self.database = 'busnopaper_db'

    
    def gen_QRcode2(self, length=16, chars=string.ascii_letters + string.digits):
        return ''.join([choice(chars) for i in range(length)])


    def insert(self, username, password, qrcode, usertype=0, money=0, email=None):
        try:
            myConnection = pymysql.connect( host=self.hostname, 
                                            user=self.username, 
                                            passwd=self.password, 
                                            database=self.database)

            cursor = myConnection.cursor()

            _sql = "INSERT INTO user( \
                            id, \
                            username, \
                            password,\
                            qrcode,\
                            usertype,\
                            money,\
                            email) \
                        VALUES({}, \"{}\", \"{}\", \"{}\", \"{}\", {}, \"{}\");".format(
                            "null",
                            "tinna",
                            "1234",
                            "tinna{}".format(self.gen_QRcode2()),
                            "0",
                            40000,
                            "tinna@gmail.com")
            cursor.execute(_sql)
            myConnection.commit()
            myConnection.close()
        except:
            raise('Insert fail')


    def update_password(self, id, password):
        try:
            myConnection = pymysql.connect( host=self.hostname, 
                                            user=self.username, 
                                            passwd=self.password, 
                                            database=self.database)

            cursor = myConnection.cursor()
            _sql = "UPDATE user                     \
                        SET password = \"{}\",      \
                    WHERE id={};".format(password, id)

            cursor.execute(_sql)
            myConnection.commit()

        except:
            raise('Update fail')


    def update_qrcode(self, id):
        try:
            myConnection = pymysql.connect( host=self.hostname, 
                                            user=self.username, 
                                            passwd=self.password, 
                                            database=self.database)

            cursor = myConnection.cursor()
            _sql = "UPDATE user                 \
                        SET qrcode = \"{}\",   \
                    WHERE id={};".format(self.gen_QRcode2(), id)

            cursor.execute(_sql)
            myConnection.commit()
            myConnection.close()
        except:
            raise('Update fail')


    def update_money(self, id, money):
        try:
            myConnection = pymysql.connect( host=self.hostname, 
                                            user=self.username, 
                                            passwd=self.password, 
                                            database=self.database)

            cursor = myConnection.cursor()
            _sql = "UPDATE user                 \
                        SET money = {},   \
                    WHERE id={};".format(money, id)

            cursor.execute(_sql)
            myConnection.commit()
            myConnection.close()
        except:
            raise('Update fail')

    def query_info(self, id):
        myConnection = pymysql.connect( host=self.hostname, 
                                        user=self.username, 
                                        passwd=self.password, 
                                        database=self.database)

        cursor = myConnection.cursor()
        _sql = "SELECT * FROM user          \
                WHERE id={};".format(id)

        cursor.execute(_sql)
        _response = cursor.fetchall()
        myConnection.close()
        return _response
