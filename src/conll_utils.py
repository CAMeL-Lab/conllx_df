from dataclasses import dataclass
from typing import List, Union

from pandas.core.frame import DataFrame
from pandas.core.series import Series

@dataclass
class SentenceToken:
    token_id: int
    form: str
    pos: str
    head: int
    deprel: str
    parent_id: int
    parent_form: str
    parent_pos: str
    direction: str

def get_sentence_column_data(sen_df: DataFrame, column_name: str) -> List[Series]:
    """Given a sentence DataFrame, return the data of a column in a list

    Args:
        sen_df (DataFrame): a sentence
        column_name (str): name of column

    Returns:
        list: a column of the DataFrame
    """
    return list(sen_df[column_name])


def get_children_ids_of(sen_df, current_token_id) -> List[int]:
    """Returns a list of ids of the children of the current token.

    Args:
        current_token_id (int): ID of the parent token
        conllx_df (DataFrame): tree data

    Returns:
        List[int]: list of children ids
    """
    # return list(conllx_df[conllx_df['HEAD'] == str(current_token_id)]["ID"])
    return list(sen_df[sen_df['HEAD'] == current_token_id]["ID"])

def get_parent_id(sen_df: DataFrame, current_token_id: int) -> int:
    """gets the id of the parent of the curent token

    Args:
        current_token_id (int): token id
        conllx_df (DataFrame): dependency tree

    Returns:
        int: parent id
    """
    if current_token_id == 0: # root has no parent
        return -1
    return int(sen_df[sen_df['ID'] == current_token_id].to_dict('records')[0]['HEAD'])

def get_token_details(sen_df, tok_id) -> Union[SentenceToken, dict]:
    """Returns a dictionary of token details, in ConllX format"""
    if type(tok_id) == int:
        pass
    elif tok_id.isdigit():
        tok_id = int(tok_id)
    else:
        raise ValueError("invalid parent ID!")
    temp_details = sen_df[sen_df["ID"] == tok_id].to_dict('records')
    
    if temp_details:
        temp_details = temp_details[0]
        return SentenceToken(
            token_id=temp_details['ID'],
            form=temp_details['FORM'],
            pos=temp_details['UPOS'],
            head=temp_details['HEAD'],
            deprel=temp_details['DEPREL'],
            parent_id=-1,
            parent_form="",
            parent_pos="",
            direction=""
        )
    elif tok_id == 0:
        return SentenceToken(
            token_id=0,
            form="ROOT",
            pos="ROOT",
            head=-1,
            deprel="---",
            parent_id=-1,
            parent_form="",
            parent_pos="",
            direction=""
        )
    else:
        return {}

def add_parent_details(sen_df, child: SentenceToken):
    # checks if parent exists and assigns it to parent_df_dict_item
    parent_id = get_parent_id(sen_df, child.token_id)
    
    if parent_df_dict_item := get_token_details(sen_df, parent_id):
        # setattr(child, parent_id, parent_df_dict_item.token_id)
        child.parent_id = parent_df_dict_item.token_id
        child.parent_form = parent_df_dict_item.form
        child.parent_pos = parent_df_dict_item.pos
    else:
        raise ValueError('parent not found')

def add_direction(child: SentenceToken):
    child.direction = 'P-C' if child.parent_id < child.token_id else 'C-P'

def get_token_count(sen_df):
    import pdb; pdb.set_trace()
    return sen_df.shape[0]