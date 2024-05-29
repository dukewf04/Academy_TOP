select lastname + '' + firstname as FullName
from dbo.students;

/*
Преобразование типов
cast() - преобразование типа данных
convert()
*/

select 'Student '+LastName+' receives' + cast(Grants as nvarchar(10))
from students;
select 'Student '+LastName+' receives' + convert(nvarchar(10), Grants)
from students;

/*
TOP - выбор определенного количества записей
PERCENT - выбор записей, количество задано в процентах
DISTINCT - выборка уникальных значений, сортировка
*/

select distinct *
from students

/*
WHERE - условие ГДЕ (Предложение)
*/

select email
from students
where id !> 3

/*
LEN() - длина
*/

select Grants
from students
where LEN(Grants) > 3

/*
	AND, OR - И, ИЛИ
	MONTH, YEAR, DAY - предикаторы для типа date
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
	ORDER BY - упорядочить информацию после выборки. ASC - по возрастанию, DESC - по убыванию.
*/

select LastName, FirstName, BirthDate
from Students
order by BirthDate ASC, FirstName DESC

/*
	IN - выборка
*/

select lastname
from students
where lastname in ('Сыропятов', 'Четин', 'Болотов')

/*
	BETWEEN - диапазон
*/

select LastName, BirthDate
from Students
WHERE BirthDate BETWEEN '2004-01-01' and '2010-01-01'

select LastName, FirstName
from Students
WHERE FirstName not BETWEEN 'Ж' and 'П'

/*
	like(%,) - поиск по текстовым полям.
	% - любая последовательность символов.
	_ - любой одиночный символ.
	[] - задаем последовательность.
	[^] - задаем последовательность отсутствия
*/
select LastName, FirstName
from Students
WHERE FirstName like 'Д%' and LastName like '%'


/*------------------------------------------------------------------------------*/

/*
	INSERT - вставка
*/

INSERT INTO Students(BirthDate, FirstName, LastName)
VALUES ('1788-10-15', 'Мария', 'Сиунова'),
('1988-05-15', 'Пахан', 'Паханович')

/*
	UPDATE - изменение записи
*/

UPDATE Students
set Grants += 500
WHERE Grants is not null

/*
	DELETE - удаление записи
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
