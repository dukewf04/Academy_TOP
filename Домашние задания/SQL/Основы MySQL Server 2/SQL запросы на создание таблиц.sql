/* Таблица Groups */
CREATE TABLE Groups (
    id INT NOT NULL IDENTITY(1,1),
	Name NVARCHAR(10) NOT NULL UNIQUE,
	Rating INT NOT NULL CHECK (Rating BETWEEN 0 AND 5),
	Year INT NOT NULL CHECK (Year BETWEEN 0 AND 5),    
    PRIMARY KEY (Id)
);

/* Таблица Departments */
CREATE TABLE Departments (
    id INT NOT NULL IDENTITY(1,1),
	Financing MONEY NOT NULL DEFAULT 0 CHECK (Financing > 0),
	Name NVARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (Id)
);

/* Таблица Faculties */
CREATE TABLE Faculties (
    id INT NOT NULL IDENTITY(1,1),
	Name NVARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (Id)
);

/* Таблица Teachers */
CREATE TABLE Teachers (
    id INT NOT NULL IDENTITY(1,1),
	EmploymentDate DATE NOT NULL CHECK(EmploymentDate >= '01.01.1990'),
	Name NVARCHAR(MAX) NOT NULL,
	Surname NVARCHAR(MAX) NOT NULL,
	Premium MONEY NOT NULL DEFAULT 0 CHECK(Premium > 0),
	Salary MONEY NOT NULL CHECK(Salary > 0),
    PRIMARY KEY (Id)
);