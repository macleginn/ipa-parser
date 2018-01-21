from sys import argv, exit, stderr
from pprint import pprint

MAIN_GLYPHS_CONS = {
    'ⱱ', #\u2c71
    'β', #\u03b2
    'θ', #\u03b8
    'χ', #\u03c7
    'ᴅ', #\u1d05
    'ᶑ', #\u1d91
    'ʙ', #\u0299
    'ʛ', #\u029
    'ʝ', #\u029d
    'ʟ', #\u029f
    'ʡ', #\u02a1
    'ʐ', #\u0290
    'ʑ', #\u0291
    'ʒ', #\u0292
    'ʔ', #\u0294
    'ʕ', #\u0295
    'ʋ', #\u028
    'ʍ', #\u028d
    'ʎ', #\u028e
    'ɸ', #\u0278
    'ɹ', #\u0279
    'ɺ', #\u027a
    'ɻ', #\u027
    'ɽ', #\u027d
    'ɾ', #\u027e
    'ʀ', #\u0280
    'ʁ', #\u0281
    'ʂ', #\u0282
    'ʃ', #\u0283
    'ʄ', #\u0284
    'ʈ', #\u0288
    'ɰ', #\u0270
    'ɱ', #\u0271
    'ɲ', #\u0272
    'ɳ', #\u0273
    'ɴ', #\u0274
    'ɫ', #\u026
    'ɬ', #\u026c
    'ɭ', #\u026d
    'ɮ', #\u026e
    'ɥ', #\u0265
    'ɦ', #\u0266
    'ɧ', #\u0267
    'ɟ', #\u025f
    'ɠ', #\u0260
    'ɡ', #\u0261
    'g', #g
    'ɢ', #\u0262
    'ɣ', #\u0263
    'ɓ', #\u0253
    'ɕ', #\u0255
    'ɖ', #\u0256
    'ɗ', #\u0257
    'z', #z
    'ç', #\xe7
    'ð', #\xf0
    'ø', #\xf8
    'ħ', #\u0127
    'ŋ', #\u014
    'b', #b
    'c', #c
    'd', #d
    'f', #f
    'h', #h
    'j', #j
    'k', #k
    'l', #l
    'm', #m
    'n', #n
    'p', #p
    'q', #q
    'r', #r
    's', #s
    't', #t
    'v', #v
    'w', #w
    'x', #x
}

# Manners

PLOSIVES = {'b', 'c', 'd', 'g', 'ɡ', 'k', 'p', 'q', 't', 'ɖ', 'ɟ', 'ɢ', 'ʈ', 'ʔ', 'ʡ'}
IMPLOSIVES = {'ɓ', 'ɗ', 'ɠ', 'ʄ', 'ʛ', 'ᶑ'}
NASALS = {'m', 'n', 'ŋ', 'ɱ', 'ɲ', 'ɳ', 'ɴ'}
TRILLS = {'r', 'ʀ', 'ʙ'}
TAPS = {'ɽ', 'ɾ'}
LATERAL_TAPS = {'ɺ'}
FRICATIVES = {'f', 'h', 's', 'v', 'x', 'z', 'ç', 'ð', 'ħ', 'ɕ', 'ɣ', 'ɦ', 'ɸ', 'ʁ', 'ʂ', 'ʃ', 'ʐ', 'ʑ', 'ʒ', 'ʕ', 'ʜ', 'ʝ', 'ʢ', 'β', 'θ', 'χ', 'ƺ', 'ʓ', 'ɧ'}
LATERAL_FRICATIVES = {'ɬ', 'ɮ'}
APPROXIMANTS = {'j', 'w', 'ɥ', 'ɰ', 'ɹ', 'ɻ', 'ʋ', 'ʍ'}
LATERAL_APPROXIMANTS = {'l', 'ɫ', 'ɭ', 'ʎ', 'ʟ'}

# Places

BILABIAL = {'b', 'm', 'p', 'ɸ', 'ʙ', 'β', 'ɓ'}
LABIAL_VELAR = {'w', 'ʍ'}
LABIAL_PALATAL = {'ɥ'}
LABIODENTAL = {'f', 'v', 'ɱ', 'ʋ'}
INTERDENTAL = {'ð', 'θ'}
ALVEOLAR = {'ɗ', 'ɹ', 'ɾ', 'ɮ', 'ɬ', 'r', 't', 'n', 'ɫ', 'l', 'd', 's', 'z', 'ɺ'}
POSTALVEOLAR = {'ʃ', 'ʒ'}
RETROFLEX = {'ɖ', 'ɭ', 'ɳ', 'ɻ', 'ɽ', 'ʂ', 'ʈ', 'ʐ', 'ᶑ'}
ALVEOLO_PALATAL = {'ɕ', 'ʑ'}
PALATAL = {'c', 'j', 'ç', 'ɟ', 'ɲ', 'ʎ', 'ʝ', 'ʄ'}
PALATAL_VELAR = {'ɧ'}
VELAR = {'g', 'ɡ', 'k', 'x', 'ŋ', 'ɣ', 'ɰ', 'ʟ', 'ɠ'}
UVULAR = {'q', 'ɢ', 'ɴ', 'ʀ', 'ʁ', 'χ', 'ʛ'}
PHARYNGEAL = {'ħ', 'ʕ'}
GLOTTAL = {'ʔ', 'h', 'ɦ'}
EPIGLOTTAL = {'ʜ', 'ʢ', 'ʡ'}

# Voiced segs

VOICED = {'b', 'd', 'g', 'ɡ', 'j', 'l', 'm', 'n', 'r', 'v', 'w', 'z', 'ð', 'ŋ', 'ɓ', 'ᶑ', 'ɖ', 'ɗ', 'ɟ', 'ɠ', 'ɢ', 'ɣ', 'ɥ', 'ɦ', 'ɭ', 'ɮ', 'ɰ', 'ɱ', 'ɲ', 'ɳ', 'ɴ', 'ɹ', 'ɺ', 'ɻ', 'ɽ', 'ɾ', 'ʀ', 'ʁ', 'ʄ', 'ʎ', 'ʐ', 'ʑ', 'ʒ', 'ʙ', 'ʛ', 'ʝ', 'ʟ', 'ʢ', 'β', 'ɫ', 'ʓ', 'ʕ'}

def get_CP():
    """Creates an empty parse dict."""
    return {
    'place': None,
    'manner': None,
    'voice': None,
    'length': None,
    'lateral': None,
    'nasal': None,
    'doubly articulated': None,
    'click': None,
    'glyph': None,
    'implosive': None,
    'click': None,
    'pre-features': [],
    'additional articulations': []
    }

# def get_WP():
# return {
    
# }

PRE_MODIFIERS = {
    #ʰt
    '\u02b0': 'pre-aspirated',
    #ˀj
    '\u02c0': 'pre-glottalised',
    #ⁿd
    '\u207f': 'pre-nasalised'
}

POST_MODIFIERS = {
    # Universal modifiers
    #aː
    '\u02d0': 'long',
    #aˑ
    '\u02d1': 'half-long',
    #aˤ
    '\u02e4': 'pharyngealised',
    #ã
    '\u0303': 'nasalised',
    #ă
    '\u0306': 'shortened',
    #a̝
    '\u031d': 'raised',
    #a̞      
    '\u031e': 'lowered',
    #a̟
    '\u031f': 'advanced',
    #a̠
    '\u0320': 'retracted', 
    #a̤
    '\u0324': 'breathy voiced',
    #ḁ
    '\u0325': 'voiceless',
    #å
    '\u030a': 'voiceless',
    #a̰
    '\u0330': 'creaky voiced',
    #a↓
    '\u2193': 'ingressive',

    # Vocalic modifiers
    #a˞
    '\u02de': 'rhotacised',
    #a͈
    '\u0348': 'faucalised',
    #ä
    '\u0308': 'centralised',
    #a̘
    '\u0318': 'ATR',
    #a̙
    '\u0319': 'RTR',
    #a̜
    '\u031c': 'less rounded',
    #a̹
    '\u0339': 'more rounded',
    #a̯
    '\u032f': 'non-syllabic',

    # Consonantal modifiers
    #aʰ
    '\u02b0': 'aspirated',
    #aʱ
    '\u02b1': 'aspirated',
    #aʲ
    '\u02b2': 'palatalised',
    #aʷ
    '\u02b7': 'labialised',
    #t’ / tʼ 
    '\u2019': 'ejective',
    '\u02bc': 'ejective',
    #dˀ
    '\u02c0': 'glottalised',
    #lˠ / l̴
    '\u02e0': 'velarised',
    '\u0334': 'velarised',
    #dˡ
    '\u02e1': 'lateral release',
    #a̚
    '\u031a': 'unreleased',
    #a̩
    '\u0329': 'syllabic',
    #a̪
    '\u032a': 'creaky voice',
    #a͇
    '\u0347': 'alveolar',
    #a̺
    '\u033a': 'apical',
    #a̻
    '\u033b': 'laminal',
    #a͉
    '\u0349': 'weakly articulated',
    #aᶣ
    '\u1da3': 'labio-palatalised',
    #aⁿ
    '\u207f': 'nasal release',
    #tˢ / dᶻ
    '\u02e2': 'affricated',
    '\u1dbb': 'affricated'
}

def eprint(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

def separate_main_glyphs(phon):
    """Assumes that pre-features and additional articulation
    have been taken care of. Failes otherwise."""
    core_els = []
    try:
        for el in phon:
            if el in MAIN_GLYPHS_CONS:
                core_els.append([el, []])
            else:
                core_els[-1][1].append(el)
    except:
        print("Problematic phoneme: %s" % phon)
        exit(1)
    return core_els

def update_parse(old_parse, new_parse):
    """Attempts to extend extendable attributes and set unset ones.
    Doesn't resolve conflicts and fails instead."""
    for k, v in new_parse.items():
        if k not in old_parse:
            raise KeyError("Wrong feature name: %s" % k)
        else:
            if not (isinstance(new_parse[k], str) or isinstance(new_parse[k], bool)):
                raise ValueError('All values in new_parse must be strings or booleans.')
            if old_parse[k] is None:
                old_parse[k] = new_parse[k]
            else:
                try:
                    old_parse[k].append(new_parse[k])
                except AttributeError:
                    print('The feature "%s" is already set with value "%s" and cannot be extended.' % (k, str(old_parse[k])))
                    raise

def parse_single_glyph(g):
    parse = get_CP()

    # Already taken care of
    del parse['glyph']

    # Clicks will not be passed to this function for now
    del parse['click']

    # Cannot infer length without diacritics
    del parse['length']

    # Check for portmanteau glyphs with additional articulations
    if g == 'ɫ':
        update_parse(parse, { 'additional articulations': 'velarised' })

    # 1. Manner: must fill manner, lateral, and nasal:
    if g in PLOSIVES:
        update_parse(parse, { 'manner': 'stop' })
    elif g in IMPLOSIVES:
        update_parse(parse, { 'manner': 'stop' })
        update_parse(parse, { 'implosive': True })
    elif g in NASALS:
        update_parse(parse, { 'manner': 'stop' })
        update_parse(parse, { 'nasal': True })
    elif g in TRILLS:
        update_parse(parse, { 'manner': 'trill' })
    elif g in TAPS:
        update_parse(parse, { 'manner': 'tap' })
    elif g in LATERAL_TAPS:
        update_parse(parse, { 'manner': 'tap' })
        update_parse(parse, { 'lateral': True })
    elif g in FRICATIVES:
        update_parse(parse, { 'manner': 'fricative' })
    elif g in LATERAL_FRICATIVES:
        update_parse(parse, { 'manner': 'fricative' })
        update_parse(parse, { 'lateral': True })
    elif g in APPROXIMANTS:
        update_parse(parse, { 'manner': 'approximant' })
    elif g in LATERAL_APPROXIMANTS:
        update_parse(parse, { 'manner': 'approximant' })
        update_parse(parse, { 'nasal': False })
    else:
        raise ValueError("Unrecognised glyph: %s" % g)
    
    # Fill the defaults
    if parse['nasal']     is None: parse['nasal']     = False
    if parse['lateral']   is None: parse['lateral']   = False
    if parse['implosive'] is None: parse['implosive'] = False

    # 2. Place
    if g in BILABIAL:
        update_parse(parse, { 'place': 'bilabial' })
    elif g in LABIAL_VELAR:
        update_parse(parse, { 'place': 'labio-velar' })
        update_parse(parse, { 'doubly articulated': True })
    elif g in LABIAL_PALATAL:
        update_parse(parse, { 'place': 'labio-palatal' })
        update_parse(parse, { 'doubly articulated': True })
    elif g in LABIODENTAL:
        update_parse(parse, { 'place': 'labio-dental' })
    elif g in INTERDENTAL:
        update_parse(parse, { 'place': 'interdental' })
    elif g in ALVEOLAR:
        update_parse(parse, { 'place': 'alveolar' })
    elif g in POSTALVEOLAR:
        update_parse(parse, { 'place': 'postalveolar' })
    elif g in RETROFLEX:
        update_parse(parse, { 'place': 'retroflex' })
    elif g in ALVEOLO_PALATAL:
        update_parse(parse, { 'place': 'alveolo-palatal' })
    elif g in PALATAL:
        update_parse(parse, { 'place': 'palatal' })
    elif g in PALATAL_VELAR:
        update_parse(parse, { 'place': 'palatal-velar' })
        update_parse(parse, { 'doubly articulated': True })
    elif g in VELAR:
        update_parse(parse, { 'place': 'velar' })
    elif g in UVULAR:
        update_parse(parse, { 'place': 'uvular' })
    elif g in PHARYNGEAL:
        update_parse(parse, { 'place': 'pharyngeal' })
    elif g in GLOTTAL:
        update_parse(parse, { 'place': 'glottal' })
    elif g in EPIGLOTTAL:
        update_parse(parse, { 'place': 'epiglottal' })
    else:
        raise ValueError("Unrecognised glyph: %s" % g)

    if parse['doubly articulated'] is None: parse['doubly articulated'] = False

    # 3. Voice
    # May be overriden due to diacritics later
    if g in VOICED:
        update_parse(parse, { 'voice': 'voiced' })
    else:
        update_parse(parse, { 'voice': 'voiceless' })

    return parse

def is_affricate(glyph_list):
    return (glyph_list[0][0] in PLOSIVES and glyph_list[1][0] in FRICATIVES) or (glyph_list[0][0] + glyph_list[1][0] in {'ɖɽ', 'ʈɽ'})

def parse_affricate(glyph_list, parse):
    pass

def is_bifocal(glyph_list):
    return (glyph_list[0][0] in VELAR and glyph_list[1][0] in BILABIAL) or (glyph_list[0][0] in BILABIAL and glyph_list[1][0] in VELAR)

def parse_bifocal(glyph_list, parse):
    update_parse(parse, { 'doubly articulated': True })
    update_parse(parse, { 'place': 'labio-velar' })
    update_parse(parse, { 'manner': 'stop' })
    s = glyph_list[0][0] + glyph_list[1][0]
    if s in {'ɡb', 'ɠɓ', 'ŋm'}:
        update_parse(parse, { 'voice': 'voiced' })
    else:
        update_parse(parse, { 'voice': 'voiceless' })
    if s == 'ɠɓ':
        update_parse(parse, { 'implosive': True })
    elif s == 'ŋm':
        update_parse(parse, { 'nasal': True })
    # Fill the defaults
    if parse['implosive'] is None:
        update_parse(parse, { 'implosive': False })
    if parse['nasal'] is None:
        update_parse(parse, { 'nasal': False })

def parse_double_glyph(phon, feat_dict):
    glyph_list = separate_main_glyphs(phon)
    # Are you a prenasalised segment?
    if glyph_list[0][0] in NASALS:
        update_parse(feat_dict, { 'pre-features': 'pre-nasalised'})
        extract_core_features(phon[1:], feat_dict)
    elif glyph_list[-1][0] == 'r':
        update_parse(feat_dict, { 'additional articulations': 'trilled release'})
        extract_core_features(phon[:-1], feat_dict)
    elif glyph_list[-1][0] == 'ɾ':
        update_parse(feat_dict, { 'additional articulations': 'flapped'})
        extract_core_features(phon[:-1], feat_dict)
    elif glyph_list[-1][0] in NASALS:
        update_parse(feat_dict, { 'additional articulations': 'nasal release'})
        extract_core_features(phon[:-1], feat_dict)
    elif glyph_list[-1][0] in LATERAL_APPROXIMANTS:
        update_parse(feat_dict, { 'additional articulations': 'lateral release'})
        extract_core_features(phon[:-1], feat_dict)
    elif is_bifocal(glyph_list):
        parse_bifocal(glyph_list, feat_dict)
    elif is_affricate(glyph_list):
        parse_affricate(glyph_list, feat_dict)
    else:
        raise ValueError("Can't parse the string: %s" % phon)

def extract_core_features(phon, feat_dict):
    glyph_list = separate_main_glyphs(phon)
    if len(glyph_list) == 4:
        # We only know /ŋmkp, ŋmɡb/ as of now
        if not glyph_list[0][0] + glyph_list[1][0] == 'ŋm':
            raise ValueError('Unrecognised 4-glyph sequence: %s' % phon)
        update_parse(feat_dict, { 'pre-features': 'pre-nasalised'})
        extract_core_features(phon[2:], feat_dict)
    elif len(glyph_list) == 3:
        # Only pre-nasalised affricates have been met with so far
        if not glyph_list[0][0] in NASALS:
            raise ValueError('Unrecognised 3-glyph sequence: %s' % phon)
        update_parse(feat_dict, { 'pre-features': 'pre-nasalised'})
        extract_core_features(phon[1:], feat_dict)
    elif len(glyph_list) == 2:
        base_parse = parse_double_glyph(phon, feat_dict)
    elif len(glyph_list) == 1:
        base_parse = parse_single_glyph(glyph_list[0][0])
        # The modifiers should've been chopped off by now.
        # If this hasn't happened, something went wrong.
        for el in glyph_list[0][1]:
            if el not in POST_MODIFIERS:
                raise ValueError('Unrecognised modifier or diacritic: \u25cc%s in the phoneme %s' % (el, phon))
        # Resolve possible conflicts
        # For now, only voiced -> voiceless is possible
        if feat_dict['voice'] == 'voiceless' and base_parse['voice'] == 'voiced':
            if not (base_parse['lateral'] or base_parse['nasal'] or base_parse['implosive']):
                feat_dict['voice'] = 'unvoiced'
            del base_parse['voice']
        elif feat_dict['voice'] == 'voiceless' and base_parse['voice'] == 'voiceless':
            eprint('Redundant voicelessness: %s' % phon)
            del base_parse['voice']
        for k,v in base_parse.items():
            if k == 'pre-features' or k == 'additional articulations':
                for el in v:
                    update_parse(feat_dict, { k: el })
            else:
                update_parse(feat_dict, { k: v })
    else:
        raise ValueError("No main glyphs found: %s" % phon)


def parse_consonant(phon):
    # Separate clicks
    # TODO: actually parse them
    for el in ['ǀ', 'ǁ', 'ǂ', 'ǃ', 'ʘ']:
        if el in phon: return { 'click': True }

    # Remove ignored diacritics
    # TODO: check for eventual duplicates at some point
    phon = phon.strip().replace('\u0353', '').replace('\u032c', '')
    parse = get_CP()
    update_parse(parse, { 'click': False })
    update_parse(parse, { 'glyph': phon })

    # Extract pre-features
    while True:
        if phon[0] not in PRE_MODIFIERS: break
        update_parse(parse, { 'pre-features': PRE_MODIFIERS[phon[0]] })
        phon = phon[1:]

    # Extract post-features
    while True:
        if phon[-1] not in POST_MODIFIERS: break
        if POST_MODIFIERS[phon[-1]] == 'voiceless':
            update_parse(parse, { 'voiceless': POST_MODIFIERS[phon[-1]] })
        elif POST_MODIFIERS[phon[-1]] == 'long':
            if parse['length'] is None:
                parse['length'] = 'long'
            elif parse['length'] == 'long':
                parse['length'] = 'overlong'
            else:
                raise ValueError('Incompatible length diacritics: %s' % phon)
        elif POST_MODIFIERS[phon[-1]] == 'half-long':
            if parse['length'] is None:
                parse['length'] = 'long'
            else:
                raise ValueError('Incompatible length diacritics: %s' % phon)
        elif POST_MODIFIERS[phon[-1]] == 'shortened':
            if parse['length'] is None:
                parse['length'] = 'shortened'
            else:
                raise ValueError('Incompatible length diacritics: %s' % phon)
        else:
            update_parse(parse, { 'additional articulations': POST_MODIFIERS[phon[-1]] })
        phon = phon[:-1]

    # Do the rest
    extract_core_features(phon, parse)

    # Fill in the remaining defaults
    if parse['length'] is None:
        parse['length'] = 'short'

    return parse

def parse_vowel(phon):
    pass

# if __name__ == '__main__':
#     if len(argv) < 3:
#         print("Please specify the segment to parse as a first argument and whether this is a consonant (c) or a vowel (v) as the second argument.")
#     else:
#         if argv[2] == 'c':
#             pprint(parse_consonant(argv[1]))
#         else:
#             pprint(parse_vowel(argv[1]))