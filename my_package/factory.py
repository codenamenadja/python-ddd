"""module for testing class documentation"""
import typing
import abc


class Base(object):
    """base class for abstrations"""
    __metaclass__ = abc.ABCMeta
    _message = "dont approach!, from Base, by:"

    @abc.abstractmethod
    def sum(self):
        """abract method, must override"""

    @abc.abstractmethod
    def subtract(self):
        """abstractmethod, must override"""

    @staticmethod
    @abc.abstractmethod
    def _set():
        """abstractmethod, staticmethod, recommends to override"""
        print('wow you didnt override...')

    @classmethod
    @abc.abstractmethod
    def display(cls, default="message", **kwargs):
        """abstractmethod, classmethod, can override but hope not

        :Keyword Arguments:
            :default: message to print

        :return: string message from class and class._message
        """
        return f"{cls._message}{cls}"


class Sample(Base):
    """sample class for testing"""
    def __init__(self, a: int, b: int):
        """Sample class instance attribute initialization.

        :param a: value to self._a
        :param b: value to self._b
        """
        self._a = a
        self._b = b

    def sum(self) -> int:
        """sum from attr.a with attr.bool

        :return: int depends on sum

        >>> from my_package.factory import Sample
        >>> test_obj = Sample(2, 3)
        >>> test_obj.sum()
        5
        """
        return self._a+self._b

    def subtract(self) -> int:
        """subtract from attr.a by attr.b

        :return: int depends on subtract

        >>> from my_package.factory import Sample
        >>> test_obj = Sample(5,4)
        >>> test_obj.subtract()
        1
        """
        return self._a - self._b

    def _set(instance: Base, args: typing.List[int] = []) -> bool:
        """overriden method, usable only by class not instance.
        :param instance: instance of Sample class
        :Keyword Arguments:
            :args: list to check length
        :return: bool depends on 
        """
        if len(args) == 2:
            instance._a = args[0]
            instance._b = args[-1]
            return True
        return False


if __name__ == "__main__":
    newone = Sample(1, 2)
    print(newone.display(default="call from newone.display()"))
    Sample._set()
    print(Sample._message)
    print(Base._message is Sample._message)
