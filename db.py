import os
import sqlite3

debe = 'test.db'
currentdir = os.path.dirname(os.path.realpath(__file__)) 

class DataBase:
	def __init__(self):
		self.path = os.path.join(currentdir, debe)
		self.con = self.konek()

	def konek(self):
		try:
			return sqlite3.connect(self.path)
		except Error as e:
			print(e)

	def create(self):
		cur = self.con.cursor()
		stud = '''CREATE TABLE IF NOT EXISTS students(
		   id INT PRIMARY KEY,
		   nama TEXT,
		   denda INT
		)'''
		book = '''CREATE TABLE IF NOT EXISTS books(
		   buku CHAR(20) NOT NULL,
		   status INT,
		   tanggal_dipinjam TEXT,
		   peminjam TEXT,
		   FOREIGN KEY (peminjam) REFERENCES students (nama)
		)'''
		cur.execute(stud)
		cur.execute(book)
		self.con.commit()
		self.tutup()

	def tutup(self):
		self.con.close()
