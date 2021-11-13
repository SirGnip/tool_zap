'''
"Vector, per-lines" commands
The vector of lines is mutated at the "line" level (adding or removing lines)
as opposed to the individual string level (changing characters in each line)

Index operations refer to lines in the text block
'''
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
    return subprocess.run(r'..\src\tool_zap\tools\cli\\' + cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, input=input_text, check=False, text=True).stdout



def test_slice_lines_in_text():
    t = do(d1, 'lines_exp.py "[lines[-2]]')
    assert t == 'mnop\n'

    t = do(d1, 'lines_exp.py "lines[1:3]')
    assert t == '''
ghijkl
mnop
'''.lstrip('\n')

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

def test_replace():
    # replace indexed/sliced line(s) with given line)
    # could be accomplished by composing a delete then an insert
    # replace 2 NEW
    t = do(d1, '''lines_exp.py "lines[:2] + ['NEW',] + lines[3:]"''')
    assert t == '''
abcdef
ghijkl
NEW
qrst
'''.lstrip('\n')

    # may be redundant with "delete & insert"
    # replace 1:3 "NEW LINE"
    t = do(d1, '''lines_exp.py "lines[:1] + ['NEW LINE',] + lines[3:]"''')
    assert t == '''
abcdef
NEW LINE
qrst
'''.lstrip('\n')

def test_insert():
    # insert 1 NEW
    t = do(short, '''lines_exp.py "lines[:1] + ['NEW',] + lines[1:]"''')
    assert t == '''
abcdef
NEW
ghijkl
'''.lstrip('\n')