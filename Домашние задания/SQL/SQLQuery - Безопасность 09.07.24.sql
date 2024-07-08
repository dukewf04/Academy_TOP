-- Задание 1.
-- 1. Запретить пользователю с логином Марк получать информацию о продавцах
CREATE USER [Марк] FOR LOGIN [Марк];
USE [SportShop]
DENY SELECT ON workers TO [Марк];

-- 2. Разрешить пользователю с логином Дэвид получать информацию только о продавцах
CREATE USER [Дэвид] FOR LOGIN [Дэвид];
GRANT SELECT ON dbo.workers TO [Дэвид];

-- 3. Предоставить полный доступ к базе данных пользователю с логином Ольга
CREATE USER Olga FOR LOGIN Olga;
GRANT CONTROL ON DATABASE::SportShop TO Olga;

-- 4. Предоставить доступ только на чтение таблиц с информацией о продавцах, товарах в наличии пользователю с логином Константин
CREATE USER [Константин] FOR LOGIN [Константин];
GRANT SELECT ON dbo.workers TO [Константин];
GRANT SELECT ON dbo.products TO [Константин];

-- Задание 2.
-- 1. Предоставить пользователю с логином Олег доступ на чтение всех таблиц
EXEC sp_msforeachtable 'GRANT SELECT ON ? TO [Олег]'

-- 2. Запретить пользователю с логином Олег изменять данные во всех таблицах
EXEC sp_msforeachtable 'DENY INSERT, UPDATE, DELETE ON ? TO [Олег]'

-- 3. Запретить всем пользователям, кроме пользователя с логином Дмитрий, читать данные из таблицы альбомов
DENY SELECT ON dbo.albums TO PUBLIC
GRANT SELECT ON dbo.albums TO [Дмитрий]

-- 4. Предоставить возможность чтения данных из таблицы стилей пользователям с логинами: Борис, Диана, Николай, Ирина
GRANT SELECT ON dbo.Styles TO [Борис]
GRANT SELECT ON dbo.Styles TO [Диана]
GRANT SELECT ON dbo.Styles TO [Николай]
GRANT SELECT ON dbo.Styles TO [Ирина]