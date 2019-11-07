from typing import List, NamedTuple, Union

from pyproj._crs import _CRS, Base, CoordinateOperation

class AreaOfInterest(NamedTuple):
    west_lon_degree: float
    south_lat_degree: float
    east_lon_degree: float
    north_lat_degree: float

class _TransformerGroup:
    _transformers: List[Transformer]
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
    input_geographic = False
    output_geographic = False
    self._input_radians = {}
    self._output_radians = {}
    self._area_of_use = None
    self.is_pipeline = False
    self.skip_equivalent = False
    self.projections_equivalent = False
    self.projections_exact_same = False
    self.type_name = "Unknown Transformer"
    self._operations = None
