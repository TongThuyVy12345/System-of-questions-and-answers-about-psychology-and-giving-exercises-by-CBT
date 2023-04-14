from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

# Khởi tạo trình điều khiển trình duyệt
driver = webdriver.Chrome('Chrome/chromedriver.exe')

# Mở trang web
driver.get('https://www.nimh.nih.gov/health/topics/anxiety-disorders')

# Tìm các câu hỏi và câu trả lời
questions = driver.find_elements(By.CSS_SELECTOR, "h2")
answers = driver.find_elements(By.CSS_SELECTOR, "p")



