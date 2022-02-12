from flask import Flask,request,render_template,redirect,session
from flask_mail import Mail,Message
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/customerdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="vtpatil1995@gmail.com"
app.config['MAIL_PASSWORD']="9975185821"
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)



#
# import os
# from werkzeug.utils import secure_filename
# UPLOAD_FOLDER='D:\\flask_practice\\static'   #D:\flask_practice\static\Screenshot_8.png
# app.config['SECRET_KEY']='l/sjkdskjkdjskdsjkhdsjdhj5656'
# app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
# ALLOWED_EXTENSIONS = {'jpg'}

#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# @app.route('/logout')
# def logout():
#     if 'user' in session:
#         session.pop('user')
#     return redirect('/')