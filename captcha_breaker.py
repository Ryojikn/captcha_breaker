from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


ticker = "ITSA4"
ticker = ticker.lower()
balance_url = f"https://www.fundamentus.com.br/balancos.php?papel={ticker}&tipo=1"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(balance_url)

print(driver.title)
