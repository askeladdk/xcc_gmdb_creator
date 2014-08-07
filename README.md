xcc_gmdb_creator
================

This script allows you to add new filenames to the XCC global mix database.dat by recreating it from a number of mix description files (included).

Usage
=====

1) Add the filenames you want to the appropriate "extra filenames" text file, one filename per line (case is important). You can (optionally) add a file description by seperating the filename and description with a tab on the same line: filename <TAB> description.

2) Execute xcc_gmdb_creator.py with Python and it will create a new global mix database.dat in the current directory.

3) Overwrite the global mix database.dat in the XCC directory with the one you just created.

Credits
=======

The mix description text files were taken from the XCC source.
