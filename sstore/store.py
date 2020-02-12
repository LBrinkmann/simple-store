from smart_open import open
import os
import pandas as pd
import numpy as np
import pickle
import json


AWS_BUCKET = os.environ.get('AWS_BUCKET')


def check_non_existence(key):
    try:
        with open(key):
            return False
    except OSError:
        return True


def create_key(*, project, experiment, name, extension, collection=None):
    assert AWS_BUCKET, 'AWS_BUCKET environment variable is not set.'
    collection = '/{group}' if collection is not None else ''
    return f's3://{AWS_BUCKET}/{project}/{experiment}{collection}/{name}.{extension}'


class MyEncoder(json.JSONEncoder):
    """
    Taken from:
    https://stackoverflow.com/questions/27050108/convert-numpy-type-to-python
    """

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


def store_json(obj, allow_overwrite=False, **keyargs):
    key = create_key(**keyargs, extension='json')
    if not allow_overwrite:
        assert check_non_existence(key), 'File exist already.'
    with open(key, 'w') as f:
        json.dump(obj, f, cls=MyEncoder)


def load_json(**keyargs):
    key = create_key(**keyargs, extension='json')
    with open(key) as f:
        return json.load(f)


def store_obj(obj, allow_overwrite=False,  **keyargs):
    key = create_key(**keyargs, extension='pkl')
    if not allow_overwrite:
        assert check_non_existence(key), 'File exist already.'
    with open(key, 'wb') as f:
        pickle.dump(obj, f)


def load_obj(**keyargs):
    key = create_key(**keyargs, extension='pkl')
    with open(key, 'rb') as f:
        return pickle.load(f)


def store_df(df, allow_overwrite=False,  **keyargs):
    key = create_key(**keyargs, extension='parquet.snappy')
    if not allow_overwrite:
        assert check_non_existence(key), 'File exist already.'
    with open(key, 'wb') as f:
        df.to_parquet(f, compression='snappy')


def load_df(**keyargs):
    key = create_key(**keyargs, extension='parquet.snappy')
    with open(key, 'rb') as f:
        return pd.read_parquet(f)
