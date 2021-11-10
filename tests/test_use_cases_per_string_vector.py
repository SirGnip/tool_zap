"""
"Vector, per-string" commands
The vector of lines is mutated at the individual string level (changing the contents of a line)
as opposed to the line level (adding or removing lines)


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


########## Operations on vector (text block treated as a vector  of items, where each line is an item in the vector)
def test_slice_chars_in_each_line():
    t = do(short, 'line_exp.py "t[2]"')
    assert t == 'c\ni\n'

    t = do(short, '''line_exp.py "t[0] + '_' + t[-2:]"''')
    assert t == 'a_ef\ng_kl\n'

def test_prepend():
    # prepend X-
    t = do(short, '''line_exp.py "'x_' + t''')
    assert t == '''
x_abcdef
x_ghijkl
'''.lstrip('\n')

def test_append():
    # append _x
    t = do(short, '''line_exp.py "t + '_x'"''')
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

def test_del_char_per_line():
    # del 1
    t = do(d1, 'line_exp.py "t[:1] + t[2:]')
    assert t == '''
acdef
gijkl
mop
qst
'''.lstrip('\n')

def test_join():
    t = do(d1, 'join.py ,')
    assert t == 'abcdef,ghijkl,mnop,qrst\n'

    t = do(d1 + '\n', 'join.py ,')
    assert t == 'abcdef,ghijkl,mnop,qrst\n'
