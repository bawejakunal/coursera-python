import sqlite3

conn = sqlite3.connect('organisationdb.sqlite')
cur = conn.cursor()

statement = 'DROP TABLE IF EXISTS Counts'
cur.execute(statement)

statement = 'CREATE TABLE Counts (org TEXT, count INTEGER)'
cur.execute(statement)

conn.commit()

filename = raw_input('Enter filename: ')
if len(filename) < 1:
	filename = 'mbox-short.txt'

handle = open(filename,'r')

for line in handle:
	if line.startswith('From: '):

		domain = line.split()[1].split('@')[1]

		statement = '''SELECT count FROM Counts WHERE org= ?'''
		cur.execute(statement,(domain,))
		
		try:
			row_count = cur.fetchone()[0]
			statement = '''UPDATE Counts SET count=count+1 WHERE org = ?'''
		except:
			statement = '''INSERT INTO Counts (org, count) VALUES (?, 1)'''
		
		cur.execute(statement,(domain,))

conn.commit()
statement = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1'

print 'Organisational Counts:'
for row in cur.execute(statement):
	print str(row[0]), row[1]

cur.close()