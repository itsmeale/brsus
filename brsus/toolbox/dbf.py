import csv
import subprocess

import pandas as pd
from dbfread import DBF


class DBC:
    """Encapsulate the behavior of DBC decompression,
    DBC conversion to CSV and DBC conversion to parquet.
    """

    def __init__(self, file_name: str):
        self.file_name = file_name

    def decompress(self, destination: str):
        subprocess.call(["./thirdy_part/blast-dbf", self.file_name, destination])

    def _dbf_data(self, dbf_file_name):
        yield from DBF(dbf_file_name)

    def to_csv(self, destination: str):
        decompressed_dbf = f"{''.join(destination.split(r'.')[:-1])}.DBF"
        self.decompress(decompressed_dbf)
        data = self._dbf_data(decompressed_dbf)

        with open(destination, "w") as f:
            header = next(data)
            writer = csv.DictWriter(f, fieldnames=header.keys())
            writer.writeheader()
            writer.writerow(header)
            writer.writerows(data)

    def to_parquet(self, destination: str):
        self.to_csv(destination)
        pd.read_csv(destination).to_parquet(destination, engine="pyarrow")


if __name__ == "__main__":
    my_dbc = DBC("data/DOSP2018.DBC")
    my_dbc.to_parquet("data/dataset.csv")
