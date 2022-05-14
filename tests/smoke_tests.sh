#!/bin/bash
# Do a basic smoke test that runs all the CLI commands and make sure they don't fail. Also serves as basic examples.

set -e  # Exit immediately if a command exits with a non-zero status.
set -u  # Treat unset variables as an error when substituting.


txt=$(cat <<MYDOC
south 3 2800 0.12 5/22/2021 blue
north 2 3550 0.08 7/23/2022 red
nw 1 4320 0.09 11/09/2021 red
island 2 3300 0.10 2/03/2022 yellow
south 2 3000 0.25 4/07/2022 red
nw 3 1100 0.04 5/20/2021 blue
nw 2 1500 0.05 5/23/2021 yellow
north 3 3500 0.02 12/03/2022 blue
island 1 800 0.05 7/07/2022 yellow
south 1 7030 0.08 1/05/2021 red
MYDOC
)

mainhdr() {
    echo
    echo ==================== $1 ====================
}

hdr() {
    echo
    echo "--> $1"
}


mainhdr "help output"
tzcounts --help
tzline_exp --help
tzlines_exp --help
tzblock_exp --help
tzjoin --help
tzsplit --help
tzgrepline --help


mainhdr tzcounts
echo "$txt" | tzcounts


mainhdr tzline_exp
hdr line-based
echo "$txt" | tzline_exp "f'#{i} {len(t)} {len(p)}'"
hdr list-based
echo "$txt" | tzline_exp --list "[r[0], r[4], r[2], pr[2], str(int(float(r[3])*100)) + '%', r[5].upper(), len(t), len(p)]"
hdr filter
echo "$txt" | tzline_exp --list "r[5]=='blue'" | tzline_exp --list "r[5], r[0], r[4]"


mainhdr tzlines_exp
hdr "first two lines and last two lines"
echo "$txt" | tzlines_exp "lines[:2] + lines[-2:]"


mainhdr tzblock_exp
hdr "first 10 characters and last 10 characters"
echo "$txt" | tzblock_exp "text[:10] + '\n' + text[-10:]"


mainhdr tzsplit
echo "$txt" | tzsplit " "


mainhdr tzjoin
echo "$txt" | tzjoin "|"


mainhdr tzgrepline
hdr "Match regex"
echo "$txt" | tzgrepline "^\S+ \d+"
hdr "Print lines that match, only showing the part of the string that matched the regex"
echo "$txt" | tzgrepline --show-match "^\S+ \d+"
hdr "Print lines that match, only showing text in the groups"
echo "$txt" | tzgrepline --groups "^\S+ (\d+)"
hdr "Print lines that match, only showing text in multiple groups, seprarated by given delimiter"
echo "$txt" | tzgrepline --groups --delimiter _ "^\S+ (\d+) \d+ (\S+)"
