# Stubs for requests.packages.urllib3.util.retry (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .. import exceptions
from .. import packages

ConnectTimeoutError = exceptions.ConnectTimeoutError
MaxRetryError = exceptions.MaxRetryError
ProtocolError = exceptions.ProtocolError
ReadTimeoutError = exceptions.ReadTimeoutError
ResponseError = exceptions.ResponseError

log = ...  # type: Any

class Retry:
    DEFAULT_METHOD_WHITELIST = ...  # type: Any
    BACKOFF_MAX = ...  # type: Any
    total = ...  # type: Any
    connect = ...  # type: Any
    read = ...  # type: Any
    redirect = ...  # type: Any
    status_forcelist = ...  # type: Any
    method_whitelist = ...  # type: Any
    backoff_factor = ...  # type: Any
    raise_on_redirect = ...  # type: Any
    def __init__(self, total=10, connect=None, read=None, redirect=None, method_whitelist=..., status_forcelist=None, backoff_factor=0, raise_on_redirect=True, _observed_errors=0): pass
    def new(self, **kw): pass
    @classmethod
    def from_int(cls, retries, redirect=True, default=None): pass
    def get_backoff_time(self): pass
    def sleep(self): pass
    def is_forced_retry(self, method, status_code): pass
    def is_exhausted(self): pass
    def increment(self, method=None, url=None, response=None, error=None, _pool=None, _stacktrace=None): pass
