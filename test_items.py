import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button_on_the_page(browser):
    browser.get(link)
    time.sleep(5)
    basket_button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert basket_button > 0, "Кнопка не найдена"

