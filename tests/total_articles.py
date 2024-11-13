import pytest
from src.pages.wikipedia_table import WikiPage


@pytest.mark.parametrize("languages_list", [["English", "French", "Russian", "Tamil"]])  # list of languages as input
def test_find_total_article_by_languages(driver, config, languages_list):
    # wiki page class instant initialization
    wiki_page = WikiPage(driver)
    wiki_page.logger.info("**************** test case started ****************")
    # base url get from config.ini
    base_url = config["settings"]["base_url"]
    # opening a wikipedia page url
    wiki_page.open_url(base_url)
    # finding total articles by languages an
    total_articles = wiki_page.find_total_articles_by_languages(languages_list)
    print(f"\nTotal Articles count: {total_articles}")
    wiki_page.logger.info("**************** end ****************")
    assert total_articles > 0, "Total article count should be greater than zero"
