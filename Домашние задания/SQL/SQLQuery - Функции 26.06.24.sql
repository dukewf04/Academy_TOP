------------------------------------------
-------------------------------- ������� 1
------------------------------------------
-- 1. ����� Hello, Name!
CREATE FUNCTION HelloName (@name nvarchar(30))
returns nvarchar(40)
as
begin
	return 'Hello ' + @name + '!'
end;
SELECT dbo.HelloName('Evgeny') AS SumValue;

-- 2. ���������������� ������� ���������� ���������� � ������� ���������� �����
CREATE FUNCTION GetMinutes()
returns int
as
begin
	declare @min int
	select @min = datepart(minute, getdate())

	return @min
end;
SELECT dbo.GetMinutes() AS 'Minutes'

-- 3. ���������������� ������� ���������� ���������� � ������� ����
CREATE FUNCTION GetYear()
returns int
as
begin
	declare @year int
	select @year = datepart(year, getdate())

	return @year
end;
SELECT dbo.GetYear() AS 'Year'

-- 4. ���������������� ������� ���������� ���������� � ���: ������ ��� �������� ���
CREATE FUNCTION EvenOrOddYear()
returns nvarchar(30)
as
begin
	declare @year int
	declare @result nvarchar(30)
	select @year = datepart(year, getdate())
	if @year % 2 = 0
		set @result = cast(@year as nvarchar(10)) + ' ��� ������'
	else
		set @result = cast(@year as nvarchar(10)) + ' ��� ��������'

	return @result
end;
SELECT dbo.EvenOrOddYear() AS '����� ���'

-- 5. ���������������� ������� ��������� ����� � ���������� yes, ���� ����� ������� � no, ���� ����� �� �������.
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
		set @result = cast(@number as nvarchar(30)) + ' ������� �����'
	else
		set @result = cast(@number as nvarchar(30)) + ' �� ������� �����'

	return @result
end;
SELECT dbo.isNumberSimple(19) AS '�����'

-- 6. ����� ������������ � ������������� �����
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
SELECT dbo.SumNumber(10, 2, 3, 4, 5) AS '�����'

------------------------------------------
-------------------------------- ������� 2
------------------------------------------
-- 1. ���������������� ������� ���������� ����������� ������� ����������� ��������
create function MinSale(@name nvarchar(30), @surname nvarchar(30))
returns table
as
return (
	select MIN(s.price) as '����������� �������'
	from sales as s
	inner join workers as w on w.id = s.worker_id
	where w.name = @name and w.surname = @surname
)
go
select * from MinSale('�������', '�������');

-- 2. ���������������� ������� ���������� ����������� ������� ����������� ����������
create function MinBuying(@name nvarchar(30), @surname nvarchar(30))
returns table
as
return (
	select MIN(s.price) as '����������� �������'
	from sales as s
	inner join clients as c on c.id = s.worker_id
	where c.name = @name and c.surname = @surname
)
go
select * from MinBuying('�����', '����������');

-- 3. ���������������� ������� ���������� ����� ����� ������
-- �� ���������� ����. ���� ������� ��������� � �������� ���������
create function SaleAmount(@date date)
returns table
as
return (
	select SUM(s.price * s.quantity) as '����������� �������'
	from sales as s
	where s.sale_date = @date
)
go
select * from SaleAmount('2024-06-15');

-- 4. ���������������� ������� ���������� ����, ����� �����
-- ����� ������ �� ���� ���� ������������
create function GetDateMaxSales()
returns table
as
return (
	select s.sale_date as '����, ����� ����� ������ - MAX'
	from sales as s
	where s.price * s.quantity = (
		select MAX(s.price * s.quantity)
		from sales as s
	)
)
go
select * from GetDateMaxSales();

-- 5. ������� �����. ���. � ���� �������� ��������� ������.
-- �������� ������ ��������� � �������� ���������
