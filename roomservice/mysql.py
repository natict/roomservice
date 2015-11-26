from flask_restful import Resource


class Mysql(Resource):
    def get(self):
        return 'yo'