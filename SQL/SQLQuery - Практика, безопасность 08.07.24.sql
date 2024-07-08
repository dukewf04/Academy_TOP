create login [Олег]
with password = '123'

-- Безопасносить. Часть 1
-- 1. Предоставьте пользователю с логином Марк возможность выполнять любые операции на уровне сервера
USE [master]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER mark
GO

-- 2. Предоставьте пользователю с логином Ирина возможность создавать базы данных
GO
ALTER SERVER ROLE [dbcreator] ADD MEMBER irina
GO

-- 3. Предоставьте пользователямс логинами Борис,Александр, Алексей, Ольга, Елена
-- возможность выполнять любые операции на уровне сервера
USE [master]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [Борис]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [Александр]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [Алексей]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [Ольга]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [Елена]
GO

-- 4. Mixed аутентификация
USE [master]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [Марк]

GO
CREATE LOGIN [Марк] WITH PASSWORD = '123456'
GO

-- Безопасносить. Часть 2. Выполнение заданий, используя хранимые процедуры или запросы:
-- 1. Показать список серверных ролей
SELECT * FROM sys.server_principals WHERE type_desc = 'SERVER_ROLE';

-- 2. Показать разрешения серверных ролей
SELECT DISTINCT permission_name
FROM sys.server_permissions
where class_desc = 'SERVER'

-- 3. Показать членов серверной роли sysadmin
EXEC sp_helpsrvrolemember 'sysadmin';

-- 4. Показать членов серверной роли dbcreator
EXEC sp_helpsrvrolemember 'dbcreator';

-- 5. Проверить является ли пользователь с логином Марк членом серверной роли sysadmin
SELECT IS_SRVROLEMEMBER('sysadmin', 'Mark') AS IsSysadmin;


-- Безопасносить. Часть 3.
-- 1. Предоставляем пользователю с логином Марк полный доступ к базе данных
USE SportShop
GO
CREATE USER Mark FOR LOGIN Mark
GO
EXEC sp_addrolemember 'db_owner', 'Марк'
GO

-- 2. Разрешаем пользователю с логином Ирина читать данные из всех таблиц
CREATE USER [Ирина] FOR LOGIN [Ирина]
GO
EXEC sp_addrolemember 'db_datareader', 'Ирина'
GO

-- 3. Запрещаем пользователю с логином Ирина запись данных во все таблицы
GO
exec sp_droprolemember 'db_datawriter', 'Ирина'
GO

-- 4. Разрешаем пользователю с логином Марат создавать резервные копии базы данных
CREATE USER [Марат] FOR LOGIN [Марат]
GO
GRANT BACKUP DATABASE TO [Марат]
GO

-- 5. Предоставляем пользователю с логином Олег возможность создавать объекты внутри базы данных
CREATE USER [Олег] FOR LOGIN [Олег]
GO
GRANT CREATE TABLE, CREATE VIEW TO [Олег]
GO