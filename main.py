"""
API - app ment to be used by other apps
web app vs API built in Python (rendered by data structures such as JSON)
API is ment to be read by computers <>  web app gets particular URL > Python code loads the data and renders the data on our web app
RESTful API - most used API
- we don't need front end interface <> input data (.csv, .txt, .xls) -> output
- get data from API to Python > requests library > JSON file
- debugger > helps to dig deep to understand the data; script gets executed until selected line (1 line before red dot)
    I see all variables declared up to red dot point (api key, content, ...)
    each list is a dictionary > I can get each element

len(content["articles"])
100
for article in content["articles"]:
    print(article["description"])

"""
import requests

api_key = "f252fcca0313459799a5a0253babe579"
# url is an endpoint!
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-27&sortBy=publishedAt&apiKey=f252fcca0313459799a5a0253babe579"

request = requests.get(url)
#content = request.text
content = request.json()
#extract particular values from key-value pair dictionary

# access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])



