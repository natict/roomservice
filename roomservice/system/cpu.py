import psutil
from flask_restful import Resource

from .. import common


class CpuLoad(Resource):
    def get(self, interval=1, percpu=True):
        return psutil.cpu_percent(interval=interval, percpu=percpu)


class CpuTimes(Resource):
    def get(self, percpu=True):
        return common.to_dict(psutil.cpu_times(percpu=percpu))


class CpuCores(Resource):
    def get(self, logical=True):
        return psutil.cpu_count(logical=True)
