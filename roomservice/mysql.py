import pymysql
from flask_restful import Resource
from flask import abort

ALLOWED_SHOW = ('processlist', 'databases', 'plugins', 'privileges')


class Mysql(Resource):
    def __init__(self):
        self.connection = pymysql.connect(user='root')
        self.cursor = self.connection.cursor()

    def _execute(self, sql):
        self.cursor.execute(sql)
        desc_id = tuple(x[0] for x in self.cursor.description)
        query_result = self.cursor.fetchall()
        results = [dict(zip(desc_id, item)) for item in query_result]
        return results

    def get(self, cmd):
        if cmd in ALLOWED_SHOW:
            return self._execute('show ' + cmd)
        else:
            abort(400)