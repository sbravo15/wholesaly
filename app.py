from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# Login - Register - Forgot Pass
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

def forgotpass():
    return render_template('forgot-password.html')    

# Error
def Error404():
    return render_template('404.html')


# Charts - Buttons - Cards 
def charts():
    return render_template('charts.html')

def buttons():
    return render_template('buttons.html')

def cards():
    return render_template('cards.html')





# Utilities    

def animations():
    return render_template('utilities-animation.html')

def borders():
    return render_template('utilities-border.html')

def color():
    return render_template('utilities-color.html')

def animations():
    return render_template('utilities-other.html')



