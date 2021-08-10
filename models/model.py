from db import DataBase


class Entity:
	def __init__(self, query, data=None):
		self.query = query
		self.data = data
		self.db = DataBase()

	def entity_in(self):
		db = self.db
		try:
			cur = db.con.cursor()
			cur.execute(self.query, self.data)
			db.con.commit()
			db.tutup()

			return True

		except:
			db.create()
			print('table baru di create')

			return False

	def entity_get(self):
		db = self.db
		try:
			cur = db.con.cursor()
			cur.execute(self.query)

			entitas = cur.fetchall()
			db.tutup()

			return entitas
		
		except:
			print('yg kamu cari ga ada')

	def entity_update(self):
		db = self.db

		cur = db.con.cursor()
		cur.execute(self.query, self.data)

		db.con.commit()
		db.tutup()
