# Bank-Management-System-project-
Bank Software Web App for Staff And User Using Python Flask to Use Services.

The flask maintains or keeps all its file in proper folders. Save the main python file in the project folder generally named as main.py. Create two more directories in the project folder with exactly with same names. 
1. static      2. templates 
The static folder contains there more directories. 
1. css    2. images   3. js 
The css directory contains .css files 
The js directory conatins .js The images has .jpg, .png. gif files Templates folder contains .html files. 
myblog/ 
      main.py 
      /static          /css             style.css             bootstrap.css          /images             logo.png 
         /js             bower.js       /templates          login.html          signup.html          index.html          userhome.html 
 
 After creating directories and storing appropriate files, following code runs the application and renders index file from templates. 
 
from flask import Flask, render_template app = Flask(__name__) @app.route('/') def index(): 
   return render_template('index.html') if __name__ == '__main__': 
   app.run(debug=True) 
