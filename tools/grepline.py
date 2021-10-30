import sys
import re
import argparse
DESC = 'Match each line with a Python regex. If groups are in the pattern, only the groups will be output, separated by a delimiter.'
parser = argparse.ArgumentParser(description=DESC)
parser.add_argument('regex', help='Python regex')
parser.add_argument('--groups', action='store_true', help='If pattern has groups, only output the groups')
parser.add_argument('--delimiter', default=' ', help='Choose which delimiter to use when outputting multiple groups (default: space)')
parser.add_argument('--show-match', action='store_true', help='When matched, only show the text that matched')
args = parser.parse_args()
regex_obj = re.compile(args.regex)
for txt in sys.stdin.readlines():
    txt = txt.rstrip('\n')
    match = regex_obj.search(txt)
    if match:
        if args.groups:
            txt = args.delimiter.join(match.groups())
        elif args.show_match:
            txt = match.group()
        print(txt)
