from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")


@app.route("/application-form")
def application_page():
    """Show Application Form."""

    return render_template("application-form.html")


@app.route("/application-response", methods=['POST', 'GET'])
def submision_conf():
    """Show application recieved"""

    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    salary = request.args.get("salary")
    title = request.args.get("title")

    return render_template("application-response.html", firstname=firstname,
                           lastname=lastname, salary=salary, title=title)

if __name__ == "__main__":
    app.run(debug=True)
