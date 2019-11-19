"""module for testing function documentation"""
from os import path
from .factory import Sample


def setter(instance: Sample, arg1: int, arg2: int) -> bool:
    """Sample instance setter

    :param instance: instance of Sample
    :type instance: Sample
    :param arg1: int to convert
    :type arg1: int
    :param arg2: int to convert
    :type arg2: int
    :Keyword Arguments:
        :do: sample1 (default True)
        :then: sample2 (default "hello")
    :return: bool depends on success

    >>> from my_package.factory import Sample
    >>> from my_package.views import setter
    >>> instance = Sample(5, 5)
    >>> setter(instance, 4, 4)
    True
    """
    return Sample._set(instance, [arg1, arg2])
