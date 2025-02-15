# '''
# Python-based Scraping Tools
# BeautifulSoup: Great for parsing HTML and extracting data.
# Requests: Used to send HTTP requests to a website.
# Scrapy: A powerful framework for large-scale web scraping.
# Selenium: Used for scraping dynamic websites with JavaScript.


# '''

# import requests
# import csv
# import time
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import pandas as pd

# # Headers to avoid bot detection
# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
# }

# URL = "https://payment.ivacbd.com/"

# # Function to scrape static content
# def scrape_static_content():
#     print("[INFO] Scraping static content...")
    
#     response = requests.get(URL, headers=HEADERS)
#     if response.status_code != 200:
#         print("[ERROR] Failed to retrieve the page")
#         return

#     soup = BeautifulSoup(response.text, "html.parser")

#     # Extract all links
#     links = [a["href"] for a in soup.find_all("a", href=True)]
    
#     # Extract page title
#     title = soup.title.text.strip() if soup.title else "No title found"
    
#     print("[SUCCESS] Static content scraped.")
    
#     return {
#         "title": title,
#         "links": links
#     }

# # Function to scrape dynamic content using Selenium
# def scrape_dynamic_content():
#     print("[INFO] Scraping dynamic content...")

#     options = Options()
#     options.add_argument("--headless")  # Run Chrome in headless mode
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     driver.get(URL)
#     time.sleep(3)  # Allow time for JavaScript to load

#     # Extract page title dynamically
#     try:
#         title = driver.title
#     except:
#         title = "Title not found"

#     # Extract visible text
#     try:
#         body_text = driver.find_element(By.TAG_NAME, "body").text
#     except:
#         body_text = "No content found"

#     driver.quit()
#     print("[SUCCESS] Dynamic content scraped.")

#     return {
#         "title": title,
#         "body_text": body_text[:500]  # Store first 500 characters
#     }

# # Function to handle form submission
# def scrape_form(application_id):
#     print(f"[INFO] Scraping form for Application ID: {'BGDRV0701425'}...")

#     options = Options()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     driver.get(URL)
#     time.sleep(3)

#     try:
#         input_box = driver.find_element(By.NAME, "application_id")  # Change if needed
#         input_box.send_keys(application_id)
#         input_box.send_keys(Keys.RETURN)
#         time.sleep(3)

#         # Extract result page text
#         result = driver.find_element(By.TAG_NAME, "body").text
#     except Exception as e:
#         result = f"Error: {e}"

#     driver.quit()
#     print("[SUCCESS] Form submitted and data extracted.")
    
#     return result[:500]  # Store first 500 characters

# # Function to save data to CSV
# def save_to_csv(data, filename="scraped_data.csv"):
#     print(f"[INFO] Saving data to {filename}...")

#     df = pd.DataFrame(data)
#     df.to_csv(filename, index=False, encoding="utf-8")

#     print("[SUCCESS] Data saved.")

# # Main function
# if __name__ == "__main__":
#     static_data = scrape_static_content()
#     dynamic_data = scrape_dynamic_content()
#     form_data = scrape_form("BGDRV0701425")  

#     # Organizing data
#     scraped_data = [{
#         "Title": static_data["title"],
#         "Links": ", ".join(static_data["links"]),
#         "Dynamic Title": dynamic_data["title"],
#         "Dynamic Body": dynamic_data["body_text"],
#         "Form Result": form_data
#     }]

#     # Save results
#     save_to_csv(scraped_data)




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (replace with the path to your WebDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

try:
    # Open the website
    driver.get("https://payment.ivacbd.com/")

    # Wait for the modal to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "modal-id"))  # Replace "modal-id" with the actual ID of the modal
    )

    # Fill in the Authentication section
    mobile_number_field = driver.find_element(By.ID, "mobile-number-id")  # Replace with the actual ID
    mobile_number_field.send_keys("1234567890")  # Replace with the actual mobile number

    password_field = driver.find_element(By.ID, "password-id")  # Replace with the actual ID
    password_field.send_keys("your_password")  # Replace with the actual password

    otp_field = driver.find_element(By.ID, "otp-id")  # Replace with the actual ID
    otp_field.send_keys("123456")  # Replace with the actual OTP

    # Click the "Next" button or similar to proceed to the next section
    next_button = driver.find_element(By.ID, "next-button-id")  # Replace with the actual ID
    next_button.click()

    # Wait for the next section (Applicant Info) to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "applicant-info-id"))  # Replace with the actual ID
    )

    # Fill in the Applicant Info section
    applicant_name_field = driver.find_element(By.ID, "applicant-name-id")  # Replace with the actual ID
    applicant_name_field.send_keys("John Doe")  # Replace with the actual name

    # Fill in the Personal Info section
    personal_info_field = driver.find_element(By.ID, "personal-info-id")  # Replace with the actual ID
    personal_info_field.send_keys("Some personal info")  # Replace with the actual info

    # Submit the form
    submit_button = driver.find_element(By.ID, "submit-button-id")  # Replace with the actual ID
    submit_button.click()

    # Wait for the submission to complete
    time.sleep(5)  # Adjust the sleep time as needed

finally:
    # Close the browser
    driver.quit()