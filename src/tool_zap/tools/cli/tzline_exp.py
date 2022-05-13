import argparse
import sys
DESC = 'Process each line from stdin with a Python expression. The line is available as the variable "t". Can also parse line into a row as variable "r".'
EPILOG = 'Example: ls | tzline_exp "t[0] + t[-2:]" (for each line, return first character plus last two characters)'
def cli():
    parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
    parser.add_argument('exp', help='Python expression')
    parser.add_argument('--list', action='store_true', help="Split each line into a list exposed to expression as "r"")
    args = parser.parse_args()
    prev_line = ''
    prev_row = None
    idx = 0
    while True:
        text = sys.stdin.readline()
        if not text: break
        line = text.rstrip('\n')
        env = {'t': line, 'p': prev_line, 'i': idx}
        prev_line = line
        if args.list:
            items = line.split()
            if prev_row is None:
                prev_row = [0] * len(items)
            env['r'] = items
            env['pr'] = prev_row
            prev_row = items
        result = eval(args.exp, {}, env)
        if isinstance(result, str):  # dynamically determine how to output results based on expression's return type
            print(result)  # str
        else:
            print(' '.join([str(r) for r in result]))  # list
        idx += 1
if __name__ == '__main__': cli()
