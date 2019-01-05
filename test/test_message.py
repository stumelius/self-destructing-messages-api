import pytest
import time
from seppuku.message import get_default_backend, write_message, read_message


@pytest.fixture
def redis():
    return get_default_backend()


def test_write_message_with_message_arg_returns_random_key(redis):
    key = write_message(value='pytest', backend=redis)
    assert isinstance(key, str)


def test_write_message_with_message_arg_writes_message_to_redis(redis):
    key = write_message(value='pytest', backend=redis)
    assert 'pytest' == redis.get(key).decode()


def test_write_message_with_message_and_expire_args_deletes_key_after_specified_time_in_seconds(redis):
    time_in_seconds = 1
    key = write_message(value='pytest', expire=time_in_seconds, backend=redis)
    time.sleep(time_in_seconds + 1)
    with pytest.raises(KeyError):
        read_message(key=key, backend=redis)


def test_read_message_with_key_arg_returns_value(redis):
    key = write_message(value='pytest', backend=redis)
    value = read_message(key=key, backend=redis)
    assert 'pytest' == value


def test_read_message_with_key_arg_deletes_the_key_from_redis(redis):
    key = write_message(value='pytest', backend=redis)
    # Message can be read only once
    read_message(key=key, backend=redis)
    with pytest.raises(KeyError):
        read_message(key=key, backend=redis)


def test_read_message_invalid_key_raises_key_error(redis):
    with pytest.raises(KeyError):
        read_message(key='non-existing key!', backend=redis)



