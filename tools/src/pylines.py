import argparse
import sys
DESC = 'Process entire block of text from stdin with expression.'
EPILOG = 'Example: pylines.py "text[1:3] + text[-1:]'
parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
parser.add_argument('exp', help='Python expression that operates on variable "text"')
args = parser.parse_args()
all_text = sys.stdin.read()
result = eval(args.exp, {}, {'text': all_text})
print(result, end='')

