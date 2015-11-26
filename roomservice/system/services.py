from sh import systemctl

from flask_restful import Resource


class Services(Resource):
    def get(self):
        services = []
        service_info = systemctl('--no-legend', '--no-pager', t='service')
        for s in service_info:
            i = s.split()
            services.append(dict(
                name=i[0],
                load=i[1],
                active=i[2],
                sub=i[3],
                description=i[4]))
        return services
