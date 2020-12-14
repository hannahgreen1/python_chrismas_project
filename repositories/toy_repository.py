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