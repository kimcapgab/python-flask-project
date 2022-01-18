# Game of Thrones Quotes API made with Python and Flask

A list of 20 Game of Thrones Quotes by Characters.

## Running the App

- Fork this repo
- Install and run pipenv shell on your local machine
- run the `main.py` file with the command: `python3 main.py`

## Routes

`/characters` - Will return all 20 quotes

`/characters/<id>` - Will return only one quote that matches the ID number

`/characters/fullname/<fullname>` - Will return the quotes that match the name entered in at the end of the route.
