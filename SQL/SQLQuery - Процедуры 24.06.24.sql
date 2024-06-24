------------------- ������� 1 ------------------------
-- 1. HelloWorld
create procedure HelloWorld
as
begin
	print('Hello World!')
end
execute HelloWorld


-- 3. ���������� ���������� � ������� ����
create procedure GetDate1
as
begin
	print(getdate())
end
execute GetDate1

-- 4. ��������� 3 ����� � ���������� �����
create procedure ABC1
as
begin
	declare
		@a int,
		@b int,
		@c int,
		@sum int

	set @a = 5
	set @b = 10
	set @c = 1

	set @sum = @a + @b +@c
	print(@sr_znach)
end
execute ABC1

-- 5,6,7. ��������� 3 ����� � ���������� AVG, MAX, MIN
create procedure avg_max_min
as
begin
	declare
		@a int,
		@b int,
		@c int,
		@avg int,
		@max int,
		@min int

	set @a = 5
	set @b = 10
	set @c = 1

	declare @temp1 table(a int)
	insert into @temp1 values(@a)
	insert into @temp1 values(@b)
	insert into @temp1 values(@c)
	select avg(a) as '������� ��������' from @temp1
	select max(a) as '������������ ��������' from @temp1
	select min(a) as '����������� ��������' from @temp1
end
execute avg_max_min

-- 8. ��������� ������� N ���
create procedure drawLine
as
begin
	declare
		@symbol nchar(1),
		@count int,
		@i int,
		@result varchar(11)

	set @symbol = '*'
	set @count = 10
	set @i = 0
	set @result = ''

	while @i < @count
	begin
		set @result = @result + @symbol
		set @i = @i + 1
	end
	print(@result)
end
execute drawLine

-- 9. ���������� ���������� �����
create procedure Factorial
as
begin
	declare
		@N int,
		@result int,
		@i int

	set	@N = 5
	set @result = 1
	set @i = 1

	while @i <= @N
	begin
		set @result = @result * @i
		set @i = @i + 1
	end
	print(@result)
end
execute Factorial

-- 10. ���������� ������� �����
create procedure stepen
as
begin
	declare
		@stepen int,
		@number int,
		@result int,
		@i int

	set	@stepen = 4
	set	@number = 3
	set @result = 1
	set @i = 1

	while @i <= @stepen
	begin
		set @result = @result * @number
		set @i = @i + 1
	end
	print(@result)
end
execute stepen

------------------------------------------------------
------------------- ������� 2 ------------------------

-- 1. ��������� ���������� ���������� � ���� ���������
create procedure getWorkerInfo
as
begin
	select a.name + ' ' + a.surname as '���', a.position
	from [SportShop].[dbo].[workers] as a
end
exec getWorkerInfo[dbo].[HelloWorld]