""" command line options, ini-file and conftest.py processing. """
from __future__ import absolute_import, division, print_function

def main(args=None, plugins=None):
    """ return exit code, after performing an in-process test run.

    :arg args: list of command line arguments.

    :arg plugins: list of plugin objects to be auto-registered during
                  initialization.
    """
    try:
        try:
            config = _prepareconfig(args, plugins)
        except ConftestImportFailure as e:
            tw = py.io.TerminalWriter(sys.stderr)
            for line in traceback.format_exception(*e.excinfo):
                tw.line(line.rstrip(), red=True)
            tw.line("ERROR: could not load %s\n" % (e.path), red=True)
            return 4
        else:
            try:
                return config.hook.pytest_cmdline_main(config=config)
            finally:
                config._ensure_unconfigure()
    except UsageError as e:
        tw = py.io.TerminalWriter(sys.stderr)
        for msg in e.args:
            tw.line("ERROR: {}\n".format(msg), red=True)
        return 4

