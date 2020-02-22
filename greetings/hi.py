from . import hello

def sentance_case_to_be_degbugged(s:str):
    """
    >>> sentance_case_to_be_degbugged("camel")
    'Ccamel'
    >>> sentance_case_to_be_degbugged("CAMEL")
    'Ccamel'
    """
    p1 = s[0].upper() 
    p2 = s[0:].lower()
    p3 = p1+p2
    return(p3)

def sentance_case(s:str):
    """
    >>> sentance_case("camel")
    'Camel'
    >>> sentance_case("CAMEL")
    'Camel'
    """
    return(s[0].upper() + s[1:].lower())

def hello_any_world(language:str= 'Swahili'):
    """
    Return hello in most languages

    Examples 
    -------
    >>> hello_any_world("Swahili")
    'Salamu Dunia!'
    >>> hello_any_world("swahili")
    'Salamu Dunia!'
    >>> hello_any_world("French")
    'Bonjour monde!'
    >>> hello_any_world("Francois")
    Traceback (most recent call last):
        ...
    KeyError: 'Francois'
    """
    d = hello.hello_dictionary()
    language = sentance_case(language)
    return d[language]

if __name__ == "__main__":
    import doctest
    # python hi.py (will only tell you if tests failed)
    # python hi.py -v (will show you the number of tests that passed)
    doctest.testmod()
    assert sentance_case_to_be_degbugged("Camel") == "Camel"