"""
"Scalar" commands
The block of text is treated as one long string

Index operations refer to character in text block
"""
import subprocess


d1 = 'abcdef'


def do(input_text, cmd):
    return subprocess.run(r'..\src\tool_zap\tools\cli\\' + cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, input=input_text, check=False, text=True).stdout


def test_initial():
    t = do(d1, 'tzblock_exp.py "text[1]"')
    assert t == 'b'

def test_slice():
    t = do(d1, 'tzblock_exp.py "text[-3]"')
    assert t == 'd'

    t = do(d1, 'tzblock_exp.py "text[1:3]"')
    assert t == 'bc'

def test_counts():
    t = do('abc\ndef ghi\njklm\n', 'tzcounts.py')
    assert t == '16 characters\n4 words\n3 lines\n'

    t = do('\n\n\n', 'tzcounts.py')
    assert t == '2 characters\n0 words\n3 lines\n'

def test_prepend():
    # block_prepend xyz
    t = do(d1, '''tzblock_exp.py "'xyz' + text"''')
    assert t == 'xyzabcdef'

def test_append():
    # block_append xyz
    t = do(d1, '''tzblock_exp.py "text + 'xyz'"''')
    assert t == 'abcdefxyz'

def test_strip():
    # block_strip
    t = do('  abc  ', 'tzblock_exp.py "text.strip()"')
    assert t == 'abc'

    # block_lstrip
    t = do('  abc  ', 'tzblock_exp.py "text.lstrip()"')
    assert t == 'abc  '

    # block_rstrip
    t = do('  abc  ', 'tzblock_exp.py "text.rstrip()"')
    assert t == '  abc'

def test_del():
    # block_del 2
    t = do(d1, 'tzblock_exp.py "text[:2] + text[3:]"')
    assert t == 'abdef'

    # block_del 1:3
    t = do(d1, 'tzblock_exp.py "text[:1] + text[3:]"')
    assert t == 'adef'

def test_replace():
    # block_replace 2 ZZZ
    # could be accomplished by composing a delete than an insert
    t = do(d1, '''tzblock_exp.py "text[:2] + 'ZZZ' + text[3:]"''')
    assert t == 'abZZZdef'

    # block_replace 1:3 ZZZ
    t = do(d1, '''tzblock_exp.py "text[:1] + 'ZZZ' + text[3:]"''')
    assert t == 'aZZZdef'

def test_insert():
    # block_insert 2 ZZZ
    t = do(d1, '''tzblock_exp.py "text[:2] + 'ZZZ' + text[2:]"''')
    assert t == 'abZZZcdef'

def test_sub():
    # block_sub bc ZZZ
    t = do('abcdefabcdef', '''tzblock_exp.py "text.replace('bc', 'ZZZ')"''')
    assert t == 'aZZZdefaZZZdef'
    # Q: Support regex?

# NOTE: delete, replace, insert, and sub are very similar

def test_case():
    # block_upper
    t = do(d1, 'tzblock_exp.py "text.upper()"')
    assert t == 'ABCDEF'

    # block_lower
    t = do('ABCDEF', 'tzblock_exp.py "text.lower()"')
    assert t == 'abcdef'

    # block_title
    t = do('abc def', 'tzblock_exp.py "text.title()"')
    assert t == 'Abc Def'

# Center doesn't make much sense with scalar

def test_split():
    # IDEA: does split have a default delimiter? default to arbitrary-length whitespace (awk style)? Support regex?

    t = do('abc,def,ghi', 'tzsplit.py ,')
    assert t == 'abc\ndef\nghi\n'

    t = do('abc,def,ghi\n123,xyz', 'tzsplit.py ,')
    assert t == 'abc\ndef\nghi\n123\nxyz\n'
