import os
from datetime import datetime
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities import read_config

def before_scenario(context,driver):
    browser = read_config.read_configuration('app info','browser')
    if browser.lower().__eq__('chrome'):
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser.lower().__eq__('firefox'):
        context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser.lower().__eq__('edge'):
        context.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()
    context.driver.get(read_config.read_configuration('app info','url'))

def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    print()
    if step.status == "failed":
        scenario_name = context.scenario.name
        step_name = step.name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{scenario_name.replace(' ', '_')}_{step_name.replace(' ', '_')}_{timestamp}.png"
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        filepath = os.path.join("screenshots", filename)
        context.driver.save_screenshot(filepath)
        # context.driver.get_screenshot_as_png()
        allure.attach.file(filepath,name=filename, attachment_type=AttachmentType.PNG)






