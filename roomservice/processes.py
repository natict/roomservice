import psutil
from flask_restful import Resource


class Processes(Resource):
    def get(self):
        return [p.as_dict() for p in psutil.process_iter()]
