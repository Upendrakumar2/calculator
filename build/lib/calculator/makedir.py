import os
import argparse
import logging
import sys
import tarfile

import pandas as pd
from six.moves import urllib  # pyright:ignore

# make dirs with mode

def data_ingest(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="path for the training dataset", type=str)
    parser.add_argument("--log-level",help="logging level",type=str,choices=["DEBUG", "WARNING", "INFO", "ERROR"],)
    parser.add_argument("--log-path", help="Log file path", type=str)
    parser.add_argument("--no-console-log",help="Log to console",type=str,choices=["False", "True"],)

    args = parser.parse_args()
    print(args)

    if args.path is None:
        HOUSING_PATH = os.path.join("datasets", "housing")
    else:
        HOUSING_PATH = os.path.join(args.path, "housing")

    logger = logging.getLogger(__name__)
    formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

    print(logger)

    if args.log_path is not None:
            os.makedirs(args.log_path, exist_ok=True)
            file_handler = logging.FileHandler(os.path.join(args.log_path, "ingest_data.log"))
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    if args.no_console_log == "False" or args.no_console_log is None:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
    HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

    def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
        os.makedirs(housing_path, exist_ok=True)
        tgz_path = os.path.join(housing_path, "housing.tgz")
        urllib.request.urlretrieve(housing_url, tgz_path)
        housing_tgz = tarfile.open(tgz_path)
        housing_tgz.extractall(path=housing_path)
        housing_tgz.close()

    def load_housing_data(housing_path=HOUSING_PATH):
        csv_path = os.path.join(housing_path, "housing.csv")
        return pd.read_csv(csv_path)

    fetch_housing_data()
    housing = load_housing_data()

if __name__ == "__main__":
    data_ingest(sys.argv)