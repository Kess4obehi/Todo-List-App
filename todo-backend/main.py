from flask import Flask, Blueprint
from authentication import auth_bp
from todo_logic import todo_logic_bp

app = Flask('__name__')
app.register_blueprint(auth_bp)
app.register_blueprint(todo_logic_bp)
app.secret_key = 'my_secrete_key'

if __name__ == '__main__':
    app.run(port=3000, debug=True)

    