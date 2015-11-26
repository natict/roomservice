import pymysql
from flask_restful import Resource


class Mysql(Resource):
    def __init__(self):
        self.connection = pymysql.connect(user='root')
        self.cursor = self.connection.cursor()

    def show_processlist(self):
        self.cursor.execute('SHOW PROCESSLIST')

        desc_id = tuple(x[0] for x in self.cursor.description)
        query_result = self.cursor.fetchall()
        results = [dict(zip(desc_id, item)) for item in query_result]
        return results


    def get(self, cmd):
        if cmd == 'processlist':
            return self.show_processlist()