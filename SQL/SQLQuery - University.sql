select lastname + '' + firstname as FullName
from dbo.students;

/*
�������������� �����
cast() - �������������� ���� ������
convert()
*/

select 'Student '+LastName+' receives' + cast(Grants as nvarchar(10))
from students;
select 'Student '+LastName+' receives' + convert(nvarchar(10), Grants)
from students;

/*
TOP - ����� ������������� ���������� �������
PERCENT - ����� �������, ���������� ������ � ���������
DISTINCT - ������� ���������� ��������, ����������
*/

select distinct *
from students

/*
WHERE - ������� ��� (�����������)
*/

select email
from students
where id !> 3

/*
LEN() - �����
*/

select Grants
from students
where LEN(Grants) > 3

/*
	AND, OR - �, ���
	MONTH, YEAR, DAY - ����������� ��� ���� date
*/

select lastname
from students
where YEAR(birthdate) % 2 = 0
AND MONTH(birthdate) % 2 <> 0

select lastname
from Students
where grants is null
print('Hello')

/*
	ORDER BY - ����������� ���������� ����� �������. ASC - �� �����������, DESC - �� ��������.
*/

select LastName, FirstName, BirthDate
from Students
order by BirthDate ASC, FirstName DESC

/*
	IN - �������
*/

select lastname
from students
where lastname in ('���������', '�����', '�������')

/*
	BETWEEN - ��������
*/

select LastName, BirthDate
from Students
WHERE BirthDate BETWEEN '2004-01-01' and '2010-01-01'

select LastName, FirstName
from Students
WHERE FirstName not BETWEEN '�' and '�'

/*
	like(%,) - ����� �� ��������� �����.
	% - ����� ������������������ ��������.
	_ - ����� ��������� ������.
	[] - ������ ������������������.
	[^] - ������ ������������������ ����������
*/
select LastName, FirstName
from Students
WHERE FirstName like '�%' and LastName like '%'


/*------------------------------------------------------------------------------*/

/*
	INSERT - �������
*/

INSERT INTO Students(BirthDate, FirstName, LastName)
VALUES ('1788-10-15', '�����', '�������'),
('1988-05-15', '�����', '���������')

/*
	UPDATE - ��������� ������
*/

UPDATE Students
set Grants += 500
WHERE Grants is not null

/*
	DELETE - �������� ������
*/

DELETE FROM Students
where id > 12


create table New_table
(
	id int primary key,
	FirstName Varchar(50),
	LastName varchar(50),
	Grants int check(Grants in (1,2,3,4,5))
);
