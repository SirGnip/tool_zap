import argparse
import sys
DESC = 'Get basic counts for block of test'
EPILOG = 'Example: counts.py'
parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
args = parser.parse_args()
text = sys.stdin.read()
char_count = len(text)
word_count = len(text.split())
line_count = len(text.split('\n'))
print(f'{char_count} characters\n{word_count} words\n{line_count} lines')