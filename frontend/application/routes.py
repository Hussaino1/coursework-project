from application import app
from application.forms import CourseworkForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "coursework-app_backend:5000"

@app.route('/')
@app.route('/home')
def home():
    all_courseworks = requests.get(f"http://{backend_host}/read/allCourseworks").json()
    app.logger.info(f"Courseworks: {all_courseworks}")
    return render_template('index.html', title="Home", all_courseworks=all_courseworks["courseworks"])

@app.route('/create/coursework', methods=['GET','POST'])
def create_coursework():
    form = CourseworkForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/coursework",
            json={"brief": form.brief.data}
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_coursework.html", title="Add a new Coursework", form=form)

@app.route('/update/coursework/<int:id>', methods=['GET','POST'])
def update_coursework(id):
    form = CourseworkForm()
    coursework = requests.get(f"http://{backend_host}/read/coursework/{id}").json()
    app.logger.info(f"Coursework: {coursework}")

    if request.method == "POST":
        response = requests.put(
            f"http://{backend_host}/update/coursework/{id}",
            json={"brief": form.brief.data}
        )
        return redirect(url_for('home'))

    return render_template('update_coursework.html', coursework=coursework, form=form)

@app.route('/delete/coursework/<int:id>')
def delete_coursework(id):
    response = requests.delete(f"http://{backend_host}/delete/coursework/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))

@app.route('/finish/coursework/<int:id>')
def finish_coursework(id):
    response = requests.put(f"http://{backend_host}/finish/coursework/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))

@app.route('/unfinished/coursework/<int:id>')
def unfinished_coursework(id):
    response = requests.put(f"http://{backend_host}/unfinished/coursework/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))