import os
from django.contrib.gis.utils import LayerMapping
from models import Municipios

municipios_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'limites_field' : 'LIMITES_',
    'limites_id' : 'LIMITES_ID',
    'munic_id' : 'MUNIC_ID',
    'depto_id' : 'DEPTO_ID',
    'depto' : 'DEPTO',
    'municipio' : 'MUNICIPIO',
    'croquis' : 'CROQUIS',
    'geom' : 'MULTIPOLYGON',
}

municipios_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/municipios_raa.shp'))

def run(verbose=True):
    lm = LayerMapping(Municipios, municipios_shp, municipios_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)