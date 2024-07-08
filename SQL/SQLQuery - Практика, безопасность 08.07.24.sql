create login [����]
with password = '123'

-- �������������. ����� 1
-- 1. ������������ ������������ � ������� ���� ����������� ��������� ����� �������� �� ������ �������
USE [master]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER mark
GO

-- 2. ������������ ������������ � ������� ����� ����������� ��������� ���� ������
GO
ALTER SERVER ROLE [dbcreator] ADD MEMBER irina
GO

-- 3. ������������ �������������� �������� �����,���������, �������, �����, �����
-- ����������� ��������� ����� �������� �� ������ �������
USE [master]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [�����]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [���������]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [�������]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [�����]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [�����]
GO

-- 4. Mixed ��������������
USE [master]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [����]

GO
CREATE LOGIN [����] WITH PASSWORD = '123456'
GO

-- �������������. ����� 2. ���������� �������, ��������� �������� ��������� ��� �������:
-- 1. �������� ������ ��������� �����
SELECT * FROM sys.server_principals WHERE type_desc = 'SERVER_ROLE';

-- 2. �������� ���������� ��������� �����
SELECT DISTINCT permission_name
FROM sys.server_permissions
where class_desc = 'SERVER'

-- 3. �������� ������ ��������� ���� sysadmin
EXEC sp_helpsrvrolemember 'sysadmin';

-- 4. �������� ������ ��������� ���� dbcreator
EXEC sp_helpsrvrolemember 'dbcreator';

-- 5. ��������� �������� �� ������������ � ������� ���� ������ ��������� ���� sysadmin
SELECT IS_SRVROLEMEMBER('sysadmin', 'Mark') AS IsSysadmin;


-- �������������. ����� 3.
-- 1. ������������� ������������ � ������� ���� ������ ������ � ���� ������
USE SportShop
GO
CREATE USER Mark FOR LOGIN Mark
GO
EXEC sp_addrolemember 'db_owner', '����'
GO

-- 2. ��������� ������������ � ������� ����� ������ ������ �� ���� ������
CREATE USER [�����] FOR LOGIN [�����]
GO
EXEC sp_addrolemember 'db_datareader', '�����'
GO

-- 3. ��������� ������������ � ������� ����� ������ ������ �� ��� �������
GO
exec sp_droprolemember 'db_datawriter', '�����'
GO

-- 4. ��������� ������������ � ������� ����� ��������� ��������� ����� ���� ������
CREATE USER [�����] FOR LOGIN [�����]
GO
GRANT BACKUP DATABASE TO [�����]
GO

-- 5. ������������� ������������ � ������� ���� ����������� ��������� ������� ������ ���� ������
CREATE USER [����] FOR LOGIN [����]
GO
GRANT CREATE TABLE, CREATE VIEW TO [����]
GO