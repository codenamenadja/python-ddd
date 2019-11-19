HOW_TO_SPHINX_AND_DDD
=====================

| basically documents, easily test.
| Provide sphinx documents at https://codenamenadja.github.io/python-ddd/index.html

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

|    using type annotation can less documentation.
|    and nice to work with type based testing(mypy).

sphinx setting
==============

doctest and sphinx
==================

