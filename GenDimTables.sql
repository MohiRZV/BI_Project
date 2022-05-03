create table DimDate
( DateKey int not null primary key,
 [Year] varchar(7), [Month] varchar(7), [Date] date, DateString varchar(10))
go
 
-- Populate Date Dimension
truncate table DimDate
go
 
declare @i int, @Date date, @StartDate date, @EndDate date, @DateKey int,
 @DateString varchar(10), @Year varchar(4),
 @Month varchar(7), @Date1 varchar(20)
set @StartDate = '2006-01-01'
set @EndDate = '2016-12-31'
set @Date = @StartDate
 
insert into DimDate (DateKey, [Year], [Month], [Date], DateString)
 values (0, 'Unknown', 'Unknown', '0001-01-01', 'Unknown') --The unknown row
 
while @Date <= @EndDate
begin
 set @DateString = convert(varchar(10), @Date, 20)
 set @DateKey = convert(int, replace(@DateString,'-',''))
 set @Year = left(@DateString,4)
 set @Month = left(@DateString, 7)
 insert into DimDate (DateKey, [Year], [Month], [Date], DateString)
 values (@DateKey, @Year, @Month, @Date, @DateString)
 set @Date = dateadd(d, 1, @Date)
end
go
 
select * from DimDate


create table DimCountry(
country_key int primary key,
country_name nvarchar(50)
);

insert into DimCountry (country_key, country_name)
select * from BI_Source.dbo.countries;

select * from DimCountry;

create table DimFoodDrink(
fd_id int primary key,
did_eat_meat bit,
was_vegan bit,
no_meals int,
no_snacks int,
alcohol_consumed int,
water_drank int
);

insert into DimFoodDrink 
(fd_id,did_eat_meat, was_vegan, no_meals, no_snacks, alcohol_consumed, water_drank)
select * from BI_Source.dbo.food_drinks;

select * from DimFoodDrink;

create table DimSleep(
sleep_id int primary key,
sleep_time int,
no_naps int
);

insert into DimSleep
(sleep_id, sleep_time, no_naps)
select * from BI_Source.dbo.sleep;

select * from DimSleep;

create table DimSocial(
social_id int primary key,
family_time int,
work_time int,
friends_time int,
productive_time int,
relaxing_time int
);

insert into DimSocial
(social_id, family_time, work_time, friends_time, productive_time, relaxing_time)
select * from BI_Source.dbo.social;

select * from DimSocial;

create table DimSpending(
spending_id int primary key,
food_drinks int,
clothes int,
entertainment int,
others int
);

insert into DimSpending
(spending_id, food_drinks, clothes, entertainment, others)
select * from BI_Source.dbo.spendings;

select * from DimSpending; 

-- Create Happiness fact table
if exists (select * from sys.tables where name = 'FactHappiness')
drop table FactHappiness
go

create table FactHappiness(
snapshot_date_key int,
happy_score int,
country_id int, fd_id int, social_id int, sleep_id int, spending_id int,
happy_id int
);