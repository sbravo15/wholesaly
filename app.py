from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

# Login - Register - Forgot Pass
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forgot-password')
def forgotpass():
    return render_template('forgot-password')    

# Error
@app.route('/404')
def Error404():
    return render_template('404.html')


# Charts - Buttons - Cards 
@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/buttons')
def buttons():
    return render_template('buttons.html')

@app.route('/cards')
def cards():
    return render_template('cards.html')

# Utilities    
@app.route('/utilities-animation')
def animations():
    return render_template('utilities-animation.html')
""" 
@app.route('/utilities-border')
def borders():
    return render_template('utilities-border.html')

@app.route('/utilities-color')
def color():
    return render_template('utilities-color.html')

@app.route('/utilities-other')
def animations():
    return render_template('utilities-other.html') """

if __name__ == '__main__':
    app.run(debug=True)
