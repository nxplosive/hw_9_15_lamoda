import time

import allure
from selene import browser, be, have

from lamoda_tests.data.data_cards import Texts


class MainPage:
    def __init__(self):
        self.search_input = browser.element('[class="_input_1su1z_19 _inputShown_1su1z_43"]')
        self.basket = browser.element('[class="_root_1kpa7_2 _link_12pcw_8 _root_f9xmk_2 _secondaryLabel_f9xmk_16"]')

    def open_url(self):
        with allure.step("Открываем главную страницу"):
            browser.open('/')
        time.sleep(2)

    def search(self, card_name):
        with allure.step(f"Ищем товар {card_name}"):
            self.search_input.type(card_name).press_enter()

    def result_by_name(self, card_name):
        with allure.step(f"Отображается товар с наименованием {card_name}"):
            browser.element('[class="x-product-card-description__product-name _productName_hcatq_7"]').should(
                have.text(f'{card_name}'))

    def result_by_brand(self, brand_name):
        with allure.step(f"Отображается товар бренда {brand_name}"):
            browser.element('[class="x-product-card-description__brand-name _brandName_hcatq_6"]').should(
                have.text(f'{brand_name}'))

    def result_by_price(self, card_price):
        with allure.step(f"Отображается товар стоимостью {card_price}"):
            browser.element(
                '[class="x-product-card-description__price-single x-product-card-description__price-WEB8507_price_bold _price_hcatq_8"]'
            ).should(have.text(card_price))

    def no_result(self):
        with allure.step(f"Отображается строка {Texts.nothing_found}"):
            browser.element('[class="_title_1jpla_24"]').should(have.text(Texts.nothing_found))

    def add_item_to_cart(self, card_name):
        with allure.step("Наводим курсор на товар"):
            browser.element('#RTLACX736301').hover()
        with allure.step("Смотрим товар подробнее"):
            browser.element('#RTLACX736301').click()
        with allure.step("Выбираем размер"):
            browser.element('[class="_root_1widv_2 _rootIsPremium_1widv_39 ui-product-page-sizes-chooser"]').click()
            browser.element(
                '[class*="_colspan_1widv_150 ui-product-page-sizes-chooser-item_enabled ui-product-page-sizes-chooser-item"]'
            ).click()
        with allure.step("Нажимаем 'Добавить в корзину'"):
            browser.element('[class="_addToCart_2z3at_18 _addToCartSticky_2z3at_171"]').click()
        with allure.step("Счётчик корзины увеличился"):
            browser.element('[class="_count_1kpa7_11"]').should(be.visible)

    def open_basket(self):
        with allure.step("Нажимаем 'Корзина'"):
            self.basket.click()

    def check_cart(self, card_name, brand_name, item_name):
        self.open_basket()
        with allure.step(f"В корзине отображается товар с наименованием {card_name} {brand_name}"):
            browser.all('[class="_box_1de25_14"]').should(have.texts(item_name))

    def remove_from_cart(self):
        self.open_basket()
        with allure.step("Удаляем товар"):
            browser.element('[class="_root_1u8uz_2 ui-checkout-cart__item"]').hover()
            browser.element('[class="_root_1mejd_2 _action_120f4_8"]').click()
        with allure.step(f"Отображается текст {Texts.empty_cart}"):
            browser.element('[class="_title_1wc5j_7"]').should(have.text(Texts.empty_cart))
