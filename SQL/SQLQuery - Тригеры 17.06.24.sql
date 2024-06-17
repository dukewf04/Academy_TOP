/* CREATE TRIGGER addStudents
on Students
for insert, update
as
raiserror('%d ����� ��������� ��� ���������������', 0, 1, @@rowcount)
return
*/

--insert into Students(FirstName, LastName, BirthDate, Grants, Email, GroupsId)
--values('King', 'Artur', '03.03.24', 12, 'kingartur@gmail.com', 1)

/*
CREATE TRIGGER addTeacher
on Teachers
for insert
as
begin
	-- ������� ���������� � ����������� �� �������� �� �������
	declare @Birthdate smalldatetime
	declare @BirthDateUserInsert smalldatetime
	SET @BirthDateUserInsert = getdate()-9125
	select @Birthdate = BirthDate
	from inserted
	if (@BirthDate >= @BirthDateUserInsert)
	begin
		print(@BirthDateUserInsert)
		print('������������� ������� �������� ' + @BirthDateUserInsert)
	end
	else
	begin
		raiserror('������������ ����', 0, 1)
		rollback transaction
	end
end

insert into Teachers(Id, LastName, FirstName, BirthDate, DepartmentId)
values(6, 'King', 'Artur', '03-03-24', 2)
*/

create Trigger CheckGroupDelete
on Groups
for delete
as
	begin
		declare @NameGroup varchar(25),
		@IdFaculty int
		select @NameGroup = deleted.GroupName
		from deleted
		if (@NameGroup = 'AAA' or @NameGroup = 'BBB')
		begin
			raiserror('�� �� ������ ������� ��� ������', 0, 1)
			rollback transaction
		end
		else
		begin
			print('�������� ������ �������')
		end
	end

delete from Groups
where GroupName = 'BBB'