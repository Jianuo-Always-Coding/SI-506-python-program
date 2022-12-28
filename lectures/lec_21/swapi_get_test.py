import requests

# 1.0 SWAPI resource URI (Uniform Resource Identifier)
resource = 'https://swapi.py4e.com/api/people/4/'

# 2.0 HTTP GET request / response
# Returns an instance of requests.models.Response
response = requests.get(resource)

# 2.1 response object type
print(f"\nresponse = {type(response)}")

# 3.0 Decode JSON response (to str)
json = response.text # returns a string

print(f"\njson ({type(json)}) = {json}")

# 4.0 Decode JSON response (to dict)
person = response.json() # you will call this regularly

print(f"\nPerson ({type(person)}) = {person}")

# 4.1 Print person name
print(f"\n{person['name']}\n")