from db.run_sql import run_sql
from models.toy import Toy

def save(toy):
    sql = "INSERT INTO toys (name, description, quantity, target, value, elf_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [toy.name, toy.description, toy.quantity, toy.target, toy.value, toy.elf.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    toy.id = id

def select_all():
    toys = []
    sql = "SELECT * FROM toys"
    results = run_sql(sql)
    for result in results:
        elf = elf_repository.select(result["elf_id"])
        toy = Toy(result["name"], result["description"], result["quantity"], result["target"], result["value"], elf, result["id"])
        toys.append(toy)
    return toys

def select(id):
    sql = "SELECT * FROM toys WHERE id = %s"
    values = [id]

    result = run_sql(sql, values)
    elf = elf_repository.select(result["elf_id"])
    toy = Toy(result["name"], result["description"], result["quantity"], result["target"], result["value"], elf, result["id"])
    return toy

def delete_all():
    sql = "DELETE FROM toys"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM toys WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM toys WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(toy):
    sql = "UPDATE toys SET (name, description, quantity, target, value, elf_id = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [toy.name, toy.description, toy.quantity, toy.target, toy.value toy.elf.id, toy.id]
    run_sql(sql, values)
