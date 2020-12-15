from db.run_sql import run_sql
from models.elf import Elf

def save(elf):
    sql = "INSERT INTO elves (name) VALUES (%s) RETURNING id"
    values = [elf.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    elf.id = id

def select_all():
    elves = []
    sql = "SELECT * FROM elves"
    results = run_sql(sql)
    for result in results:
        elf = Elf(result["name"], result["id"])
        elves.append(elf)
    return elves


def select(id):
    sql = "SELECT * FROM elves WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    elf = Elf(result["name"], result["id"])
    return elf


def delete_all():
    sql = "DELETE FROM elves"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM elves WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(elf):
    sql = "UPDATE elves SET name = %s WHERE id = %s"
    values = [elf.name, elf.id]
    run_sql(sql, values)