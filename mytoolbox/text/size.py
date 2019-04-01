import os

def blocks(files, size=65536):
    while True:
        b = files.read(size)
        if not b: break
        yield b

def wc_l(text_input_fn):
    """
    Count the number of line in a file
    
    Parameters
    ----------
    text_input_fn : str
        filepath
    
    """
    if not os.path.exists(text_input_fn):
        raise FileNotFoundError("{0} does not exists !".format(text_input_fn))

    with open(text_input_fn, "r",encoding="utf-8",errors='ignore') as f:
        return (sum(bl.count("\n") for bl in blocks(f)))