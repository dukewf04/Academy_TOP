-------------------------------------------------------
------- ��������� ����������� � ��������������  -------
-------------------------------------------------------

-- ������� 1. ��������� �����������

-- 1. �������� ������ (full backup) ��������� �����
alter database SportShop
set recovery full

backup database SportShop
to disk = 'D:\DB_back.bak'
with init;

-- 2. ��������� �������� �� �������, ���������� ������ � �������� ���� ������
insert into SportShop.dbo.workers
values('������', '�����', '�', '��������', '2020-01-01', '25000')

-- 3. ��������� �������� �� ����������������� ���������� ������.
backup database SportShop
to disk = 'D:\DB_back_diff.bak'
with differential

-- 4. ��������� �������� �� �������, ���������� ������ � �������� ���� ������
insert into SportShop.dbo.clients
values('������', '�����', '�', 'maxp@gmail.com', '895491984', '�������', 0, 0)

-- 5. ��������� ��������� ����� ������� ����������
backup log SportShop
to disk = 'D:\Log_backup.trn'
with init;

-- ������� 2. ��������� ��������������
-- 1. �������������� �� ������ ��������� �����
restore database SportShop
from disk = 'D:\DB_back.bak'
with norecovery, replace;

-- 2. �������� �������������� �� ���������� ��������� �����
restore database SportShop
from disk = 'D:\DB_back_diff.bak'
with norecovery;

-- 3.  �������� �������������� �� ��������� ����� ������� ����������.
restore log SportShop
from disk = 'D:\DB_log.trn'
with recovery;
