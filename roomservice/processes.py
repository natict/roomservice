from time import sleep

import psutil
from flask_restful import Resource
from psutil import NoSuchProcess


class Processes(Resource):
    def get(self):
        return [p.as_dict() for p in psutil.process_iter()]


class Process(Resource):
    def get(self, pid):
        try:
            return psutil.Process(pid=pid).as_dict()
        except NoSuchProcess:
            return '', 404

    def delete(self, pid):
        cmdline = None
        try:
            cmdline = psutil.Process(pid=pid).as_dict().get('cmdline')
            psutil.Process(pid=pid).kill()
            sleep(1)
        except NoSuchProcess:
            return '', 404
        finally:
            try:
                if psutil.Process(pid=pid).as_dict().get('cmdline') == cmdline:
                    return 'Process won\'t die by SIGTERM', 500
            except NoSuchProcess:
                pass
        return 'It\'s dead Jim!', 201
