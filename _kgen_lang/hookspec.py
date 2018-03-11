""" hook specifications for kgen_lang plugins, invoked from main.py and builtin plugins.  """

from pluggy import HookspecMarker

hookspec = HookspecMarker("kgen_lang")

# -------------------------------------------------------------------------
# Initialization hooks called for every plugin
# -------------------------------------------------------------------------


@hookspec(historic=True)
def kgen_lang_addhooks(pluginmanager):
    """called at plugin registration time to allow adding new hooks via a call to
    ``pluginmanager.add_hookspecs(module_or_class, prefix)``.


    :param _kgen_lang.config.KGenLangPluginManager pluginmanager: kgen_lang plugin manager

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """

@hookspec(historic=True)
def kgen_lang_namespace():
    """
    (**Deprecated**) this hook causes direct monkeypatching on kgen_lang, its use is strongly discouraged
    return dict of name->object to be made globally available in
    the kgen_lang namespace.

    This hook is called at plugin registration time.

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """


@hookspec(historic=True)
def kgen_lang_plugin_registered(plugin, manager):
    """ a new kgen_lang plugin got registered.

    :param plugin: the plugin module or instance
    :param _kgen_lang.config.KGenLangPluginManager manager: kgen_lang plugin manager

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """

@hookspec(historic=True)
def kgen_lang_addoption(parser):
    """register argparse-style options and ini-style config values,
    called once at the beginning of a test run.

    .. note::

        This function should be implemented only in plugins or ``conftest.py``
        files situated at the tests root directory due to how kgen_lang
        :ref:`discovers plugins during startup <pluginorder>`.

    :arg _kgen_lang.config.Parser parser: To add command line options, call
        :py:func:`parser.addoption(...) <_kgen_lang.config.Parser.addoption>`.
        To add ini-file values call :py:func:`parser.addini(...)
        <_kgen_lang.config.Parser.addini>`.

    Options can later be accessed through the
    :py:class:`config <_kgen_lang.config.Config>` object, respectively:

    - :py:func:`config.getoption(name) <_kgen_lang.config.Config.getoption>` to
      retrieve the value of a command line option.

    - :py:func:`config.getini(name) <_kgen_lang.config.Config.getini>` to retrieve
      a value read from an ini-style file.

    The config object is passed around on many internal objects via the ``.config``
    attribute or can be retrieved as the ``kgen_langconfig`` fixture.

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """


@hookspec(historic=True)
def kgen_lang_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.

    This hook is called for every plugin and initial conftest file
    after command line options have been parsed.

    After that, the hook is called for other conftest files as they are
    imported.

    .. note::
        This hook is incompatible with ``hookwrapper=True``.

    :arg _kgen_lang.config.Config config: kgen_lang config object
    """

# -------------------------------------------------------------------------
# Bootstrapping hooks called for plugins registered early enough:
# internal and 3rd party plugins.
# -------------------------------------------------------------------------


@hookspec(firstresult=True)
def kgen_lang_cmdline_parse(pluginmanager, subcmd, args):
    """return initialized config object, parsing the specified args.

    Stops at first non-None result, see :ref:`firstresult`

    .. note::
        This hook will not be called for ``confextract.py`` files, only for setuptools plugins.

    :param _kgen_lang.config.KGenLangPluginManager pluginmanager: kgen_lang plugin manager
    :param str subcmd: kgen-lang sub-command
    :param list[str] args: list of arguments passed on the command line
    """


@hookspec(firstresult=True)
def kgen_lang_cmdline_main(config):
    """ called for performing the main command line action. The default
    implementation will invoke the configure hooks and runtest_mainloop.

    .. note::
        This hook will not be called for ``confextract.py`` files, only for setuptools plugins.

    Stops at first non-None result, see :ref:`firstresult`

    :param _kgen_lang.config.Config config: kgen_lang config object
    """


def kgen_lang_load_initial_conftests(early_config, parser, subcmd, args):
    """ implements the loading of initial conftest files ahead
    of command line option parsing.

    .. note::
        This hook will not be called for ``confextract.py`` files, only for setuptools plugins.

    :param _kgen_lang.config.Config early_config: kgen_lang config object
    :param str subcmd: kgen-lang sub-command
    :param list[str] args: list of arguments passed on the command line
    :param _kgen_lang.config.Parser parser: to add command line options
    """

