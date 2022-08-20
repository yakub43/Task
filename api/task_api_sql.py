"""
1 . Write a program to insert a record in sql table via api database
2.  Write a program to update a record via api
3 . Write a program to delete a record via api
4 . Write a program to fetch a record via api
5 . All the above questions you have to answer for mongo db as well .
"""

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akku43@123",
    database="test"
)

# 1 . Write a program to insert a record in sql table via api

@app.route('/insert_record', methods=['GET', 'POST'])
def solution_1():
    if(request.method=='POST'):
        mycursor = mydb.cursor()
        query = "INSERT INTO student (rollno, name, city) VALUES (%s,%s,%s)"
        rollno = request.json['rollno']
        name = request.json['name']
        city = request.json['city']
        val = (rollno, name, city)
        mycursor.execute(query, val)
        mydb.commit()
        row = mycursor.rowcount

        return jsonify((str(row)))


# 2.  Write a program to update a record via api

@app.route('/update_record', methods=['GET', 'POST'])
def solution_2():
    if(request.method=='POST'):
        mycursor = mydb.cursor()
        query = "UPDATE STUDENT SET name = %s WHERE rollno = %s "
        rollno = request.json['rollno']
        name = request.json['name']
        val = (name,rollno)
        mycursor.execute(query, val)
        mydb.commit()
        row = mycursor.rowcount

        return jsonify((str(row)))

# 3 . Write a program to delete a record via api

@app.route('/delete_record', methods=['GET', 'POST'])
def solution_3():
    if(request.method=='POST'):
        mycursor = mydb.cursor()
        query = "DELETE FROM STUDENT WHERE rollno = %s "
        rollno = request.json['rollno']
        val = (rollno,)
        mycursor.execute(query, val)
        mydb.commit()
        row = mycursor.rowcount
        return jsonify((str(row)))

# 4 . Write a program to fetch a record via api
@app.route('/fetch_record', methods=['GET', 'POST'])
def solution_4():
    if(request.method=='POST'):
        mycursor = mydb.cursor()
        query = "SELECT *  FROM STUDENT WHERE rollno = %s "
        rollno = request.json['rollno']
        val = (rollno,)
        mycursor.execute(query, val)
        count = mycursor.fetchone()
        return jsonify((str(count)))


if __name__=='__main__':
    app.run()

