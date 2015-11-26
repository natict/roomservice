from flask_restful import Resource, Api
from flask import Blueprint
import sh
from memory import Memory
from processes import Processes, Process


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
    def __init__(self):
        # self._dnf = sh.Command('dnf')
        # self._rpm = sh.Command('rpm')
        pass


    def list(self):
        ret = self._rpm('-qa', '--qf', "%{name}\t%{version}\n")
        return [dict(zip(('name', 'version'), line.split('\t'))) for line in ret.stdout.split('\n')]


# TODO: use dynamic providers
# package_provider = provider_for('packages', os_info)
package_provider = DnfPackageProvider()

api.add_resource(Packages, '/packages', resource_class_kwargs={'provider': package_provider})
api.add_resource(PackageResource, '/packages/<string:package_name>', resource_class_kwargs={'provider': package_provider})
api.add_resource(Memory, '/memory')
api.add_resource(Processes, '/processes')
api.add_resource(Process, '/processes/<int:pid>')
