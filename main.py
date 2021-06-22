from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return "<h1>Hi santoshi</h1>"

if __name__=="__main__":  # __main__ we can include within a single quote or double quote
    app.run()
# We have get result like hi santoshi open  http://127.0.0.1:5000/ in new browser
# Now our task is to deploy this application on heroku
# execute one command like pip freeze>requirements.txt  -> contain al lib name
# Pip install gunicorn--> is allow us to run our application in linux environment.

# Heroku use linux operating system and we are using windows so need to intall gunicorn

# if gunicorn is intall again execute ---> pip freeze>requirements.txt command again execute
# heroku is web server so need to istall gunicor is compulsory for mac , windows and

#  now create one file called Procfile with any extension /(P capital blank file)file for heroku deployment
# Open Ineuron folder in d drive and then open procfile with any editor like notepad++ .
# web: gunicorn main:app   # main is the file and app is object of your class.
# means Procfile understand by heroku means there is main file with flask app object which is run by flask class to run this project.
# also we can change main file name and flask app object name as per the our requirements and give the same file and object name in Procfile.
# once it is done save Procfile control s
# run this main file and Now open git hub
# Go to git create repo
# now come on pycharm terminal and enter git init  (initialized empty git repository)
# now add file . indicate include all files(main.py, Procfile,req)
# now execute git commit -m "first commit for our application"
#   git config --global user.email "you@example.com"
#   git config --global user.name "Your Name"
# Now execute git commit -m "first commit for our application
# git branch -M main  # Rename our branch name to main
# add github link -->  git remote add origin https://github.com/santoshiml/flask_deployement_heroku.git
# will upload the files to the git hub --->  git push -u origin main


