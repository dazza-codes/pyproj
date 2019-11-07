from array import array
from typing import Iterable, List, Tuple, Union

AnyArrayOrScalar = Union[Iterable, List, Tuple, float, int, array]
geodesic_version_str: str

class Geod:
    def __init__(
        self, a: float, f: float, sphere: bool, b: float, es: float
    ) -> None: ...
    def __reduce__(self) -> Tuple[Geod, str]: ...
    def __repr__(self) -> str: ...
