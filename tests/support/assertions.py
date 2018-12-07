import json
import os
from hamcrest import *

from jsonschema import validate, RefResolver
from utils import list_to_set

def get_resolver(schema):
    schema = schema

    schema_path = 'file:////{0}/schemas/'.format(
            os.path.dirname(__file__))

    resolver = RefResolver(schema_path, schema)

    return resolver

def assert_valid_schema(data, schema_file):
    """ Checks whether the given data matches the schema """

    schema = _load_json_schema(schema_file)
    return validate(data, schema, resolver=get_resolver(schema_file))

def _load_json_schema(filename):
    """Loads the given schema file"""

    relative_path = os.path.join('schemas', filename)
    absolute_path = os.path.join(os.path.dirname(__file__), relative_path)

    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())

def assert_valid_response(response, status_code):
    assert response.status_code == status_code
    assert response.headers['Content-Type'] == 'application/json'

def assert_should_be_in(arr, **kwargs):
    payload = arr
    for key in kwargs:
        res_arr = list(filter(lambda item: item[key] == kwargs[key], arr))
        if len(res_arr) == 0:
            raise AssertionError(f"{kwargs} not found in payload {payload}")
        arr = res_arr

def assert_each_has(arr, k, v):
    res_arr = list(filter(lambda item: item[k] != v, arr))
    if len(res_arr) > 0:
        raise AssertionError(f"{res_arr} has not {k}:{v}")

def assert_no_duplicates(arr):
    dset = list_to_set(arr)

    if len(arr) != len(dset):
        raise AssertionError(f"{arr} has duplicates")
