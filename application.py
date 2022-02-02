from flask import Flask, render_template, request
application = app = Flask(__name__)

@application.route("/")
def hello():
    return render_template('index.html')

@application.route("/", methods=['POST'])
def message():
    mes = request.form['text']
    message = "You said: " + mes
    return render_template('index.html', message=message)
    
@application.route("/<string:name>")
def api(name):
    return "<h1>Hello {} this is a flask app</h1>".format(name)

if __name__ == '__main__':
    application.run()
