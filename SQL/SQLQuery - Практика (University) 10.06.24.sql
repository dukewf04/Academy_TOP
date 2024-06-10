/* Объединение таблиц */
/*********************/

/* EXIST - возвращает истину и помещает запрос в результирующую таблицу. */
/* Для EXIST обязательным условием - в SELECT указана звездочка (*) */
select firstname, lastname, birthdate, email
from Students
where exists(
		select *
		from Achievements as ach
		where ach.StudentId = Students.Id
)

/* ANY/SOME - выполняют одно и тоже действие - проверку выполнения заданного условия, который определяется подзапросом */
select firstname, lastname, birthdate, email
from Students
where id = ANY(
		select ach.studentId
		from Achievements as ach
		where ach.StudentId = Students.Id
)

/* 
	ALL - используется при сравнении результатов подзапроса, таким образом,
	чтобы указать условию все результаты, удовлетворяющие значению подзапроса без исключения
*/

select lastname, firstname, Assesment
from Students as s, Achievements as a
where a.StudentId = s.Id and
a.Assesment >= ALL (
		select avg(assesment)
		from Achievements
		group by StudentId
)

/* 
	UNION - объединение результатов запроса. Количество столбцов в обеих таблицах должно быть одинаковым.
*/

select firstName + ' ' + lastname as fullname, birthdate
from Students
where month(BirthDate) > 5 and month(BirthDate) < 9
UNION
select t.FirstName + ' ' + t.lastname as fullname, birthdate
from Teachers as t
where month(BirthDate) > 1 and month(BirthDate) < 12
order by birthdate

