"""core.judge のテスト（最初から緑）。機能を足しても緑を保とう＝回帰テスト。"""

from hitblow.core import judge, make_secret


def test_all_hit():
    assert judge("123", "123") == (3, 0)


def test_all_blow():
    assert judge("123", "231") == (0, 3)


def test_mix():
    assert judge("123", "132") == (1, 2)


def test_none():
    assert judge("123", "456") == (0, 0)


def test_make_secret_default_digits():
    secret = make_secret()
    assert len(secret) == 3
    assert secret.isdigit()
    assert len(set(secret)) == 3


def test_make_secret_custom_digits():
    secret = make_secret(5)
    assert len(secret) == 5
    assert secret.isdigit()
    assert len(set(secret)) == 5
