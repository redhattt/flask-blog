-- drop tables if exist
drop table if exists users;
drop table if exists posts;

-- generate tables
create table users (
    id integer primary key autoincrement,
    username text not null unique,
    password text not null
);

create table posts (
    id integer primary key autoincrement,
    user_id integer not null references users(id),
    create_ts timestamp not null default current_timestamp,
    title text not null unique,
    body text not null
);