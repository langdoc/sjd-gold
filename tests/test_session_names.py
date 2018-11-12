import glob
import os
import re

session_names = glob.glob("../*.eaf")

for session_name in session_names:
    session_basename = os.path.basename(session_name)
    if re.match(r"sjd", session_basename) == False:
        print('File ' + session_basename + ' incorrectly named!')