import argparse
import sys
DESC = 'Using a delimiter, split text into individual lines'
EPILOG = 'Example: mycmd | tzsplit , (splits text into a new line at each comma, existing newlines are preserved)'
def cli():
    parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
    parser.add_argument('delimiter', help='Delimiter character or string')
    args = parser.parse_args()
    text = sys.stdin.read()
    if text.endswith('\n'):  # remove final line that is added to output
        text = text[:-1]
    print(text.replace(args.delimiter, '\n'))
if __name__ == '__main__': cli()
