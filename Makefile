all: base.sqlite3

base.sqlite3: base.sql
	@-rm base.sqlite3
	sqlite3 base.sqlite3 < base.sql

clean:
	@-rm *.pyc base.sqlite3
