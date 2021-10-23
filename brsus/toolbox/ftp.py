from ftplib import FTP

from brsus.interfaces.dataset import DatasetInterface


class FTPWrapper:
    def __init__(self, url: str, dataset: DatasetInterface):
        self.url = url
        self.ftp = FTP(url)
        self.ftp.login()
        self.dataset = dataset

    def download(self, destination: str = None):
        cwd, file_name = self.dataset.cwd_and_file_name()
        file_destination = file_name
        self.ftp.cwd(cwd)

        print(destination)
        if destination:
            file_destination = destination

        with open(file_destination, "wb") as f:
            self.ftp.retrbinary(f"RETR {file_name}", f.write)
