import requests
import tarfile
import os
import pandas as pd


def download_data():
    url = "https://github.com/ageron/data/raw/main/housing.tgz"
    tgz = "./data/housing.tgz"
    target_folder = "./data"
    csv = os.path.join(target_folder, "housing", "housing.csv")

    if os.path.isfile(csv):
        return csv

    res = requests.get(url)
    with open(tgz, "wb") as f:
        f.write(res.content)

    with tarfile.open(tgz) as f:
        f.extractall(target_folder)

    return csv


# def split_test_and_train(df, test_ratio=0.2):
#     test_size = round(len(df) * test_ratio)
#     index = list(df.index)
#     np.random.shuffle(index)
#     return df.iloc[index[:test_size]], df.iloc[index[test_size:]]


raw = pd.read_csv(download_data())

