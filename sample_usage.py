

from src.conllx_df import ConllxDf
from src.conll_utils import get_token_details, get_sentence_column_data, get_children_ids_of, get_parent_id, add_parent_details, add_direction, get_token_count


if __name__ == '__main__':
    conll_file = "./data/sample.conllx"
    conll_df = ConllxDf(conll_file)
    
    # see full conll file:
    print(conll_df.df)
    
    # get single sentence (get the first sentence):
    sen_df = conll_df.get_df_by_id(0)
    
    # get number of tokens in a sentence
    print(get_token_count(sen_df))
    
    # get a full row; details of a token (get details of token 2):
    token_2 = get_token_details(sen_df, 2)
    print(token_2)
    
    # token details of root (token ID = 0):
    print(get_token_details(sen_df, 0))
    
    # invalid token details (of an invalid ID):
    print(get_token_details(sen_df, -1))
    
    # get data of a single column (given the 'FORM' column):
    print(get_sentence_column_data(sen_df, 'FORM'))
    
    # get the IDs of the children of a parent (of ID 1):
    print(get_children_ids_of(sen_df, 1))
    
    # get parent ID (of token ID 4)
    print(get_parent_id(sen_df, 4))
    
    # add parent details to a token dict (adds parent id, form, pos)
    add_parent_details(sen_df, token_2) # call by reference
    
    # adds a direction key (parent comes before child or vice versa)
    add_direction(token_2) # call by reference
    