set -e  # Exit immediately if a command exits with a non-zero status.
set -u  # Treat unset variables as an error when substituting.
python pyline.py -h
python pylines.py -h

ls -la | python pyline.py 't.strip()[:3]'
ls -la | python pylines.py 'lines[1:]' | python pyline.py 't[:10]'