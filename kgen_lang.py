# PYTHON_ARGCOMPLETE_OK
"""
kgen_lang: Automated code extraction tool.
"""


# else we are imported

from _kgen_lang.config import (
    main
)
#from _kgen_lang.config import (
#    main, UsageError, cmdline,
#    hookspec, hookimpl
#)

#from _kgen_lang.fixtures import fixture, yield_fixture
#from _kgen_lang.assertion import register_assert_rewrite
#from _kgen_lang.freeze_support import freeze_includes
from _kgen_lang import __version__
#from _kgen_lang.debugging import kgen_langPDB as __kgen_langPDB
#from _kgen_lang.recwarn import warns, deprecated_call
#from _kgen_lang.outcomes import fail, skip, importorskip, exit, xfail
#from _kgen_lang.mark import MARK_GEN as mark, param
#from _kgen_lang.main import Session
#from _kgen_lang.nodes import Item, Collector, File
#from _kgen_lang.fixtures import fillfixtures as _fillfuncargs
#from _kgen_lang.python import (
#    Module, Class, Instance, Function, Generator,
#)

#from _kgen_lang.python_api import approx, raises

#set_trace = __kgen_langPDB.set_trace

__all__ = [
    'main',
    'UsageError',
    'cmdline',
    'hookspec',
    'hookimpl',
    '__version__',
#    'register_assert_rewrite',
#    'freeze_includes',
#    'set_trace',
#    'warns',
#    'deprecated_call',
#    'fixture',
#    'yield_fixture',
#    'fail',
#    'skip',
#    'xfail',
#    'importorskip',
#    'exit',
#    'mark',
#    'param',
#    'approx',
#    '_fillfuncargs',
#
#    'Item',
#    'File',
#    'Collector',
#    'Session',
#    'Module',
#    'Class',
#    'Instance',
#    'Function',
#    'Generator',
#    'raises',


]

if __name__ == '__main__':
    # if run as a script or by 'python -m kgen_lang'
    # we trigger the below "else" condition by the following import
    import kgen_lang
    raise SystemExit(kgen_lang.main())
else:
    pass
    #from _kgen_lang.compat import _setup_collect_fakemodule
    #_setup_collect_fakemodule()
