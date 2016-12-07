from logging import info
from re import compile, search, sub


# accentuation problem, pt-br many words have accentuation, but not always it
# is used, for FreqDist we need to take out all accentuation because for
# FreqDist teríamos and teriamos are not the same
def accentuation_replacer(token):
    accentuation_a = compile('[áãâ]')
    accentuation_e = compile('[éẽê]')
    accentuation_i = compile('[íĩî]')
    accentuation_o = compile('[óõô]')
    accentuation_u = compile('[úũû]')

    if accentuation_a.search(token):
        return sub(accentuation_a, 'a', token)
    elif accentuation_e.search(token):
        return sub(accentuation_e, 'e', token)
    elif accentuation_i.search(token):
        return sub(accentuation_i, 'i', token)
    elif accentuation_o.search(token):
        return sub(accentuation_o, 'o', token)
    elif accentuation_u.search(token):
        return sub(accentuation_u, 'u', token)
    else:
        return token

# print('removing accentuation')
def replace_accentuation(tokens):
    info('replacing accetuation...')
    for i in range(len(tokens)):
        tokens[i] = accentuation_replacer(tokens[i])
    return tokens
