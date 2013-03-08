#!/usr/bin/python
#
# multi-file rename script for Nautilus
# (c) Andrey Yurovsky http://andrey.thedotcommune.com/
#
# To install, place this script into your .gnome2/nautilus-scripts/ directory,
# which is located in your home directory. 'rename' should appear in your
# 'scripts' menu when you restart Nautilus (or log out and then log in again).
#
# Select one or more files in Nautilus, right-click one of the selected files,
# and choose 'rename' from the 'scripts' menu. A dialog box will ask for a
# new name. Enter a new name, with a starting index in square brackets
# (ex: [1]). The selected files will be renamed to this new name, incrementing
# the index each time. For example, if the new name is "photo[1].jpg", the
# files will be renamed "photo1.jpg", "photo2.jpg", and so on.

import sys
import os
import re

# make sure we're passed at least one file name
if len(sys.argv) < 2:
    sys.exit(1)

# grab file names
files = sys.argv[1:]

# get 'new name' pattern
dialog = os.popen( "zenity --title=\"Rename Files\" --entry --text=name:" )
name = dialog.readline()
dialog.close()

if not name:
    sys.exit(0)

# 'new name' should be "optional words [starting index] optional words"
name_re = re.compile( r'(.*)\[(\d+)\](.*)' )
name_match = name_re.match( name )
if not name_match:
    os.system( "zenity --error --text=\"The name should contain a number in "\
                "square brackets, for example 'photo[1].jpg' is valid.\"" )
    sys.exit(1)
name_parts = name_match.groups()

# grab name parts
name_start = name_parts[0]
name_index = int(name_parts[1])
name_end = name_parts[2].replace( '\n', '' )

# rename each file, incrementing the index each time
i = 0
for file in files:
    new_name = name_start+str(name_index+i)+name_end
    cmd = "mv \""+file+"\" \""+new_name+"\""
    os.system(cmd)
    i += 1
