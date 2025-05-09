import pytest

from src.conll_utils import get_tree_column
from src.conllx_df import ConllxDf

@pytest.fixture
def df():
    conll_file = "./data/sample.conllx"
    return ConllxDf(conll_file)

def test_get_tree_column(df):
    get_tree_column(df, 0, 1)