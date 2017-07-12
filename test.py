from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_login import LoginManager, UserMixin, current_user, login_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
todos = {}
app.config['SECRET_KEY'] = '12121'

@login_manager.user_loader
def load_user(session_token):
    print('load_user called')
    print('token = ', session_token)
    return None

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login')
def login():
    print('login user called')
    if current_user.is_authenticated:
        print('authencaited', current_user.test())
        # redirect main page
    else:
        print('not authenticated')
        login_user(User('ys', '1'), remember=True)
        
    return "hello world"

class User():
    
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def test(self):
        return self.id

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
    
parser = reqparse.RequestParser()
parser.add_argument(
    'token',
    type=str,
    required=True,
    help='token needed'
)

class TodoSimple(Resource):
    def get(self):
        args = parser.parse_args()
        token = args['token']
        print('token = ', token)
        return {'hello': 'world'}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class Todo3(Resource):
    def get(self):
        s = Serializer('sssdf23e139e13', expires_in=600)
        return {"token": s.dumps({'id': 123}).decode()}, 200

api.add_resource(Todo3, '/todo3', endpoint='test')
api.add_resource(TodoSimple, '/todo1')

if __name__ == '__main__':
    app.run(debug=True)