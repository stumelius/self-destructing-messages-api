import uuid
import os
from redis import Redis


def get_default_backend() -> Redis:
    """
    Return default key-value data store backend.

    :return:
    """
    return Redis(host=os.environ['REDIS_HOSTNAME'], port=os.environ['REDIS_PORT'])


def write_message(value: str, backend: Redis, expire: int=None) -> str:
    """
    Write a message to a key-value store and return a random-generated key.

    :param value:
    :param backend: key-value store backend (e.g., redis)
    :param expire: auto-expire message after specified number of seconds. If None (default), no auto-expiry is set.
    :return: key
    """
    key = str(uuid.uuid4())
    backend.set(name=key, value=value, ex=expire)
    return key


def read_message(key: str, backend: Redis) -> str:
    """
    Read and delete a message with a specified key from a key-value store.

    :param key:
    :param backend: key-value store backend (e.g., redis)
    :raises KeyError: Key does not exist
    :return:
    """
    pipe = backend.pipeline()
    pipe.get(key)
    pipe.delete(key)
    byte_arr, key_was_deleted = pipe.execute()
    if byte_arr is None:
        raise KeyError('Key does not exist')
    return byte_arr.decode()
