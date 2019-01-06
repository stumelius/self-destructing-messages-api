#!/usr/bin/env python
import os
import argparse
from seppuku import create_app, logger
parser = argparse.ArgumentParser()
parser.add_argument('-e', help='Environment variables', type=str, nargs='*')


if __name__ == '__main__':
    args = parser.parse_args()
    if args.e is not None:
        for env_str in args.e:
            name, value = env_str.split('=')
            os.environ[name] = value
    app = create_app()
    logger.info('Serving /api/v1/seppuku-message at port 5002')
    app.run(port='5002')
