from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/lists')
def lists():
    return render_template('list.html')

if __name__== "__main__":
    app.run(debug=True)