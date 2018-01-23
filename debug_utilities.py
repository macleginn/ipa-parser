import json
import pandas as pd

d = pd.read_csv('phoible-phonemes.tsv', sep = '\t')
cons = d.loc[d['Class'] == 'consonant']['Phoneme'].unique()

eur = set()
with open('phono_dbase.json', 'r', encoding='utf-8') as inp:
    db = json.load(inp)
    for v in db.values():
        for c in v['cons']:
            eur.add(c)

pp = lambda x: set.union(*parsePhon(x))

def new2old(parse_dic):
    parse = set()
    parse.add('consonant')
    for k,v in parse_dic.items():
        if k == 'length' and v != 'short':
            parse.add(v)
        elif k == 'nasal' and v:
            parse.add('nasal')
        elif k == 'implosive' and v:
            parse.add('implosive')
        elif k == 'lateral':
            if not v:
                parse.add('non_lateral')
            else:
                parse.add('lateral')
                parse.add('lateral_' + parse_dic['manner'])
        elif k in {'manner', 'place', 'voice'}:
            parse.add(v)
        elif k == 'pre-features' or k == 'additional articulations':
            for el in v:
                parse.add(el)
    # Naming conventions
    if 'stop' in parse:
        parse.remove('stop')
        parse.add('plosive')
    if 'unvoiced' in parse:
        parse.remove('unvoiced')
        parse.add('voiceless')
    if 'ejective' in parse:
        parse.remove('ejective')
        parse.add('glottalised')
    if 'nasal' in parse and 'plosive' in parse:
        parse.remove('plosive')
    if 'labio-dental' in parse:
        parse.remove('labio-dental')
        parse.add('labiodental')
    if 'labio-velar' in parse:
        parse.remove('labio-velar')
        parse.add('labial-velar')
    if 'rhotacised' in parse:
        parse.remove('rhotacised')
        parse.add('rhotic')
    if 'breathy voiced' in parse:
        parse.remove('breathy voiced')
        parse.add('breathy-voiced')
    if 'less rounded' in parse:
        parse.remove('less rounded')
        parse.add('less-rounded')
    if 'RTR' in parse:
        parse.remove('RTR')
        parse.add('retracted-tongue-root')
    if 'labio-palatal' in parse:
        parse.remove('labio-palatal')
        parse.add('labial-palatal')
    return parse

pco = lambda x: new2old(pc(x))

for el in eur:
    try:
        p_old = pp(el)
        p_new = pco(el)
        if p_old != p_new:
            print(el)
            print('Old:', p_old - p_new)
            print('New:', p_new - p_old)
            print()
    except Exception as e:
        print(el, e)
        print()

