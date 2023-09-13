from flask import *
from markupsafe import escape

app = Flask(__name__, template_folder='templates')

@app.route('/index')
@app.route('/')
def hello_workd(): return 'Hello, World!'
#@app.route('/users/<username>')
#def get_user(username) : return 'User %s' % escape(username)
#@app.route('/posts/<int:post_id>')
#def get_post(post_id) : return 'Post %d' % post_id
#@app.route('/uuid/<uuid:uuid>')
#def get_uuid(uuid) : return 'uuid %s' % escape(uuid)