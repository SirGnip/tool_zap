import argparse
import sys
DESC = 'Get basic counts for block of test'
EPILOG = 'Example: ls | tzcounts'
def cli():
    parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
    args = parser.parse_args()
    text = sys.stdin.read()
    if text.endswith('\n'):  # remove final line that is added to output
        text = text[:-1]
    char_count = len(text)
    word_count = len(text.split())
    line_count = len(text.split('\n'))
    print(f'{char_count} characters\n{word_count} words\n{line_count} lines')
if __name__ == '__main__': cli()
