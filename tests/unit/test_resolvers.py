import pytest
import json
from kontent_delivery.content_item import ContentItem
from sample.resolvers.custom_item_resolver import CustomItemResolver
from sample.resolvers.custom_link_resolver import CustomLinkResolver


# PATHS
@pytest.fixture
def content_item_path():
    return "tests/fixtures/content_item.json"


# FIXTURES
@pytest.fixture
def new_content_item(content_item_path):
    json = get_json(content_item_path)
    content_item = ContentItem(json["item"]["system"], json["item"]["elements"])
    return content_item


@pytest.fixture
def new_inline_link(content_item_path):
    json = get_json(content_item_path)
    content_item = ContentItem(json["item"]["system"], json["item"]["elements"])
    # convert types.SimpleNamespace object to dict
    links = vars(content_item.elements.body_copy.links)
    first_link = next(iter(links.values()))
    return first_link


# MISC.
def get_json(path):
    with open(path) as f:
        data = json.load(f)
    return data


# TESTS
def test_inline_item_resolver(new_content_item):
    item_resolver = CustomItemResolver()
    result = item_resolver.resolve_item(new_content_item)
    assert result == "<h1>Coffee processing techniques</h1>"


def test_inline_link_resolver(new_inline_link):
    link_resolver = CustomLinkResolver()
    result = link_resolver.resolve_link(new_inline_link)
    assert result == "/coffees/kenya-gakuyuni-aa"

