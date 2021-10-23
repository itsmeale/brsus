from collections import OrderedDict
from enum import Enum
from typing import Dict


class CIDS(Enum):
    CID10: str = "CID10"
    CID9: str = "CID9"


CID_PATTERNS: Dict = {
    CIDS.CID10: OrderedDict(
        file_pattern=lambda state, year: f"DO{state}{year}.DBC",
        cwd_pattern="/dissemin/publicos/SIM/CID10/DORES",
    ),
    CIDS.CID9: OrderedDict(
        file_pattern=lambda state, year: f"DOR{state}{str(year)[-2:].zfill(2)}.DBC",
        cwd_pattern="/dissemin/publicos/SIM/CID9/DORES",
    ),
}
