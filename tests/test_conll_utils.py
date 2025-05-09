import pytest

from src.conll_utils import get_all_sentence_form_columns, get_sentence_form_column
from src.conllx_df import ConllxDf

@pytest.fixture
def conllx():
    conll_file = "./data/sample_2.conllx"
    return ConllxDf(conll_file)

def test_get_tree_column(conllx):
   assert get_sentence_form_column(conllx, 0) == 'ف+ اتصل على +ي أحد أصدقاء +ي و+ قال ل +ي : أن +ني متواجد أمام بيت +ك ,'

def test_get_all_sentence_form_columns(conllx):
    df = conllx._df
    assert get_all_sentence_form_columns(conllx) == [
        'ف+ اتصل على +ي أحد أصدقاء +ي و+ قال ل +ي : أن +ني متواجد أمام بيت +ك ,',
        'ف+ نزلت و+ سلمت على +ه قبل أن أسافر ,',
        'و+ بعد +ها جاء أصدقاء +ي و+ ذهبت مع +هم ,',
        'كان في طريق +ي إلى المطار حادث و+ خشيت أن تفوت +ني الرحلة ,',
        'و+ هل س+ يشرحون +ها ?'
    ]