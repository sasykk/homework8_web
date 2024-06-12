import json
from models import Author
from mongoengine import connect

connect(host="mongodb+srv://sasykk:<password>@cluster0.gtx4smv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)

for author_data in authors_data:
    author = Author(**author_data)
    author.save()
