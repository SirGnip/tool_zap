import argparse
import sys
DESC = 'Join each individual line with given character'
EPILOG = 'Example: join.py " " (joins each line with a space)'
parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
parser.add_argument('delimiter', help='Delimiter character or string')
args = parser.parse_args()
lines = sys.stdin.readlines()
lines = [line.rstrip('\n') for line in lines]  # strip off trailing newlines
print(args.delimiter.join(lines))
