create database lms;
show databases;
use lms;
create table books(book_id varchar(255),book_name varchar(255),author_name varchar(255),primary key(book_id));
select * from books;
insert into books values("B002","AWS for Beginners","Deepak Singh");
create table student(studentid varchar(255),spassword varchar(255),primary key(studentid));
select * from student;
insert into student values("SachinDesai2000@mylibrary.com","12345");
create table admin(adminid varchar(255),apassword varchar(255),primary key(adminid));
select * from admin;
insert into admin values("librarian01@mylibrary.com","admin9999");
create table issue(issueid varchar(255),book_id varchar(255),studentid varchar(255),primary key(issueid));
select * from issue;


