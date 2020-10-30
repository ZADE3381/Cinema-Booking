from flask import Blueprint, render_template

web = Blueprint('web', __name__, template_folder='website-templates')

@web.route("/")
def home():
    return "lol"

@web.route("/test")
def test():
    return "Hi Dad!"