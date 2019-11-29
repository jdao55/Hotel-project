-- Calculates the total charges - uses a weekly rate if the stay is longer than 7 days
-- Otherwise it will be a nightly rate
DROP TRIGGER IF EXISTS insert_total_charges;
DELIMITER //
CREATE TRIGGER insert_total_charges BEFORE INSERT ON hotelapp_reservation
	FOR EACH ROW
	BEGIN
		SET @days := 0;
		SET @rate := 0;
		SELECT ABS(DATEDIFF(NEW.checkin_date, NEW.checkout_date)) INTO @days;
		IF @days > 7 THEN
			SELECT room_rate_weekly FROM hotelapp_room WHERE room_id = NEW.room_id INTO @rate;
			SET NEW.total_charges = @rate * (@days / 7);
		ELSE
			SELECT room_rate_nightly FROM hotelapp_room WHERE room_id = NEW.room_id INTO @rate;
			SET NEW.total_charges = @rate * @days;
		END IF;
	END;//
DELIMITER ;

-- Set the parking space to "empty" when a record is deleted from the reservation table
-- i.e, checkout event
DROP TRIGGER IF EXISTS free_parking_space;
DELIMITER //
CREATE TRIGGER free_parking_space BEFORE DELETE ON hotelapp_reservation
	FOR EACH ROW
	BEGIN
		UPDATE hotelapp_parkingspace SET room_id = NULL, customer_id = NULL WHERE room_id = OLD.room_id AND customer_id = OLD.customer_id;
	END;//
DELIMITER ;

-- Assigns a free parking space if they choose to have one
-- h_id = hotel_id, r_id = room_id, c_id = customer_id
DROP PROCEDURE IF EXISTS assign_parking_space;
DELIMITER //
CREATE PROCEDURE assign_parking_space(IN pl_id INT(11), IN r_id INT(11), IN c_id INT(11))
BEGIN
	SET @pspace_id := 0;
	SELECT parking_space_id INTO @pspace_id FROM hotelapp_parkingspace WHERE parking_lot_id = pl_id AND room_id IS NULL AND customer_id IS NULL LIMIT 1;
	UPDATE hotelapp_parkingspace SET room_id = r_id, customer_id = c_id WHERE parking_space_id = @pspace_id;
END; //
DELIMITER ;
