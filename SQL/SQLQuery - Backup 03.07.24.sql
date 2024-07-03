-------------------------------------------------------
------- Резервное копирование и восстановление  -------
-------------------------------------------------------

-- Задание 1. Резервное копирование

-- 1. Создайть полную (full backup) резервную копию
alter database SportShop
set recovery full

backup database SportShop
to disk = 'D:\DB_back.bak'
with init;

-- 2. Выполнить операции по вставке, обновлению данных в таблицах базы данных
insert into SportShop.dbo.workers
values('Максим', 'Попов', 'м', 'Продавец', '2020-01-01', '25000')

-- 3. Выполнить операцию по дифференциальному сохранению бэкапа.
backup database SportShop
to disk = 'D:\DB_back_diff.bak'
with differential

-- 4. Выполнить операции по вставке, обновлению данных в таблицах базы данных
insert into SportShop.dbo.clients
values('Максим', 'Попов', 'м', 'maxp@gmail.com', '895491984', 'Ноутбук', 0, 0)

-- 5. Выполнить резервную копию журнала транзакций
backup log SportShop
to disk = 'D:\Log_backup.trn'
with init;

-- Задание 2. Резервное восстановление
-- 1. Восстановление из полной резервной копии
restore database SportShop
from disk = 'D:\DB_back.bak'
with replace

-- 2. Провести восстановление из разностной резервной копии
RESTORE DATABASE SportShop
FROM DISK = 'D:\DB_back.bak'
WITH NORECOVERY

RESTORE DATABASE SportShop
FROM DISK = 'D:\DB_back_diff.bak'
WITH NORECOVERY;

ALTER DATABASE SportShop
SET MULTI_USER;
GO


-- 3.  Провести восстановление из резервной копии журнала транзакций.
restore log SportShop
from disk = 'D:\Log_backup.trn'
