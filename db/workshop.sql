DROP TABLE IF EXISTS toys;
DROP TABLE IF EXISTS elves;

CREATE TABLE elves
(
    id SERIAL primary key,
    name VARCHAR(255) not null
);

CREATE TABLE toys
(
  id SERIAL primary key,
  name VARCHAR(255) not null,
  description VARCHAR(255),
  quantity INT,
  target INT,
  value INT,
  elf_id INT REFERENCES elves(id)
);