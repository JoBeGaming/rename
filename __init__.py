# `rename` module

# (c) 2025 JoBe

__author__ = "JoBe"
__github__ = "https://github.com/JoBeGaming/rename/"
__version__ = "1.0.1"

from sys import version_info
from collections.abc import Callable
from types import FunctionType

if version_info >= (3, 11):
    from typing import ParamSpec, TypeVar, Never, Generic
else:
    from typing import ParamSpec, TypeVar, NoReturn as Never, Generic


__all__ = [
    "rename",
]


T = TypeVar("T")
P = ParamSpec("P")

# TODO: Implement `local` functionality.
# TODO: Rename `local` to `scoped`?
class rename:
    """
    Rename the object, after which the new name will replace the old one,
    making the old object not callable anymore::

        >>> @rename("hi")
        >>> def hello(name):
        ...     print(f"Hi: {name}!")
        ...
        >>> # Works
        >>> hi("John")
        Hi: John!
        >>> # Throws a NameError
        >>> hello("John")

    This also works for classes and methods::

        >>> class cls():
        ...
        ...     @rename("cls.hi", _local=True)
        ...     def hello(name):
        ...         print(f"Hi: {name}!")
        ...
        >>> cls.hi("John")
        >>>
        >>> # Throws a NameError
        >>> cls.hello("John")


    Attempting to call the old object will raise a NameError,
    that will look like this for the context given above:  
    `Name 'cls.hello' is not defined. Maybe you meant 'cls.hi'?`.
    The docstring of the object will have every mention of the old 
    name renamed to the new one.
    """

    __slots__: tuple[str, ...] = ("func", "_called", "_name")

    # Helper to raise a NameError
    def _error(self) -> Never:
        raise NameError(
            f"Name '{self._name}' is not defined. Maybe you meant '{self.func}'?" #fn.__name__
        )

    def __init__(self, func) -> None:
        self.func = func
        self._called: bool = False

    def __call__(self, *args, **kwargs):
        if self._called:
            return self.func(*args[1:], **kwargs) # just Args?

        # Rename the old object, without modifying the 
        # `id()` of the object
        globals()[self.func] = args[0]
        globals()[args[0]] = self._error

        self._name: str = args[0].__name__
        #self.?.__doc__.replace(?, ?)
        self._called: bool = True

        # Make the old object reroute to
        # `renames._error`, which throws 
        # a NameError:
        #   "Name'{self._name}' is not 
        #   defined. Maybe you meant 
        #   '{self.func}'?" 
        return self._error



class invalid_rename(Generic[P, T]):
    def __init__(self, func: Callable[P,T], name: str):
        self.func = func
        self.name = name

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        if not isinstance(args, tuple): # type: ignore[unnecessaryIsInstance]
            args = (args,) # type: ignore[assignment]
        
        representable_args: list[str] = []
        for arg in args:
            representable_args.append(repr(arg))

        arg_repr = ", ".join(representable_args)

        try:
            raise NameError(
                f"Name '{self.func.__name__}' is not defined; did you mean to do "
                f"{self.name}({arg_repr}, {kwargs or ""})?" #fn.__name__
            )
        except NameError as e:
            raise e from e.__cause__



class rename(Generic[P, T]):
    def __init__(self, name: str, /, *, scoped: bool = False):
        self.name = name
        self.scoped = scoped

    def __getattr__(self, attr: str) -> object:
        print(attr)
        return "EE"
    
    def _repr_(self, func: Callable[P, T], name: str) -> Callable[[], str]:

        def __repr__(self) -> str:
            return repr(func).replace(func.__name__, name)

        return __repr__

    def __call__(self, func: Callable[P, T]) -> invalid_rename[P, T]:
        func.__repr__ = self._repr_(func, self.name)
        globals()[self.name] = func


        if not self.scoped:
            globals()[func.__name__] = invalid_rename(func, self.name)
        else:
            # BUiltins dont have __qualname__?
            # but wrappers can return em
            globals()[func.__qualname__] = invalid_rename(func, self.name) 
            #_make_scope_getattr(...)

        # Make the old object reroute to
        # `invalid_rename`, which throws 
        # a NameError:
        #   "Name'{self._name}' is not 
        #   defined. Maybe you meant 
        #   '{self.func}'?" 

        return invalid_rename(func, self.name)


@rename("fn2")
def fn(a: str, b, c) -> int:
    return 12013


#fn("", 1,c=2)
fn2("", 1,c=2)
print(globals())
