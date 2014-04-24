import requests

from pickle_warehouse import Warehouse
from picklecache import downloader as _downloader

from download_opendatasoft.download_opendatasoft import download as _download, catalogs

__version__ = '0.0.1'

def download(catalog):
    get = _downloader(requests.get, Warehouse('.opendatasoft'))
    return _download(get, catalog)
