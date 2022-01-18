from flask import Flask
from flask import request
from flask import jsonify

from peewee import *
from playhouse.shortcuts import model_to_dict

db = PostgresqlDatabase('characters', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db
    
class Characters(BaseModel):
  fullname = CharField()
  house_name = CharField()
  quote = CharField()
  
db.connect()
# db.drop_tables([Character])
# db.create_tables([Character])

# jon = Character(fullname='Jon Snow', house_name='House Stark of Winterfell', quote="If I fall, don't bring me back.")
# jon1 = Character(fullname='Jon Snow', house_name='House Stark of Winterfell', quote='There is only one war that matters. The Great War. And it is here.')
# jon2 = Character(fullname='Jon Snow', house_name='House Stark of Winterfell', quote='Love is the death of duty.')
# jon3 = Character(fullname='Jon Snow', house_name='House Stark of Winterfell', quote='Everything before the word \"but\" is horseshit.')
# jon4 = Character(fullname='Jon Snow', house_name='House Stark of Winterfell', quote="The war is not over. And I promise you, friend, the true enemy won't wait out the storm. He brings the storm.")
# sansa = Character(fullname='Sansa Stark', house_name='House Stark of Winterfell', quote="I hate the king more than any of them.")
# sansa1 = Character(fullname='Sansa Stark', house_name='House Stark of Winterfell', quote="No need to seize the last word, Lord Baelish. I'll assume it was something clever.")
# jaime = Character(fullname='Jaime Lannister', house_name='House Lannister of Casterly Rock', quote="By what right does the wolf judge the lion?")
# tyrion = Character(fullname='Tyrion Lannister', house_name='House Lannister of Casterly Rock', quote="Never forget what you are. The rest of the world will not. Wear it like armour, and it can never be used to hurt you.")
# dany = Character(fullname='Daenerys Targaryen', house_name="House Targaryen of King's Landing", quote="I am the dragon's daughter, and I swear to you that those who would harm you will die screaming.")
# jon.save()
# jon1.save()
# jon2.save()
# jon3.save()
# jon4.save()
# sansa.save()
# sansa1.save()
# jaime.save()
# tyrion.save()
# dany.save()



app = Flask(__name__)

@app.route('/characters', methods=['GET'])
@app.route('/characters/<id>', methods=['GET'])
def character(id=None):
  if id:
    characters = Characters.get(Characters.id == id)
    characters = model_to_dict(characters)
    return jsonify(characters)
  else:
    char = []
    for characters in Characters.select():
      char.append(model_to_dict(characters))
    return jsonify(char)
  
@app.route('/characters/fullname/<fullname>', methods=['GET'])
def fullname(fullname=None):
  if fullname:
    game = []
    for characters in Characters.select().where(Characters.fullname == fullname):
      game.append(model_to_dict(characters))
    if len(game) == 0:
      return jsonify({"Error": "Width not found"})
    else:
      return jsonify(game)

@app.route('/characters/house_name/<house_name>', methods=['GET'])
def house_name(house_name=None):
  if house_name:
    game = []
    for characters in Characters.select().where(Characters.house_name == house_name):
      game.append(model_to_dict(characters))
    if len(game) == 0:
      return jsonify({"Error": "Width not found"})
    else:
      return jsonify(game)

# @app.route('/characters/quote/<quote>', methods=['GET'])
# def quote(quote=None):
#   if quote:
#     characters = Characters.get(Characters.quote == quote)
#     characters = model_to_dict(characters)
#     return jsonify(characters)
#   else:
#     game = []
#     for characters in Characters.select():
#       game.append(model_to_dict(characters))
#     return jsonify(game)



  
app.run(port=9000, debug=True)