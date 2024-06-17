/* CREATE TRIGGER addStudents
on Students
for insert, update
as
raiserror('%d строк добавлено или модифицированно', 0, 1, @@rowcount)
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
	-- Создаем переменную и присваиваем ей значение из вставки
	declare @Birthdate smalldatetime
	declare @BirthDateUserInsert smalldatetime
	SET @BirthDateUserInsert = getdate()-9125
	select @Birthdate = BirthDate
	from inserted
	if (@BirthDate >= @BirthDateUserInsert)
	begin
		print(@BirthDateUserInsert)
		print('Преподаватель успешно добавлен ' + @BirthDateUserInsert)
	end
	else
	begin
		raiserror('Некорректная дата', 0, 1)
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
			raiserror('Вы не можете удалить эту группу', 0, 1)
			rollback transaction
		end
		else
		begin
			print('Удаление группы успешно')
		end
	end

delete from Groups
where GroupName = 'BBB'