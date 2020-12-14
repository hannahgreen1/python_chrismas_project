from flask import Blueprint, Flask, redirect, render_template, request

from models.toy import Toy
from repositories.toy_repository as toy_repository
