#!/usr/bin/env python3

import re


_SLUGIFY_MAPA = {
    32: 45,  # space -> hyphen
    33: None,  # exclamation mark
    34: None,  # double quotes
    35: None,  # hash
    36: None,  # dollar
    37: None,  # percent
    38: None,  # ampersand
    39: None,  # simple quote
    40: None,  # open par
    41: None,  # close par
    42: None,  # asterisk
    43: 45,  # plus -> hyphen
    44: None,  # comma
    46: None,  # dot or full stop
    47: 45,  # slash -> hyphen
    58: 45,  # colon -> hyphen
    59: 45,  # semicolon -> hyphen
    60: None,  # open angled bracket
    61: 45,  # equals -> hyphen
    62: None,  # close angled bracket
    63: None,  # question mark
    64: 45,  # @ -> hyphen
    91: None,  # open bracket
    92: 45,  # backslash -> hyphen
    93: None,  # close bracket
    94: 45,  # caret -> hyphen
    95: 45,  # underscore -> hyphen
    96: None,  # grave accent
    123: None,  # open brace
    124: 45,  # pipe -> hyphen
    125: None,  # close brace
    126: 45,  # equivalency sign (~) -> hyphen
    133: 45,  # ellipsis
    191: None,  # open question mark
    193: 65,
    201: 69,
    205: 73,
    209: 78,
    211: 79,
    218: 85,
    220: 85,
    225: 97,  # a
    233: 101,
    237: 105,
    241: 110,
    243: 111,
    250: 117,
    252: 117,
    8230: 45,  # ellipsis
}

_SLUGIFY_PAT_MULTIPLE_HYPHENS = re.compile(r'--+')


def slugify(s: str) -> str:
    global _SLUGIFY_PAT_MULTIPLE_HYPHENS, _SLUGIFY_MAPA
    s = s.lower()
    s = s.replace('ñ', 'ni')
    s = s.replace('€', '-euros')
    s = s.translate(_SLUGIFY_MAPA)
    s = ''.join([_ for _ in s if ord(_) < 129])
    s = _SLUGIFY_PAT_MULTIPLE_HYPHENS.sub('-', s)
    return s
