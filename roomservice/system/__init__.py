from flask_restful import Resource, Api
from flask import Blueprint
import sh

import memory
import processes
import services
import platform
import cpu
import disk


blueprint = Blueprint('system', __name__)
api = Api(blueprint)


class Packages(Resource):
    def __init__(self, provider):
        self._provider = provider

    def get(self):
        return self._provider.list()


class PackageResource(Resource):
    def get(self, package_name):
        return self._provider.get(package_name)

    def delete(self, package_name):
        return self._provider.delete(package_name)


class DnfPackageProvider(object):
    @staticmethod
    def is_compatible():
        try:
            sh.Command('dnf')
            sh.Command('rpm')
            return True
        except Exception:
            return False

    def __init__(self):
        # self._dnf = sh.Command('dnf')
        # self._rpm = sh.Command('rpm')
        pass

    def list(self):
        ret = self._rpm('-qa', '--qf', "%{name}\t%{version}\n")
        return [dict(zip(('name', 'version'), line.split('\t')))
                for line in ret.stdout.split('\n')]


# TODO: use dynamic providers
# package_provider = provider_for('packages', os_info)
for pkg_provider in [DnfPackageProvider]:
    if pkg_provider.is_compatible():
        package_provider = pkg_provider()
        break
else:
    package_provider = None


api.add_resource(
    Packages, '/packages',
    resource_class_kwargs={'provider': package_provider})
api.add_resource(
    PackageResource, '/packages/<string:package_name>',
    resource_class_kwargs={'provider': package_provider})
api.add_resource(memory.Memory, '/memory')
api.add_resource(processes.Processes, '/processes')
api.add_resource(processes.Process, '/processes/<int:pid>')
api.add_resource(services.Services, '/services')
api.add_resource(platform.Platform, '/platform')
api.add_resource(cpu.CpuLoad, '/cpu/load')
api.add_resource(cpu.CpuTimes, '/cpu/times')
api.add_resource(cpu.CpuCores, '/cpu/cores')
api.add_resource(disk.DiskPartitions, '/disk/partitions')
api.add_resource(disk.DiskUsage, '/disk/usage/<string:path>')
api.add_resource(disk.DiskIO, '/disk/io')
api.add_resource(disk.DiskIOPerDisk, '/disk/ioperdisk')
