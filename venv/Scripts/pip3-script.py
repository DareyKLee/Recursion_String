#!C:\Users\Alternate\Computer_Science_II_Projects\Recursion_String\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==9.0.3','console_scripts','pip3'
__requires__ = 'pip==9.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==9.0.3', 'console_scripts', 'pip3')()
    )
