from flask import Flask, request
from caesar import rotate_string 
app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
    <!DOCTYPE html>
    <html>
        <head>
            <title> ::: Web Caesar ::: </title>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
                p {
                    color: #909090
                }
            </style>
        </head>
        <body>
"""
page_footer = """
        </body>
    </html>

"""
form = """
    <form action='/encrypted' method='post' >
        <label for='rotation-value'> Rotate by:
            <input type='text' id='rotation-value' name='rot' value='0' />
        </label>
        <br>
        <textarea name='text'></textarea>
        <input type='submit' value= 'Go'/>
    </form>
"""

page_middle = '<p> Welcome to my app! </p>'

@app.route('/encrypted', methods = ['POST'])
def encrypt():
    text_to_rotate = request.form['text']
    rotation = request.form['rot']
    encrypted_text = rotate_string(text_to_rotate,int(rotation))
    return '<h1>{}</h1>'.format(encrypted_text)
    



@app.route("/")
def index():
    content = page_header + page_middle + form + page_footer
    return content

app.run()