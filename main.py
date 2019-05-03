from flask import Flask, request, render_template
from caesar import rotate_string 
app = Flask(__name__)
app.config['DEBUG'] = True

string1 =''


@app.route('/encrypt', methods = ['POST'])
def encrypt():
    text_to_rotate = request.form['text']
    rotation = request.form['rot']
    encrypted_text = rotate_string(text_to_rotate,int(rotation))
    return '<h1>{}</h1>'.format(encrypted_text)
    

@app.route("/")
def index():
    return render_template('form.html',bigbox = string1)

app.run()