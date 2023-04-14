from flask_pymongo import PyMongo
import flask


app = flask.Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydb'
mongodb_client = PyMongo(app)
db = mongodb_client.db



@app.route('/create_user')
def create_user():
    user = {
        'name': 'test',
        'last_name': 'test',
        'email': 'test@example.com',
        'password': 'test123'
    }
    db.users.insert_one(user)
    return 'Пользователь успешно создан '

if __name__ == '__main__':
    app.run(debug=True)
