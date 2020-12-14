from flask import Blueprint, Flask, redirect, render_template, request

from models.elf import Elf
from repositories.elf_repository as elf_repository

@elves_blueprint.route("/elves")
def elves():
    elves = elf_repository.select_all() # NEW
    return render_template("elves/index.html", elves = elves)
