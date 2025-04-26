# `rename` module
# (c) 2025 JoBe

__author__ = "JoBe"
__github__ = "https://github.com/JoBeGaming/rename/"
__version__ = "1.0"

__all__ = [
    "rename"
]

from sys import version_info
from collections.abc import Callable

if version_info >= (3, 11):
    from typing import Any, Never
else:
    from typing import Any, NoReturn as Never


class rename():
    """
    Rename the object, after which the new name will replace the old one,
    making the old object not callable anymore::

        >>> @rename("hi")
        >>> def hello(name):
        >>>     print(f"Hi: {name}!")
        ...
        >>> # Works
        >>> hi("John")
        Hi: John!
        ...
        >>> # Throws a NameError
        >>> hello("John")

    This also works for classes and methods::
    
        >>> class cls():
        ...
        >>>     @rename("cls.hi", _local=True)
        >>>     def hello(name):
        >>>         print(f"Hi: {name}!")
        ...
        >>> cls.hi("John")
        ...
        >>> # Throws a NameError
        >>> cls.hello("John")


    Attempting to call the old object will raise a NameError,
    that will look like this for the context given above:  
    `Name 'cls.hello' is not defined. Maybe you meant 'cls.hi'?`
    """

    __slots__: tuple[str, ...] = ("func", "_called", "_name")

    # Helper to raise a `TypeError`
    def _error(self) -> Never:
        raise NameError(
            f"Name '{self._name}' is not defined. Maybe you meant '{self.func}'?"
        )

    def __init__(self, func: Callable) -> None:
        self.func = func   
        self._called = False

    def __call__(self, *args, **kwargs) -> Any:
        if not self._called:
            # Rename the old object, without modifying the 
            # `id()` of the object
            globals()[self.func] = args[0]
            globals()[args[0]] = self._error
            self._name = args[0].__name__
            self._called = True
            # Make the old object reroute to
            # `renames._error`, which throws 
            # a `TypeError`:
            #   "Name'{self._name}' is not 
            #   defined. Maybe you meant 
            #   '{self.func}'?" 
            return self._error
        return self.func(*args[1:], **kwargs)
