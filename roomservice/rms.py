#!/usr/bin/env python

import click
import platform

from flask import Flask
from flask_restful import Api
from memory import Memory
from mysql import Mysql
from processes import Processes, Process


def _get_os_props():
    distro, _, release = platform.linux_distribution(
        full_distribution_name=False)
    return distro.lower(), release.lower()


@click.command()
@click.option('-p', '--port', default=31337)
@click.option('--debug', default=False, is_flag=True)
@click.option('-r', '--run-command', type=str, required=False)
def main(port, debug, run_command):
        app = Flask('roomservice')
        api = Api(app)

        api.add_resource(Processes, '/processes')
        api.add_resource(Memory, '/memory')
        api.add_resource(Mysql, '/mysql')
        api.add_resource(Process, '/processes/<int:pid>')

        app.run(port=port, debug=debug)


if __name__ == '__main__':
    main()
