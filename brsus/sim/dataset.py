from typing import Tuple

from brsus.interfaces.dataset import DatasetInterface
from brsus.sim.metadata import CID_PATTERNS, CIDS


class DatasetSIM(DatasetInterface):
    def __init__(self, state: str, year: int):
        self.state = state.upper()
        self.year = year
        self.cwd, self.file_name = self.cwd_and_file_name()

    @property
    def _cid(self):
        if self.year <= 1996:
            return CIDS.CID9
        return CIDS.CID10

    def cwd_and_file_name(self) -> Tuple[str, str]:
        return (
            CID_PATTERNS[self._cid]["cwd_pattern"],
            CID_PATTERNS[self._cid]["file_pattern"](self.state, self.year),
        )
