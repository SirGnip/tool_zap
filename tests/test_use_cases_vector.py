"""

# some kind of template formatting where lines get read, parsed into pieces and fed into a template? fstring? variable expansion? regex transform?

# read
index/slice #/#:#  # return only lines that match
stats (char, word, line count)

# mutate
prepend <line>
append <line>
strip r/l/both
del #/#:#  # delete lines
replace #/#:# <str>  # <str> can be a string with embedded newlines

"""
import subprocess

# Remove redundant command and have them only be in the vector side. Only use the scalar/block naming if it absolutely has to be differentiated.


short = '''
abcdef
ghijkl'''.lstrip('\n')

d1 = '''
abcdef
ghijkl
mnop
qrst'''.lstrip('\n')

def do(input_text, cmd):
    return subprocess.run(r'..\tools\src\\' + cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, input=input_text, check=False, text=True).stdout


def test_initial():
    t = do(d1, 'pyline.py "t[1]"')
    assert t == 'b\nh\nn\nr\n'  # TODO: get rid of trailing newline?

########## Operations on vector (text block treated as a vector  of items, where each line is an item in the vector)
# Index operations refer to lines in the text block
def test_slice():
    t = do(d1, 'slice.py -2')
    assert t == 'mnop'

    t = do(d1, 'slice.py 1:3')
    assert t == '''
ghijkl
mnop'''.rstrip('\n')

def test_stats():
    t = do(d1, 'stats.py')
    assert t == '13 characters, 2 words, 2 lines'

def test_prepend():
    t = do(short, 'prepend.py x_')
    assert t == '''
x_abcdef
x_ghijkl'''.rstrip('\n')

def test_append():
    t = do(short, 'append.py _x')
    assert t == '''
abcdef_x
ghijkl_x'''.rstrip('\n')

def test_strip():
    orig = '''
  abc  def  
  ghi  jkl  '''.rstrip('\n')

    t = do(orig, 'strip.py')
    assert t == 'abc  def\nghi  jkl'

    t = do(orig, 'lstrip.py')
    assert t == 'abc  def  \nghi  jkl  '

    t = do(orig, 'rstrip.py')
    assert t == '  abc  def\n  ghi  jkl'

def test_del():
    t = do(d1, 'del 1')
    assert t == '''
abcdef
mnop
qrst'''.lstrip('\n')

    t = do(d1, 'del 1:3')
    assert t == '''
abcdef
qrst'''.lstrip('\n')

def test_replace():
    t = do(d1, 'replace 2 NEW')
    assert t == '''
abcdef
ghijkl
NEW
qrst'''.lstrip('\n')

    # may be redundant with "delete & insert"
    t = do(d1, 'replace 1:3 "NEW LINE"')
    assert t == '''
abcdef
NEW LINE
qrst'''.lstrip('\n')

def test_insert():
    t = do(short, 'insert 1 NEW')
    assert t == '''
abcdef
NEW
ghijkl'''.lstrip('\n')

def test_join():
    t = do(d1, 'join ,')
    assert t == 'abcdef,ghijkl,mnop,qrst'

    t = do(d1 + '\n', 'join ,')
    assert t == 'abcdef,ghijkl,mnop,qrst,'


# Implemented in scalar, but don't make sense to have scalar and vector.
# Could just name with "plain" name and not use the scalar name:
# commands: sub, case

