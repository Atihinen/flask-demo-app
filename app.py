from flask import Flask, render_template
from services.finnkino import FinnKinoXML
from services.leffatykki import LeffaTykkiRSS
app = Flask(__name__)
fk = FinnKinoXML()
lt = LeffaTykkiRSS()

def get_movies_with_reviews(area_code):
	movie_container = {}
	movies = fk.get_movies_from_area(area_code)
	reviews = lt.get_movie_reviews()
	for id, movie in movies.iteritems():
		review_link = ""
		title = movie['title']
		if title in reviews:
			review_link = reviews[movie['title']]
		movie_container[id] = {
			'title': movie['title'],
			'rating': movie['rating'],
			'genres': "".join(movie['genres']),
			'review': review_link
		}
	return movie_container

@app.route('/')
def index():
	areas = fk.get_area_codes()
	data = {
		'areas': areas
	}
	return render_template('index.html', data=data)

@app.route('/movies/<area>')
def get_movies(area):
	movies = get_movies_with_reviews(area)
	data = {
		'movies': movies
	}
	return render_template('_movies.html', data=data)

if __name__ == "__main__":
	app.run(debug=True)