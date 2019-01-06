import logging
import sys
from flask import Flask
from flask_restful import Api
logging.basicConfig(stream=sys.stdout,
                    format='[%(asctime)s.%(msecs)03d] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger('rest-api')
__version__ = '0.1.0'


def create_app():
    from seppuku.api import SeppukuMessage
    app = Flask(__name__)
    api = Api(app, prefix='/api/v1')
    api.add_resource(SeppukuMessage, SeppukuMessage.endpoint)
    return app
