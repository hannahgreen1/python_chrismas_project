from models.elf import Elf
import repositories.elf_repository as elf_repository

from models.toy import Toy
import repositories.toy_repository as toy_repository

toy_repository.delete_all()
elf_repository.delete_all()

elf_1 = Elf("Buddy")
elf_repository.save(elf_1)

elf_2 = Elf("Candy")
elf_repository.save(elf_2)

toy_1 = Toy("Ted", "teddy bear", 5, 8, 7, elf_1)
toy_repository.save(toy_1)