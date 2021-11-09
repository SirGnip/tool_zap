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


abc
def
ghi

slice 2
line: def
chars: b e g

call once:
- block
- lines
call once per line
- per line

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
    t = do(d1, 'line_exp.py "t[1]"')
    assert t == 'b\nh\nn\nr\n'  # TODO: get rid of trailing newline?

########## Operations on vector (text block treated as a vector  of items, where each line is an item in the vector)
# Index operations refer to lines in the text block
def test_slice_lines_in_text():
    t = do(d1, 'lines_exp.py "[lines[-2]]')
    assert t == 'mnop\n'

    t = do(d1, 'lines_exp.py "lines[1:3]')
    assert t == '''
ghijkl
mnop
'''.lstrip('\n')

def test_slice_chars_in_each_line():
    t = do(short, 'line_exp.py "t[2]"')
    assert t == 'c\ni\n'

    t = do(short, 'line_exp.py "t[0] + \'_\' + t[-2:]"')
    assert t == 'a_ef\ng_kl\n'

def test_counts():
    t = do(short, 'counts.py')
    assert t == '13 characters\n2 words\n2 lines\n'

def test_prepend():
    # prepend X-
    t = do(short, 'line_exp.py "\'x_\' + t')
    assert t == '''
x_abcdef
x_ghijkl
'''.lstrip('\n')

def test_append():
    # append _x
    t = do(short, 'line_exp.py "t + \'_x\'"')
    assert t == '''
abcdef_x
ghijkl_x
'''.lstrip('\n')

def test_strip():
    orig = '''
  abc  def  
  ghi  jkl  '''.lstrip('\n')

    # strip
    t = do(orig, 'line_exp.py "t.strip()')
    assert t == 'abc  def\nghi  jkl\n'

    # lstrip
    t = do(orig, 'line_exp.py "t.lstrip()"')
    assert t == 'abc  def  \nghi  jkl  \n'

    # rstrip
    t = do(orig, 'line_exp.py "t.rstrip()"')
    assert t == '  abc  def\n  ghi  jkl\n'

def test_del_line():
    # del 1
    t = do(d1, 'lines_exp.py "lines[:1] + lines[2:]')
    assert t == '''
abcdef
mnop
qrst
'''.lstrip('\n')

    # del 1:3
    t = do(d1, 'lines_exp.py "[lines[0],] + lines[3:]')
    assert t == '''
abcdef
qrst
'''.lstrip('\n')

def test_del_char_per_line():
    # del 1
    t = do(d1, 'line_exp.py "t[:1] + t[2:]')
    assert t == '''
acdef
gijkl
mop
qst
'''.lstrip('\n')

def test_replace():
    # replace indexed/sliced line(s) with given line)
    # could be accomplished by composing a delete then an insert
    # replace 2 NEW
    t = do(d1, 'lines_exp.py "lines[:2] + [\'NEW\',] + lines[3:]"')
    assert t == '''
abcdef
ghijkl
NEW
qrst
'''.lstrip('\n')

    # may be redundant with "delete & insert"
    # replace 1:3 "NEW LINE"
    t = do(d1, 'lines_exp.py "lines[:1] + [\'NEW LINE\',] + lines[3:]"')
    assert t == '''
abcdef
NEW LINE
qrst
'''.lstrip('\n')

def test_insert():
    # insert 1 NEW
    t = do(short, 'lines_exp.py "lines[:1] + [\'NEW\',] + lines[1:]"')
    assert t == '''
abcdef
NEW
ghijkl
'''.lstrip('\n')

def test_join():
    t = do(d1, 'join.py ,')
    assert t == 'abcdef,ghijkl,mnop,qrst\n'

    t = do(d1 + '\n', 'join.py ,')
    assert t == 'abcdef,ghijkl,mnop,qrst\n'


# Implemented in scalar, but don't make sense to have scalar and vector.
# Could just name with "plain" name and not use the scalar name:
# commands: sub, case

