from flask.templating import render_template
from sample import app, client


@app.route("/")
def index():
    resp = client.get_content_item("home")
    if resp:
        hero_units = resp.get_linked_items("hero_unit")
        hero = hero_units[0]

        articles = resp.get_linked_items("articles")

        return render_template("home/index.html", hero=hero, articles=articles)
    return render_template("error_pages/404.html"), 404
