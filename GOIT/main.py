from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['POST',])
def join():
    if request.method == 'POST':
        try:
            name = request.form['name']
            surname = request.form['surname']
            email = request.form['email']
            sex = request.form['sex']
            with sqlite3.connect("sqlite_python.db") as users:
                cursor = users.cursor()
                cursor.execute("INSERT INTO sqlite_developers (name, surname, email, sex) VALUES (?,?,?,?)",
                               (name, surname, email, sex))
                users.commit()
        except Exception as e:
            return str(e)
    return render_template('index.html')


@app.route('/1', methods=['GET'])
def select():
    try:
        connect = sqlite3.connect('sqlite_python.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM sqlitedb_developers')
        data = cursor.fetchall()
        return render_template('home2.html', data=data)
    except Exception as e:
        return str(e)


@app.route('/2', methods=['GET'])
def select_name():
    if request.method == 'GET':
        try:
            username = request.form['username']
            connect = sqlite3.connect('sqlite_python.db')
            cursor = connect.cursor()
            cursor.execute('SELECT * FROM sqlitedb_developers WHERE name=?', (username,))
            data = cursor.fetchall()
            return render_template('table.html', data=data)
        except Exception as e:
            return str(e)
    else:
        return render_template('home2.html')


@app.route('/3', methods=['DELETE'])
def delete():
    if request.method == 'DELETE':
        try:
            username = request.form['username']
            connect = sqlite3.connect('sqlite_python.db')
            cursor = connect.cursor()
            cursor.execute('DELETE FROM sqlitedb_developers WHERE name=?', (username,))
            connect.commit()
            cursor.close()
        except Exception as e:
            return str(e)
    return render_template('html.html')


@app.route('/4', methods=['PUT'])
def update():
    if request.method == 'PUT':
        try:
            old_username = request.form['old_username']
            new_username = request.form['new_username']
            new_password = request.form['new_password']
            connect = sqlite3.connect('sqlite_python.db')
            cursor = connect.cursor()
            cursor.execute('UPDATE sqlitedb_developers SET username=?, password=? WHERE username=?',
                           (new_username, new_password, old_username,))
            connect.commit()
            cursor.close()
        except Exception as e:
            return str(e)
    return render_template('html.html')


if __name__ == '__main__':
    app.run(port=8000)
