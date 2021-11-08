import argparse
import sys
DESC = 'Process block of text from stdin with expression split into lines.'
EPILOG = 'Example: pylines.py "lines[1:3] + lines[-1:] (return first, second and last line)'
parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
parser.add_argument('exp', help='Python expression that operates on the lines of text provided at stdin')
args = parser.parse_args()
input_lines = sys.stdin.readlines()
all_lines = [line.rstrip('\n') for line in input_lines]  # strip off trailing newline
result = eval(args.exp, {}, {'lines': all_lines})
if isinstance(result, str):
    raise Exception('Expression returned a string. It must return a list.')
print('\n'.join(result))

