from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pytest

# Test fonksiyonu
def test_saucedemo_login():
    # WebDriver konfigürasyonu
    driver = webdriver.Chrome()

    # SauceDemo'ya giriş yapmak için kullanıcı adı ve şifre
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'

    # SauceDemo web sitesini aç
    driver.get('https://www.saucedemo.com')

    # Kullanıcı adı ve şifre ile giriş yap
    sleep(3)
    driver.find_element(By.ID, 'user-name').send_keys(USERNAME)
    driver.find_element(By.ID, 'password').send_keys(PASSWORD)
    driver.find_element(By.ID, 'login-button').click()

    # İlk ürünü sepete ekle
    sleep(3)
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

    # Sepet sayfasına git
    sleep(3)
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # Sepetin içindeki ürünleri doğrula
    sleep(3)
    assert 'Sauce Labs Backpack' in driver.page_source



def test_sauce_demo():
    # WebDriver konfigürasyonu
    driver = webdriver.Chrome()

    # SauceDemo'ya giriş yapmak için kullanıcı adı ve şifre
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'

    # SauceDemo web sitesini aç
    driver.get('https://www.saucedemo.com')

    # Kullanıcı adı ve şifre ile giriş yap
    driver.find_element(By.ID, 'user-name').send_keys(USERNAME)
    driver.find_element(By.ID, 'password').send_keys(PASSWORD)
    driver.find_element(By.ID, 'login-button').click()

    # İlk ürünü sepete ekle
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

    # Sepet sayfasına git
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    sleep(3)
    # Sepetten ürünü çıkar
    driver.find_element(By.ID, 'remove-sauce-labs-backpack').click()
    sleep(3)
    # Sepetin boş olduğunu doğrula
    assert 'Sauce Labs Backpack' not in driver.page_source

# Test fonksiyonu
@pytest.fixture
def browser():
    # WebDriver konfigürasyonu
    driver = webdriver.Chrome()
    yield driver
    # Testi bitir ve tarayıcıyı kapat
    driver.quit()

def test_checkout_complete(browser):
    # SauceDemo'ya giriş yapmak için kullanıcı adı ve şifre
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'

    # SauceDemo web sitesini aç
    browser.get('https://www.saucedemo.com')
    sleep(3)

    # Kullanıcı adı ve şifre ile giriş yap
    browser.find_element(By.ID, 'user-name').send_keys(USERNAME)
    browser.find_element(By.ID, 'password').send_keys(PASSWORD)
    browser.find_element(By.ID, 'login-button').click()
    sleep(3)

    # İlk ürünü sepete ekle
    browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    sleep(3)

    # Checkout sayfasına git
    browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    browser.find_element(By.ID, 'checkout').click()
    sleep(3)

    # Checkout bilgilerini gir
    browser.find_element(By.ID, 'first-name').send_keys('Test')
    browser.find_element(By.ID, 'last-name').send_keys('User')
    browser.find_element(By.ID, 'postal-code').send_keys('12345')
    browser.find_element(By.ID, 'continue').click()
    sleep(3)

    # Checkout işlemini tamamla
    browser.find_element(By.ID, 'finish').click()
    sleep(3)
    # Checkout işleminin tamamlandığını doğrula
    assert 'Thank you for your order!' in browser.page_source
