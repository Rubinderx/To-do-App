# imports create app function from the website module
from website import create_app

# creates an instance of the flask application
app = create_app()

# runs the flask app in fubug mode
if __name__=="__main__":
    app.run(debug=True)