import time
import datetime
from flask import request
from flask_restful import Resource
from models.model import Entity

class InputBook(Resource):
	def post(self):
		book = request.json['book']
		query = "INSERT INTO books (buku,status) VALUES (?,?)"
		data = (book, 0)
		buku = Entity(query, data)

		if buku.entity_in():
			return {'msg':'buku berhasil di input'}
		else:
			return {'msg':'buku gagal di input'}

class GetBook(Resource):
	def get(self, book):
		query = 'SELECT buku from books WHERE buku = "%s"' % book
		buku = Entity(query)
		return buku.entity_get()

class GetBooks(Resource):
	def get(self):
		query = 'SELECT buku from books'
		buku = Entity(query)
		return buku.entity_get()

class InputStud(Resource):
	def post(self):
		murid = request.json['murid']
		query = "INSERT INTO students (nama) VALUES (?)"
		data = murid,
		stud = Entity(query, data)

		if stud.entity_in():
			return {'msg':'murid berhasil di input'}
		else:
			return {'msg':'murid gagal di input'}

class GetStud(Resource):
	def get(self, stud):
		query = 'SELECT nama from students WHERE nama = "%s"' % stud
		murid = Entity(query)
		return murid.entity_get()

class PinjamBuku(Resource):
	def post(self):
		murid = request.json['murid']
		book = request.json['book'] 
		query = 'SELECT buku from books WHERE status = 0'
		buku = Entity(query)

		for i in  buku.entity_get():
			if book != i[0]: continue 
			que = ''' UPDATE books
	              SET status = ? ,
	                  tanggal_dipinjam = ? ,
	                  peminjam = ?
	              WHERE buku = ?'''

			now = datetime.date.today() 
			data = (1, now.strftime('%Y-%m-%d'), murid, book)
			terpinjam = Entity(que, data)
			terpinjam.entity_update() 

			return {'msg':'buku berhasil di pinjam oleh %s'% murid}
		
		return {'msg':'maaf buku telah di pinjam'}

class BalikinBuku(Resource):
	def post(self):
		book = request.json['book'] 
		query = ''' UPDATE books
	          SET status = ? ,
	              tanggal_dipinjam = ? ,
	              peminjam = ?
	          WHERE buku = ?'''
		data = (0, None, None, book)
		buku = Entity(query, data)
		buku.entity_update() 
		
		return {'msg':'buku telah dikembalikan'}

class Denda(Resource):
	def get(self):
		query = 'SELECT buku, tanggal_dipinjam, peminjam from books WHERE status = 1'
		buku = Entity(query)

		now = int(time.time())
		denda = 0
		limit = 86400 * 3
		tersangka = []
		for i in  buku.entity_get():
			tgl = datetime.datetime.strptime(i[1], '%Y-%m-%d').strftime('%s') 
			selisih = now - int(tgl)
			if selisih < limit: continue

			perhari = int((selisih - limit) / 86400) 
			denda = 5000 * perhari 
			que = ''' UPDATE students
		          SET denda = ? 
		          WHERE nama = ?'''
			terdakwa = (denda, i[-1])
			tersangka.append({'nama': i[-1], 'denda': denda})

			debt = Entity(que, terdakwa)
			debt.entity_update()

		return tersangka


