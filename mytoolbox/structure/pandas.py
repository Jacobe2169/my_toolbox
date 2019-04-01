#coding = utf-8

"""
Module that contains tweaks for Pandas DataFrame.

"""


def highlight_max(s,color="yellow"):
    '''
    Highlight the maximum in a Series yellow.
    '''
    is_max = s == s.max()
    return ['background-color: {0}'.format(color) if v else '' for v in is_max]

def highlight_min(s,color="#d64541"):
    '''
    Highlight the maximum in a Series yellow.
    '''
    is_max = s == s.min()
    return ['background-color:{0};color:white;'.format(color) if v else '' for v in is_max]

def colorize_min_and_max(df,columns):
    """
    Highlight max and min value on specified columns
    
    Parameters
    ----------
    df : pandas.DataFrame
        dataframe
    columns : list of str
        name(s) of the column(s) you want to colorize
    
    Returns
    -------
    pandas.Dataframe
        colorized dataframe
    """

    return df.style.apply(highlight_max,subset=columns).apply(highlight_min,subset=columns)