-- https://s3.top-academy.tech/omni/materials/4uBd5AJmm-WnRfOfCNlpi_KxREw1BzbH.pdf?response-content-disposition=inline%3B%20filename%3D%22SQL_urok_02_2019_ver2_1582279134.pdf%22

/* Таблица products */
CREATE TABLE products (
    id INT NOT NULL IDENTITY(1,1),
	name NVARCHAR(100) NOT NULL,
	type_id INT not null,
	stock_quantity int,
	cost_price money not null,
	manufacturer NVARCHAR(100) NOT NULL,
	price money not null
    PRIMARY KEY (id),
);

/* Таблица products */
CREATE TABLE types (
    id INT NOT NULL IDENTITY(1,1),
	name NVARCHAR(100) NOT NULL,
    PRIMARY KEY (id),
);

/* Таблица sales */
CREATE TABLE sales (
    id INT NOT NULL IDENTITY(1,1),
	product_id INT not null,
	quantity int,
	price money not null,
	sale_date date,
	worker_id int NOT NULL,
	client_id int NOT NULL,
    PRIMARY KEY (id),
);

/* Таблица workers */
CREATE TABLE workers (
    id INT NOT NULL IDENTITY(1,1),
	name NVARCHAR(30) NOT NULL,
	surname NVARCHAR(30) NOT NULL,
	gender NVARCHAR(10) NOT NULL,
	position NVARCHAR(30) NOT NULL,
	employment_date date not null,
	salary money not null,
    PRIMARY KEY (id),
);

/* Таблица clientns */
CREATE TABLE clients (
    id INT NOT NULL IDENTITY(1,1),
	name NVARCHAR(30) NOT NULL,
	surname NVARCHAR(30) NOT NULL,
	gender NVARCHAR(10) NOT NULL,
	email NVARCHAR(30) NOT NULL,
	phone NVARCHAR(20) NOT NULL,
	history_trades NVARCHAR(MAX) NOT NULL,
	discount int,
	subscribed bit,
    PRIMARY KEY (id),
);

/* Таблица order_histories */
CREATE TABLE order_histories (
    id INT NOT NULL IDENTITY(1,1),
	product_id INT not null,
	sale_date date,
	worker_id int NOT NULL,
	client_id int NOT NULL,
    PRIMARY KEY (id),
);

/* Таблица archives */
CREATE TABLE archives (
    id INT NOT NULL IDENTITY(1,1),
	name NVARCHAR(100) NOT NULL, -- наименование товара
    PRIMARY KEY (id),
);

/* Триггеры */
-- 1. При продаже товара, заносить информацию о продаже в таблицу «order_histories»
create trigger addSaleHistory
on sales
for insert
as
begin
	declare @product_id int
	declare @sale_date date
	declare @worker_id int
	declare @client_id int

	select
		@product_id = product_id,
		@sale_date = sale_date,
		@worker_id = worker_id,
		@client_id = client_id
	from inserted

	insert into order_histories(product_id, sale_date, worker_id, client_id)
	values (@product_id, @sale_date, @worker_id, @client_id)
end

-- 2. Если товаров не осталось, то переносим информацию о товаре в таблицу archives
create trigger addProductInHistory
on products
for update
as
begin
	declare @name NVARCHAR(100)
	declare @quantity int
	select
		@name = name,
		@quantity = stock_quantity
	from inserted	
	if (@quantity = 0)
	begin
		print('Товар ' + @name + ' пернесен в архив')
		insert into archives(name)
		values (@name)
	end
end

-- 3. Не позволять регистрировать уже существующего клиента. При вставке проверять наличие клиента по ФИО и email.
create trigger checkUser
on clients
INSTEAD OF INSERT
as
begin
	if exists(
		select 1
		from clients
		where
			name = (SELECT name FROM inserted) and
			surname = (SELECT surname FROM inserted) and
			email = (SELECT email FROM inserted)
	)
	begin
		raiserror('Человек, с таким именем уже существует!',0,1)
	end
end

insert into clients(name, surname, gender, email, history_trades)
values ('Sasha', 'Popov', 'm', 'sasha@gmail.com', 1)

-- 4. Запретить удаление существующих клиентов
create trigger stopDeletingClients
on clients
INSTEAD OF delete
as
begin
	if exists(
		select 1
		from clients
		where
			name = (SELECT name FROM deleted) and
			surname = (SELECT surname FROM deleted)
	)
	begin
		raiserror ('Нельзя удалять, существующих клиентов!',0,1)
	end
end

DELETE FROM clients
WHERE name = 'Sasha' and surname = 'Popov'

-- 5. Запретить удаление сотрудников, принятых на работу до 2015 года
create trigger stopDeletingWorker
on workers
INSTEAD OF delete
as
begin
	if exists(
		select *
		from deleted
		where
			employment_date < '2015-01-01'
	)
	begin
		raiserror ('Нельзя удалять, сотрудников, принятых на работу до 2015г!',0,1)
		RETURN
	end

	DELETE FROM workers
	WHERE id IN (SELECT id FROM deleted);
end

DELETE FROM workers
WHERE name = 'аа'

-- 6. При новой покупке товара нужно проверять общую сумму покупок клиента. Если сумма превысила 50000 грн, необходимо установить процент скидки в 15%
CREATE TRIGGER CheckPurchaseTotal
ON sales
AFTER INSERT
AS
BEGIN
    IF @@ROWCOUNT > 0
    BEGIN
        -- Получаем ID клиента из вставленной строки
        DECLARE @CustomerID INT;
        SELECT @CustomerID = client_id FROM inserted;

        DECLARE @TotalPurchaseAmount DECIMAL(10,2);
        SELECT @TotalPurchaseAmount = SUM(s.quantity * s.price)
        FROM sales as s
        WHERE client_id = @CustomerID;

        IF @TotalPurchaseAmount > 50000
        BEGIN
            UPDATE clients
            SET discount = 0.15
            WHERE id = @CustomerID;
        END
    END
END

-- 7. Запретить добавлять товар конкретной фирмы. Например, товар фирмы «Спорт, солнце и штанга»
CREATE TRIGGER PreventSportSunAndBarbellInsert
ON products
INSTEAD OF INSERT
AS
BEGIN
  IF EXISTS (SELECT 1 FROM inserted WHERE manufacturer = 'Спорт, солнце и штанга')
  BEGIN
    raiserror('Нельзя добавлять товары фирмы "Спорт, солнце и штанга".', 16, 1)
    ROLLBACK TRANSACTION	
  END
END

-- 8. При продаже проверять количество товара в наличии. Если осталась одна единица товара, необходимо внести информацию об этом товаре в таблицу «Последняя Единица»
create trigger CheckLastUnitOnSale
on products
for update
as
begin
	declare @name NVARCHAR(100)
	declare @quantity int
	select
		@name = name,
		@quantity = stock_quantity
	from inserted	
	if (@quantity = 1)
	begin
		print('Товар ' + @name + ' пернесен в таблицу lastunits')
		insert into lastunits(name)
		values (@name)
	end
end