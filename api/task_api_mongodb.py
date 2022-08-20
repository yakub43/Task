
"""
1 . Write a program to insert a record in sql table via api database
2.  Write a program to update a record via api
3 . Write a program to delete a record via api
4 . Write a program to fetch a record via api
5 . All the above questions you have to answer for mongo db as well .
"""

from flask import Flask, request, jsonify
import mysql.connector
import pymongo


client = pymongo.MongoClient("mongodb+srv://james43:james123@cluster0.1vlp1xz.mongodb.net/?retryWrites=true&w=majority")

mydb = client["API_TEST"]
collection = mydb["Student"]

app = Flask(__name__)

# 1 . Write a program to insert a record in sql table via api

@app.route('/insert_record_mongodb', methods=['GET', 'POST'])
def solution_1():
    if(request.method=='POST'):
        rollno = request.json["rollno"]
        name = request.json["name"]
        city = request.json["city"]
        record = {"rollno" : rollno, "name" : name, "city" : city}
        col = collection.insert_one(record)
        return jsonify((str(col.inserted_id)))


# 2.  Write a program to update a record via api
@app.route('/update_record_mongodb', methods=['GET', 'POST'])
def solution_2():
    if(request.method=='POST'):
        name = request.json["name"]
        old = {"name" : "james"}
        update = {"$set" : {"name" : name}}
        col = collection.update_one(old,update)
        return jsonify((str(col.modified_count)))

# 3 . Write a program to delete a record via api
@app.route('/delete_record_mongodb', methods=['GET', 'POST'])
def solution_3():
    if (request.method == 'POST'):
        rollno = request.json["rollno"]
        query = {"rollno" : rollno}
        col = collection.delete_one(query)
        return jsonify((str(col.deleted_count)))

# 4 . Write a program to fetch a record via api
@app.route('/fetch_record_mongodb', methods=['GET', 'POST'])
def solution_4():
    if (request.method == 'POST'):
        col = collection.find_one()
        return jsonify((str(col)))

if __name__=='__main__':
    app.run()
