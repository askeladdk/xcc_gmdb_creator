#
#	XCC Global Mix Database Creator
#	By Askeladd
#

import struct

games = {
	'td' : [
		'td mix description.txt',
		'td extra filenames.txt',
	],

	'ra1' : [
		'ra1 mix description.txt',
		'ra1 extra filenames.txt',
	],

	'ts' : [
		'ts mix description.txt',
		'ts extra filenames.txt',
	],

	'ra2' : [
		'ra2 mix description.txt',
		'ra2 extra filenames.txt',
	],
}

def append_filenames(path, entries):
	f = open(path)
	for line in f:
		s = (line + '\t').split('\t')
		entries[ s[0].strip() ] = s[1].strip()

def write_entries(f_db, entries):
	n_entries = struct.pack('<L', len(entries))
	f_db.write(n_entries)
	for k, v in entries.iteritems():
		s = '%s\x00%s\x00' % (k, v)
		f_db.write(s)

def write_game(f_db, game):
	entries = {}
	for src in game:
		append_filenames(src, entries)
	write_entries(f_db, entries)

f_db = open('global mix database.dat', 'wb')

write_game(f_db, games['td'])
write_game(f_db, games['ra1'])
write_game(f_db, games['ts'])
write_game(f_db, games['ra2'])

f_db.close()
