-- ------------------------------------------------------
-- Database script for Django Rest Framework Tutorials
-- Venkata Bhattaram (c)
-- ------------------------------------------------------
-- Create Database
create database djangodb;

use djangodb;

-- Create Dept and Emp tables
-- --------------------------
create table dept (
	deptid  int
   ,dname   varchar(100)
   ,primary key(deptid)
);

create table emp (
    empid   int
   ,ename   varchar(100)
   ,jdate   date
   ,salary  int
   ,deptid  int
   ,primary key(empid)
   ,foreign key(deptid) references dept(deptid)
);

select * from dept;
select * from emp;

-- ------------------------------------------------------


