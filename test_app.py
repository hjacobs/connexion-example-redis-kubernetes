from app import get_redis_key


def test_get_redis_key():
    assert get_redis_key("jdoe") == "pets:jdoe"
