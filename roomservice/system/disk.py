import psutil
from flask_restful import Resource

from .. import common


class DiskPartitions(Resource):
    def get(self):
        return common.to_dict(psutil.disk_partitions(all=True))


class DiskUsage(Resource):
    def get(self, path):
        return common.to_dict(psutil.disk_usage(path))


class DiskIO(Resource):
    def get(self):
        return common.to_dict(psutil.disk_io_counters(perdisk=False))


class DiskIOPerDisk(Resource):
    def get(self):
        return common.to_dict(psutil.disk_io_counters(perdisk=True))
