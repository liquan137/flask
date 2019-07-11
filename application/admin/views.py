from . import admin


@admin.route("/")
def index():
    return "this is admin"
