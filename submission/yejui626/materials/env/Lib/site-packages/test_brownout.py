from datetime import timedelta
from datetime import datetime

import pytest

from setup import get_brownout_schedule
from setup import maybe_raise_error


def test_brownout():
    brownout_schedule = get_brownout_schedule()

    brownout_iter = iter(brownout_schedule)

    start_datetime = next(brownout_iter).start_datetime
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime)
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=4))
    maybe_raise_error(start_datetime + timedelta(minutes=5))

    start_datetime = next(brownout_iter).start_datetime
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime)
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=9))

    maybe_raise_error(start_datetime + timedelta(minutes=10))

    start_datetime = next(brownout_iter).start_datetime
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime)
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=14))
    maybe_raise_error(start_datetime + timedelta(minutes=15))

    start_datetime = next(brownout_iter).start_datetime
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime)
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=9))
    maybe_raise_error(start_datetime + timedelta(minutes=10))
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=30))
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=39))
    maybe_raise_error(start_datetime + timedelta(minutes=40))

    start_datetime = next(brownout_iter).start_datetime
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime)
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=14))
    maybe_raise_error(start_datetime + timedelta(minutes=15))
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=30))
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=44))
    maybe_raise_error(start_datetime + timedelta(minutes=45))

    start_datetime = next(brownout_iter).start_datetime
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime)
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=19))
    maybe_raise_error(start_datetime + timedelta(minutes=20))
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=30))
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=49))
    maybe_raise_error(start_datetime + timedelta(minutes=50))

    start_datetime = next(brownout_iter).start_datetime
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime)
    with pytest.raises(SystemExit):
        maybe_raise_error(start_datetime + timedelta(minutes=59))

    checked_datetime = datetime(2030, 1, 1)
    with pytest.raises(SystemExit):
        maybe_raise_error(checked_datetime)


def test_allow_sklearn_package_install_environment_variable(monkeypatch):
    with monkeypatch.context() as context:
        context.setenv("SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL", "True")
        checked_datetime = datetime(2030, 1, 1)
        maybe_raise_error(checked_datetime)

        context.setenv("SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL", "False")
        checked_datetime = datetime(2020, 1, 1)
        with pytest.raises(SystemExit):
            maybe_raise_error(checked_datetime)
