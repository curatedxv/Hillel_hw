from sqlite3 import connect

from flask import Flask, request, render_template, redirect
import sqlite3
app = Flask(__name__)
'''
/login [GET, POST]

/register [GET, POST]

/logout [GET ? POST ?? DELETE]

/profile (/user, /me) [GET, DELETE]

      ?  /favouties [GET, POST, DELETE]

      ??  /favouties/<favourite_id> [GET, DELETE]

      ?  /search_history [GET, DELETE]

/items [GET, POST]

/items/<item_id> [GET, DELETE]

/leasers [GET]

/leasers/<leaser_id> [GET]

/contracts [GET, POST]

/contracts/<contract_id> [GET, PATCH/PUT]

/search [GET, POST]

/complain [POST]

/compare [GET, PUT]
'''

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class Database(object):
    def __init__(self, filename):
        self.con = sqlite3.connect('db1.db')
        self.con.row_factory = dict_factory
        self.cur = self.con.cursor()
    def __enter__(self):
        return self.cur
    def __exit__(self, type, value, traceback):
        self.con.commit()
        self.con.close()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        return 'POST'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        with Database('db1.db') as cur:
            form_data = request.form
            cur.execute('''INSERT INTO user 
            (login, password, ipn, full_name, contacs, photo, passport) 
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
  (form_data['login'], form_data['password'], form_data['ipn'], form_data['full_name'], form_data['contacts'], form_data['photo'], form_data['passport']))
        with Database('db1.db') as cur:
            cur.execute('SELECT * FROM user')
            user = cur.fetchall()
            return render_template('register_sub.html', user=user)

@app.route('/logout', methods=['GET', 'POST', 'DELETE'])
def logout():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'
    if request.method == 'DELETE':
        return 'DELETE'

@app.route('/profile', methods=['GET', 'DELETE'])
def profile():
    if request.method == 'GET':
        return render_template('user.html')
    if request.method == 'DELETE':
        return 'DELETE'

@app.route('/profile/favouties', methods=['GET', 'POST', 'DELETE'])
def favouties():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'
    if request.method == 'DELETE':
        return 'DELETE'

@app.route('/profile/favouties/<favourite_id>', methods=['GET', 'DELETE'])
def favourite(favourite_id):
    if request.method == 'GET':
        return f'GET {favourite_id}'
    if request.method == 'DELETE':
        return f'DELETE {favourite_id}'

@app.route('/profile/search_history', methods=['GET', 'DELETE'])
def search_history():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'DELETE':
        return 'DELETE'
@app.route('/items',  methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        with Database('db1.db') as cur:
            cur.execute('SELECT * FROM item')
            items = cur.fetchall()
            return render_template('items.html', items=items)
    if request.method == 'POST':
        with Database('db1.db') as cur:
            form_data = request.form
            cur.execute('''INSERT INTO item
            (photo, name, description, price_hour, price_day, price_week, price_month)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
  (form_data['photo'], form_data['name'], form_data['description'], form_data['price_hour'], form_data['price_day'], form_data['price_week'], form_data['price_months']))
            return redirect('/items')

@app.route('/items/<item_id>', methods=['GET', 'DELETE'])
def item(item_id):
    if request.method == 'GET':
        return f'GET {item_id}'
    if request.method == 'DELETE':
        return f'DELETE {item_id}'

@app.route('/leasers', methods=['GET'])
def leasers():
    if request.method == 'GET':
        return 'GET'
@app.route('/leasers/<leaser_id>', methods=['GET'])
def leaser(leaser_id):
    if request.method == 'GET':
        return f'GET {leaser_id}'

@app.route('/contracts', methods=['GET', 'POST'])
def contracts():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'

@app.route('/contracts/<contract_id>', methods=['GET', 'PATCH', 'PUT'])
def contract(contract_id):
    if request.method == 'GET':
        return f'GET {contract_id}'
    if request.method == 'PATCH':
        return f'DELETE {contract_id}'
    if request.method == 'PUT':
        return f'PATCH {contract_id}'

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'

@app.route('/complain', methods=['GET', 'POST'])
def complain():
    if request.method == 'GET':
        return render_template('complain.html')
    if request.method == 'POST':
        with Database('db1.db') as cur:
            form_data = request.form
            cur.execute('''INSERT INTO feedback
            (author, user, text, grade, contract)
            VALUES (?, ?, ?, ?, ?)''',
  (form_data['author'], form_data['user'], form_data['text'], form_data['grade'], form_data['contract']))
            return render_template('complain_sub.html')

@app.route('/compare', methods=['GET', 'PUT'])
def compare():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'PUT':
        return 'PUT'


if __name__ == '__main__':
    app.run(debug=True)
