def safe_execute(default, exception, function, *args):
    """
    Inline Try/Except

    Parameters
    ----------
    default : Object
        value returned in case of failure
    exception : Exception
        type of exception you want to catch
    function : function
        the function to execute
    args
        argument(s) of the function

    >>> def foo(x,y):return x/y
    >>> safe_execute("What did you expect !",ZeroDivisionError,foo,12,0)
    'What did you expect !'
    >>> safe_execute("What did you expect !",ZeroDivisionError,foo,12,3)
    4
    """
    try:
        return function(*args)
    except exception:
        return default