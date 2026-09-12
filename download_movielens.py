import os
import urllib.request
import zipfile

def download_data():
    url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
    file_name = "ml-latest-small.zip"
    print("Downloading MovieLens Dataset...")
    urllib.request.urlretrieve(url, file_name)
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall("data/")
    print("Download and extraction complete.")

if __name__ == "__main__":
    download_data()
