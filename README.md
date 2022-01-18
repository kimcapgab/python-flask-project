# Game of Thrones Quotes API made with Python and Flask

This API will return a list of 20 Game of Thrones Quotes by Characters.

API Used: https://gameofthronesquotes.xyz/

## Running the App

- Fork this repo
- Install and run pipenv shell on your local machine
- run the `main.py` file with the command: `python3 main.py`

## Routes

`/characters` - Will return all 20 quotes with related character and character's house name.

`/characters/<id>` - Will return only one quote that matches the ID number for that quote.

Example: `/characters/6`

![alt text][id]

[id]: https://res.cloudinary.com/dn2x2ldxj/image/upload/v1642538814/Screen_Shot_2022-01-18_at_3.46.50_PM_rsg84m.png

`/characters/fullname/<fullname>` - Will return all the quotes that match the name entered in at the end of the route.

Example:`/characters/fullname/Jon%20Snow`
![alt text][name]

[name]: https://res.cloudinary.com/dn2x2ldxj/image/upload/v1642538779/Screen_Shot_2022-01-18_at_3.46.14_PM_p5fnza.png

`/characters/house_name/<house_name>` - Will return all the quotes that are related to the matching house name.

Example:`/characters/house_name/House%20Lannister%20of%20Casterly%20Rock`
![alt text][house]

[house]: https://res.cloudinary.com/dn2x2ldxj/image/upload/v1642539148/Screen_Shot_2022-01-18_at_3.52.23_PM_fz3wke.png
