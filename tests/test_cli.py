"""cli.main のテスト。"""

from hitblow import cli


def test_main_uses_default_digits(monkeypatch):
    called = {}

    def fake_play(*, digits):
        called["digits"] = digits

    monkeypatch.setattr(cli, "play", fake_play)
    monkeypatch.setattr(cli.sys, "argv", ["hitblow"])

    cli.main()

    assert called["digits"] == 3


def test_main_uses_cli_digits(monkeypatch):
    called = {}

    def fake_play(*, digits):
        called["digits"] = digits

    monkeypatch.setattr(cli, "play", fake_play)
    monkeypatch.setattr(cli.sys, "argv", ["hitblow", "5"])

    cli.main()

    assert called["digits"] == 5


def test_main_rejects_invalid_digits(monkeypatch, capsys):
    called = {"play": False}

    def fake_play(*, digits):
        called["play"] = True

    monkeypatch.setattr(cli, "play", fake_play)
    monkeypatch.setattr(cli.sys, "argv", ["hitblow", "11"])

    cli.main()

    assert called["play"] is False
    assert "桁数は 1〜10 の整数で指定してね" in capsys.readouterr().out
