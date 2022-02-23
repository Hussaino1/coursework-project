from application import app, db
from application.models import Coursework
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/coursework', methods=['POST'])
def create_coursework():
    package = request.json
    new_coursework = Coursework(brief=package["brief"])
    db.session.add(new_coursework)
    db.session.commit()
    return Response(f"Added coursework with brief: {new_coursework.brief}", mimetype='text/plain')

@app.route('/read/allCoursework', methods=['GET'])
def read_coursework():
    all_coursework = Coursework.query.all()
    coursework_dict = {"coursework": []}
    for coursework in all_coursework:
        coursework_dict["coursework"].append(
            {
                "id": coursework.id,
                "brief": coursework.brief,
                "finished": coursework.finished
            }
        )
    return jsonify(coursework_dict)

@app.route('/read/coursework/<int:id>', methods=['GET'])
def read_coursework(id):
    coursework = Coursework.query.get(id)
    coursework_dict = {
                    "id": coursework.id,
                    "brief": coursework.brief,
                    "finished": coursework.finished
                }
    return jsonify(coursework_dict)

@app.route('/update/coursework/<int:id>', methods=['PUT'])
def update_coursework(id):
    package = request.json
    coursework = Coursework.query.get(id)
    coursework.brief = package["brief"]
    db.session.commit()
    return Response(f"Updated coursework (ID: {id}) with brief: {coursework.brief}", mimetype='text/plain')

@app.route('/delete/coursework/<int:id>', methods=['DELETE'])
def delete_coursework(id):
    coursework = Coursework.query.get(id)
    db.session.delete(coursework)
    db.session.commit()
    return Response(f"Deleted coursework with ID: {id}", mimetype='text/plain')

@app.route('/finished/coursework/<int:id>', methods=['PUT'])
def finished_coursework(id):
    coursework = Coursework.query.get(id)
    coursework.finished = True
    db.session.commit()
    return Response(f"Coursework with ID: {id} set to finished = True", mimetype='text/plain')

@app.route('/unfinished/coursework/<int:id>', methods=['PUT'])
def unfinished_coursework(id):
    coursework = Coursework.query.get(id)
    coursework.finished = False
    db.session.commit()
    return Response(f"Coursework with ID: {id} set to finished = False", mimetype='text/plain')
