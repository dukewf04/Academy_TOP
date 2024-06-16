/* 1. Вывести названия аудиторий, в которых читает лекции преподаватель “Edward Hopper”. */
select lr.Name
from LectureRooms as lr
inner join Sheldues as s on s.LectureRoomId = lr.Id
inner join Lectures as l on l.Id = s.LectureId
inner join Teachers as t on t.Id = l.TeacherId
where t.Name = 'Edward' and t.Surname = 'Hopper'

/* 2. Вывести фамилии ассистентов, читающих лекции в группе F505 */
select t.Surname
from Teachers as t
inner join Lectures as l on l.TeacherId = t.Id
inner join GroupsLectures as gl on gl.LectureId = l.Id
inner join Groups as g on g.Id = gl.GroupId
where g.Name = 'F505'

/* 3. Вывести дисциплины, которые читает преподаватель “AlexCarmack” для групп 5-го курса */
select s.Name
from Subjects as s
inner join Lectures as l on l.SubjectId = s.Id
inner join GroupsLectures as gl on gl.LectureId = l.Id
inner join Groups as g on g.Id = gl.GroupId
inner join Teachers as t on t.Id = l.TeacherId
where t.Name = 'Alex' and t.Surname = 'Carmack' and g.Year = 5

/* 4. Вывести фамилии преподавателей, которые не читают лекции по понедельникам. */
select t.Surname
from Teachers as t
inner join Lectures as l on l.TeacherId = t.Id
inner join Schedules as s on s.LectureId = l.Id
where s.DayOfWeek <> 1

/* 5. Вывести названия аудиторий, с указанием их корпусов, в которых нет лекций в среду второй недели на третьей паре. */
select lr.Name, lr.Building
from LectureRooms as lr
left join Schedules as s on s.LectureRoomId = lr.Id
where s.DayOfWeek <> 3 and s.Week = 2

/* 6. Вывести полные имена преподавателей факультета "Computer Science", которые не курируют группы кафедры "Software Development" */
select t.Surname, t.Name
from Teachers as t
left join Deans as d on d.TeacherId = t.Id
left join Faculties as f on f.DeanId = d.Id
left join Departments as dep on dep.FacultyId = f.Id
where f.Name = 'Computer Science' and dep.Name <> 'Software Development'

/* 7. Вывести список номеров всех корпусов, которые имеются в таблицах факультетов, кафедр и аудиторий */
select f.Building
from Faculties as f
UNION
select d.Building
from Departments as d
UNION
select lr.Building
from LectureRooms as lr

/* 8. Вывести полные имена преподавателей в следующем порядке: деканы факультетов, заведующие кафедрами, преподаватели, кураторы, ассистенты. */
With cte as(
SELECT t.Surname, t.name,
  CASE
    WHEN t.Id = Deans.TeacherId THEN 1
	WHEN t.Id = Heads.TeacherId THEN 2
	WHEN t.Id = Curators.TeacherId THEN 4
	WHEN t.Id = Assistants.TeacherId THEN 5
    ELSE 3
  END AS category
FROM Teachers as t
LEFT JOIN Deans ON Deans.TeacherId = t.Id
LEFT JOIN Heads ON Heads.TeacherId = t.Id
LEFT JOIN Curators ON Curators.TeacherId = t.Id
LEFT JOIN Assistants ON Assistants.TeacherId = t.Id
)
select Surname, name as 'ФИО'
from cte
Order by category, Surname, name

/* Вывести дни недели (без повторений), в которые имеются занятия в аудиториях “A311” и “A104” корпуса 6. */
select Distinct s.DayOfWeek
from Schedules as s
inner join LectureRooms as lr on lr.Id = s.LectureRoomId
where lr.Name in ('A311', 'A104') and lr.Building = 6