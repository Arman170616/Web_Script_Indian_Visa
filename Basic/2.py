from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import getpass
import time

# Initialize WebDriver with options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-infobars')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.get("https://payment.ivacbd.com/")

# Increase wait time to 20 seconds
wait = WebDriverWait(driver, 20)

try:
    # Wait for page to load completely
    time.sleep(3)  # Increased initial wait time
    
    # Get mobile number input
    mobile_number = input("Enter mobile number (e.g., 017XXXXXXXX): ").strip()
    while not (mobile_number.isdigit() and len(mobile_number) == 11):
        print("Invalid format! Must be 11 digits (e.g. 01712345678)")
        mobile_number = input("Enter valid mobile number: ").strip()

    # Check for iframes and switch if necessary
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    if iframes:
        for iframe in iframes:
            try:
                driver.switch_to.frame(iframe)
                mobile_input = driver.find_element(By.CSS_SELECTOR, "input[name='mobile_no']")
                if mobile_input.is_displayed():
                    break
                driver.switch_to.default_content()
            except:
                driver.switch_to.default_content()
                continue

    # Try multiple selectors for mobile input
    selectors = [
        "input[name='mobile_no']",
        "#mobile_no",
        "input[type='tel']",
        "input[placeholder*='mobile']",
        "input[placeholder*='Mobile']"
    ]

    mobile_input = None
    for selector in selectors:
        try:
            mobile_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            if mobile_input.is_displayed():
                break
        except:
            continue

    if not mobile_input:
        raise Exception("Mobile input field not found with any selector!")

    # Try different methods to input the mobile number
    try:
        # Method 1: Clear and send keys
        mobile_input.clear()
        time.sleep(1)
        mobile_input.send_keys(mobile_number)
        
        # Method 2: If Method 1 fails, try JavaScript
        if not mobile_input.get_attribute('value'):
            driver.execute_script(
                "arguments[0].value = arguments[1];", 
                mobile_input, 
                mobile_number
            )
        
        # Method 3: If still empty, try character by character
        if not mobile_input.get_attribute('value'):
            mobile_input.clear()
            for digit in mobile_number:
                mobile_input.send_keys(digit)
                time.sleep(0.1)
        
        print(f"Mobile number entered: {mobile_input.get_attribute('value')}")
        
        # Verify the input
        if not mobile_input.get_attribute('value'):
            raise Exception("Failed to input mobile number!")
            
    except Exception as e:
        print(f"Error entering mobile number: {str(e)}")
        driver.save_screenshot("mobile_input_error.png")
        raise

    # Click submit button with retry
    max_retries = 3
    for attempt in range(max_retries):
        try:
            submit_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#submitButton"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", submit_button)
            print("Mobile number submitted successfully!")
            break
        except TimeoutException:
            if attempt == max_retries - 1:
                print("Submit button not clickable after multiple attempts!")
                raise
            print(f"Retry attempt {attempt + 1} of {max_retries}")
            time.sleep(2)

    # Enter password with explicit wait
    password = getpass.getpass("Enter password: ")
    try:
        password_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
        )
        time.sleep(1)
        password_input.clear()
        password_input.send_keys(password)
    except TimeoutException:
        print("Password input field not found!")
        raise

    # Click login button
    login_submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//form[@id='applicationForm']//button[@id='submitButton']")))
    driver.execute_script("arguments[0].click();", login_submit_button)
    print("Password submitted successfully! Waiting for OTP...")

    # Enter OTP
    otp_input = wait.until(EC.presence_of_element_located((By.NAME, "otp")))
    otp = input("Enter OTP (received via SMS): ")
    otp_input.clear()
    otp_input.send_keys(otp)

    otp_submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.execute_script("arguments[0].click();", otp_submit_button)
    print("OTP submitted successfully! Waiting for next steps...")

    # Fill Application Info
    fields = {
        "name": "John Doe",
        "address": "123 Main Street",
        "dob": "1990-01-01",
        "email": "john.doe@example.com",
        "overview": "This is a test application."
    }

    for field, value in fields.items():
        try:
            input_field = wait.until(EC.presence_of_element_located((By.NAME, field)))
            input_field.clear()
            input_field.send_keys(value)
            print(f"{field.capitalize()} input field filled.")
        except Exception as e:
            print(f"Error locating {field} input field: {str(e)}")
            raise

    # Click next and submit buttons
    for button_id in ["nextButton", "submitFormButton"]:
        try:
            button = wait.until(EC.element_to_be_clickable((By.ID, button_id)))
            driver.execute_script("arguments[0].click();", button)
            print(f"{button_id} clicked.")
        except Exception as e:
            print(f"Error locating {button_id}: {str(e)}")
            raise

    # Confirm submission
    try:
        confirmation_message = wait.until(EC.presence_of_element_located((By.ID, "confirmationMessage")))
        print(f"Confirmation message: {confirmation_message.text}")
    except Exception as e:
        print(f"Error locating confirmation message: {str(e)}")
        raise

except Exception as e:
    print(f"Error occurred: {str(e)}")
    # Take screenshot on error
    driver.save_screenshot("error_screenshot.png")
    print("Error screenshot saved as 'error_screenshot.png'")
finally:
    input("Press Enter to close browser...")
    driver.quit()