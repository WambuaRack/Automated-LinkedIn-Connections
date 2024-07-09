from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

def run_linkedin_automation(email, password):
    driver = None
    try:
        # Set up the Chrome driver
        driver = webdriver.Chrome(r"C:\src\chromedriver-win64\chromedriver.exe")

        # Open LinkedIn login page
        driver.get('https://www.linkedin.com/login')

        # Enter your email and password
        email_input = driver.find_element(By.ID, 'username')
        email_input.send_keys(email)

        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys(password)

        # Submit the login form
        password_input.send_keys(Keys.ENTER)

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.title_contains('LinkedIn'))

        # Go to the "My Network" page
        driver.get('https://www.linkedin.com/mynetwork/')

        # Scroll down to load more connections
        scroll_element = driver.find_element(By.XPATH, '//body')
        scroll_element.send_keys(Keys.END)

        # Connect with all suggested connections
        connect_buttons = driver.find_elements(By.XPATH, '//button[text()="Connect"]')
        for button in connect_buttons:
            button.click()

    except WebDriverException as e:
        print(f"Selenium WebDriver exception occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            driver.quit()
