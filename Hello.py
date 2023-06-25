from flask import Flask

app = Flask(__name__)

@app.route('/users/TommyLee')
#@app.route('username')
def get_user(username) : return username

@app.route('/posts/123')
def get_post(post_id) : return str(post_id)

@app.route('/uuid/23947-sdkfh12-ajh4dfhs-djdh2')
def get_uuid(uuid) : return str(uuid)