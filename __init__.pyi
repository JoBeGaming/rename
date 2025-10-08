from collections.abc import Callable
from typing import Any



def rename(fn: Callable[[], Any] | Callable[..., Any]) -> None: 
    ...