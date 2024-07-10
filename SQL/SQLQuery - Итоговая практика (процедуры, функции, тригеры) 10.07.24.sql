-- Задание 1
CREATE TABLE barbers (
    id INT NOT NULL IDENTITY(1,1),
	name NVARCHAR(30) not null,
	surname NVARCHAR(30) not null,
	phone int unique,
	email NVARCHAR(30) unique,
	birthday date,
	employment_date date,
	position_id int not null,
	service_id int not null,
	feedback_id int not null, 
	grade_id int not null,
    PRIMARY KEY (id)
);

INSERT INTO barbers
VALUES 
('Александр', 'Смирнов', 912345678, 'a.smirnov@email.com', '1980-06-15', '2010-05-01', 1, 1, 1, 1),
('Михаил', 'Иванов', 923456789, 'm.ivanov@email.com', '1985-07-20', '2012-08-15', 2, 1, 2, 2),
('Дмитрий', 'Петров', 934567890, 'd.petrov@email.com', '1990-08-25', '2015-09-20', 3, 1, 3, 3),
('Евгений', 'Николаев', 945678901, 'e.nikolaev@email.com', '1975-09-30', '2008-10-10', 1, 2, 4, 4),
('Андрей', 'Соколов', 956789012, 'a.sokolov@email.com', '1982-11-05', '2011-11-11', 2, 2, 5, 5);
----------------------------------------------
----------------------------------------------
CREATE TABLE positions (
    id INT NOT NULL IDENTITY(1,1),
	name nvarchar(50) not null unique,
    PRIMARY KEY (id)
);

INSERT INTO positions (name) 
VALUES
('чиф-барбер'),
('синьор-барбер'),
('джуниор-барбер');
----------------------------------------------
----------------------------------------------
CREATE TABLE services (
    id INT NOT NULL IDENTITY(1,1),
	name nvarchar(50) not null unique,
	price money not null,
	duration time not null,
    PRIMARY KEY (id)
);

INSERT INTO services 
VALUES
('Стрижка', 1000, '0:40'),
('Бритье бороды', 600, '0:30');
----------------------------------------------
----------------------------------------------
CREATE TABLE feedbacks (
    id INT NOT NULL IDENTITY(1,1),
	client_id int not null,
	barber_id int not null,
	feedback nvarchar(250),
    PRIMARY KEY (id)
);

INSERT INTO feedbacks 
VALUES
(1, 2, 'Круто!'),
(2, 2, 'Супер, всем советую!'),
(3, 1, 'На троечку(');
----------------------------------------------
----------------------------------------------
CREATE TABLE grades (
    id INT NOT NULL IDENTITY(1,1),
	client_id int not null,
	barber_id int not null,
	grade int not null,
    PRIMARY KEY (id)
);

INSERT INTO grades 
VALUES
(1, 2, 5),
(2, 2, 5),
(3, 1, 3);
----------------------------------------------
----------------------------------------------
CREATE TABLE barber_schedules (
    id INT NOT NULL IDENTITY(1,1),
	barber_id int not null,
	date date not null,
	is_available bit not null,
	client_id int,
    PRIMARY KEY (id)
);

INSERT INTO barber_schedules 
VALUES
(1, '2024-07-15', 1, null),
(1, '2024-08-15', 0, 2),
(2, '2024-07-25', 1, null);
----------------------------------------------
----------------------------------------------
CREATE TABLE clients (
    id INT NOT NULL IDENTITY(1,1),
	name NVARCHAR(30) not null,
	surname NVARCHAR(30) not null,
	phone NVARCHAR(20) unique,
	email NVARCHAR(30) unique,
	feedback_id int not null,
	grade_id int not null,
    PRIMARY KEY (id)
);

INSERT INTO clients 
VALUES 
('Иван', 'Иванов', '1234567890', 'ivan.ivanov@email.com', 1, 1),
('Петр', 'Петров', '2345678901', 'petr.petrov@email.com', 2, 2),
('Сергей', 'Сергеев', '3456789012', 'sergey.sergeev@email.com', 3, 3),
('Алексей', 'Алексеев', '4567890123', 'alexey.alekseev@email.com', 4, 4),
('Николай', 'Николаев', '5678901234', 'nikolay.nikolaev@email.com', 5, 5);
----------------------------------------------
----------------------------------------------
CREATE TABLE visits (
    id INT NOT NULL IDENTITY(1,1),
	client_id int not null,
	barber_id int not null,
	service_id int not null,
	visit_date date,
	cost money,
	grade int,
	feedback NVARCHAR(250),
    PRIMARY KEY (id)
);

INSERT INTO visits 
VALUES
(1, 1, 1, '2024-03-15', 600, 5, 'Вроде ок'),
(2, 3, 1, '2024-02-5', 800, 5, 'Вроде ок'),
(3, 2, 2, '2024-01-1', 600, 2, 'Был пьяный!');

-- Задание 2
-- 1. Вернуть ФИО всех барберов салона
create procedure getAllBarbersName
as
begin
	select surname + ' ' + name as 'Фамилия Имя'
	from barbers
end
exec getAllBarbersName

-- 2. Вернуть информацию о всех синьор-барберах
create procedure getAllSeniorBarbers
as
begin
	select b.*
	from barbers as b
	inner join positions as p on p.id = b.position_id
	where p.name = 'синьор-барбер'
end
exec getAllSeniorBarbers

-- 3. Вернуть информацию о всех барберах, которые могут предоставить услугу традиционного бритья бороды
create procedure getAllBarbersWithShavingService
as
begin
	select b.*
	from barbers as b
	inner join services as s on s.id = b.service_id
	where s.name = 'Бритье бороды'
end
exec getAllBarbersWithShavingService

-- 4. Вернуть информацию о всех барберах, которые могут предоставить конкретную услугу.
-- Информация о требуемой услуге предоставляется в качестве параметра
create function funcGetBarbersServices(@name nvarchar(50))
returns table
as
return (
	select b.*
	from barbers as b
	inner join services as s on s.id = b.service_id
	where s.name = @name
)
go
select * from funcGetBarbersServices('Стрижка');

-- 5. Вернуть информацию о всех барберах, которые работают свыше указанного количества лет. Количество лет передаётся в качестве параметра
create function funcGetBarbersWithWorkExperience(@year int)
returns table
as
return (
	select *
	from barbers
	where (datepart(year, getdate()) - YEAR(employment_date)) > @year
)
go
select * from funcGetBarbersWithWorkExperience(13);

-- 6. Вернуть количество синьор-барберов и количество джуниор-барберов
create procedure getSeniorAndJuniorBarbers
as
begin
	select
		case
			when p.name like '%джуниор%' THEN count(b.position_id)
			else null
		end as 'Количество джунов',
		case
			when p.name like '%синьор%' THEN count(b.position_id)
			else null
		end as 'Количество синьоров'
	from barbers as b
	inner join positions as p on p.id = b.position_id
end
exec getSeniorAndJuniorBarbers

CREATE PROCEDURE getSeniorAndJuniorBarbers
AS
BEGIN
    SELECT
        SUM(CASE WHEN p.name LIKE '%джуниор%' THEN 1 ELSE 0 END) AS 'Количество джунов',
        SUM(CASE WHEN p.name LIKE '%синьор%' THEN 1 ELSE 0 END) AS 'Количество синьоров'
    FROM barbers AS b
    INNER JOIN positions AS p ON p.id = b.position_id
    GROUP BY p.name
END
EXEC getSeniorAndJuniorBarbers;