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
    try:
        password_input = wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        print("Password input field found.")
    except Exception as e:
        print(f"Error locating password input field: {str(e)}")
        raise

    password_input.clear()
    password_input.send_keys(password)

    # Find and click the login submit button
    try:
        login_submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//form[@id='applicationForm']//button[@id='submitButton']"))
        )
        print("Login submit button found.")
    except Exception as e:
        print(f"Error locating login submit button: {str(e)}")
        raise

    driver.execute_script("arguments[0].click();", login_submit_button)

    print("Password submitted successfully! Waiting for OTP...")

    # Wait for the OTP input field to be present
    try:
        otp_input = wait.until(
            EC.presence_of_element_located((By.NAME, "otp"))
        )
        print("OTP input field found.")
    except Exception as e:
        print(f"Error locating OTP input field: {str(e)}")
        raise

    otp = input("Enter OTP (received via SMS): ")
    otp_input.clear()
    otp_input.send_keys(otp)

    # Click the OTP submit button
    try:
        otp_submit_button = wait.until(
            EC.element_to_be_clickable((By.ID, 'submitButton'))
        )
        print("OTP submit button found.")
    except Exception as e:
        print(f"Error locating OTP submit button: {str(e)}")
        raise

    driver.execute_script("arguments[0].click();", otp_submit_button)

    print("OTP submitted successfully! Waiting for next steps...")

    # Fill in Application Info
    # Example: Fill in name, address, etc.
    try:
        name_input = wait.until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        print("Name input field found.")
    except Exception as e:
        print(f"Error locating name input field: {str(e)}")
        raise

    name_input.clear()
    name_input.send_keys("John Doe")

    try:
        address_input = driver.find_element(By.NAME, "address")
        print("Address input field found.")
    except Exception as e:
        print(f"Error locating address input field: {str(e)}")
        raise

    address_input.clear()
    address_input.send_keys("123 Main Street")

    # Click the next button to proceed
    try:
        next_button = driver.find_element(By.ID, "nextButton")
        print("Next button found.")
    except Exception as e:
        print(f"Error locating next button: {str(e)}")
        raise

    driver.execute_script("arguments[0].click();", next_button)

    # Fill in Personal Info
    # Example: Fill in date of birth, email, etc.
    try:
        dob_input = wait.until(
            EC.presence_of_element_located((By.NAME, "dob"))
        )
        print("Date of birth input field found.")
    except Exception as e:
        print(f"Error locating date of birth input field: {str(e)}")
        raise

    dob_input.clear()
    dob_input.send_keys("1990-01-01")

    try:
        email_input = driver.find_element(By.NAME, "email")
        print("Email input field found.")
    except Exception as e:
        print(f"Error locating email input field: {str(e)}")
        raise

    email_input.clear()
    email_input.send_keys("john.doe@example.com")

    # Click the next button to proceed
    try:
        next_button = driver.find_element(By.ID, "nextButton")
        print("Next button found.")
    except Exception as e:
        print(f"Error locating next button: {str(e)}")
        raise

    driver.execute_script("arguments[0].click();", next_button)

    # Fill in Overview
    # Example: Fill in any additional details
    try:
        overview_input = wait.until(
            EC.presence_of_element_located((By.NAME, "overview"))
        )
        print("Overview input field found.")
    except Exception as e:
        print(f"Error locating overview input field: {str(e)}")
        raise

    overview_input.clear()
    overview_input.send_keys("This is a test application.")

    # Submit the form
    try:
        submit_form_button = driver.find_element(By.ID, "submitFormButton")
        print("Form submit button found.")
    except Exception as e:
        print(f"Error locating form submit button: {str(e)}")
        raise

    driver.execute_script("arguments[0].click();", submit_form_button)

    print("Form submission successful! Waiting for confirmation...")

    # Handle any confirmation messages
    try:
        confirmation_message = wait.until(
            EC.presence_of_element_located((By.ID, "confirmationMessage"))
        )
        print(f"Confirmation message: {confirmation_message.text}")
    except Exception as e:
        print(f"Error locating confirmation message: {str(e)}")
        raise

except Exception as e:
    print(f"Error occurred: {str(e)}")
finally:
    # Keep browser open for observation
    input("Press Enter to close browser...")
    driver.quit()


