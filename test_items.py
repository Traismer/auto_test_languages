from selenium.webdriver.common.by import By
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# 3. должен объявляться в фикстуре "browser" у меня "driver", т.к. я использую match case проверку, спасибо
def test_get_order_button(driver):
    
    driver.get(link)
    time.sleep(5) # для проверки на --language=fr кнопку "Ajouter au panier"
    button_order = driver.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    
    assert button_order, 'Button order not found'


if __name__ == '__main__':
    pytest.main()
