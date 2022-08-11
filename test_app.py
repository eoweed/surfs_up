# PART 1
# --------------------------------
# import dependency
from flask import Flask

# create new flask app instance
app = Flask(__name__)       # double underscore is a magic method


# PART 2
# --------------------------------
# create flask routes
@app.route('/')
def hello_world():
    return 'Hello world'

# create another flask 
@app.route('/Hi')
def hi():
    return "HI !"

# PART 3
# --------------------------------
if __name__ == "__main__" :
    app.run(debug=True)

