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

jon = Character(full_name='Jon Snow', house_name='House Stark of Winterfell', quote="If I fall, don't bring me back.")
jon1 = Character(full_name='Jon Snow', house_name='House Stark of Winterfell', quote='There is only one war that matters. The Great War. And it is here.')
jon2 = Character(full_name='Jon Snow', house_name='House Stark of Winterfell', quote='Love is the death of duty.')
jon3 = Character(full_name='Jon Snow', house_name='House Stark of Winterfell', quote='Everything before the word \"but\" is horseshit.')
jon4 = Character(full_name='Jon Snow', house_name='House Stark of Winterfell', quote="The war is not over. And I promise you, friend, the true enemy won't wait out the storm. He brings the storm.")
sansa = Character(full_name='Sansa Stark', house_name='House Stark of Winterfell', quote="I hate the king more than any of them.")
sansa1 = Character(full_name='Sansa Stark', house_name='House Stark of Winterfell', quote="No need to seize the last word, Lord Baelish. I'll assume it was something clever.")
jaime = Character(full_name='Jaime Lannister', house_name='House Lannister of Casterly Rock', quote="By what right does the wolf judge the lion?")
tyrion = Character(full_name='Tyrion Lannister', house_name='House Lannister of Casterly Rock', quote="Never forget what you are. The rest of the world will not. Wear it like armour, and it can never be used to hurt you.")
dany = Character(full_name='Daenerys Targaryen', house_name="House Targaryen of King's Landing", quote="I am the dragon's daughter, and I swear to you that those who would harm you will die screaming.")
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
  
  
app.run(port=9000, debug=True)