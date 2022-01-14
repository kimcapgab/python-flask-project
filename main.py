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
  fullname = CharField()
  house_name = CharField()
  quote = CharField()
  
db.connect()
db.drop_tables([Character])
db.create_tables([Character])

jon = Character(fullname='Jon Snow', house_name='House Stark of Winterfell', quote="If I fall, don't bring me back.")
jon1 = Character(fullname='Jon Snow', house_name='House Stark of Winterfell', quote='There is only one war that matters. The Great War. And it is here.')
jon2 = Character(fullname='Jon Snow', house_name='House Stark of Winterfell', quote='Love is the death of duty.')
jon3 = Character(fullname='Jon Snow', house_name='House Stark of Winterfell', quote='Everything before the word \"but\" is horseshit.')
jon4 = Character(fullname='Jon Snow', house_name='House Stark of Winterfell', quote="The war is not over. And I promise you, friend, the true enemy won't wait out the storm. He brings the storm.")
sansa = Character(fullname='Sansa Stark', house_name='House Stark of Winterfell', quote="I hate the king more than any of them.")
sansa1 = Character(fullname='Sansa Stark', house_name='House Stark of Winterfell', quote="No need to seize the last word, Lord Baelish. I'll assume it was something clever.")
jaime = Character(fullname='Jaime Lannister', house_name='House Lannister of Casterly Rock', quote="By what right does the wolf judge the lion?")
tyrion = Character(fullname='Tyrion Lannister', house_name='House Lannister of Casterly Rock', quote="Never forget what you are. The rest of the world will not. Wear it like armour, and it can never be used to hurt you.")
dany = Character(fullname='Daenerys Targaryen', house_name="House Targaryen of King's Landing", quote="I am the dragon's daughter, and I swear to you that those who would harm you will die screaming.")
jon.save()
jon1.save()
jon2.save()
jon3.save()
jon4.save()
sansa.save()
sansa1.save()
jaime.save()
tyrion.save()
dany.save()



app = Flask(__name__)

@app.route('/character', methods=['GET'])
@app.route('/character/<id>', methods=['GET'])
def character(id=None):
  if id:
    character = Character.get(Character.id == id)
    character = model_to_dict(character)
    return jsonify(character)
  else:
    char = []
    for character in Character.select():
      char.append(model_to_dict(character))
    return jsonify(char)
  
@app.route('/fullname/<fullname>', methods=['GET'])
def fullname(fullname=None):
  if fullname:
    character = Character.get(Character.fullname == fullname)
    character = model_to_dict(character)
    return jsonify(character)
  else:
    game = []
    for character in Character.select():
      game.append(model_to_dict(character))
    return jsonify(game)

@app.route('/house_name/<house_name>', methods=['GET'])
def house_name(house_name=None):
  if house_name:
    character = Character.get(Character.house_name == house_name)
    character = model_to_dict(character)
    return jsonify(character)
  else:
    game = []
    for character in Character.select():
      game.append(model_to_dict(character))
    return jsonify(game)

@app.route('/quote/<quote>', methods=['GET'])
def quote(quote=None):
  if quote:
    character = Character.get(Character.quote == quote)
    character = model_to_dict(character)
    return jsonify(character)
  else:
    game = []
    for character in Character.select():
      game.append(model_to_dict(character))
    return jsonify(game)



  
app.run(port=9000, debug=True)