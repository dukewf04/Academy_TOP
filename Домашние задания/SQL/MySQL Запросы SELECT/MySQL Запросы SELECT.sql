/* 1. ������� ���������� ������� ����� */
select *
from Wards

/* 2. ������� ������� � �������� ���� ������. */
select d.Surname, d.Phone
from Doctors as d

/* 3. ������� ��� ����� ��� ����������, �� ������� ������������� ������. */
select distinct w.floor
from Wards as w

/* 4. �������� ������� ����������� ��� ������ �NameofDisease� � ������� �� ������� ��� ������ �Severity of Disease�. */
select name as 'NameofDisease', severity as 'Severity of Disease'
from Diseases

/* 5. ������������ ��������� FROM ��� ����� ���� ������ ���� ������, ��������� ��� ��� ����������. */
select doc.Name, w.floor, dis.Severity
from Doctors as doc, Wards as w, Diseases as dis

/* 6. ������� �������� ���������, ������������� � ������� 5 � ������� ���� �������������� ����� 30000. */
select d.Name
from Departments as d
where d.Building = 5 and d.Financing < 30000

/* 7. ��������������� ���������, ������������� � 3-�������� � ������ �������������� � ��������� �� 12000 �� 15000. */
select d.Name
from Departments as d
where d.Building = 3 and d.Financing between 12000 and 15000

/* 8. ������� �������� �����, ������������� � �������� 4 � 5 �� 1-� ����� */
select w.Name
from Wards as w
where w.Building in (4,5) and w.Floor = 1

/* 9. ������� ��������, ������� � ����� �������������� ���������, ������������� � �������� 3 ��� 6 � ������� ���� �������������� ������ 11000 ��� ������ 25000. */
select d.Name, d.Financing
from Departments as d
where (d.Building = 3 or d.Building = 6) and (d.Financing < 11000 or d.Financing > 25000)

/* 10. ������� ������� ������, ��� �������� (����� ������ � ��������) ��������� 1500 */
select d.Surname
from Doctors as d
where (d.Salary + d.Premium) > 1500

/* 11. ������� ������� ������, � ������� �������� �������� ��������� ����������� �������� */
select d.Surname
from Doctors as d
where d.Salary/2 > d.Premium * 3

/* 12. ������� �������� ������������ ��� ����������, ���������� � ������ ��� ��� ������ � 12:00 �� 15:00. */
select distinct e.Name
from Examinations as e
where (e.DayOfWeek between 1 and 3) and (e.StartTime >= '12:00' and e.EndTime <= '15:00')

/* 13. ������� �������� � ������ �������� ���������, ������������� � �������� 1, 3, 8 ��� 10. */
select d.Name, d.Building
from Departments as d
where d.Building in (1,3,8,10)

/* 14. ������� �������� ����������� ���� �������� �������, ����� 1-� � 2-�. */
select d.Name
from Diseases as d
where d.Severity  not in (1,2)

/* 15. ������� �������� ���������, ������� �� ������������� � 1-� ��� 3-� �������. */
select d.Name
from Departments as d
where d.Building not in (1,3)

/* 16. ������� �������� ���������, ������� ������������� � 1-� ��� 3-� ������� */
select d.Name
from Departments as d
where d.Building in (1,3)

/* 17. ������� ������� ������, ������������ �� ����� �N�. */
select d.Name
from Doctors as d
where d.Name LIKE 'N%'