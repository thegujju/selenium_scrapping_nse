from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

lis = pd.read_csv('C:/Users/Admin/Downloads/NIFTY500.csv')

L = []

for q in lis.Symbol:


    driver = webdriver.Edge()

    query = q
    url = f"https://www.nseindia.com/get-quotes/equity?symbol={query}&section=trade_info"

    driver.get(url)
    time.sleep(5)
    try:
        free_float_market_cap_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "orderBookTradeFFMC"))
        )
        total_mar_cap = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "orderBookTradeTMC"))
        )
        impact_cost = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "orderBookTradeIC"))
        )

        L.append({
            "Symbol": q,
            "free_float_market_cap_element": free_float_market_cap_element.text,
            "total_mar_cap": total_mar_cap.text,
            "impact_cost": impact_cost.text
        })

        print(total_mar_cap)
        driver.quit()

    except Exception as e:
        print(f"Error occurred while extracting data for {q}: {e}")

driver.quit()

L = pd.DataFrame(L)
L.to_csv("C:/Users/Admin/Downloads/market_cap_ffmc_ic.csv", index=False)

