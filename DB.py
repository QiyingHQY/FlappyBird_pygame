# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:DB.py
@time:2019/2/6 15:53
"""
# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:SQLite.py
@time:2018/11/26 8:35
"""

import sqlite3


class DB():
    def __init__(self):
        self.conn = sqlite3.connect('./source/record/database.db')
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def ceatTable(self):
        sql = '''CREATE TABLE Record
               (ID INTEGER PRIMARY KEY AUTOINCREMENT,
               SCORE            INT     NOT NULL,
               CreatedTime timestamp default current_timestamp);'''
        print(sql)
        self.c.execute(sql)

        self.conn.commit()

    def insertRecord(self, score):
        sql = '''INSERT INTO Record (SCORE) VALUES ({score})'''.format( \
            score=score)
        print(sql)
        self.c.execute(sql)

        self.conn.commit()

    def updateRecord(self, id, score, creattime):
        sql = '''UPDATE Record SET SCORE={score},CreatedTime='{creattime}' WHERE ID={id}'''.format( \
            id=id, score=score,creattime=creattime)
        print(sql)
        self.c.execute(sql)

        self.conn.commit()

    def selectRecord(self):
        sql = "SELECT ID, SCORE,CreatedTime  FROM Record ORDER BY SCORE desc,CreatedTime "
        print(sql)
        cursor = self.c.execute(sql)
        print("ID   SCORE    CreatedTime")

        record=[]
        for row in cursor:
            item=[row[0],row[1],row[2]]
            record.append(item)
            print("{id}    {SCORE}  {CreatedTime}".format(id=row[0], SCORE=row[1], CreatedTime=row[2]))

        return record

    def deletRecord(self, id):
        sql = "DELETE from Record where ID={id};".format(id=id)
        print(sql)
        self.c.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    db = DB()

    db.ceatTable()

    db.selectRecord()