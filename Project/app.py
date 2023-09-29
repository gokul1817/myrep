from flask import *


movie_reviews = {
    1: {"name":"Titanic (1997)","rating": 9, "num_reviews": 10,"link":"https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_FMjpg_UX1000_.jpg","review":["Excellent Movie!"]},
    2: {"name":"Oppenheimer (2023)","rating": 8, "num_reviews": 10,"link":"https://m.media-amazon.com/images/M/MV5BMDBmYTZjNjUtN2M1MS00MTQ2LTk2ODgtNzc2M2QyZGE5NTVjXkEyXkFqcGdeQXVyNzAwMjU2MTY@._V1_.jpg","review":["Awesome Movie!"]},
    3: {"name":"Barbie (2023)","rating": 9, "num_reviews": 10,"link":"https://upload.wikimedia.org/wikipedia/en/0/0b/Barbie_2023_poster.jpg","review":["Super Movie!"]},
}


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('movies.html',movie_reviews=movie_reviews)


@app.route('/movies/<name>')
def movies(name):
    return render_template('detail.html', movie_reviews=movie_reviews,name=name)


@app.route('/Success_for_<name>',methods=['POST','GET'])
def update(name):
    myrating=int(request.form.get('Rate'))
    myreview= request.form.get('review')
    for val in movie_reviews.values():
        if(val["name"]==name):
            num=val["num_reviews"]
            val["num_reviews"]+=1
            val["rating"]=round(((val["rating"]*num)+myrating)/val["num_reviews"],2)
            val["review"].append(myreview)

    return render_template('success.html')


if __name__=='__main__':
    app.run(debug=True)