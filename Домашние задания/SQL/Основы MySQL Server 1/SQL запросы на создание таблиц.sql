/* Таблица Departments */
CREATE TABLE Departments (
    id INT NOT NULL IDENTITY(1,1),
    Building INT NOT NULL,
    Financing MONEY NOT NULL DEFAULT 0,
    Name NVARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (Id),
    CHECK (Building BETWEEN 1 AND 5),
	CHECK (Financing >= 0)
);

/* Таблица Diseases */
CREATE TABLE Diseases (
    id INT NOT NULL IDENTITY(1,1),
    Name NVARCHAR(100) NOT NULL UNIQUE,
    Severity INT NOT NULL DEFAULT 1,
    PRIMARY KEY (Id),
	CHECK (Severity >= 1)
);

/* Таблица Doctors */
CREATE TABLE Doctors (
    id INT NOT NULL IDENTITY(1,1),
    Name NVARCHAR(MAX) NOT NULL,
	Surname NVARCHAR(MAX) NOT NULL,
    Phone CHAR(10),
	Salary MONEY NOT NULL,
    PRIMARY KEY (Id),
	CHECK (Salary > 0)
);

/* Таблица Examinations */
CREATE TABLE Examinations (
    id INT NOT NULL IDENTITY(1,1),
	DayOfWeek INT NOT NULL CHECK(DayOfWeek BETWEEN 1 AND 7),
	EndTime TIME NOT NULL,
	StartTime TIME NOT NULL CHECK(StartTime BETWEEN '8:00' AND '18:00'),
    Name NVARCHAR(100) NOT NULL,
    PRIMARY KEY (Id),
	CHECK(EndTime > StartTime)
);