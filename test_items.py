import pytest
        
def test_add_to_basket_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_elements_by_css_selector("#add_to_basket_form > button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(button) > 0, "кнопка не найдена"
