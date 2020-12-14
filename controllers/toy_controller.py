from flask import Blueprint, Flask, redirect, render_template, request

from models.toy import Toy
from repositories.toy_repository as toy_repository

@toys_blueprint.route("/toys")
def toys():
    toys = toy_repository.select_all() 
    return render_template("toys/index.html", toys = toys)

