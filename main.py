from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Setup Chrome driver using WebDriver Manager
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Start the browser maximized
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)

# Login to LinkedIn
driver.get('https://www.linkedin.com/login')

# Provide your LinkedIn credentials
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys('khushi.ojha@ninebit.in')  # Replace with your LinkedIn email
password.send_keys('Khushi@Ninebit123')  # Replace with your LinkedIn password

# Submit the login form
password.send_keys(Keys.RETURN)

# Wait for login to complete
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'global-nav__content')]"))
)

# Navigate to the profile URL
profile_url = 'https://www.linkedin.com/in/khushi-ojha-2061a3347'
driver.get(profile_url)

# Extract details using updated XPaths
try:
    name_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(@class, 'text-heading-xlarge')]"))
    )
    name = name_element.text.strip()
except:
    name = "Name not found"

try:
    headline_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'text-body-medium break-words')]"))
    )
    headline = headline_element.text.strip()
except:
    headline = "Headline not found"

try:
    location_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'text-body-small inline')]"))
    )
    location = location_element.text.strip()
except:
    location = "Location not found"

try:
    job_title_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 't-bold')]"))
    )
    job_title = job_title_element.text.strip()
except:
    job_title = "Job title not found"

try:
    summary_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//section[contains(@class, 'pv-about-section')]//span[contains(@class, 'visually-hidden')]"))
    )
    summary = summary_element.text.strip()
except:
    summary = "Summary not found"

# Print extracted information
print('Name:', name)
print('Headline:', headline)
print('Location:', location)
print('Current Job Title:', job_title)
print('Profile Summary:', summary)

# Close the browser
driver.quit()
