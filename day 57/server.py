from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
age_api = 'https://api.agify.io'
gender_api = 'https://api.genderize.io'

@app.route('/')
def home():
    random_number = random.randint(1,10)
    year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=year)

@app.route('/<name>')
def guess(name):
    params = {'name':name}
    gender_request = requests.get(url=age_api, params=params)
    gender_data = gender_request.json()
    gender = gender_data.get('gender')
    age_request = requests.get(url=age_api, params=params)
    age_data = age_request.json()
    age = age_data.get('age')
    return render_template('guess.html', name=name, gender=gender, age=age)    


@app.route('/blog/<num>')
def blog(num):
    blog_url = 'https://www.npoint.io/docs/c790b4d5cab58020d391'
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts = all_posts)

if __name__ == '__main__':
    app.run(debug=True)