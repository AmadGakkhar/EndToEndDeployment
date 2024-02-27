from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", [
    "root_dir",
    "source_url",
    "local_data_file",
    "unzip_dir",
])