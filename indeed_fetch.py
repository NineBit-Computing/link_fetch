import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set ChromeDriver path manually
chrome_driver_path = r"C:\Users\KhushiOjha\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)

# Optional Chrome options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open the Indeed job link
driver.get("https://www.linkedin.com/jobs/view/4133579813")

try:
    # Wait for the job title to be visible
    job_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    ).text

    # Extract company name
    try:
        company_name = driver.find_element(By.CLASS_NAME, "jobsearch-InlineCompanyRating").text
    except Exception:
        company_name = "Company name not found"

    # Extract job description
    try:
        job_description = driver.find_element(By.ID, "jobDescriptionText").text
    except Exception:
        job_description = "Job description not found"

    # Print the extracted data
    print("Job Title:", job_title)
    print("Company Name:", company_name)
    print("Job Description:", job_description)

except Exception as e:
    print("An error occurred:", e)

# Close the browser
driver.quit()
