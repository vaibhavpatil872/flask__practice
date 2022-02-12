from config_ import *

class Customer(db.Model):
    eid=db.Column('Id',db.Integer,primary_key=True)
    name=db.Column('Name',db.String(30))
    area=db.Column('Area',db.String(50))
    email=db.Column('cust_email',db.String(30),unique=True)
    gender=db.Column('cust_gender',db.String(10))
    meterno=db.Column('cust_meterno',db.Integer(),unique=True)
    bill_amount=db.Column('cust_bill',db.Integer())
    # image=db.Column('emg_image',db.LargeBinary(),nullable=True)



    @classmethod
    def dummy_cust(cls):
        return Customer(eid='',name='',area='',email='',gender='',meterno='',bill_amount='')

class Candidate(db.Model):
    eid=db.Column('Id',db.Integer,primary_key=True)
    name=db.Column('Name',db.String(50))
    email=db.Column('cand_email',db.String(30),unique=True)
    contact=db.Column('contact',db.BigInteger())
    password = db.Column('cand_password', db.Text(1000))

    @classmethod
    def dummy_cand(cls):
        return Candidate(eid='', name='', email='', contact='',password='')



# class Login(db.Model):
#     cid=db.Column('Id',db.Integer,primary_key=True)
#     password=db.Column('Password',db.String(50))
#     login=db.Column(db.Integer,db.ForeignKey('candidate.Id'),unique=True,nullable=False)


db.create_all()