drop table if exists user;
create table user (
  id integer primary key autoincrement,
  name string not null,
  age integer not null
);