import argparse
import sys
DESC = 'Process each line from stdin with a Python expression. The line is available as the variable "t"'
EPILOG = 'Example: pyline.py "t[0] + t[-2:]" (for each line, return first character plus last two characters)'
parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
parser.add_argument('exp', help='Python expression')
args = parser.parse_args()
for text in sys.stdin.readlines():
    print(eval(args.exp, {}, {'t': text.rstrip('\n')}))
