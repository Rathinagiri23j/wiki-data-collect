import time
from selenium.webdriver.common.by import By
from src.locators.wiki_locators import WikiLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.utils.logger import LogGen


class WikiPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = LogGen.loggen()

    def open_url(self, url: str) -> None:
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)

    @staticmethod
    def text_to_int(string: str) -> int:
        return int(string.replace(',', ''))

    def find_total_articles_by_languages(self, languages_list: list[str]) -> int:
        """

        :param languages_list: list of language to be summed
        :return: int total article count
        """
        total_articles = 0
        # explicit wait used, to wait till the all the element in the page is visible.
        rows = WebDriverWait(self.driver, 10).until(ec.visibility_of_any_elements_located(WikiLocators.No_OF_ROWS))
        no_of_rows = len(rows)
        self.logger.info(f"no of rows in the 1st table: {no_of_rows}")

        for i in range(1, no_of_rows + 1):
            # dynamic xpath : to the text of the language.
            language_xpath = f"(//tbody)[1]/tr[{i}]/td[2]"
            language_item = self.driver.find_element(By.XPATH, language_xpath)
            # check if the language name is present in the language list params
            if language_item.text.strip() in languages_list:
                # get of article counts
                article_count_xpath = f"(//tbody)[1]/tr[{i}]/td[5]"
                article_count_str = self.driver.find_element(By.XPATH, article_count_xpath)
                # Convert article count in strings to int
                article_count_int = self.text_to_int(article_count_str.text)
                # summing the article count.
                total_articles += article_count_int

        self.logger.info(f"The total articles: {total_articles}")
        return total_articles
