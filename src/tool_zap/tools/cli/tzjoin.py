import argparse
import sys
DESC = 'Join each individual line with given character'
EPILOG = 'Example: mycmd | tzjoin " " (joins each line with a space)'
def cli():
    parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
    parser.add_argument('delimiter', help='Delimiter character or string')
    args = parser.parse_args()
    lines = sys.stdin.readlines()
    lines = [line.rstrip('\n') for line in lines]  # strip off trailing newlines
    print(args.delimiter.join(lines))
if __name__ == '__main__': cli()
