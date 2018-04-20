drop table if exists palindromes;
create table palindromes (
  id integer primary key autoincrement,
  title text not null,
  starttime datetime not null
);