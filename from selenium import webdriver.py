from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

Postcode = "E12PY"
Step1_url = "https://s-order.love2laundry.com/?step=1"

# Navigate to the URL
driver.get(Step1_url)
time.sleep(5)

# Step 1: Enter the postcode
postcode_input = driver.find_element(
    By.CSS_SELECTOR, "input[placeholder='Postcode']")
postcode_input.send_keys(Postcode)
print("Postcode entered.")

time.sleep(5)  # Wait for the suggestions to load


SelectAddress = "Flat 4 300 Commercial Road"

try:
    print("Waiting for address suggestions...")

    # Locate the input field and enter the address
    SelectAddress_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[data-placeholder='SelectAddress']"))
    )
    SelectAddress_input.clear()
    SelectAddress_input.send_keys(SelectAddress)

    time.sleep(5)  # Wait for the suggestions to load

    # Wait for suggestions dropdown to load
    # suggestions = WebDriverWait(driver, 10).until(
    # EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".selectaddress.form-control-lg.font_14.w-100.d-flex.align-items-center.Style_placeAddress__pynoH"))
    # )
    # print("Address suggestions loaded.")

    # time.sleep(5)  # Wait for the suggestions to load

    # Iterate through the suggestions and click the matching one
    for suggestion in suggestions:
        if suggestion.text.strip() == SelectAddress:  # Check for exact match
            driver.execute_script(
                "arguments[0].scrollIntoView(true);", suggestion)
            suggestion.click()
            print("Address selected.")
            break
    else:
        print("No matching address found.")

except Exception as e:
    print(f"Error selecting address: {e}")

finally:
    # Close the driver when done
    driver.quit()
