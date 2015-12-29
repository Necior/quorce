drop table if exists quotes;
create table quotes (
  'id' integer primary key autoincrement,
  'text' text not null,
  'source' text
);
