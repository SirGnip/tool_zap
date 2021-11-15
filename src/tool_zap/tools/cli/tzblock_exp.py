import argparse
import sys
DESC = 'Process entire block of text from stdin with expression.'
EPILOG = 'Example: pyblock.py "text[:10] + text[-10:] (first 10 characters and last 10 characters)'
def cli():
    parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
    parser.add_argument('exp', help='Python expression that operates on variable "text"')
    args = parser.parse_args()
    all_text = sys.stdin.read()
    result = eval(args.exp, {}, {'text': all_text})
    print(result, end='')
if __name__ == '__main__': cli()
