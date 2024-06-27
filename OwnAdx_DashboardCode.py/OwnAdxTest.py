from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to perform the test
def perform_test():
    # Initialize WebDriver
    driver = webdriver.Chrome()  # You can change this to Firefox or any other supported browser

    # Navigate to the webpage
    driver.get("https://example.com")  # Replace "https://example.com" with your target webpage URL

    try:
        # Find the element before executing the step
        element_before = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "element_id"))  # Replace "element_id" with the ID of the element you want to check
        )
        
        # Get the value before executing the step
        value_before = element_before.text  # You can use ".get_attribute('value')" if the element is an input field

        # Execute the step (e.g., clicking a button or performing some action)
        # driver.find_element(By.ID, "button_id").click()  # Example: Clicking a button with ID "button_id"

        # Find the element after executing the step
        element_after = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "element_id"))  # Same as above, replace "element_id"
        )

        # Get the value after executing the step
        value_after = element_after.text  # or ".get_attribute('value')" if needed

        # Compare values before and after
        if value_before != value_after:
            print("Value changed after executing the step.")
        else:
            print("Value remains the same after executing the step.")

    finally:
        # Quit the WebDriver
        driver.quit()

# Call the function to perform the test
perform_test()