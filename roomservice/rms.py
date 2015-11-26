#!/usr/bin/env python

import click
import platform

from flask import Flask
from flask_restful import Api
from processes import Processes


def _get_os_props():
    distro, _, release = platform.linux_distribution(
        full_distribution_name=False)
    return distro.lower(), release.lower()


def get_meminfo():
    with open('/proc/meminfo', 'r') as f:
        for l in f.read():
            data = l.split(' ')
            print data


@click.command()
@click.option('-p', '--port', default=31337)
@click.option('--debug', default=False, is_flag=True)
@click.option('-r', '--run-command', type=str, required=False)
def main(port, debug, run_command):
    if run_command:
        if hasattr(globals(), run_command):
            getattr(globals(), run_command)
    else:
        app = Flask('roomservice')
        api = Api(app)

        api.add_resource(Processes, '/processes')

        app.run(port=port, debug=debug)


if __name__ == '__main__':
    main()
