#THIS IS A TUTORIAL ON HOW TO USE AN API (HOW TO REQUEST DATA FROM AN API) WHICH DOES NOT REQUIRE AUTHENTICATION

import requests

#why use an API instead of a static CSV dataset you can download from the web? APIs are useful in the following cases:

#The data is changing quickly. An example of this is stock price data. It doesn’t really make sense to regenerate a dataset and download it every minute — t
#his will take a lot of bandwidth, and be pretty slow.
#You want a small piece of a much larger set of data. Reddit comments are one example.
#What if you want to just pull your own comments on Reddit? It doesn’t make much sense to download the entire Reddit database, then filter just your own comments.
#There is repeated computation involved. Spotify has an API that can tell you the genre of a piece of music.
#You could theoretically create your own classifier, and use it to compute music categories, but you’ll never have as much data as Spotify does.

#An API, or Application Programming Interface, is a server that you can use to retrieve and send data to using code.
#APIs are most commonly used to retrieve data, and that will be the focus of this beginner tutorial.

#example of request from non existing database
#we expect a 404 message which stands for that the request could not find the file we seek

#response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
#print(response.status_code)


#the following contain some of the status codes and their meanings

#301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
#400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
#401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
#403: The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.
#404: The resource you tried to access wasn’t found on the server.
#503: The server is not ready to handle the request.

#Often there will be multiple APIs available on a particular server. Each of these APIs are commonly called endpoints.
# The first endpoint we’ll use is http://api.open-notify.org/astros.json, which returns data about astronauts currently in space.

#request without specifying the endpoint
response = requests.get("https://api.thedogapi.com/")
print(response)

#request specifying that the endpoint is breeds
response = requests.get("https://api.thedogapi.com/v1/breeds")
print(response)
print(response.content)
#print(response.text)

#the same but only works for JSON objects
print(response.json())

#command to distinguish the content type. Mainly this will be JSON but it might be video or image etc.
#JSON is an encoding type
print(response.headers.get("Content-Type"))

#hot to deal with a non JSON object let's say an image

response = requests.get("http://placegoat.com/200/200")
print(response)
print(response.headers.get("Content-Type"))
print(response.content)

#we can see that the content command is not that helpful

#we shall try to save the image in the pc

file = open("goat.jpeg", "wb")
file.write(response.content)
file.close()
#methods for changing the existing data source
#most apis do not allow someone anything more than get the data
#so for the other commands we expect a response code 405 which means that the api developer does not allow users
#other actions
print(requests.post("https://api.thedogapi.com/v1/breeds/1"))
print(requests.get("https://api.thedogapi.com/v1/breeds/1"))
print(requests.put("https://api.thedogapi.com/v1/breeds/1"))
print(requests.delete("https://api.thedogapi.com/v1/breeds/1"))

#QUERY PARAMETERS
#parameters used to filter the data of our request
#for example from a database which randomly generates information about both males and females we only wish to keep the females
#in order to add a query parameter we need the ? symbol to be placed

#we seek the content type
response=requests.get("https://randomuser.me/api/")
print(response.headers.get("Content-Type"))

#it is json so
#male or female
print(requests.get("https://randomuser.me/api/").json())

#we expect a female
print(requests.get("https://randomuser.me/api/?gender=female").json())

#if we want to add another  filter or an other query parameter we use the & symbol as shown below
#let's suppose that we want only females which are fron Norway

print(requests.get("https://randomuser.me/api/?gender=female&nat=no").json())

#APIS THAT REQUIRE AUTHENTICATION

#The most common level of authentication is the API key.
# These keys are used to identify you as an API user or customer and to trace your use of the API.
# API keys are typically sent as a request header or as a query parameter.

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# Replace DEMO_KEY below with your own key if you generated one.
#this cases just demand a name for the api key so the user can be traced
api_key = "DEMO_KEY"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get(endpoint, params=query_params)
print(response.json())

#you can click on the link that shows up in the output window to see the related mars photo
photos = response.json()["photos"]
print(f"Found {len(photos)} photos")
photos[4]["img_src"]

#let's try a different date
api_key = "DEMO_KEY"
query_params = {"api_key": api_key, "earth_date": "2020-07-07"}
response = requests.get(endpoint, params=query_params)
print(response.json())
photos = response.json()["photos"]
print(f"Found {len(photos)} photos")
photos[4]["img_src"]



