-- ������� 1.
-- 1. ��������� ������������ � ������� ���� �������� ���������� � ���������
CREATE USER [����] FOR LOGIN [����];
USE [SportShop]
DENY SELECT ON workers TO [����];

-- 2. ��������� ������������ � ������� ����� �������� ���������� ������ � ���������
CREATE USER [�����] FOR LOGIN [�����];
GRANT SELECT ON dbo.workers TO [�����];

-- 3. ������������ ������ ������ � ���� ������ ������������ � ������� �����
CREATE USER Olga FOR LOGIN Olga;
GRANT CONTROL ON DATABASE::SportShop TO Olga;

-- 4. ������������ ������ ������ �� ������ ������ � ����������� � ���������, ������� � ������� ������������ � ������� ����������
CREATE USER [����������] FOR LOGIN [����������];
GRANT SELECT ON dbo.workers TO [����������];
GRANT SELECT ON dbo.products TO [����������];

-- ������� 2.
-- 1. ������������ ������������ � ������� ���� ������ �� ������ ���� ������
EXEC sp_msforeachtable 'GRANT SELECT ON ? TO [����]'

-- 2. ��������� ������������ � ������� ���� �������� ������ �� ���� ��������
EXEC sp_msforeachtable 'DENY INSERT, UPDATE, DELETE ON ? TO [����]'

-- 3. ��������� ���� �������������, ����� ������������ � ������� �������, ������ ������ �� ������� ��������
DENY SELECT ON dbo.albums TO PUBLIC
GRANT SELECT ON dbo.albums TO [�������]

-- 4. ������������ ����������� ������ ������ �� ������� ������ ������������� � ��������: �����, �����, �������, �����
GRANT SELECT ON dbo.Styles TO [�����]
GRANT SELECT ON dbo.Styles TO [�����]
GRANT SELECT ON dbo.Styles TO [�������]
GRANT SELECT ON dbo.Styles TO [�����]