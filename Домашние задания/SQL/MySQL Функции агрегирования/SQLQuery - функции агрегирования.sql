/* ������� Departments */
CREATE TABLE Departments (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY (Id),
	Financing MONEY NOT NULL DEFAULT 0 CHECK (Financing > 0),
	Name NVARCHAR(100) NOT NULL UNIQUE,
    FacultyId int not null,
	FOREIGN KEY (FacultyId) REFERENCES Faculties(Id)
);

/* ������� Faculties */
CREATE TABLE Faculties (
    id INT NOT NULL IDENTITY(1,1),
	Name NVARCHAR(100) NOT NULL UNIQUE check(name <> ''),
    PRIMARY KEY (Id)
);

/* ������� Groups */
CREATE TABLE Groups (
    id INT NOT NULL IDENTITY(1,1),
	Name NVARCHAR(10) NOT NULL UNIQUE check(name <> ''),
	Year INT NOT NULL CHECK (Year BETWEEN 0 AND 5),
	DepartmentId int not null,
    PRIMARY KEY (Id),
	foreign key (DepartmentId) references Departments(Id)
);

/* ������� GroupsLectures */ 
CREATE TABLE GroupsLectures (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY (Id),
	GroupId int not null,
	LectureId int not null,
	foreign key (GroupId) references Groups(Id),
	foreign key (LectureId) references Lectures(Id),
);

/* ������� Lectures */
CREATE TABLE Lectures (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY (Id),
	DayOfWeek int not null check(DayOfWeek between 1 and 7),
	LectureRoom nvarchar(max) not null check(LectureRoom <> ''),
	SubjectId int not null,
	TeacherId int not null,
	foreign key (SubjectId) references Subjects(Id),
	foreign key (TeacherId) references Teachers(Id),
);

/* ������� Subjects */ 
CREATE TABLE Subjects (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY (Id),
	name nvarchar(100) not null unique check(name <> ''),
);

/* ������� Teachers */ 
CREATE TABLE Teachers (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY (Id),
	name nvarchar(max) not null check(name <> ''),
	Surname nvarchar(max) not null check(Surname <> ''),
	Salary money not null check(Salary > 0)
);


/* ������� � �������� */ 

/* 1. ���������� �������������� ������� Software Development */
select count(*) as 'Count teachers'
from Teachers as t, Lectures as l, GroupsLectures as gl, Groups as g, Departments as d
where t.Id = l.TeacherId and l.id = gl.LectureId and gl.GroupId = g.Id and g.DepartmentId = d.Id
and d.Name = 'Software Development'

/* 2. ������� ���������� ������, ������� ������ ������������� �Dave McQueen� */
select count(*) as 'Count lectures'
from Lectures as l, Teachers as t
where t.Id = l.TeacherId and t.name = 'Dave' and t.Surname = 'McQueen'

/* 3. ������� ���������� �������, ���������� � ��������� �D201� */
select count(*) as 'Count lectures'
from Lectures
where LectureRoom = 'D201'

/* 4. ������� �������� ��������� � ���������� ������, ���������� � ��� */
select LectureRoom, count(SubjectId) as '���������� ������'
from Lectures
group by LectureRoom

/* 5. ������� ���������� ���������, ���������� ������ ������������� �Jack Underhill� */
/* � ������� ��� ���������� �� ���������! */

/* 6. ������� ������� ������ �������������� ���������� �Computer Science�. */
select avg(t.Salary) as '������� ������'
from Teachers as t, Lectures as l, GroupsLectures as gl, Groups as g, Departments as d, Faculties as f
where t.Id = l.TeacherId and l.id = gl.LectureId and gl.GroupId = g.Id and g.DepartmentId = d.Id and d.FacultyId = f.Id
and f.Name = 'Computer Science'

/* 7. ������� ����������� � ������������ ���������� ��������� ����� ���� ����� */
/* � ������� ��� ���������� �� ���������! */

/* 8. ������� ������� ���� �������������� ������ */
select avg(Financing) as '������� ���� ��������������'
from Departments

/* 9. ������� ������ ����� �������������� � ���������� �������� ��� ��������� */
select t.name + ' ' + t.Surname as '���', count(l.SubjectId) as '���������� �������� ���������'
from Teachers as t, Lectures as l
group by t.name + ' ' + t.Surname

/* 9. ������� ������ ����� �������������� � ���������� �������� ��� ��������� */
select t.name + ' ' + t.Surname as '���', count(l.SubjectId) as '���������� �������� ���������'
from Teachers as t
left join Lectures as l on t.id = l.TeacherId
group by t.name + ' ' + t.Surname

/* 10. ������� ���������� ������ � ������ ���� ������ */
select DayOfWeek, count(SubjectId) as '���������� ������ � ������ ���� ������'
from Lectures
group by DayOfWeek

/* 11. ������� ������ ��������� � ���������� ������, ��� ������ � ��� ��������. */ --
select l.LectureRoom, count(g.DepartmentId) '���������� ������'
from Lectures as l
left join GroupsLectures as gl on gl.LectureId = l.id
left join Groups as g on g.id = gl.GroupId
group by l.LectureRoom

/* 12. ������� �������� ����������� � ���������� ���������, ������� �� ��� �������� */
select f.Name, count(gl.LectureId) as '���������� ���������'
from Faculties as f
left join Departments as d on d.FacultyId = f.id
left join Groups as g on g.DepartmentId = d.Id
left join GroupsLectures as gl on gl.GroupId = g.id
group by f.Name

/* 13. ������� ���������� ������ ��� ������ ���� �������������-��������� */
select t.name + ' ' + t.Surname as '���', l.LectureRoom, count(l.SubjectId) as '���������� ������'
from Teachers as t
left join Lectures as l on l.TeacherId = t.id
group by t.name + ' ' + t.Surname, l.LectureRoom
having l.LectureRoom is not null