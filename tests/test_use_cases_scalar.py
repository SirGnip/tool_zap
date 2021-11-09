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

def test_prepend():
    t = do(d1, 'block_prepend.py xyz')
    assert t == 'xyzabcdef'

def test_append():
    t = do(d1, 'block_append.py xyz')
    assert t == 'abcdefxyz'

def test_strip():
    t = do('  abc  ', 'block_strip.py')
    assert t == 'abc'

    t = do('  abc  ', 'block_lstrip.py')
    assert t == 'abc  '

    t = do('  abc  ', 'block_rstrip.py')
    assert t == '  abc'

def test_del():
    t = do(d1, 'block_del 2')
    assert t == 'abdef'

    t = do(d1, 'block_del 1:3')
    assert t == 'adef'

def test_replace():
    t = do(d1, 'block_replace 2 ZZZ')
    assert t == 'abZZZdef'

    t = do(d1, 'block_replace 1:3 ZZZ')
    assert t == 'aZZZdef'

def test_insert():
    t = do(d1, 'block_insert 2 ZZZ')
    assert t == 'abZZZcdef'

def test_sub():
    t = do('abcdefabcdef', 'block_sub bc ZZZ')
    assert t == 'aZZZdefaZZZdef'
    # Q: Support regex?

# NOTE: delete, replace, insert, and sub are very similar

def test_case():
    t = do(d1, 'block_upper')
    assert t == 'ABCDEF'

    t = do('ABCDEF', 'block_lower')
    assert t == 'abcdef'

    t = do('abc def', 'block_title')
    assert t == 'Abc Def'

# Center doesn't make much sense with scalar

def test_split():
    t = do('abc,def,ghi', 'split ,')
    assert t == 'abc\ndef\nghi'
    # IDEA: does split have a default delimiter? arbitrary whitespace (awk style). Use regex?



