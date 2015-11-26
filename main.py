#!/usr/bin/env python

from flask import Flask
from flask_restful import Api, Resource
import click


app = Flask('roomservice')
api = Api(app)


@click.command()
@click.option('--port', default=31337)
@click.option('--debug', default=False, is_flag=True)
def main(port, debug):
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    main()