from flask.templating import render_template
from kontent_delivery.builders.filter_builder import Filter
from kontent_delivery.builders.image_builder import ImageBuilder
from sample import app, client

@app.route("/articles")
def articles():
    articles = client.get_content_items(
        Filter("system.type", "[eq]", "article")
    )

    if articles:
        for article in articles.items:
            image = ImageBuilder(article.elements.teaser_image.value[0].url)
            transformed_image = image.transform(
                image.height(169),
                image.width(279),
                image.fit_mode("crop")
            )
            article.elements.teaser_image.value[0].url = transformed_image
        return render_template("articles/listing.html", articles=articles.items)
    return render_template("error_pages/404.html"), 404


@app.route("/articles/<url_slug>")
def detail(url_slug):
    resp = client.get_content_items(
        Filter("elements.url_pattern", "[eq]", url_slug)
    )

    if resp:
        article = resp.items[0]
        related_articles = article.get_linked_items("related_articles")
        return render_template("articles/detail.html", article=article, related_articles=related_articles)
    return render_template("error_pages/404.html"), 404


