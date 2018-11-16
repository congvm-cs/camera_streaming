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
                            "tinna{}".format(GenPasswd2()),
                            "0",
                            40000,
                            "tinna@gmail.com")
            cursor.execute(_sql)
            myConnection.commit()
        except Exception as e:
            raise('Insert fail')

# Simple routine to run a query on a database and print the results:
def doQuery(conn) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname FROM employee" )

    for firstname, lastname in cur.fetchall() :
        print firstname, lastname

