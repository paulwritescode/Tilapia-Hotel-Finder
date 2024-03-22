from flask import Flask, redirect, render_template, request, url_for

from database import db_session, init_db
from models.restaurants import Restaurants

app = Flask(__name__)

@app.before_request
def init():
    init_db()

# after all the requests are done we will remove the databse session.
@app.teardown_appcontext
def shutdown_session(exception = None):
    db_session.remove()

@app.route('/')
def start():
    return 'This is my first flask project'


@app.route('/create_restaurant', methods=['GET', 'POST'])
def create_restaurant():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        site_url = request.form.get('site_url')

        restaurant = Restaurants(name = name , description = description, site_url = site_url)
        db_session.add(restaurant)
        db_session.commit()

        return redirect(url_for('restaurant_list'))

    return render_template('create_restaurant.html')



# Displaying all list of restaurants
@app.route('/restaurants')
def restaurant_list():
    restaurants = Restaurants.query.all()

    return render_template('restaurant.html', restaurants = restaurants, title = 'Restaurants List')




if __name__ == '__main__':
    # this makes sure that jinja loads and shows the latest template
    # when the page is refreshed the changes will happen
    app.jinja_env.auto_reload = True
    app.run(debug=True)


#This is the first time that i am wornking with vim editor


