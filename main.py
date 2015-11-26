#!/usr/bin/env python

from flask import Flask
from flask_restful import Api, Resource
import click
import platform


app = Flask('roomservice')
api = Api(app)


def _get_os_props():
    distro, _, release = platform.linux_distribution(
        full_distribution_name=False)
    return distro.lower(), release.lower()


@click.command()
@click.option('--port', default=31337)
@click.option('--debug', default=False, is_flag=True)
def main(port, debug):
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    main()
