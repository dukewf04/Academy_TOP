/* Таблица Wards */
CREATE TABLE Wards (
    id INT NOT NULL IDENTITY(1,1),
	Name NVARCHAR(20) NOT NULL UNIQUE CHECK(Name <> ''),
	Places INT NOT NULL CHECK(Places >= 1),
	DepartmentId INT NOT NULL,
	PRIMARY KEY (Id),
);

/* Таблица Departments */
CREATE TABLE Departments (
    id INT NOT NULL IDENTITY(1,1),
    Building INT NOT NULL CHECK (Building BETWEEN 1 AND 5),
	Name NVARCHAR(100) NOT NULL UNIQUE CHECK (Name <> ''),
    Financing MONEY NOT NULL DEFAULT 0,    
    PRIMARY KEY (Id)
);

/* Таблица DoctorsExaminations */
CREATE TABLE DoctorsExaminations (
    id INT NOT NULL IDENTITY(1,1),
	EndTime TIME NOT NULL,
	StartTime TIME NOT NULL CHECK(StartTime BETWEEN '8:00' AND '18:00'),
	DoctorId INT NOT NULL,
	ExaminationId INT NOT NULL,
	WardId INT NOT NULL,
    PRIMARY KEY (Id),
	CHECK(EndTime > StartTime)
);

/* Таблица Doctors */
CREATE TABLE Doctors (
    id INT NOT NULL IDENTITY(1,1),
    Name NVARCHAR(MAX) NOT NULL CHECK(Name <> ''),
	Surname NVARCHAR(MAX) NOT NULL CHECK(Surname <> ''),	
	Premium MONEY NOT NULL DEFAULT 0 CHECK(Premium >=0),
	Salary MONEY NOT NULL CHECK (Salary > 0),	
    PRIMARY KEY (Id)	
);

/* Таблица Examinations */
CREATE TABLE Examinations (
    Id INT NOT NULL IDENTITY(1,1),
	Name NVARCHAR(MAX) NOT NULL CHECK(Name <> ''),
    PRIMARY KEY (Id)
);

/* SQL Запросы */
/* 1 */ 
select count(Places) as 'Количество палат с вместимостью > 10'
from Wards
where Places > 10

/* 3 */ 
select d.Name, sum(Places) as 'PlaceCount'
from Departments as d
join wards as w on w.DepartmentId = d.id
group by d.name

/* 4 */ 
select d.Name, sum(Premium) as 'PremiumCount'
from Departments as d
join wards as w on w.DepartmentId = d.id
join DoctorsExaminations as de on w.id = de.WardId
join Doctors as doc on doc.id = de.DoctorId
group by d.name

/* 5 */
select d.Name, count(d.Name) as 'Количество врачей, которые проводят обследования в отделении'
from Departments as d
join wards as w on w.DepartmentId = d.id
join DoctorsExaminations as de on w.id = de.WardId
join Doctors as doc on doc.id = de.DoctorId
group by d.Name
having count(d.Name) >= 5

/* 6 */
select count(d.Name) as 'Количество врачей', sum(d.Salary) + sum(d.Premium) as 'Суммарная зарплата'
from Doctors as d

/* 7 */
select (sum(d.Salary) + sum(d.Premium))/count(d.id) as 'Средняя зарплата'
from Doctors as d

/* 8 */
select w.Name, count(Places) as 'Количество мест'
from Wards as w
where w.Places = (select MIN(w.Places) from wards as w)
group by w.name

/* 9 */
select d.Building
from Departments as d
join wards as w on w.DepartmentId = d.id
where (d.Building BETWEEN 1 and 3) and (w.Places > 10)
group by d.Building
having sum(w.Places) > 40
