from flask import Blueprint, render_template, request, flash, jsonify

page = Blueprint("page", __name__)

@page.route('/')
def home():
    return render_template("home.html")