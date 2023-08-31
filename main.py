from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#открываем сайт авито
browser= webdriver.Chrome()
link="https://www.avito.ru/"
browser.get(link)


#search_field = browser.find_element(By.CSS_SELECTOR,"#app > div > div.styles-singlePageWrapper-eKDyt > div > div.index-header-kdkEW.index-stickyHeader-WbpLL > div > div.index-search-xHvcz > div.index-form-ENoC5 > div.index-suggest-zkzTd > div > div > div > label.input-layout-input-layout-_HVr_.input-layout-size-s-COZ10.input-layout-text-align-left-U2OZJ.width-width-12-_MkqF.suggest-input-X6pqt.js-react-suggest > input")
#search_field.send_keys("Ноутбуки")

#открываем раздел Электроника-техника apple
button=browser.find_element(By.CSS_SELECTOR,"#app > div > div.styles-singlePageWrapper-eKDyt > div > div.index-center-_TsYY.index-center_withTitle-_S7ge.index-center_noMarginTop-xAh5X.index-centerWide-_7ZZ_ > div.index-outerPosition-VKXYP > div > div > a:nth-child(9)")
button.click()
bLaptops=browser.find_element(By.CSS_SELECTOR,"#app > div > div.styles-singlePageWrapper-eKDyt > div > div.index-center-_TsYY.index-center_withTitle-_S7ge.index-center_marginTop_1-ewXHO.index-centerWide-_7ZZ_ > div.index-inner-dqBR5 > div.index-content-_KxNP > div.index-root-b_qF9 > div.styles-module-root-RbY1_.styles-module-root_columns_12-fuk_8.styles-module-root_bottom-XgXHc.styles-module-margin-bottom_64-cVX9t > div:nth-child(2) > div > div > div:nth-child(1) > div > a")
bLaptops.click()
bheart=browser.find_element(By.CSS_SELECTOR,"#i3397889112 > div > div > div.iva-item-body-KLUuy > div.iva-item-favoritesStep-__W3E > div")
bheart.click()


#открываем объявление по ссылке
link2="https://www.avito.ru/lobnya/koshki/koshechka_v_dobrye_ruki_3354950438"
browser.get(link2)
bheart=browser.find_element(By.CSS_SELECTOR,"#app > div > div.index-root-k1Ib4.index-responsive-aOpFS.index-page_default-_b5bD > div:nth-child(1) > div > div.style-item-view-PCYlM > div.style-item-view-content-SDgKX > div.style-item-view-content-left-bb5Ih > div.js-item-view-title-info > div > div.style-title-info-actions-NEXbl > div > div > div > div.style-header-add-favorite-M7nA2 > button")
bheart.click()

#открываем объявление по ссылке
link3="https://www.avito.ru/moskva/kollektsionirovanie/kofeynyy_serviz_sssr_3153830702?slocation=107620"
browser.get(link3)
bheart=browser.find_element(By.CSS_SELECTOR,"#app > div > div.index-root-k1Ib4.index-responsive-aOpFS.index-page_default-_b5bD > div:nth-child(1) > div > div.style-item-view-PCYlM > div.style-item-view-content-SDgKX > div.style-item-view-content-left-bb5Ih > div.js-item-view-title-info > div > div.style-title-info-actions-NEXbl > div > div > div > div.style-header-add-favorite-M7nA2 > button")
bheart.click()

#открываем страницу Избранного
bFavourites=browser.find_element(By.CSS_SELECTOR,"#app > div > div.styles-module-theme-JeQ0D > div > div > div.index-counters-m9aGk > a:nth-child(1) > div > svg > path")
bFavourites.click()


time.sleep(100)
browser.quit()
