import requests

from pickle_warehouse import Warehouse
from picklecache import downloader as _downloader

from download_opendatasoft.dl import combine, catalogs

__version__ = '0.0.2'

def download(catalog):
    get = _downloader(requests.get, Warehouse('.opendatasoft'))
    yield from combine(get, catalog)
