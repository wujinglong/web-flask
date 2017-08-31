from flask import Flask
from flask_cas import CAS
from flask_cas import login_required

app = Flask(__name__)
app.secret_key = "super secret key"
cas = CAS(app,'/cas')
app.config['CAS_SERVER'] = 'https://cas.uuzu.com'
app.config['CAS_AFTER_LOGIN'] = 'test'
app.config['CAS_VALIDATE_ROUTE'] = '/serviceValidate'

@app.route('/test')
@login_required
def test():
	username = cas.username
	return "test page" + username

@app.route("/")
@login_required
def index():
	username = cas.username
	return "index  " + username

if __name__ == "__main__":
	app.run()