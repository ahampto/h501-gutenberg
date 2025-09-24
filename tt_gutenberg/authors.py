from .loader import *


def list_authors(by_languages=True, alias=True):
    if by_languages and alias:
        return load_lang_alias()

    if by_languages and not alias:
        return load_just_lang()

    if alias and not by_languages:
        return just_alias()

    else:
        return no_lang_alias() 