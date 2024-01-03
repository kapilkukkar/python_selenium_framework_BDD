import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilites import readconfig


def before_scenario(context, scenario):
    browser = readconfig.read_file("basic info", "browser")
    url = readconfig.read_file("basic info", "url")

    if browser.lower() == "chrome":
        context.driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        context.driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(url)


def after_scenario(context, scenario):
    context.driver.quit()


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name="failed_assertion",
                      attachment_type=AttachmentType.PNG)
