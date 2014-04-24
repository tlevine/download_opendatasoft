import json

catalogs = [
    'http://data.iledefrance.fr',
    'http://opendata.paris.fr.opendatasoft.com',
    'http://tourisme04.opendatasoft.com',
    'http://tourisme62.opendatasoft.com',
    'http://grandnancy.opendatasoft.com',
    'http://bistrotdepays.opendatasoft.com',
    'http://scisf.opendatasoft.com',
    'http://pod.opendatasoft.com',
    'http://dataratp.opendatasoft.com',
    'http://public.opendatasoft.com',
    'http://ressources.data.sncf.com',
    'http://data.enseignementsup-recherche.gouv.fr',
]

def datasets(get, catalog):
    # Search an OpenDataSoft portal, and add things.
    # I chose OpenDataSoft because they care a lot about metadata.
    response = get(catalog + '/api/datasets/1.0/search?rows=1000000')
    result = json.loads(response.text)['datasets']
    for r in result:
        r['catalog'] = catalog
    return result

def dataset_download(get, catalog, datasetid):
    url = '%s/explore/dataset/%s/download/?format=csv' % (catalog, datasetid)
    return get(url)

def combine(get, catalog):
    '''
    Download everything from an OpenDataSoft catalog.
    '''
    for dataset in datasets(get, catalog):
        dataset['download'] = dataset_download(get, catalog, dataset['datasetid'])
        yield dataset
