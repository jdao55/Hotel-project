SET FOREIGN_KEY_CHECKS=0;
-- Hotels
TRUNCATE hotelapp_hotel; -- Reset id's to 0, necessary because they're hardcoded
INSERT INTO hotelapp_hotel (name,address_line1,address_line2,city,state,country,phone,fax,has_pool,has_gym,has_free_breakfast,has_restaurant,general_manager,manager_email)
	VALUES ('Royal York','123 Jane Street','','Toronto','ON','Canada','4165551234','',1,1,1,1,'Yuki Nagato','yuki.nagato@hotel.com');
INSERT INTO hotelapp_hotel (name,address_line1,address_line2,city,state,country,phone,fax,has_pool,has_gym,has_free_breakfast,has_restaurant,general_manager,manager_email)
	VALUES ('Budget Inn','573 Avenue Road','','Windsor','ON','Canada','2265557986','',0,0,0,0,'Lain Iwakura','lain.iwakura@hotel.com');
INSERT INTO hotelapp_hotel (name,address_line1,address_line2,city,state,country,phone,fax,has_pool,has_gym,has_free_breakfast,has_restaurant,general_manager,manager_email)
	VALUES ('Holiday Express','8253 Longcat Road','','London','ON','Canada','5197654321','',1,0,0,1,'Misaka Mikoto','misaka.mikoto@hotel.com');
INSERT INTO hotelapp_hotel (name,address_line1,address_line2,city,state,country,phone,fax,has_pool,has_gym,has_free_breakfast,has_restaurant,general_manager,manager_email)
	VALUES ('Omnistar Place','978 Le Rue Incredible','','Montral','QC','Canada','7830978123','',0,0,1,1,'Megumin','megumin@hotel.com');
INSERT INTO hotelapp_hotel (name,address_line1,address_line2,city,state,country,phone,fax,has_pool,has_gym,has_free_breakfast,has_restaurant,general_manager,manager_email)
	VALUES ('McGuffs Hostel','7071 Suspicious Blvd','Unit 3','Detroit','MI','USA','3139877771','',0,1,1,1,'Hatsune Miku','hatsune.miku@hotel.com');

-- Rooms in hotel 1
TRUNCATE hotelapp_room;
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('230',2,'Single',1,375.00,1600.00,1);
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('314',3,'Double',1,575.00,2200.00,1);
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('450',4,'Suite',1,750.00,3600.00,1);

-- Rooms in hotel 2
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('E14',2,'Single',0,80.00,500.00,2);
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('F15',2,'Single',0,85.00,550.00,2);
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('G20',3,'Double',0,110.00,700.00,2);

-- Rooms in hotel 3
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('401',4,'Double',0,100.00,500.00,3);
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('502',5,'Double',0,125.00,750.00,3);
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('603',6,'Suite',1,200.00,900.00,3);

-- Rooms in hotel 4
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('P980',28,'Suite',1,1000.00,6000.00,4);
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('P990',29,'Suite',1,2000.00,10000.00,4);
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('P1000',30,'Suite',1,5000.00,25000.00,4);

-- Rooms in hotel 5
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('10',1,'Single',0,30.00,150.00,5);
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('11A',1,'Single',0,35.00,170.00,5);
INSERT INTO hotelapp_room (room_number,room_floor,room_type,has_balcony,room_rate_nightly,room_rate_weekly,hotel_id)
	VALUES ('11B',1,'Single',1,42.00,180.00,5);

-- Parking lots
TRUNCATE hotelapp_parkinglot;
INSERT INTO hotelapp_parkinglot (lot_name,floors,hotel_id) VALUES ('Royale Parking Lot',5,1);
INSERT INTO hotelapp_parkinglot (lot_name,floors,hotel_id) VALUES ('Carspace Lot 2B',3,2);
INSERT INTO hotelapp_parkinglot (lot_name,floors,hotel_id) VALUES ("Hell's Parking Lot",4,3);
INSERT INTO hotelapp_parkinglot (lot_name,floors,hotel_id) VALUES ('Ultra Lux Parking Lot',5,4);
INSERT INTO hotelapp_parkinglot (lot_name,floors,hotel_id) VALUES ('Ultimax Parking Lot',7,4);
INSERT INTO hotelapp_parkinglot (lot_name,floors,hotel_id) VALUES ('Front Office Lot',1,5);

-- Parking space
TRUNCATE hotelapp_parkingspace;
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('A123','','',1);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('B100','','',1);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('D203','','',1);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('113','','',2);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('115','','',2);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('118','','',2);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('G3','','',3);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('G5','','',3);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('G7','','',3);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('Space 10','','',4);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('Space 12','','',4);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('Space 14','','',4);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('Luxury 8','','',4);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('Luxury 9','','',4);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('Luxury 10','','',4);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('Slot 1','','',5);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('Slot 2','','',5);
INSERT INTO hotelapp_parkingspace (space_number,license_plate,car_make,parking_lot_id) VALUES ('Slot 3','','',5);

SET FOREIGN_KEY_CHECKS=1;
