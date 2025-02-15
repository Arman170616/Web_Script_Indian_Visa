# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import getpass  # For secure input

# # Initialize WebDriver
# driver = webdriver.Chrome()
# driver.get("https://payment.ivacbd.com/")

# try:
#     # Get mobile number from user input
#     mobile_number = input("Enter mobile number (e.g., 017XXXXXXXX): ").strip()
    
#     # Basic validation
#     while not (mobile_number.isdigit() and len(mobile_number) == 11):
#         print("Invalid format! Must be 11 digits (e.g. 01712345678)")
#         mobile_number = input("Enter valid mobile number: ").strip()

#     # Find and fill mobile number field
#     mobile_input = driver.find_element(By.NAME, "mobile_no")
#     mobile_input.clear()
#     mobile_input.send_keys(mobile_number)

#     # Find and click submit button
#     submit_button = driver.find_element(By.ID, "submitButton")
#     submit_button.click()

#     print("Submission successful! Waiting for next steps...")

# except Exception as e:
#     print(f"Error occurred: {str(e)}")
# finally:
#     # Keep browser open for observation
#     input("Press Enter to close browser...")
#     driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass  # For secure input

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://payment.ivacbd.com/")

try:
    # Get mobile number from user input
    mobile_number = input("Enter mobile number (e.g., 017XXXXXXXX): ").strip()
    
    # Basic validation
    while not (mobile_number.isdigit() and len(mobile_number) == 11):
        print("Invalid format! Must be 11 digits (e.g. 01712345678)")
        mobile_number = input("Enter valid mobile number: ").strip()

    # Find and fill mobile number field
    mobile_input = driver.find_element(By.NAME, "mobile_no")
    mobile_input.clear()
    mobile_input.send_keys(mobile_number)

    # Wait for the submit button to be clickable
    wait = WebDriverWait(driver, 10)
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'submitButton')))

    # Scroll to the submit button if necessary
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)

    # Use JavaScript to click the button if it's still not clickable
    driver.execute_script("arguments[0].click();", submit_button)

    print("Mobile number submitted successfully! Waiting for next steps...")

    # Wait for the password input field to be present
    password = getpass.getpass("Enter password: ")

    # Wait for the password input field to be present
    password_input = wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.clear()
    password_input.send_keys(password)

    # Find and click the login submit button
    login_submit_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//form[@id='applicationForm']//button[@id='submitButton']"))
    )
    driver.execute_script("arguments[0].click();", login_submit_button)

    print("Password submitted successfully! Waiting for OTP...")

    # Wait for the OTP input field to be present
    otp_input = wait.until(
        EC.presence_of_element_located((By.NAME, "otp"))
    )
    otp = input("Enter OTP (received via SMS): ")
    otp_input.clear()
    otp_input.send_keys(otp)

    # Click the OTP submit button
    otp_submit_button = wait.until(
        EC.element_to_be_clickable((By.ID, 'submitButton'))
    )
    driver.execute_script("arguments[0].click();", otp_submit_button)

    print("OTP submitted successfully! Waiting for next steps...")

    # Fill in Application Info
    # Example: Fill in name, address, etc.
    name_input = wait.until(
        EC.presence_of_element_located((By.NAME, "name"))
    )
    name_input.clear()
    name_input.send_keys("John Doe")

    address_input = driver.find_element(By.NAME, "address")
    address_input.clear()
    address_input.send_keys("123 Main Street")

    # Click the next button to proceed
    next_button = driver.find_element(By.ID, "nextButton")
    driver.execute_script("arguments[0].click();", next_button)

    # Fill in Personal Info
    # Example: Fill in date of birth, email, etc.
    dob_input = wait.until(
        EC.presence_of_element_located((By.NAME, "dob"))
    )
    dob_input.clear()
    dob_input.send_keys("1990-01-01")

    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys("john.doe@example.com")

    # Click the next button to proceed
    next_button = driver.find_element(By.ID, "nextButton")
    driver.execute_script("arguments[0].click();", next_button)

    # Fill in Overview
    # Example: Fill in any additional details
    overview_input = wait.until(
        EC.presence_of_element_located((By.NAME, "overview"))
    )
    overview_input.clear()
    overview_input.send_keys("This is a test application.")

    # Submit the form
    submit_form_button = driver.find_element(By.ID, "submitFormButton")
    driver.execute_script("arguments[0].click();", submit_form_button)

    print("Form submission successful! Waiting for confirmation...")

    # Handle any confirmation messages
    confirmation_message = wait.until(
        EC.presence_of_element_located((By.ID, "confirmationMessage"))
    )
    print(f"Confirmation message: {confirmation_message.text}")

except Exception as e:
    print(f"Error occurred: {str(e)}")
finally:
    # Keep browser open for observation
    input("Press Enter to close browser...")
    driver.quit()
'''


'''


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import getpass  # For secure input

# # Initialize WebDriver
# driver = webdriver.Chrome()
# driver.get("https://payment.ivacbd.com/")

# try:
#     # Get mobile number from user input
#     mobile_number = input("Enter mobile number (e.g., 017XXXXXXXX): ").strip()
    
#     # Basic validation
#     while not (mobile_number.isdigit() and len(mobile_number) == 11):
#         print("Invalid format! Must be 11 digits (e.g. 01712345678)")
#         mobile_number = input("Enter valid mobile number: ").strip()

#     # Find and fill mobile number field
#     mobile_input = driver.find_element(By.NAME, "mobile_no")
#     mobile_input.clear()
#     mobile_input.send_keys(mobile_number)

#     # Find and click submit button
#     submit_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, 'submitButton'))
#     )
#     driver.execute_script("arguments[0].scrollIntoView();", submit_button)
#     driver.execute_script("arguments[0].click();", submit_button)

#     # Wait for the next page to load and handle authentication
#     password = getpass.getpass("Enter password: ")
#     password_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "password"))
#     )
#     password_input.clear()
#     password_input.send_keys(password)

#     # Click the login button
#     login_button = driver.find_element(By.ID, "loginButton")
#     driver.execute_script("arguments[0].click();", login_button)

#     # Handle OTP verification
#     otp = input("Enter OTP (received via SMS): ")
#     otp_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "otp"))
#     )
#     otp_input.clear()
#     otp_input.send_keys(otp)

#     # Click the OTP submit button
#     otp_submit_button = driver.find_element(By.ID, "otpSubmitButton")
#     driver.execute_script("arguments[0].click();", otp_submit_button)

#     # Fill in Application Info
#     # Example: Fill in name, address, etc.
#     name_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "name"))
#     )
#     name_input.clear()
#     name_input.send_keys("John Doe")

#     address_input = driver.find_element(By.NAME, "address")
#     address_input.clear()
#     address_input.send_keys("123 Main Street")

#     # Click the next button to proceed
#     next_button = driver.find_element(By.ID, "nextButton")
#     driver.execute_script("arguments[0].click();", next_button)

#     # Fill in Personal Info
#     # Example: Fill in date of birth, email, etc.
#     dob_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "dob"))
#     )
#     dob_input.clear()
#     dob_input.send_keys("1990-01-01")

#     email_input = driver.find_element(By.NAME, "email")
#     email_input.clear()
#     email_input.send_keys("john.doe@example.com")

#     # Click the next button to proceed
#     next_button = driver.find_element(By.ID, "nextButton")
#     driver.execute_script("arguments[0].click();", next_button)

#     # Fill in Overview
#     # Example: Fill in any additional details
#     overview_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "overview"))
#     )
#     overview_input.clear()
#     overview_input.send_keys("This is a test application.")

#     # Submit the form
#     submit_form_button = driver.find_element(By.ID, "submitFormButton")
#     driver.execute_script("arguments[0].click();", submit_form_button)

#     print("Form submission successful! Waiting for confirmation...")

#     # Handle any confirmation messages
#     confirmation_message = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "confirmationMessage"))
#     )
#     print(f"Confirmation message: {confirmation_message.text}")

# except Exception as e:
#     print(f"Error occurred: {str(e)}")
# finally:
#     # Keep browser open for observation
#     input("Press Enter to close browser...")
#     driver.quit()



'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass  # For secure input

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://payment.ivacbd.com/")

try:
    # Get mobile number from user input
    mobile_number = input("Enter mobile number (e.g., 017XXXXXXXX): ").strip()
    
    # Basic validation
    while not (mobile_number.isdigit() and len(mobile_number) == 11):
        print("Invalid format! Must be 11 digits (e.g. 01712345678)")
        mobile_number = input("Enter valid mobile number: ").strip()

    # Find and fill mobile number field
    mobile_input = driver.find_element(By.NAME, "mobile_no")
    mobile_input.clear()
    mobile_input.send_keys(mobile_number)

    # Find and click submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'submitButton'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)

    # Wait for the next page to load and handle authentication
    password = getpass.getpass("Enter password: ")

    # Wait for the password input field to be present
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.clear()
    password_input.send_keys(password)

    # Find and click the login submit button
    login_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//form[@id='applicationForm']//button[@id='submitButton']"))
    )
    driver.execute_script("arguments[0].click();", login_submit_button)

    # Wait for the OTP verification page to load
    otp_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "otp"))
    )
    otp = input("Enter OTP (received via SMS): ")
    otp_input.clear()
    otp_input.send_keys(otp)

    # Click the OTP submit button
    otp_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'submitButton'))
    )
    driver.execute_script("arguments[0].click();", otp_submit_button)

    # Fill in Application Info
    # Example: Fill in name, address, etc.
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )
    name_input.clear()
    name_input.send_keys("John Doe")

    address_input = driver.find_element(By.NAME, "address")
    address_input.clear()
    address_input.send_keys("123 Main Street")

    # Click the next button to proceed
    next_button = driver.find_element(By.ID, "nextButton")
    driver.execute_script("arguments[0].click();", next_button)

    # Fill in Personal Info
    # Example: Fill in date of birth, email, etc.
    dob_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "dob"))
    )
    dob_input.clear()
    dob_input.send_keys("1990-01-01")

    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys("john.doe@example.com")

    # Click the next button to proceed
    next_button = driver.find_element(By.ID, "nextButton")
    driver.execute_script("arguments[0].click();", next_button)

    # Fill in Overview
    # Example: Fill in any additional details
    overview_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "overview"))
    )
    overview_input.clear()
    overview_input.send_keys("This is a test application.")

    # Submit the form
    submit_form_button = driver.find_element(By.ID, "submitFormButton")
    driver.execute_script("arguments[0].click();", submit_form_button)

    print("Form submission successful! Waiting for confirmation...")

    # Handle any confirmation messages
    confirmation_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "confirmationMessage"))
    )
    print(f"Confirmation message: {confirmation_message.text}")

except Exception as e:
    print(f"Error occurred: {str(e)}")
finally:
    # Keep browser open for observation
    input("Press Enter to close browser...")
    driver.quit()

'''