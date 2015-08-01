from flask import Flask
from flask import render_template,request,send_from_directory

# flask-peewee bindings
from flask_peewee.db import Database
from peewee import *

# configure our database
DATABASE = {
    'name': 'feedback.db',
    'engine': 'peewee.SqliteDatabase',
}
DEBUG = True
SECRET_KEY = 'sharingan1pythonworkshop'



#the app

app = Flask(__name__,static_url_path='',static_folder='templates')
app.config.from_object(__name__)


# instantiate the db wrapper
db = Database(app)




#the model

class Feedback(db.Model):
    score = IntegerField(null=False)
    feedback = TextField(default="None")
    newThingToLearn = TextField(default="None")


@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        score = request.form['q2']
        some_thing_else = request.form['q4']
        disliked = request.form['q1']
        Feedback.create(score=score,feedback=disliked,newThingToLearn=some_thing_else)


        return "Your response has been recorded "
    return send_from_directory('templates', "index.html")





if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")