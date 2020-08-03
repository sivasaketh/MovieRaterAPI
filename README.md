# MovieRaterAPI
A Django API to rate movies

## Register Users
Register users with the help of a post request to api/users/
The user and hashed password are stored in DB.
Also, a corresponding token object is also created.

## Authenticate users
Get the token for registered user using post request to auth/
Use that token to access rate movies function

## Rate movies and see ratings of movies
Using the api/movies/ and api/ratings/ we will view, create and update movie ratings

