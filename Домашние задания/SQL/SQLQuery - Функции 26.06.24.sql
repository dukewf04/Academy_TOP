------------------------------------------
-------------------------------- Задание 1
------------------------------------------
-- 1. Вывод Hello, Name!
CREATE FUNCTION HelloName (@name nvarchar(30))
returns nvarchar(40)
as
begin
	return 'Hello ' + @name + '!'
end;
SELECT dbo.HelloName('Evgeny') AS SumValue;

-- 2. Пользовательская функция возвращает информацию о текущем количестве минут
CREATE FUNCTION GetMinutes()
returns int
as
begin
	declare @min int
	select @min = datepart(minute, getdate())

	return @min
end;
SELECT dbo.GetMinutes() AS 'Minutes'

-- 3. Пользовательская функция возвращает информацию о текущем годе
CREATE FUNCTION GetYear()
returns int
as
begin
	declare @year int
	select @year = datepart(year, getdate())

	return @year
end;
SELECT dbo.GetYear() AS 'Year'

-- 4. Пользовательская функция возвращает информацию о том: чётный или нечётный год
CREATE FUNCTION EvenOrOddYear()
returns nvarchar(30)
as
begin
	declare @year int
	declare @result nvarchar(30)
	select @year = datepart(year, getdate())
	if @year % 2 = 0
		set @result = cast(@year as nvarchar(10)) + ' год четный'
	else
		set @result = cast(@year as nvarchar(10)) + ' год нечетный'

	return @result
end;
SELECT dbo.EvenOrOddYear() AS 'Какой год'

-- 5. Пользовательская функция принимает число и возвращает yes, если число простое и no, если число не простое.
CREATE FUNCTION isNumberSimple(@number int)
returns nvarchar(30)
as
begin
	declare @i int
	declare @isSimple bit
	declare @result nvarchar(30)
	set @i = 2
	set @isSimple = 0

	WHILE @i < @number / 2
	BEGIN
		IF @number % @i = 0
			SET @isSimple = 1
			BREAK
		SET @i = @i + 1
	END

	if @isSimple = 0
		set @result = cast(@number as nvarchar(30)) + ' простое число'
	else
		set @result = cast(@number as nvarchar(30)) + ' не простое число'

	return @result
end;
SELECT dbo.isNumberSimple(19) AS 'Число'

-- 6. Сумма минимального и максимального числа
CREATE FUNCTION SumNumber
(@n1 int, @n2 int, @n3 int, @n4 int, @n5 int)
returns int
as
begin
	declare @min int, @max int
	declare @temp table(field int)

	insert into @temp values(@n1)
	insert into @temp values(@n2)
	insert into @temp values(@n3)
	insert into @temp values(@n4)
	insert into @temp values(@n5)

	select @min = MIN(field) from @temp
	select @max = MAX(field) from @temp

	return @min + @max

end;
SELECT dbo.SumNumber(10, 2, 3, 4, 5) AS 'Сумма'

------------------------------------------
-------------------------------- Задание 2
------------------------------------------
-- 1. Пользовательская функция возвращает минимальную продажу конкретного продавца
create function MinSale(@name nvarchar(30), @surname nvarchar(30))
returns table
as
return (
	select MIN(s.price) as 'Минимальная продажа'
	from sales as s
	inner join workers as w on w.id = s.worker_id
	where w.name = @name and w.surname = @surname
)
go
select * from MinSale('Евгений', 'Болотов');

-- 2. Пользовательская функция возвращает минимальную покупку конкретного покупателя
create function MinBuying(@name nvarchar(30), @surname nvarchar(30))
returns table
as
return (
	select MIN(s.price) as 'Минимальная покупка'
	from sales as s
	inner join clients as c on c.id = s.worker_id
	where c.name = @name and c.surname = @surname
)
go
select * from MinBuying('Алена', 'Желтовских');

-- 3. Пользовательская функция возвращает общую сумму продаж
-- на конкретную дату. Дата продажи передаётся в качестве параметра
create function SaleAmount(@date date)
returns table
as
return (
	select SUM(s.price * s.quantity) as 'Минимальная покупка'
	from sales as s
	where s.sale_date = @date
)
go
select * from SaleAmount('2024-06-15');

-- 4. Пользовательская функция возвращает дату, когда общая
-- сумма продаж за день была максимальной
create function GetDateMaxSales()
returns table
as
return (
	select s.sale_date as 'Дата, когда сумма продаж - MAX'
	from sales as s
	where s.price * s.quantity = (
		select MAX(s.price * s.quantity)
		from sales as s
	)
)
go
select * from GetDateMaxSales();

-- 5. Функция возвр. инф. о всех продажах заданного товара.
-- Название товара передаётся в качестве параметра
create function getAllSales(@product nvarchar(30))
returns table
as
return (
	select s.*
	from sales as s
	inner join products as p on p.id = s.product_id
	where p.name = @product
)
go
select * from getAllSales('Компьютер');

-- 6. Функция возвр. инф. о всех покупателях однофамильцах.
create function famioClient()
returns table
as
return(
	select *
	from clients as c
	group by c.surname
)
go

select * from famioClient()

-- 8. Функция возвр. инф. о всех покупателях и продавцах однофамильцах.
create function famio()
returns table
as
return(
	select c.name, c.surname, c.gender, 'Покупатель' as 'Кем является'
	from clients as c
	where c.surname in (
		select surname
		from workers
	)

	union

	select w.name, w.surname, w.gender, 'Продавец' as 'Кем является'
	from workers as w
	where w.surname in (
		select surname
		from clients
	)
)
go

select * from famio()