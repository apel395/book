from flask import Flask
from flask_restful import Api
from resources.api import InputBook, GetBook, GetBooks
from resources.api import InputStud, GetStud
from resources.api import PinjamBuku, BalikinBuku, Denda

app = Flask(__name__)
api = Api(app)

api.add_resource(InputBook, '/buku')
api.add_resource(GetBook, '/buku/<string:book>')
api.add_resource(GetBooks, '/buku/all')
api.add_resource(InputStud, '/stud')
api.add_resource(GetStud, '/stud/<string:stud>')
api.add_resource(PinjamBuku, '/pinjam')
api.add_resource(BalikinBuku, '/balikin')
api.add_resource(Denda, '/denda')
