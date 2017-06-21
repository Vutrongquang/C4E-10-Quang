from flask import *
import mlab
from mongoengine import *

app = Flask(__name__)

mlab.connect()

class Course(Document):
    image = StringField()
    title = StringField()
    price = FloatField()

course1 = Course(image = "http://hourofcode.vn/wp-content/uploads/2016/05/l%E1%BB%9Bp-h%E1%BB%8Dc-hourofcode1.jpg",
                 title = "Hour of code1",
                 price = 2200000)

# các hàm phải là duy nhất

course1.save()

# image = "http://hourofcode.vn/wp-content/uploads/2015/10/HOUROFCODE.VN_.jpg"
# title = "Hour of code"
# price = "2,500,000 VNĐ"


@app.route('/')
def index():
    return render_template("index.html",courses = Courses()
                           )

@app.route('/add-course', methods= ["GET"])
def add_course():
    return render_template("add_course.html")



@app.route("/about")
def about():
    return " Hi, welcome to Zig Home"

@app.route("/Introduction")
def Introduction():
    return " Hi, Chào mừng tới Zig Home"

@app.route("/News")
def News():
    return " Những thông tin mới nhất"

@app.route("/Courses")
def Courses():
    return " Những khóa học mới nhất"

@app.route("/Library")
def Library():
    return " Thư viện học tập - giải trí"



##url agurement

@app.route("/users/<username>")
def user(username):
    return"Hello my name is "+ username + ", welcome to my page <3"

## template: HTML, static: CSS
@app.route("/add/<int:a>/<int:b>")
def add(a, b):

    return "{0} + {1} = {2}".format(a, b, a+b)

if __name__ == '__main__':
    app.run()
