from app import app
from flask import render_template, request, redirect, make_response, jsonify


@app.template_filter('custom_filter')
def custom_filter(a):
    return 'Custom filter + {0}'.format(a)

@app.route("/")
def main():
    return render_template('public/templates/index.html')

@app.route("/about")
def about():
    return '<h1>About</h1>'

@app.route("/sign_up", methods=['GET', 'POST'])
def sig_up():
    if request.method == 'POST':
        req = request.form
    return render_template('public/templates/sign_up.html')

@app.route('/profile/<username>')
def profile(username):


    return render_template('public/templates/profile.html')

@app.route('/json', methods=['POST'])
def json():

    if request.is_json:
        req = request.get_json()
        response = {
            "name":req.get("name")
        }
        res = make_response(jsonify(response), 200)

        return res

    else:
        res = make_response(jsonify({"message":"No json received"}), 400)

    return "no Json received", 400


@app.route("/guestbook")
def guestbook():
    return render_template("public/templates/guestbook.html")

@app.route("/jinja")
def jinja():

    my_name = 'Name'

    langs = ['Python', 'Java', 'C#']

    more = {'Steve':30,
            'John':45,
            'Mete':89,
            'Vere':45}

    other=('Last', 'Lost')

    class New:
        def __init__(self, name, other):
            self.name = name
            self.other = other

        def pull(self):
            return f'Name is {self.name}'

    def repeat(x, qty):
        return x * qty

    my_new=New('First', 'Second')

    return render_template('public/templates/jinja.html',
                           langs=langs,
                           more=more,
                           New=New,
                           repeat=repeat,
                           my_new=my_new,
                           my_name=my_name,
                           other=other)