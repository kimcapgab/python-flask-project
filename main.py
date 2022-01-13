from re import fullmatch
from flask import Flask
from flask import request
from flask import jsonify

from peewee import *
from playhouse.shortcuts import model_to_dict

db = PostgresqlDatabase('game', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db
    
class Character(BaseModel):
  full_name = CharField()
  house_name = CharField()
  quote = CharField()
  
db.connect()
db.drop_tables([Character])
db.create_tables([Character])

jon = Character(full_name='Jon Snow', house_name='House Stark of Winterfell', quote='There is only one war that matters. The Great War. And it is here.')

jon.save()


app = Flask(__name__)

@app.route('/character', methods=['GET'])
@app.route('character/<id>', methods=['GET'])
def person(id=None):
  if id:
    character = Character.get(Character.id == id)
    character = model_to_dict(character)
    return jsonify(character)
  else:
    char = []
    for character in Character.select():
      char.append(model_to_dict(character))
    return jsonify(char)
  
  
app.run(port=900, debug=True)