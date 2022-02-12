from config_ import *
from models_ import *
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER='D:\\flask_practice\\static'
app.config['SECRET_KEY']='l/sjkdskjkdjskdsjkhdsjd'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
ALLOWED_EXTENSIONS={'jpg','png'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# def valid_meterno(formdata):
#     meterno=formdata.get('meterno')
#     if 6>len(meterno)<6 or type(meterno)!=int:
#         print("Invalid Meter No")
#     else:
#         return meterno
@app.route('/welcome')
def welcomepage():
    if session.get('user'):
        return render_template('Welcome.html')
    else:
        return redirect('/')

@app.route('/addcust',methods=['GET','POST'])
def add_cust():
    flag=False
    msg = ''
    if session.get('user'):
        if request.method=='POST':
            formdata=request.form
            image=request.files['image']
            filename=secure_filename(image.filename)
            if image and allowed_file(image.filename):
                image.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            else:
                flag=True
            id=formdata.get('cid')
            print(id)
            customer=Customer.query.filter_by(eid=id).first()
            if customer and not flag:
                customer.name=formdata.get('cname')
                customer.area=formdata.get('carea')
                customer.email=formdata.get('email')
                customer.gender=formdata.get('gender')
                customer.meterno=formdata.get('meterno')
                customer.bill_amount=formdata.get('bill')
                # customer.image=formdata.get('image')


                db.session.add(customer)
                db.session.commit()

            elif not customer and not flag:
                cust=Customer(eid=formdata.get('cid'),name=formdata.get('cname'),
                              area=formdata.get('carea'),email=formdata.get('email'),
                              gender=formdata.get('gender'),meterno=formdata.get('meterno'),
                              bill_amount=formdata.get('bill'))

                db.session.add(cust)
                db.session.commit()
            elif flag:
                msg='Invalid File'



        return render_template('cust.html',cust=Customer.dummy_cust(),msg=msg)
    else:
        return redirect('/')
@app.route('/edit/<int:id>',methods=['GET'])
def edit_cust(id):
    if session.get('user'):
        if id:
            customer = Customer.query.filter_by(eid=id).first()
            return render_template('cust.html',cust=customer)
        else:
            customer=Customer.dummy_cust()
            return render_template('cust.html',cust=customer)
    else:
        return redirect('/')

@app.route('/getcust',methods=['GET','POST'] )
def get_cust():
    if session.get('user'):
        if request.method == 'POST':
            formdata = request.form
            customer=Customer.query.filter_by(eid=formdata.get('id')).first()
            if customer:
                return render_template('get_cust.html', cust=customer)
            else:
                msg="Customer Not Found"
                return render_template('get_cust.html', message=msg)
        return render_template('get_cust.html')
    else:
        return redirect('/')

@app.route('/getall')
def allcust():
    if session.get('user'):
        customers=Customer.query.all()
        return render_template('allcust.html', custm=customers)
    else:
        return redirect('/')

@app.route('/delete/<int:id>')
def delete_cust(id):
    if session.get('user'):
        customer=Customer.query.filter_by(eid=id).first()
        if customer:
            db.session.delete(customer)
            db.session.commit()
            msg = "Customer Successfully Deleted"
            return redirect('/getall')

        else:
            msg = "Customer Not Found"
            return render_template('allcust.html', message=msg)
    else:
        return redirect('/')
@app.route('/addcand',methods=['GET','POST'])
def add_cand():
    if request.method=='POST':
        formdata=request.form
        id=formdata.get('cid')
        print(id)
        candidate=Candidate.query.filter_by(eid=id).first()
        if candidate:
            candidate.name=formdata.get('cname')
            candidate.email=formdata.get('email')
            candidate.contact=formdata.get('ccont')
            candidate.password = formdata.get('cpass')
            db.session.commit()

        else:
            candt=Candidate(name=formdata.get('cname'),
                            email=formdata.get('cmail'),contact=formdata.get('ccont'),
                            password=formdata.get('cpass')
                            )
            db.session.add(candt)
            db.session.commit()
    return render_template('cand.html', cand=Candidate.dummy_cand())


@app.route('/sendmail',methods=['GET','POST'])
def send_mail():
    if session.get('user'):
        mesg='Message Sent'
        if request.method=='POST':
            email=request.form['email']
            subject=request.form['subject']
            msg=request.form['message']

            message=Message(subject,sender='vtpatil1995@gmail.com',recipients=[email])
            message.body=msg
            mail.send(message)
        return render_template('send_mail.html',message=mesg)
    else:
        return redirect('/')

@app.route('/',methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST':
        formdata = request.form
        cmail = formdata.get('cmail')
        passw = formdata.get('cpass')
        candidate = Candidate.query.filter_by(email=cmail).first()
        password  = Candidate.query.filter_by(password=passw).first()
        if candidate and password:
            session['user']=formdata.get('cmail')
            msg='Login successful'
            return render_template('welcome.html',msg=msg)
        else:
            msg='Login unsuccessful'
            return redirect('/')
    return render_template('login.html')


@app.route('/logout')
def logout():
    if 'user'in session:
        session.pop('user')
    return redirect('/')


app.run(debug=True)