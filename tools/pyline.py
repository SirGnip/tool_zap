import argparse
import sys
parser = argparse.ArgumentParser(description='Process each line from stdin with a Python expression. The line is available as the variable "t"')
parser.add_argument('exp', help='Python expression')
args = parser.parse_args()
for text in sys.stdin.readlines():
    print(eval(args.exp, {}, {'t': text.rstrip('\n')}))
