# from whitenoise import WhiteNoise
from flask import Flask, render_template


# portfolio = ("portfolio", __name__, template_folder="templates")
app = Flask(__name__)

@app.route("/")
def index():
    title = "Portfolio"
    description = "About Me"
    return render_template(
        "index.html",
        title=title,
        description=description,
    )


@app.route("/projects/")
def projects():
    title = "Projects"
    description = "Project"
    return render_template(
        "projects.html",
        title=title,
        description=description,
    )


@app.route("/contact/")
def contact():
    title = "Contact"
    description = "contact"
    return render_template(
        "contact.html",
        title=title,
        description=description,
    )


@app.route("/resume/")
def resume():
    title = "Resume"
    description = "Resume"
    return render_template(
        "resume.html",
        title=title,
        description=description,
    )




@app.errorhandler(404)
def not_found(error_message):
    return render_template("404.html")


if __name__ == "__main__":
    app.run()
