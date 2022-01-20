from selenium.common import exceptions
from random import random
from datetime import datetime
from time import sleep
import csv
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from tkinter import *
from tkinter import ttk


"""
    forked from https://github.com/israel-dryer/Amazon-Scraper.git

"""
"""
    
    Amazon Web scraper

    Modified:   2020-12-20
    Author:     Israel Dryer
"""


def generate_filename(search_term):
    timestamp = datetime.now().strftime("%Y%m%d%H%S%M")
    stem = path = '_'.join(search_term.split(' '))
    filename = stem + '_' + timestamp + '.csv'
    return filename


def save_data_to_csv(record, filename, new_file=False):
    header = ['description', 'price', 'rating', 'review_count', 'url']
    if new_file:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
    else:
        with open(filename, 'a+', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(record)


def create_webdriver():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver


def generate_url(search_term, page):
    base_template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
    search_term = search_term.replace(' ', '+')
    stem = base_template.format(search_term)
    url_template = stem + '&page={}'
    if page == 1:
        return stem
    else:
        return url_template.format(page)


def extract_card_data(card):
    description = card.find_element_by_xpath('.//h2/a').text.strip()
    url = card.find_element_by_xpath('.//h2/a').get_attribute('href')
    try:
        price = card.find_element_by_xpath(
            './/span[@class="a-price-whole"]').text
    except exceptions.NoSuchElementException:
        return
    try:
        temp = card.find_element_by_xpath(
            './/span[contains(@aria-label, "out of")]')
        rating = temp.get_attribute('aria-label')
    except exceptions.NoSuchElementException:
        rating = ""
    try:
        temp = card.find_element_by_xpath(
            './/span[contains(@aria-label, "out of")]/following-sibling::span')
        review_count = temp.get_attribute('aria-label')
    except exceptions.NoSuchElementException:
        review_count = ""
    return description, price, rating, review_count, url


def collect_product_cards_from_page(driver):
    cards = driver.find_elements_by_xpath(
        '//div[@data-component-type="s-search-result"]')
    return cards


def sleep_for_random_interval():
    time_in_seconds = random() * 2
    sleep(time_in_seconds)


def run(term, number_pages):
    """Run the Amazon webscraper"""
    print(term, number_pages)
    filename = generate_filename(term)
    save_data_to_csv(None, filename, new_file=True)  # initialize a new file
    driver = create_webdriver()
    num_records_scraped = 0

    for page in range(0, int(number_pages)):  # max of 20 pages
        # load the next page
        search_url = generate_url(term, page)
        print(search_url)
        driver.get(search_url)
        print('TIMEOUT while waiting for page to load')

        # extract product data
        cards = collect_product_cards_from_page(driver)
        for card in cards:
            record = extract_card_data(card)
            if record:
                save_data_to_csv(record, filename)
                num_records_scraped += 1
        sleep_for_random_interval()

    # shut down and report results
    driver.quit()
    print(
        f"Scraped {num_records_scraped:,d} for the search term: {term}")

# Manipulate data from registration fields

"""
own code based on tutorials
"""
class tkinter:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x320")
        self.window.title("AmazonScraper.exe")
        self.window.resizable(False, False)
        self.window.config(background="Gray")
        main_title = Label(text="Scraping para Amazon",
                           bg="Green", fg="black", width="500", height="2")
        main_title.pack()
        term_label = Label(text="Producto",)
        term_label.place(x=22, y=70)
        number_pages_label = Label(text="Numero de paginas")
        number_pages_label.place(x=22, y=130)
        self.term = StringVar()
        self.number_pages = StringVar()
        term_entry = Entry(textvariable=self.term, width="30")
        number_pages_entry = Entry(
            textvariable=self.number_pages, width="30")

        term_entry.place(x=22, y=100)
        number_pages_entry.place(x=22, y=160)

        # Submit Button
        submit_btn = Button(self.window, text="Buscar",
                            width="20", height="2", command=self.send_data,)
        submit_btn.place(x=100, y=220)

        self.window.mainloop()

    def send_data(self):
        term_info = self.term.get()
        number_pages_info = self.number_pages.get()
        self.window.destroy()
        sleep(2)
        run(term_info, number_pages_info)


if __name__ == '__main__':

    Aplication = tkinter()
