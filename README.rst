HOW_TO_SPHINX_AND_DDD
=====================

| basically documents, easily test.
| Provide sphinx documents at https://junehan-dev.github.io/python-ddd/index.html

INDEX
=====

- :`folder structure`_: with intro.
- :`how to docstring`_: to recognize fine with sphinx.
- :`sphinx setting`_: auto documenting in simple way.
- :`doctest and sphinx`_: build document with doctest as unittest.

folder structure
=================

- :``project folder/``: root dir
  - :``setup.py``: file to automate setup project
  - :``my_package/``: package 1
    - :``__init__.py``: package recognization
    - :``factory.py``: sample class module
    - :``views.py``: sample function module
    - :``tests/``: test dir
      - :``test_factory_views.py``: sample testing scenario

how to docstring
================

- before type annotations

>>> def sample(arg1:int, arg2) -> bool:
...     """Sample class for testing docstring.
...  
...     :param arg1: value to be ~ed.
...     :param arg2: value to be ~ed.
...     :type arg2: int
... 
...     :Keyword Arguments:
...         :message: some keyword arg.(default to (,))
... 
...     :return: return will be...
...     :rtype: bool
...     """

    - using type annotation can less documentation.
    - and nice to work with type based testing(mypy).
- with type annotations

>>> import typing
... def test_view(arg1: int, arg2: int, callback: typing.Callable) -> bool:
...     """Sample view to manage somthing.
... 
...     :param arg1: manages response type
...     :param arg2: manages header length
... 
...     :Keyword Arguments:
...         :callback: func to work while something.
... 
...     :return: dependant to callback work.
...     """

    - can reduce 4~5 lines with typings

sphinx setting
==============

1. sphinx-quick start make dir with name docsrc
#. edit ``conf.py`` for project rootdir and extension setup.
#. edit ``index.rst`` to make structural documentation.
#. by ``Makefile``, ``make html`` command will generate html documentation.

doctest and sphinx
==================

1. before ``make html`` command, ``sphinx-build -b doctest docsrc/source docsrc/build``.
#. will test all inner doctest literals in modules specifed.
#. command line will tell you the coverage.
4. then by the result all passed, ``make html`` would be fine.

:TODO_1: combine with ``test_and_build.sh`` to automate testing with documentation.
:TODO_2: combine unit tests with functional test.
:TODO_3: combine with git command to remote changes and versions.

1. unittest with doctest,
#. functional test.
#. make build
#. not to push git, push files to remote server with scp the archive or rsync.
#. restart or reload server service.

