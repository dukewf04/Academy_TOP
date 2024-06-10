/* ����������� ������ */
/*********************/

/* EXIST - ���������� ������ � �������� ������ � �������������� �������. */
/* ��� EXIST ������������ �������� - � SELECT ������� ��������� (*) */
select firstname, lastname, birthdate, email
from Students
where exists(
		select *
		from Achievements as ach
		where ach.StudentId = Students.Id
)

/* ANY/SOME - ��������� ���� � ���� �������� - �������� ���������� ��������� �������, ������� ������������ ����������� */
select firstname, lastname, birthdate, email
from Students
where id = ANY(
		select ach.studentId
		from Achievements as ach
		where ach.StudentId = Students.Id
)

/* 
	ALL - ������������ ��� ��������� ����������� ����������, ����� �������,
	����� ������� ������� ��� ����������, ��������������� �������� ���������� ��� ����������
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
	UNION - ����������� ����������� �������. ���������� �������� � ����� �������� ������ ���� ����������.
*/

select firstName + ' ' + lastname as fullname, birthdate
from Students
where month(BirthDate) > 5 and month(BirthDate) < 9
UNION
select t.FirstName + ' ' + t.lastname as fullname, birthdate
from Teachers as t
where month(BirthDate) > 1 and month(BirthDate) < 12
order by birthdate

