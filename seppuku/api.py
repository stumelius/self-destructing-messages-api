from flask_restful import Resource, reqparse
from seppuku import logger
from seppuku.message import get_default_backend, write_message, read_message


def check_expire(expire: int) -> int:
    """
    Check that the expire value is a positive integer.

    :param expire:
    :return:
    """
    expire_int = int(expire)
    if expire_int < 0:
        raise ValueError('Expire must be a positive integer')
    return expire_int


post_parser = reqparse.RequestParser(bundle_errors=True)
post_parser.add_argument('value', help='Please provide a message string', type=str, required=True)
post_parser.add_argument('expire', help='Please provide the number of future days for which Activations are generated',
                         type=check_expire, required=False)
get_parser = reqparse.RequestParser(bundle_errors=True)
get_parser.add_argument('key', help='Please provide a message key', type=str, required=True)


class SeppukuMessage(Resource):
    endpoint = '/seppuku-message'

    def post(self):
        logger.debug(f'POST {self.endpoint} called')
        args = post_parser.parse_args()
        key = write_message(value=args.value, backend=get_default_backend(), expire=args.expire)
        return {'key': key, 'expire': args.expire}, 200

    def get(self):
        logger.debug(f'GET {self.endpoint} called')
        args = get_parser.parse_args()
        try:
            value = read_message(key=args.key, backend=get_default_backend())
        except KeyError:
            # Key does not exist
            return {}, 400
        return {'value': value}, 200
