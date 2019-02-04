import _common

# Override the regular excepthook too -- it doesn't change anything either way
# because ipython doesn't use it, but we want to make sure exceptiongroup
# doesn't warn about it.
import sys


def custom_excepthook(*args):
    print("custom running!")
    return sys.__excepthook__(*args)


sys.excepthook = custom_excepthook

import IPython

ip = IPython.get_ipython()


# Set this to some random nonsense
class SomeError(Exception):
    pass


def custom_exc_hook(etype, value, tb, tb_offset=None):
    ip.showtraceback()


ip.set_custom_exc((SomeError,), custom_exc_hook)

import exceptiongroup

# The custom excepthook should run, because we were polite and didn't
# override it
raise exceptiongroup.ExceptionGroup(
    "demo", [ValueError(), KeyError()], ["a", "b"]
)
