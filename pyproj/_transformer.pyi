from typing import Iterable, List, NamedTuple, Union

from pyproj._crs import _CRS, AreaOfUse, Base, CoordinateOperation
from pyproj.enums import TransformDirection

class AreaOfInterest(NamedTuple):
    west_lon_degree: float
    south_lat_degree: float
    east_lon_degree: float
    north_lat_degree: float

class _TransformerGroup:
    _transformers: List[_Transformer]
    _unavailable_operations: List[CoordinateOperation]
    _best_available: bool
    def __init__(
        self,
        crs_from: _CRS,
        crs_to: _CRS,
        skip_equivalent: bool = False,
        always_xy: bool = False,
        area_of_interest: Union[None, AreaOfInterest] = None,
    ) -> None: ...

class _Transformer(Base):
    input_geographic: bool
    output_geographic: bool
    is_pipeline: bool
    skip_equivalent: bool
    projections_equivalent: bool
    projections_exact_same: bool
    type_name: str
    @property
    def id(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def definition(self) -> str: ...
    @property
    def has_inverse(self) -> bool: ...
    @property
    def accuracy(self) -> float: ...
    @property
    def area_of_use(self) -> AreaOfUse: ...
    @property
    def operations(self) -> Union[None, List[CoordinateOperation]]: ...
    @staticmethod
    def from_crs(
        crs_from: _CRS,
        crs_to: _CRS,
        skip_equivalent: bool = False,
        always_xy: bool = False,
        area_of_interest: Union[None, AreaOfInterest] = None,
    ) -> _Transformer: ...
    @staticmethod
    def from_pipeline(proj_pipeline: str) -> _Transformer: ...
    def _transform(
        self,
        inx: Union[Iterable[float], float],
        iny: Union[Iterable[float], float],
        inz: Union[None, Iterable[float], float],
        intime: Union[None, Iterable[float], float],
        direction: Union[str, TransformDirection],
        radians: bool,
        errcheck: bool,
    ) -> None: ...
    def _transform_sequence(
        self,
        stride: int,
        inseq: Union[Iterable[float], float],
        switch: bool,
        direction: Union[str, TransformDirection],
        time_3rd: bool,
        radians: bool,
        errcheck: bool,
    ) -> None: ...
