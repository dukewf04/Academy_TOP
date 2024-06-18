-- Задание 1.1.
CREATE TRIGGER update_stock_on_new_product
BEFORE INSERT ON products
FOR EACH ROW
BEGIN
    DECLARE existing_quantity INT;
    
    SELECT quantity 
    INTO existing_quantity
    FROM products
    WHERE name = NEW.name 
    AND code = NEW.code;
    
    IF existing_quantity IS NOT NULL THEN
        UPDATE products
        SET quantity = existing_quantity + NEW.quantity
        WHERE Наименование = NEW.Наименование 
        AND code = NEW.code;
        
        SET NEW.name = NULL; 
        SET NEW.code = NULL;        
    END IF
END 

-- Задание 1.2.
CREATE TRIGGER employee_termination_trigger
BEFORE DELETE ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO ArchivedEmployees (
        EmployeeID,
        FirstName,
        LastName,
        Position,
        HireDate,
        TerminationDate
    )
    VALUES (
        OLD.EmployeeID,
        OLD.FirstName,
        OLD.LastName,
        OLD.Position,
        OLD.HireDate,
        NOW()
    )
END

-- Задание 1.3.
CREATE TRIGGER check_salesperson_count 
BEFORE INSERT ON Salesperson
FOR EACH ROW
BEGIN
  DECLARE existing_count INT;

  SELECT COUNT() INTO existing_count FROM Salesperson;

  IF existing_count >= 6 THEN
	raiserror('Нельзя добавить нового продавца. Максимальное количество продавцов - 6.', 0, 1)
	rollback transaction
  END IF
END

------------------------------------------------------
-- Задание 2.1.
CREATE TRIGGER prevent_duplicate_albums
BEFORE INSERT ON Albums
FOR EACH ROW
BEGIN
  IF EXISTS (SELECT 1 FROM Albums WHERE AlbumName = NEW.AlbumName) THEN
	raiserror('Альбом с таким названием уже существует.', 0, 1)
	rollback transaction
  END IF
END

-- Задание 2.2.
CREATE TRIGGER BeatlesDiskProtection
BEFORE DELETE ON music_collections
FOR EACH ROW
BEGIN
  IF OLD.Group = 'The Beatles' THEN
	raiserror('Нельзя удалять диски группы The Beatles', 0, 1)
	rollback transaction
  END IF
END

-- Задание 2.3.
CREATE TRIGGER DeleteDiskTrigger
BEFORE DELETE ON music_collections
FOR EACH ROW
BEGIN
  INSERT INTO archive (
    name,
    singer,
    genre,
    year,
    added_date,
    comment
  )
  VALUES (
    OLD.name,
    OLD.singer,
    OLD.genre,
    OLD.year,
    OLD.added_date,
    OLD.comment
  );
END

-- Задание 2.4.
CREATE TRIGGER prevent_dark_power_pop_insertion
BEFORE INSERT ON music_collections
FOR EACH ROW
BEGIN
  IF NEW.style = 'Dark Power Pop' THEN
	raiserror('Нельзя добавлять диски стиля "Dark Power Pop" в коллекцию.', 0, 1)
	rollback transaction
  END IF
END

------------------------------------------------------
-- Задание 3.1.
CREATE TRIGGER check_duplicate_surname
BEFORE INSERT ON customers
FOR EACH ROW
BEGIN
  IF EXISTS (SELECT 1 FROM customers WHERE surname = NEW.surname) THEN
    INSERT INTO dublicate_surnames (surname) VALUES (NEW.surname);
  END IF
END

-- Задание 3.2.
CREATE TRIGGER TransferPurchasesOnCustomerDelete
BEFORE DELETE ON customers
FOR EACH ROW
BEGIN
  INSERT INTO history_trades (customer_number, purchase_date, product, price)
  SELECT customer_number, purchase_date, product, price
  FROM sales
  WHERE customer_number = OLD.customer_number;
END

-- Задание 3.3.
CREATE TRIGGER check_seller_before_insert
BEFORE INSERT ON sales.seller
FOR EACH ROW
BEGIN
  IF EXISTS (SELECT 1 FROM sales.customer WHERE name = NEW.name AND surname = NEW.surname) THEN
	raiserror('Продавец с таким именем и фамилией уже существует в таблице Покупатели.', 0, 1)
	rollback transaction
  END IF
END

-- Задание 3.4.
CREATE TRIGGER check_existing_seller
BEFORE INSERT ON customers
FOR EACH ROW
BEGIN
  IF EXISTS (SELECT 1 FROM seller WHERE id_seller = NEW.id_customer) THEN
	raiserror('Этот ID уже существует в таблице продавцов.', 0, 1)
	rollback transaction
  END IF
END

-- Задание 3.4.
CREATE TRIGGER PreventForbiddenFruitSales
BEFORE INSERT ON Sales
FOR EACH ROW
BEGIN
  IF NEW.product_name IN ('apple', 'pear', 'plum', 'cilantro') THEN
	raiserror('Нельзя добавлять продажи запрещенных продуктов.', 0, 1)
	rollback transaction
  END IF
END