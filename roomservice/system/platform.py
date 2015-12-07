import ld
import os
import sys
from flask_restful import Resource

IS_WIN = os.name == 'nt'
IS_LINUX = sys.platform.startswith('linux')
IS_DARWIN = sys.platform.startswith('darwin')


class Platform(Resource):
    def get(self):

        if IS_LINUX:
            return dict(
                id=ld.id(),
                name=ld.name(),
                version=ld.version(),
                like=ld.like(),
                codename=ld.codename(),
                base=ld.base()
            )
