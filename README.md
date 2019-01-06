[![Build Status](https://travis-ci.org/smomni/self-destructing-messages-api.svg?branch=master)](https://travis-ci.org/smomni/self-destructing-messages-api)
[![codecov](https://codecov.io/gh/smomni/self-destructing-messages-api/branch/master/graph/badge.svg)](https://codecov.io/gh/smomni/self-destructing-messages-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/34b7685d825a9a9a96a2/maintainability)](https://codeclimate.com/github/smomni/self-destructing-messages-api/maintainability)
[![Updates](https://pyup.io/repos/github/smomni/self-destructing-messages-api/shield.svg)](https://pyup.io/repos/github/smomni/self-destructing-messages-api/)

# self-destructing-messages-api

REST API for writing and reading self-destructing messages with optional auto-expiry timers using a redis backend.


## Usage

First, run redis backend in Docker:

```bash
docker run -p 6379:6379 -d redis
```

Next, start the API server:

```bash
serve_seppuku_api.py -e REDIS_HOSTNAME=localhost REDIS_PORT=6379
```

Send message "foo" with a 600-second auto-expiry timer as a `POST` request:

```bash
curl -sX POST http://localhost:5002/api/v1/seppuku-message?value=foo\&expire=600
```

The response should look something like this: `{"key": "b366fa0e-448c-433f-83e2-5e3b1723f8ab", "expire": 600}`. 
Now, send `GET` request to read the message:

```bash
curl -sX GET http://localhost:5002/api/v1/seppuku-message?key=b366fa0e-448c-433f-83e2-5e3b1723f8ab
``` 

The response should be `{"value": "foo"}`. 
If you re-send the same `GET` request, you'll get `{}` and a status code `400` because the key-message pair does not exist anymore.

Alternatively, you can use tools like `jq` to parse the `POST` response and use the extracted `key` to compose the `GET` response:

```bash
key=$(curl -sX POST http://localhost:5002/api/v1/seppuku-message?value=foo\&expire=600 | jq -r '.key')
curl -sX GET http://localhost:5002/api/v1/seppuku-message?key=$key
```
