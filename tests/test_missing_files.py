import importlib
import sys
import types
import pytest
import tests.streamlit_stub as st

sys.modules['streamlit'] = st


def test_missing_datasets():
    st.errors.clear()
    if 'app' in sys.modules:
        del sys.modules['app']

    pd_stub = types.ModuleType('pandas')

    def raise_fn(*args, **kwargs):
        raise FileNotFoundError('missing')
    pd_stub.read_csv = raise_fn
    sys.modules['pandas'] = pd_stub

    with pytest.raises(RuntimeError):
        importlib.import_module('app')

    assert st.errors
    assert 'dataset' in st.errors[0].lower()
