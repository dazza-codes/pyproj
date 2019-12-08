from typing import Iterable, Tuple, Union

geodesic_version_str: str

class Geod:
    def __init__(
        self, a: float, f: float, sphere: bool, b: float, es: float
    ) -> None: ...
    def __reduce__(self) -> Tuple[Geod, str]: ...
    def __repr__(self) -> str: ...
    def _fwd(
        self,
        lons: Union[Iterable[float], float],
        lats: Union[Iterable[float], float],
        az: Union[Iterable[float], float],
        dist: Union[Iterable[float], float],
        radians: bool = False,
    ) -> None: ...
    def _inv(
        self,
        lons1: Union[Iterable[float], float],
        lats1: Union[Iterable[float], float],
        lons2: Union[Iterable[float], float],
        lats2: Union[Iterable[float], float],
        radians: bool = False,
    ) -> None: ...
    def _npts(
        self,
        lon1: float,
        lat1: float,
        lon2: float,
        lat2: float,
        npts: int,
        radians: bool = False,
    ) -> None: ...
    def _line_length(
        self,
        lons: Union[Iterable[float], float],
        lats: Union[Iterable[float], float],
        radians: bool = False,
    ) -> None: ...
    def _polygon_area_perimeter(
        self,
        lons: Union[Iterable[float], float],
        lats: Union[Iterable[float], float],
        radians: bool = False,
    ) -> None: ...
