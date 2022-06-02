from flask import Flask, jsonify 
# jsonify is a function that converts a python dictionary into a json string (basically formats the data in ood form)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is my first API call!'

@app.route('/x/<int:a>')
def x(a):
    if a%2==0:
        print("a is even")
        result = {
            "number": a,
            "even": True
        }
    
    else:
        print("a is odd")
        result = {
            "number": a,
            "even": False
        }
    return jsonify(result)
        
if __name__ == '__main__':
    app.run(debug=True)