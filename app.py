from flask import Flask, jsonify, request, make_response
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from database.database import Student, db
from datetime import datetime


def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/university.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    Session = sessionmaker(bind=db)

    # returns a json with list of all the entrys as jsons, no input expected.    
    @app.route('/students/list', methods=['GET'])
    def list_students():
        try:
            session = Session()
            students = session.query(Student).all()
            result = [student.to_dict() for student in students]
            number_students = len(result)
            resp = {'message': f'All {number_students} students listed!',
                    'status': 200,
                    'data': result
                    }
            session.close()
            return make_response(jsonify(resp))
        except SQLAlchemyError:
            return {'message': 'Database connection error', 'status' : 500}
    

    # expects a json with the new student information and returns it as json
    # returns an error if there is any problem with database like no database file, no session created or wrong type data as input
    # view tests/tests.py for a simple json exemple
    @app.route('/students/add', methods=['POST'])
    def add_student():
        data = request.get_json()
        new_student = Student(
            registry=data['registry'],
            first_name=data['first_name'], 
            last_name=data['last_name'],
            email=data['email'],
            phone_number=data['phone_number'],
            degree=data['degree'],
            birth_date=datetime.strptime(data['birth_date'], '%Y-%m-%d').date())
        try:
            session = Session()
            session.add(new_student)
            session.commit()            
            result = new_student.to_dict()
            session.close()
            resp = {'message': 'New student added!',
                    'status': 201,
                    'data': result
                    }
            return make_response(jsonify(resp))
        except SQLAlchemyError:
            return {'message': 'Database connection error', 'status' : 500}
    

    # expects a json with the information to be updated and returns the updated student as json
    # returns an error if there is any problem with database like no database file, no session created or wrong type data as input
    # view tests/tests.py for a simple json exemple
    @app.route('/students/update', methods=['PATCH'])
    def update_student():
        try:
            session = Session()
            data = request.get_json()
            student = session.get(Student, data['registry'])
            if student:             
                for field, value in data.items():
                    if hasattr(student, field):
                        if field == 'birth_date':
                            setattr(student, field, datetime.strptime(value, '%Y-%m-%d').date())
                        else:
                            setattr(student, field, value)
                session.commit()
                student = session.get(Student, data['registry'])
                result = student.to_dict()
                resp = {'message': 'Student information updated!',
                        'status': 200,
                        'data': result
                        }
                session.close()
                return make_response(jsonify(resp))           
        
            return {'message': 'Student not found!', 'status' : 404}
        except SQLAlchemyError:
            return {'message': 'Database connection error', 'status' : 500}
    

    # expects a registry of thee student in the url and returns the deleted student information
    # returns an error if there is any problem with database like no database file or no session created
    # returns an error if there is no registry
    @app.route('/students/delete/<int:reg>', methods=['DELETE'])
    def delete_student(reg):
        try:
            session = Session()
            student = session.get(Student, reg)
            if student:
                session.delete(student)
                session.commit()
                result = student.to_dict()
                resp = {'message': 'Student deleted!',
                        'status': 200,
                        'data': result
                        }
                session.close()
                return make_response(jsonify(resp))
            else:
                return {'message': 'Student not found!', 'status' : 404}
        except SQLAlchemyError:
            return {'message': 'Database connection error', 'status' : 500}


    return app


if __name__ == '__main__':
    app = create_app()    
    app.run()

    