-- https://s3.top-academy.tech/omni/materials/4uBd5AJmm-WnRfOfCNlpi_KxREw1BzbH.pdf?response-content-disposition=inline%3B%20filename%3D%22SQL_urok_02_2019_ver2_1582279134.pdf%22

/* ������� products */
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

/* ������� products */
CREATE TABLE types (
    id INT NOT NULL IDENTITY(1,1),
	name NVARCHAR(100) NOT NULL,
    PRIMARY KEY (id),
);

/* ������� sales */
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

/* ������� workers */
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

/* ������� clientns */
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

/* ������� order_histories */
CREATE TABLE order_histories (
    id INT NOT NULL IDENTITY(1,1),
	product_id INT not null,
	sale_date date,
	worker_id int NOT NULL,
	client_id int NOT NULL,
    PRIMARY KEY (id),
);

/* ������� archives */
CREATE TABLE archives (
    id INT NOT NULL IDENTITY(1,1),
	name NVARCHAR(100) NOT NULL, -- ������������ ������
    PRIMARY KEY (id),
);

/* �������� */
-- 1. ��� ������� ������, �������� ���������� � ������� � ������� �order_histories�
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

-- 2. ���� ������� �� ��������, �� ��������� ���������� � ������ � ������� archives
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
		print('����� ' + @name + ' �������� � �����')
		insert into archives(name)
		values (@name)
	end
end

-- 3. �� ��������� �������������� ��� ������������� �������. ��� ������� ��������� ������� ������� �� ��� � email.
create trigger checkUser
on clients
INSTEAD OF INSERT
as
begin
	declare @name NVARCHAR(30), @surname NVARCHAR(30), @email NVARCHAR(30)
	select
		@name = name,
		@surname = surname,
		@email = email
	from inserted	
	if (@quantity = 0)
	begin
		print('����� ' + @name + ' �������� � �����')
		insert into archives(name)
		values (@name)
	end
end