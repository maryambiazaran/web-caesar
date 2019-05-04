from flask import Flask, request, render_template
from caesar import rotate_string 
app = Flask(__name__)
app.config['DEBUG'] = True

rotation = 0
encrypted_text =''

@app.route('/', methods = ['POST'])
def encrypt():
    error = ''
    text_to_rotate = request.form['text']
    rotation = request.form['rot']
    try:
        rotation = int(rotation)
        encrypted_text = rotate_string(text_to_rotate,rotation)
        return render_template('form.html',bigbox = encrypted_text,rotation = rotation)

    except ValueError:
        error = 'Please enter an integer'
        return render_template('form.html',bigbox=text_to_rotate,rotaion = '0',error=error)
        
    

@app.route("/")
def index():
    return render_template('form.html',bigbox = encrypted_text,rotation = rotation)

app.run()