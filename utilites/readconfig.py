from configparser import ConfigParser


def read_file(category, key):
    config = ConfigParser()
    config.read("C:\\Users\\kumar\\PycharmProjects\\Selenium_BDD_Framework\\configuration\\config.ini")
    return config.get(category, key)


