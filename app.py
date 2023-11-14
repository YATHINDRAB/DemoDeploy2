# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
    return 'Hello, World! This is my first web application on AWS.'

# Run the application if this script is executed
if __name__ == '__main__':
    # Set the host to '0.0.0.0' to make it accessible from outside the local machine
    app.run(host='0.0.0.0', port=5000)
