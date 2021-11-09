"""
Enumerate all use cases and see how the current implementation handles them

- let out before/after in most consise way possible for documentation. Then see if you can code it in a similar way.
- list out use cases, then match with commands of how to do it. Then decide if the commands are too opaque.
- TDD
- create testing and then see if my simple commands can satisfy all the tests
- create only the commands I need first? try using the basics/flexible commands and then expand?

slice syntax: # or #:# or :# or #:

### scalar
# read
index/slice # or #:#
stats (char, word, line count)

# mutate
prepend <str>
append <str>
strip r/l/both
del #/#:#
replace #/#:# <str>  # can also handle setting of one char
insert # <str>  # simplification of replace?
sub <match> <target>  # regex?
capital upper/lower/title
center <width>

# type conversion
split <char>
"""
import subprocess


d1 = 'abcdef'


def do(input_text, cmd):
    return subprocess.run(r'..\tools\src\\' + cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, input=input_text, check=False, text=True).stdout


def test_initial():
    t = do(d1, 'block_exp.py "text[1]"')
    assert t == 'b'

########## Operations on scalar (text block treated as one string, operations done on whole block)
# Index operations refer to character in text block
def test_slice():
    t = do(d1, 'block_exp.py "text[-3]"')
    assert t == 'd'

    t = do(d1, 'block_exp.py "text[1:3]"')
    assert t == 'bc'

def test_counts():
    t = do('abc\ndef ghi\njklm\n', 'counts.py')
    assert t == '16 characters\n4 words\n3 lines\n'

    t = do('\n\n\n', 'counts.py')
    assert t == '2 characters\n0 words\n3 lines\n'

def test_prepend():
    # block_prepend xyz
    t = do(d1, '''block_exp.py "'xyz' + text"''')
    assert t == 'xyzabcdef'

def test_append():
    # block_append xyz
    t = do(d1, '''block_exp.py "text + 'xyz'"''')
    assert t == 'abcdefxyz'

def test_strip():
    # block_strip
    t = do('  abc  ', 'block_exp.py "text.strip()"')
    assert t == 'abc'

    # block_lstrip
    t = do('  abc  ', 'block_exp.py "text.lstrip()"')
    assert t == 'abc  '

    # block_rstrip
    t = do('  abc  ', 'block_exp.py "text.rstrip()"')
    assert t == '  abc'

def test_del():
    # block_del 2
    t = do(d1, 'block_exp.py "text[:2] + text[3:]"')
    assert t == 'abdef'

    # block_del 1:3
    t = do(d1, 'block_exp.py "text[:1] + text[3:]"')
    assert t == 'adef'

def test_replace():
    # block_replace 2 ZZZ
    # could be accomplished by composing a delete than an insert
    t = do(d1, '''block_exp.py "text[:2] + 'ZZZ' + text[3:]"''')
    assert t == 'abZZZdef'

    # block_replace 1:3 ZZZ
    t = do(d1, '''block_exp.py "text[:1] + 'ZZZ' + text[3:]"''')
    assert t == 'aZZZdef'

def test_insert():
    # block_insert 2 ZZZ
    t = do(d1, '''block_exp.py "text[:2] + 'ZZZ' + text[2:]"''')
    assert t == 'abZZZcdef'

def test_sub():
    # block_sub bc ZZZ
    t = do('abcdefabcdef', '''block_exp.py "text.replace('bc', 'ZZZ')"''')
    assert t == 'aZZZdefaZZZdef'
    # Q: Support regex?

# NOTE: delete, replace, insert, and sub are very similar

def test_case():
    # block_upper
    t = do(d1, 'block_exp.py "text.upper()"')
    assert t == 'ABCDEF'

    # block_lower
    t = do('ABCDEF', 'block_exp.py "text.lower()"')
    assert t == 'abcdef'

    # block_title
    t = do('abc def', 'block_exp.py "text.title()"')
    assert t == 'Abc Def'

# Center doesn't make much sense with scalar

def test_split():
    # split ,
    t = do('abc,def,ghi', r'''block_exp.py "text.replace(',', '\n')"''')
    assert t == 'abc\ndef\nghi'
    # IDEA: does split have a default delimiter? arbitrary whitespace (awk style). Use regex?



