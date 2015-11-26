from time import sleep

import psutil
from flask_restful import Resource
from psutil import NoSuchProcess


def _process_enrich(p):
    process_dict = p.as_dict()
    try:
        environ = open('/proc/{pid}/environ'.format(pid=process_dict.get('pid'))).read()
        process_dict['environ'] = {var.split('=', 1)[0]: var.split('=', 1)[1] for var in environ.split('\0') if var}
    except Exception:
        pass  # no environ for you!
    return process_dict


class Processes(Resource):
    def get(self):
        return [_process_enrich(p) for p in psutil.process_iter()]


class Process(Resource):
    def get(self, pid):
        try:
            return _process_enrich(psutil.Process(pid=pid))
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
