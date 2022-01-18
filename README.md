# Game of Thrones Quotes API made with Python and Flask

This API will return a list of 20 Game of Thrones Quotes by Characters.

API Used: https://gameofthronesquotes.xyz/

## Running the App

- Fork this repo
- Install and run pipenv shell on your local machine
- run the `main.py` file with the command: `python3 main.py`

## Routes

`/characters` - Will return all 20 quotes with related character and character's house name.

Example:

`/characters/<id>` - Will return only one quote that matches the ID number for that quote.

Example:

`/characters/fullname/<fullname>` - Will return all the quotes that match the name entered in at the end of the route.

Example:

`/characters/house_name/<house_name>` - Will return all the quotes that are related to the matching house name.

Example:
