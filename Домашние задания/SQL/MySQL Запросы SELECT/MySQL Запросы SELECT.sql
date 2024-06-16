/* 1. Вывести содержимое таблицы палат */
select *
from Wards

/* 2. Вывести фамилии и телефоны всех врачей. */
select d.Surname, d.Phone
from Doctors as d

/* 3. Вывести все этажи без повторений, на которых располагаются палаты. */
select distinct w.floor
from Wards as w

/* 4. Вывестин азвания заболеваний под именем “NameofDisease” и степень их тяжести под именем “Severity of Disease”. */
select name as 'NameofDisease', severity as 'Severity of Disease'
from Diseases

/* 5. Использовать выражение FROM для любых трех таблиц базы данных, используя для них псевдонимы. */
select doc.Name, w.floor, dis.Severity
from Doctors as doc, Wards as w, Diseases as dis

/* 6. Вывести названия отделений, расположенных в корпусе 5 и имеющих фонд финансирования менее 30000. */
select d.Name
from Departments as d
where d.Building = 5 and d.Financing < 30000

/* 7. Вывестиназвания отделений, расположенных в 3-мкорпусе с фондом финансирования в диапазоне от 12000 до 15000. */
select d.Name
from Departments as d
where d.Building = 3 and d.Financing between 12000 and 15000

/* 8. Вывести названия палат, расположенных в корпусах 4 и 5 на 1-м этаже */
select w.Name
from Wards as w
where w.Building in (4,5) and w.Floor = 1

/* 9. Вывести названия, корпуса и фонды финансирования отделений, расположенных в корпусах 3 или 6 и имеющих фонд финансирования меньше 11000 или больше 25000. */
select d.Name, d.Financing
from Departments as d
where (d.Building = 3 or d.Building = 6) and (d.Financing < 11000 or d.Financing > 25000)

/* 10. Вывести фамилии врачей, чья зарплата (сумма ставки и надбавки) превышает 1500 */
select d.Surname
from Doctors as d
where (d.Salary + d.Premium) > 1500

/* 11. Вывести фамилии врачей, у которых половина зарплаты превышает троекратную надбавку */
select d.Surname
from Doctors as d
where d.Salary/2 > d.Premium * 3

/* 12. Вывести названия обследований без повторений, проводимых в первые три дня недели с 12:00 до 15:00. */
select distinct e.Name
from Examinations as e
where (e.DayOfWeek between 1 and 3) and (e.StartTime >= '12:00' and e.EndTime <= '15:00')

/* 13. Вывести названия и номера корпусов отделений, расположенных в корпусах 1, 3, 8 или 10. */
select d.Name, d.Building
from Departments as d
where d.Building in (1,3,8,10)

/* 14. Вывести названия заболеваний всех степеней тяжести, кроме 1-й и 2-й. */
select d.Name
from Diseases as d
where d.Severity  not in (1,2)

/* 15. Вывести названия отделений, которые не располагаются в 1-м или 3-м корпусе. */
select d.Name
from Departments as d
where d.Building not in (1,3)

/* 16. Вывести названия отделений, которые располагаются в 1-м или 3-м корпусе */
select d.Name
from Departments as d
where d.Building in (1,3)

/* 17. Вывести фамилии врачей, начинающиеся на букву “N”. */
select d.Name
from Doctors as d
where d.Name LIKE 'N%'