from flask import render_template , request

from models import Person

def register_routes(app,db):
    @app.route('/',methods=["GET","POST","HEAD"])
    def index():
        if request.method == 'GET':
          people = Person.query.all()
          return render_template("index.html",people=people)
        elif request.method == 'POST':
          name = request.form.get('name')
          age = request.form.get('age')
          job = request.form.get('job')
          
          person = Person(name=name,age=age,job=job)
          db.session.add(person)
          db.session.commit()
          people = Person.query.all()
          return render_template("index.html",people=people)
        else:
          return "status:ok :)"
    @app.route('/intro',methods=['GET'])  
    def start():
       return render_template("start.html")
    @app.route("/home")
    def home():
       return "This is home page"