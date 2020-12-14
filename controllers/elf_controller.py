from flask import Blueprint, Flask, redirect, render_template, request

from models.elf import Elf
from repositories.elf_repository as elf_repository