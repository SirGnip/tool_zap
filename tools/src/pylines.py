import argparse
import sys
DESC = 'Process all lines from stdin with expression.'
EPILOG = 'Example: pylines.py "lines[1:3] + lines[-1:]'
parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
parser.add_argument('exp', help='Python expression with lines in list "lines"')
args = parser.parse_args()
lines = sys.stdin.readlines()
result = eval(args.exp, {}, {'lines': lines})
print(''.join(result), end='')

