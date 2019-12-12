from typing import Any, Tuple

geodesic_version_str: str

class Geod:
    def __init__(
        self, a: float, f: float, sphere: bool, b: float, es: float
    ) -> None: ...
    def __reduce__(self) -> Tuple[Geod, str]: ...
    def __repr__(self) -> str: ...
    def _fwd(
        self, lons: Any, lats: Any, az: Any, dist: Any, radians: bool = False
    ) -> None: ...
    def _inv(
        self, lons1: Any, lats1: Any, lons2: Any, lats2: Any, radians: bool = False
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
    def _line_length(self, lons: Any, lats: Any, radians: bool = False) -> None: ...
    def _polygon_area_perimeter(
        self, lons: Any, lats: Any, radians: bool = False
    ) -> None: ...
