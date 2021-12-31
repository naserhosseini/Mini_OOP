import mysql.connector
from datetime import datetime,timedelta
from mysql.connector import errorcode

class Employee:
    MIN_SALARY=0
    def add(self,name,DOB):
        '''
        add employee to the SQL data base
        :param name:
        :param DOB: Date of Birth (mm/dd/yyyy)
        :param id: Store primary key of employee in order to access to other tables
        :return:
        '''
        self.name=name
        obj_DOB=datetime.strptime(DOB,'%m/%d/%Y')
        self.DOB=obj_DOB.date().strftime('%Y-%m-%d')

        _col = '(name, DOB)'
        _val = (self.name, self.DOB)
        _sql = 'INSERT employee ({}) VALUES ({});'.format(_col, _val)
        mycrs.execute(_sql)
        cnx.commit()
        _sql='SELECT MAX(id) FROM employee'
        mycrs.execute(_sql)
        row=mycrs.fetchone()
        if row!=None:
            self.id=row[0]
        return

    def UpdateEmployee(self,new_date,new_address=None,new_phone=None,new_email=None,position=None,manager_id=None,new_salary=None):
        '''
        for update the employee by employee id.
        :param new_date:
        :param new_address:
        :param new_email:
        :param new_salary:
        :param new_phone:
        :param position:
        :param manager_id:
        :return:
        '''
        self.update_date=new_date
        self.address=new_address
        self.phone=new_phone
        self.email=new_email
        self.salary=new_salary
        _id=self.id

        _col='employee_id, update_date'
        _val='{}, "{}"'.format(_id,new_date)
        if new_email:
            _col+=', '+ 'email'
            _val+=', "{}"'.format(new_email)
        if new_address:
            _col+=', ' + 'address'
            _val +=', "{}"'.format(new_address)
        if new_salary:
            _col+= ', ' + 'salary'
            _val += ', {}'.format(new_salary)
        if new_phone:
            _col += ', ' + 'phone'
            _val += ', "{}"'.format(new_phone)
        if position:
            _col += ', ' + 'position'
            _val += ', "{}"'.format(position)
        if manager_id:
            _col += ', ' + 'manager_id'
            _val += ', "{}"'.format(manager_id)

        _sql='INSERT update_employee ({}) VALUES ({});'.format(_col,_val)
        mycrs.execute(_sql)
        cnx.commit()

class Order:
    def add(self,customer_id,date,product,type,quantities,delivery,status=False):
        '''
        add placed order to the SQL data base
        :customer_id:
        :param date: order date
        :param product: either cookies, or cupcakes or cakes
        :param type: [{'cookies':['Large','Small']},{cupcakes:['chocolate','vanilla','strawberry','coconut','lemon','carrot','red velvet','pineapple','rainbow']},{cakes:['8X6','10X8','6X4','6','8','10']}]
        :param quantities:[{'cookies':dozen},{cupcakes:dozen},{cakes:initger]
        :param delivery: delivery date
        :param status: boolean, if the order is done (true) or not (false)
        '''
        self.customer_id=customer_id
        self.date=date
        self.product=product
        self.type=type
        self.quantities=quantities
        self.delivery=delivery
        self.status=status
        _col='customer_id,date,product,type,quantities,delivery,status'
        _val='{},"{}","{}","{}",{},"{}",{}'.format(customer_id,date,product,type,quantities,delivery,status)
        _sql = 'INSERT orders ({}) VALUES ({});'.format(_col, _val)
        mycrs.execute(_sql)
        cnx.commit()

    def ongoing_orders(self):
        _sql='SELECT * FROM orders WHERE delivery<"{}" AND delivery>"{}" AND status=0'.format(datetime.now().date()+timedelta(days=5),datetime.now().date())
        mycrs.execute(_sql)
        return mycrs.fetchall()

try:
    config = {
        'user': 'root',
        'password': 'Password',
        'host': '127.0.0.1',
        'database': 'minioop',
        'raise_on_warnings': True}
    cnx = mysql.connector.connect(**config)
    mycrs=cnx.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    quit()

'''Naser=Employee()
Naser.add(name='Naser',DOB='4/28/1980')
Nafise=Employee()
Nafise.add('Nafiseh','3/24/1985')
Nafise.UpdateEmployee('2020/01/20',new_salary=3400,new_email='nafiseh@info.com')
Naser.UpdateEmployee('2020/5/12',new_salary=2000,new_phone='888-777-6655')
Nafise.UpdateEmployee('2020/10/15',new_salary='5500')
bdCake=Order()
bdCake.add(customer_id=12,date='2021/12/21',product='cake',type='8X6',quantities=1,delivery='2021/12/25')
bdCake.add(customer_id=30,date='2020/12/21',product='cake',type='8',quantities=1,delivery='2020/12/25')
for item in bdCake.ongoing_orders():
    print(item)'''
cnx.close()