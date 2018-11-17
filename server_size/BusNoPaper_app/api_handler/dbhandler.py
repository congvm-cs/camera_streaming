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

    def insert(self, username, password, qrcode, usertype=0, money=0, email=None):
        try:
            myConnection = pymysql.connect(host=self.hostname,
                                           user=self.username,
                                           passwd=self.password)

            cursor = myConnection.cursor()

            _sql = "USE busnopaper_db"
            cursor.execute(_sql)

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
                username,
                password,
                qrcode,
                usertype,
                money,
                email)
            cursor.execute(_sql)
            myConnection.commit()
            myConnection.close()
        except:
            raise('Insert fail')

    def update_password(self, username, password):
        try:
            myConnection = pymysql.connect(host=self.hostname,
                                           user=self.username,
                                           passwd=self.password)

            cursor = myConnection.cursor()

            _sql = "USE busnopaper_db"
            cursor.execute(_sql)

            _sql = "UPDATE user                     \
                        SET password = \"{}\",      \
                    WHERE username=\"{}\";".format(password, username)

            cursor.execute(_sql)
            myConnection.commit()

        except:
            raise('Update fail')

    def update_qrcode(self, username, code):
        try:
            myConnection = pymysql.connect(host=self.hostname,
                                           user=self.username,
                                           passwd=self.password)
            cursor = myConnection.cursor()

            _sql = "USE busnopaper_db"
            cursor.execute(_sql)

            _sql = "UPDATE user                 \
                        SET qrcode = \"{}\"     \
                    WHERE username=\"{}\";".format(code, username)

            cursor.execute(_sql)
            myConnection.commit()
            myConnection.close()
        except:
            raise('Update fail')

    def update_money(self, username, money):
        try:
            myConnection = pymysql.connect(host=self.hostname,
                                           user=self.username,
                                           passwd=self.password)

            cursor = myConnection.cursor()
            _sql = "USE busnopaper_db"
            cursor.execute(_sql)

            _sql = "UPDATE user                 \
                        SET money = {}   \
                    WHERE username=\"{}\";".format(money, username)

            cursor.execute(_sql)
            myConnection.commit()
            myConnection.close()
        except:
            raise('Update fail')

    def query_info(self, username):
        myConnection = pymysql.connect(host=self.hostname,
                                       user=self.username,
                                       passwd=self.password)

        cursor = myConnection.cursor()
        _sql = "USE busnopaper_db"
        cursor.execute(_sql)

        _sql = "SELECT * FROM user          \
                WHERE username=\"{}\";".format(username)

        cursor.execute(_sql)
        _response = cursor.fetchall()
        myConnection.close()
        return _response


    def update_usertype(self, username, usertype, email=""):
        try:
            myConnection = pymysql.connect(host=self.hostname,
                                        user=self.username,
                                        passwd=self.password)

            cursor = myConnection.cursor()

            _sql = "USE busnopaper_db"
            cursor.execute(_sql)

            print(username)
            _sql = "UPDATE user \
                        SET usertype = \"{}\",\
                            email = \"{}\" \
                    WHERE username=\"{}\";".format(usertype, email, username)

            cursor.execute(_sql)
            myConnection.commit()
            myConnection.close()
        except:
            raise('Insert fail')
