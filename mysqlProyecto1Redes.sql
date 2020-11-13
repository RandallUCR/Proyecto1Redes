CREATE DATABASE proyecto1Redes;
use proyecto1Redes;
CREATE table cliente(
    ip_address varchar(20) not null,
    puerto varchar(10) not null
);
drop table cliente;
CREATE TABLE hash_virus (
	id_hash int auto_increment primary key,
    hash_virus varchar(200)
);
insert into hash_virus (hash_virus) values('872adc3781372f12fd76254844b65d25'),('493cf0d6bec0303e8e0d224c87bb8baa'),
('f388180ac6b5c97e9e7946c27363b808'),('63dc99230d962d8ac0d1db56ffadfb64');

select * from hash_virus;
select * from cliente;

