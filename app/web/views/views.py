from flask.views import MethodView
from flask import g, current_app, request, jsonify, Response
from app.web.models.models import Applicant

class TempView(MethodView):


    def post(self):
        print 'in get!!!'
        try:
            action = request.json['action']
        except KeyError:
            return Response(response='Must Have Action',status=400,mimetype='text/html')
        try:
            name = request.json['name']
        except KeyError:
            return Response(response='Must Have Name',status=400,mimetype='text/html')

        try:
            password = request.json['password']
        except KeyError:
            return Response(response='Must Have Password', status=400, mimetype='text/html')

        if action == 'create':
            response = self.user_create(name, password)
        elif action == 'login':
            response = self.user_login(name, password)
        else:
            return Response(response='Must Have Correct Action',status=400,mimetype='text/html')


        return response

    def options(self):

        return jsonify({'Allow': 'POST'}, 200, {'Access-Control-Allow-Origin': '*',
                                                'Access-Control-Allow-Methods': 'POST,GET'})

    def user_create(self, name, password):
        pw_hash = current_app.bcrypt.generate_password_hash(
            current_app.config['SALT'] + password + current_app.config['SALT'])

        applicant = Applicant(name=name, password=pw_hash)
        applicant.save()
        return Response(response='OK', status=200, mimetype='text/html')

    def user_login(self, name, password):
        print 'in user login'
        pw_hash = current_app.config['SALT'] + password + current_app.config['SALT']
        applicant = Applicant.query.filter_by(name=name).first()

        if applicant:
            print 'In applicant'
            validate = current_app.bcrypt.check_password_hash(applicant.password, pw_hash)
            if validate:
                str = 'Applicant name = ' + applicant.name
                print str
                return Response(response=str, status=200, mimetype='text/html')

            else:
                return Response(response='wrong password',status=400,mimetype='text/html')

        else:
            print 'No Aplicant'
            return Response(response='applicant not found', status=400, mimetype='text/html')
