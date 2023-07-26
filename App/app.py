# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:21:15 2023

@author: biraaj

Team Member 1:
Name: Biraaj Rout
"""

from flask import Flask, render_template, request,flash,redirect,url_for
from flask_mysqldb import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
app.secret_key = b'_5#y2L"F5Q8z\n\xec]/'

# Required
app.config["MYSQL_USER"] = "bxr1886"
app.config["MYSQL_PASSWORD"] = "Rourkela@95"
app.config["MYSQL_DB"] = "bxr1886"
app.config["MYSQL_HOST"] = "academicmysql.mysql.database.azure.com"
app.config["MYSQL_PORT"] = 3306
mysql = MySQL(app)


# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        cur = mysql.connection.cursor()
        cur.execute("INSERT into OWNER(Name,Owner_type) VALUES ('"+name+"','"+type+"');")
        mysql.connection.commit()
        cur.close()
        flash('Owner added successfully')
        return redirect(url_for('list_owners'))
    else:
        return render_template('add_owner.html')
    
#Delete Owner
@app.route('/delete_owner', methods=['GET', 'POST'])
def delete_owner():
    if request.method == 'POST':
        owner_id = request.form['owner_id']
        cur = mysql.connection.cursor()
        cur.execute("delete from OWNER where Owner_id="+owner_id+";")
        mysql.connection.commit()
        cur.close()
        flash('Owner deleted successfully')
        return redirect(url_for('list_owners'))
    else:
        cur = mysql.connection.cursor()
        cur.execute("select * from OWNER;")
        _owners = cur.fetchall()
        cur.close()
        return render_template('delete_owner.html',owners=_owners)
#Delete owner

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT into CUSTOMER(Name,Phone) VALUES ('"+name+"','"+phone+"');")
        mysql.connection.commit()
        cur.close()
        flash('Customer added successfully')
        return redirect(url_for('list_customers'))
    else:
        return render_template('add_customer.html')
    
#Delete Customer
@app.route('/delete_customer', methods=['GET', 'POST'])
def delete_customer():
    if request.method == 'POST':
        Customer_id = request.form['customer_id']
        cur = mysql.connection.cursor()
        cur.execute("delete from CUSTOMER where Customer_id="+Customer_id+";")
        mysql.connection.commit()
        cur.close()
        flash('Customer deleted successfully')
        return redirect(url_for('list_customers'))
    else:
        cur = mysql.connection.cursor()
        cur.execute("select * from CUSTOMER;")
        _customers = cur.fetchall()
        cur.close()
        return render_template('delete_customer.html',customers=_customers)
#delete Customer

#Car booking block START.........................................................................................................
@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        owner_id = request.form['owner_id']
        model = request.form['model']
        year = request.form['year']
        color = request.form['color']
        car_type = request.form['car_type']
        car_category = request.form['car_category']
        avail_from = request.form['avail_from']
        avail_till = request.form['avail_till']
        daily_rate = request.form['daily_rate']
        weekly_rate = request.form['weekly_rate']
        cur = mysql.connection.cursor()
        cur.execute("INSERT into CAR (OwnerID, Model,Year,Color,Car_type,Car_category) VALUES ("+owner_id+",'"+model+"',"+year+",'"+color+"','"+car_type+"','"+car_category+"');")
        mysql.connection.commit()
        cur.execute("select MAX(VehicleID) from CAR;")
        vechile_id = cur.fetchall()[0][0]
        cur.execute("INSERT into AVAILABILITY (Vehicle_ID, Available_from,Available_till) VALUES ("+str(vechile_id)+",'"+avail_from+"','"+avail_till+"');")
        mysql.connection.commit()
        cur.execute("INSERT into RATES (Vehicle_ID, Daily_rate,Weekly_rate) VALUES ("+str(vechile_id)+","+daily_rate+","+weekly_rate+");")
        mysql.connection.commit()
        cur.close()
        flash('Car added successfully')
        return redirect(url_for('list_cars'))
    else:
        return render_template('add_car.html')

#delete Car
@app.route('/delete_car', methods=['GET', 'POST'])
def delete_car():
    if request.method == 'POST':
        Car_id = request.form['car_id']
        cur = mysql.connection.cursor()
        cur.execute("delete from CAR where VehicleID="+Car_id+";")
        mysql.connection.commit()
        cur.close()
        flash('Car deleted successfully')
        return redirect(url_for('list_cars'))
    else:
        cur = mysql.connection.cursor()
        cur.execute("select * from CAR;")
        _cars = cur.fetchall()
        cur.close()
        return render_template('delete_car.html',cars=_cars)
#delete Car

@app.route('/rent_car', methods=['GET', 'POST'])
def add_rental():
    cur = mysql.connection.cursor()
    cur.execute("""select * from CUSTOMER;""")
    _cust = cur.fetchall()
    cur.close()
    return render_template('rent_car.html',customers=_cust)
    
@app.route('/find_car', methods=['GET', 'POST'])
def find_car():
    if request.method == 'POST':
        customer_id = request.form["customer_id"]
        start_date = request.form["start_date"]
        rental_type = request.form["rental_type"]
        if rental_type == "Weekly":
            increment = "WEEK"
        else:
            increment = "DAY"
        rental_duration = request.form["rental_duration"]
        cur = mysql.connection.cursor()
        cur.execute("select DISTINCT CAR.VehicleID,CAR.MODEL,CAR.Year,CAR.Color,CAR.Car_type,CAR.Car_category,RATES.Daily_rate,RATES.Weekly_rate \
                        from (CAR\
                        INNER JOIN RATES ON CAR.VehicleID = RATES.Vehicle_ID)\
                        WHERE CAR.VehicleID NOT IN (select Vehicle_id from (select Vehicle_id,min(Start_date) as Start_date,max(end_date) as end_date  from (select *,\
                        CASE\
                            WHEN RENTAL.RentalType = 'Weekly' THEN DATE_ADD(RENTAL.Start_date,INTERVAL RENTAL.NO_OF_WEEKS_DAYS WEEK)\
                            ELSE DATE_ADD(RENTAL.Start_date,INTERVAL RENTAL.NO_OF_WEEKS_DAYS DAY)\
                        END as end_date\
                    FROM RENTAL) as new_rental_data\
                    GROUP BY new_rental_data.Vehicle_id) as compared_data\
                    WHERE ('"+start_date+"' >= compared_data.Start_date and '"+start_date+"' <= compared_data.end_date) or (DATE_ADD('"+start_date+"',INTERVAL "+rental_duration+" "+increment+") >= compared_data.Start_date and DATE_ADD('"+start_date+"',INTERVAL "+rental_duration+" "+increment+") <= compared_data.end_date));")
        available_cars = cur.fetchall()
        cur.close()

        return render_template('book_car.html',cars=available_cars,customer=(customer_id,start_date,rental_type,rental_duration))

@app.route('/book_car', methods=['GET', 'POST'])
def book_car():
    if request.method == 'POST':
        customer_id = request.form["customer_id"]
        start_date = request.form["start_date"]
        rental_type = request.form["rental_type"]
        rental_duration = request.form["rental_duration"]
        vehicle_id = request.form["car_id"]
        location = 'ARLINGTON,TEXAS,USA'
        cur = mysql.connection.cursor()
        cur.execute("select Daily_rate,Weekly_rate from RATES where Vehicle_ID = "+vehicle_id+";")
        results = cur.fetchall()
        if rental_type == "Weekly":
            rate = results[0][1]
        else:
            rate = results[0][0]
        price = int(rental_duration)*int(rate)            
        cur.execute("INSERT INTO RENTAL (Customer_id, Vehicle_id, RentalType, Location, Start_date, NO_OF_WEEKS_DAYS, PAYMENT_DUE) VALUES ("+customer_id+","+vehicle_id+",'"+rental_type+"','"+location+"','"+start_date+"',"+rental_duration+","+str(price)+");")
        mysql.connection.commit()
        cur.close()

        flash("Car booked succesfully for customer with customerID: "+str(customer_id))
        return redirect(url_for('list_rentals'))

#Car booking block END.........................................................................................................

#Car Return Start--------
@app.route('/return_car', methods=['GET', 'POST'])
def car_return():
    cur = mysql.connection.cursor()
    cur.execute("""select * from CUSTOMER;""")
    _cust = cur.fetchall()
    cur.close()
    return render_template('return_car.html',customers=_cust)

@app.route('/find_bookings', methods=['GET', 'POST'])
def find_booking():
    customer_id = request.form["customer_id"]
    cur = mysql.connection.cursor()
    cur.execute("select * from RENTAL where Customer_id="+customer_id+";")
    _rental = cur.fetchall()
    cur.close()
    if(_rental == ()):
        flash("No bookings for the customer with customer id "+customer_id)
        return redirect(url_for('car_return'))
    return render_template('update_booking.html',rental=_rental)

# @app.route('/update_booking', methods=['GET', 'POST'])
# def update_booking():
#     customer_id = request.form["customer_id"]
#     cur = mysql.connection.cursor()
#     cur.execute("select * from RENTAL where Customer_id="+customer_id+";")
#     _rental = cur.fetchall()
#     cur.close()
#     if(_rental == ()):
#         return "No bookings"
#     return render_template('update_booking.html',rental=_rental)

@app.route('/process_payment', methods=['GET', 'POST'])
def process_payment():
    cur = mysql.connection.cursor()
    rental_id = request.form["rent_id"]
    cur.execute("delete from RENTAL where Rental_id="+rental_id+";")
    mysql.connection.commit()
    cur.close()

    flash("Succesfully processed payment")
    return redirect(url_for('list_rentals'))

#Car Return End----------

#Update Rates
@app.route('/update_rate', methods=['GET', 'POST'])
def update_rate():
    if request.method == 'POST':
        car_type = request.form["car_type"]
        daily_rate = request.form["daily_rate"]
        weekly_rate = request.form["weekly_rate"]
        cur = mysql.connection.cursor()
        cur.execute("update RATES\
                        set Daily_rate = "+str(daily_rate)+", Weekly_rate = "+str(weekly_rate)+\
                        " where Vehicle_ID in (select VehicleID from CAR where Car_type = '"+car_type+"');")
        mysql.connection.commit()

        flash("Succesfully Updated for car_type "+car_type)
        return redirect(url_for('list_cars'))
    else:
        return render_template('rate_update.html')
#Update Rates


@app.route('/list_owners')
def list_owners():
    cur = mysql.connection.cursor()
    cur.execute("""select * from OWNER;""")
    owners = cur.fetchall()
    cur.close()
    return render_template('list_owners.html', owners=owners)

@app.route('/list_customers')
def list_customers():
    cur = mysql.connection.cursor()
    cur.execute("""select * from CUSTOMER;""")
    _customers = cur.fetchall()
    cur.close()
    return render_template('list_customers.html', customer=_customers)

@app.route('/list_cars')
def list_cars():
    cur = mysql.connection.cursor()
    cur.execute("""select CAR.VehicleID,CAR.MODEL,CAR.Year,CAR.Color,CAR.Car_type,CAR.Car_category,RATES.Daily_rate,RATES.Weekly_rate 
                        from CAR
                        INNER JOIN RATES ON CAR.VehicleID = RATES.Vehicle_ID;""")
    cars = cur.fetchall()
    cur.close()
    return render_template('list_cars.html', cars=cars)

@app.route('/list_rentals')
def list_rentals():
    cur = mysql.connection.cursor()
    cur.execute("""select * from Rental;""")
    _rentals = cur.fetchall()
    cur.close()
    return render_template('list_rentals.html', rentals=_rentals)

#List owner Average weekly income
@app.route('/list_owner_income')
def list_income():
    cur = mysql.connection.cursor()
    cur.execute("SELECT o.Name AS Owner_Name, c.Car_type, c.Car_category, COUNT(c.VehicleID) AS Num_Cars,\
                    SUM(r.WEEKLY_RATE) AS Weekly_Earnings, SUM(r.WEEKLY_RATE) / COUNT(c.VehicleID) AS Earnings_Per_Car\
                    FROM OWNER o\
                    INNER JOIN CAR c ON o.Owner_id = c.OwnerID\
                    INNER JOIN RATES r ON c.VehicleID = r.Vehicle_ID\
                    GROUP BY o.Name, c.Car_type, c.Car_category\
                    ORDER BY o.Name, c.Car_type, c.Car_category")

    _incomes = cur.fetchall()
    cur.close()
    return render_template('list_owner_income.html', incomes=_incomes)