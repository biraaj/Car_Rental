#inserting for customer
select * from CUSTOMER;

INSERT INTO CUSTOMER
  ( Name, Phone )
VALUES
("John Smith", "123-456-7890"),
("Samantha Lee", "987-654-3210"),
("Michael Johnson", "555-555-5555"),
("Jessica Wong", "123-123-1234"),
("David Kim", "555-123-4567"),
("Karen Davis", "888-555-1212"),
("Kevin Chen", "123-555-7890"),
("Melissa Martinez", "555-987-6543"),
("Steven Nguyen", "555-321-6547"),
("Rachel Patel", "777-888-9999");

select * from CUSTOMER;

INSERT INTO OWNER
  ( Name, Owner_type )
VALUES
("John Doe", "individual"),
("ABC Inc.", "company"),
("Jane Lee", "individual"),
("Den Bank", "bank"),
("Robert Brown", "individual"),
("QWERTY Corp.", "company"),
("Sarah Davis", "individual"),
("carlos Bank", "bank"),
("William Chen", "individual"),
("puntiq Inc.", "company");

select * from OWNER;

INSERT INTO CAR
  ( OwnerID, Model,Year,Color,Car_type,Car_category)
VALUES
(2, "Ford-Fiesta", 2019, "Red", "COMPACT", "REGULAR"),
(1, "Toyota-Corolla", 2016, "Silver", "MEDIUM", "REGULAR"),
(4, "Honda-Civic", 2020, "White", "COMPACT", "REGULAR"),
(8, "Jeep-Cherokee", 2018, "Blue", "SUV", "LUXURY"),
(7, "GMC-Sierra", 2021, "Black", "TRUCK", "LUXURY"),
(3, "BMW-3 Series", 2017, "Grey", "MEDIUM", "LUXURY"),
(5, "Chevrolet-Colorado", 2015, "Green", "TRUCK", "REGULAR"),
(6, "Nissan-Altima", 2018, "Red", "MEDIUM", "REGULAR"),
(10, "Dodge-Grand Caravan", 2019, "White", "VAN", "LUXURY"),
(9, "Toyota-Sienna", 2020, "Silver", "VAN", "REGULAR"),
(3, "Audi-A4", 2018, "Black", "MEDIUM", "LUXURY"),
(1, "Hyundai-Elantra", 2017, "Red", "COMPACT", "REGULAR"),
(4, "Ford-Mustang", 2022, "Blue", "LARGE", "LUXURY"),
(6, "Honda-Accord", 2019, "White", "MEDIUM", "REGULAR"),
(2, "Mazda-MX-5 Miata", 2016, "Grey", "COMPACT", "LUXURY"),
(10, "Chrysler-Pacific", 2018, "Silver", "VAN", "REGULAR"),
(9, "Kia-Sedona", 2021, "Black", "VAN", "LUXURY"),
(7, "Ram-1500", 2015, "Red", "TRUCK", "REGULAR"),
(5, "Chevrolet-Impala", 2019, "Silver", "LARGE", "REGULAR"),
(8, "Subaru-Outback", 2017, "Green", "SUV", "REGULAR"),
(1, "Ford-Focus", 2016, "Black", "COMPACT", "REGULAR"),
(2, "Nissan-370Z", 2022, "Red", "COMPACT", "LUXURY"),
(3, "Mercedes-Benz-C-Class", 2017, "White", "MEDIUM", "LUXURY"),
(4, "Acura-TLX", 2018, "Blue", "MEDIUM", "LUXURY"),
(5, "Dodge-Charger", 2019, "Black", "LARGE", "REGULAR"),
(6, "Toyota-Camry", 2021, "Grey", "MEDIUM", "REGULAR"),
(7, "Ford-Ranger", 2016, "Silver", "TRUCK", "REGULAR"),
(8, "Jeep-Grand Cherokee", 2018,"Black", "SUV", "LUXURY"),
(9, "Honda-Odyssey", 2020, "White", "VAN", "LUXURY"),
(10, "GMC-Savana", 2017, "Grey", "VAN", "REGULAR"),
(1, "Chevrolet-Cruze", 2018, "Blue", "COMPACT", "REGULAR"),
(2, "Hyundai-Veloster", 2019, "Black", "COMPACT", "LUXURY"),
(3, "Lexus-ES", 2016, "White", "MEDIUM", "LUXURY"),
(4, "BMW-5 Series", 2017, "Grey", "LARGE", "LUXURY"),
(5, "Ford-Taurus", 2015, "Red", "LARGE", "REGULAR"),
(6, "Nissan-Sentra", 2022, "Silver", "MEDIUM", "REGULAR"),
(7, "Toyota-Tacoma", 2018, "Blue", "TRUCK", "REGULAR"),
(8, "Jeep-Wrangler", 2021, "Orange", "SUV", "LUXURY"),
(9, "Kia-Carnival", 2019, "Black", "VAN", "LUXURY"),
(10, "Chevrolet-Express", 2017, "White", "VAN", "REGULAR");

select * from CAR;

INSERT INTO AVAILABILITY
  ( Vehicle_ID, Available_from,Available_till)
VALUES
(1001, '2021-06-01', '2026-06-01'),
(1002, '2021-07-10', '2026-07-10'),
(1003, '2021-05-12', '2026-05-12'),
(1004, '2021-08-15', '2025-08-15'),
(1005, '2022-06-20', '2027-06-20'),
(1006, '2020-09-30', '2025-09-30'),
(1007, '2021-07-25', '2026-07-25'),
(1008, '2022-06-10', '2027-06-10'),
(1009, '2022-06-05', '2028-06-05'),
(1010, '2021-08-01', '2026-08-01'),
(1011, '2019-05-15', '2027-05-15'),
(1012, '2020-07-12', '2026-07-12'),
(1013, '2021-06-15', '2026-06-15'),
(1014, '2021-09-02', '2026-09-02'),
(1015, '2021-06-05', '2026-06-05'),
(1016, '2020-07-15', '2027-07-15'),
(1017, '2020-08-10', '2025-08-10'),
(1018, '2020-05-02', '2026-05-02'),
(1019, '2021-09-08', '2026-09-08'),
(1020, '2020-07-30', '2027-07-30'),
(1021, '2020-06-05', '2027-06-05'),
(1022, '2020-05-03', '2027-05-03'),
(1023, '2020-09-15', '2028-09-15'),
(1024, '2020-08-01', '2027-08-01'),
(1025, '2021-07-05', '2026-07-05'),
(1026, '2021-05-08', '2026-05-08'),
(1027, '2021-06-10', '2027-06-10'),
(1028, '2021-09-20', '2028-09-20'),
(1029, '2020-05-15', '2027-05-15'),
(1030, '2020-07-01', '2026-07-01'),
(1031, '2020-06-25', '2026-06-25'),
(1032, '2020-08-15', '2027-08-15'),
(1033, '2020-07-18', '2028-07-18'),
(1034, '2020-05-20', '2027-05-20'),
(1035, '2020-08-05', '2028-09-05'),
(1036, '2020-09-12', '2027-08-12'),
(1037, '2020-09-12', '2027-04-12'),
(1038, '2020-09-12', '2027-06-12'),
(1039, '2020-09-12', '2027-07-12'),
(1040, '2020-09-12', '2027-08-12');

select * from AVAILABILITY;


INSERT INTO RATES
  ( Vehicle_ID, Daily_rate,Weekly_rate)
VALUES
(1001, 80, 480),
(1002, 90, 540),
(1003, 70, 420),
(1004, 110, 660),
(1005, 75, 450),
(1006, 100, 600),
(1007, 85, 510),
(1008, 95, 570),
(1009, 65, 390),
(1010, 120, 720),
(1011, 100, 600),
(1012, 80, 480),
(1013, 90, 540),
(1014, 70, 420),
(1015, 110, 660),
(1016, 75, 450),
(1017, 85, 510),
(1018, 95, 570),
(1019, 65, 390),
(1020, 120, 720),
(1021, 168, 1008),
(1022, 192, 1152),
(1023, 156, 936),
(1024, 264, 1584),
(1025, 180, 1080),
(1026, 240, 1440),
(1027, 204, 1224),
(1028, 228, 1368),
(1029, 120, 720),
(1030, 288, 1728),
(1031, 240, 1440),
(1032, 80, 480),
(1033, 90, 540),
(1034, 70, 420),
(1035, 110, 660),
(1036, 75, 450),
(1037, 204, 1224),
(1038, 95, 570),
(1039, 65, 390),
(1040, 120, 720);

select * from RATES;

INSERT INTO RENTAL (Customer_id, Vehicle_id, RentalType, Location, Start_date, NO_OF_WEEKS_DAYS, PAYMENT_DUE)
VALUES 
(11, 1040, 'Daily', 'ARLINGTON,TEXAS,USA', '2023-05-12', 4, 480),
(2, 1025, 'Daily', 'ARLINGTON,TEXAS,USA', '2023-05-09', 5, 1320),
(3, 1003, 'Weekly', 'ARLINGTON,TEXAS,USA', '2023-05-07', 2, 840),
(4, 1021, 'Weekly', 'ARLINGTON,TEXAS,USA', '2023-05-13', 1, 1008),
(5, 1018, 'Weekly', 'ARLINGTON,TEXAS,USA', '2023-05-10', 3, 1710);

INSERT INTO RENTAL (Customer_id, Vehicle_id, RentalType, Location, Start_date, NO_OF_WEEKS_DAYS, PAYMENT_DUE)
VALUES 
(3, 1003, 'Weekly', 'ARLINGTON,TEXAS,USA', '2023-05-03', 2, 840);

select * from RENTAL;
select * from CAR;
select * from RATES; 

select DISTINCT CAR.VehicleID,CAR.MODEL,CAR.Year,CAR.Color,CAR.Car_type,CAR.Car_category,RATES.Daily_rate,RATES.Weekly_rate 
from (CAR
INNER JOIN RATES ON CAR.VehicleID = RATES.Vehicle_ID)
WHERE CAR.VehicleID NOT IN (select Vehicle_id from (select Vehicle_id,min(Start_date) as Start_date,max(end_date) as end_date  from (select *,
	CASE
		WHEN RENTAL.RentalType = "Weekly" THEN DATE_ADD(RENTAL.Start_date,INTERVAL RENTAL.NO_OF_WEEKS_DAYS WEEK)
        ELSE DATE_ADD(RENTAL.Start_date,INTERVAL RENTAL.NO_OF_WEEKS_DAYS DAY)
	END as end_date
FROM RENTAL) as new_rental_data
GROUP BY new_rental_data.Vehicle_id) as compared_data
WHERE ('2023-05-07' >= compared_data.Start_date and '2023-05-07' <= compared_data.end_date) or (DATE_ADD('2023-05-07',INTERVAL 2 WEEK) >= compared_data.Start_date and DATE_ADD('2023-05-07',INTERVAL 2 WEEK) <= compared_data.end_date));



select Customer_id,SUM(PAYMENT_DUE) 
from RENTAL
group by Customer_id;

select VehicleID from CAR where Car_type = "TRUCK";
drop table RATES;
select * from RATES;
select Daily_rate,Weekly_rate from RATES where Vehicle_ID="1005";

update RATES
set Daily_rate = (Daily_rate+Daily_rate*0.20),Weekly_rate = (Weekly_rate+Weekly_rate*0.20)
where Vehicle_ID in (select VehicleID from CAR where Car_type = "TRUCK"); 