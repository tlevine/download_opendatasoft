from collections import namedtuple
import json

import nose.tools as n

import download_opendatasoft.download_opendatasoft

Response = namedtuple('Response', ['text','ok'])

def test_datasets():
    def get(url):
        return Response(text = '{"datasets":[{"foo":8}]}', ok = True)
    catalog = 'stnoheustahoe'

    observed = download_opendatasoft.download_opendatasoft.datasets(get, catalog)
    expected = [{'foo':8,'catalog':catalog}]
    n.assert_list_equal(observed, expected)
