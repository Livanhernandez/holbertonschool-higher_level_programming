-- script that creates the database hbtn_0d_usa and the table cities on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id int serial DEFAULT value,
    state_id int not null,
    primary key (id),
    foreign key (state_id) references states(id),
    name VARCHAR(256) not null
);