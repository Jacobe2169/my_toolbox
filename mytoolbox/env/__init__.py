# coding = utf-8
import sys,os
def type_of_script():
    if "nteract" in str(os.environ): # no jupyter widget integration, thus nteract notebook are considered as terminal (for now!)
        return "terminal"
    try:
        ipy_str = str(type(get_ipython()))
        if 'zmqshell' in ipy_str:
            return 'jupyter'
        if 'terminal' in ipy_str:
            return 'ipython'
    except:
        return 'terminal'

def in_ipython():
    return type_of_script() == "ipython"

def in_notebook():
    """
    Returns ``True`` if the module is running in IPython kernel,
    ``False`` if in IPython shell or other Python shell.
    """
    return  type_of_script() not in  ["terminal","ipython"]

def yes_or_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.
 
    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).
 
    The "answer" return value is one of "yes" or "no".
    """
    if not default in ["yes","no"]:
        raise ValueError("Default argument must be in {yes,no} !")

    valid = {"yes":True,   "y":True,  "ye":False,
             "no":False,     "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
 
    while 1:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid.keys():
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")


def today(to_str=False,str_format="%y_%m_%d_%H_%M"):
    import datetime
    now = datetime.datetime.now()
    if to_str:
        return now.strftime(str_format)
    return now