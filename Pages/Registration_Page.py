from Utility import Config_Reader, Json_Reader, Excel_Reader
from Global import Base
from Objects import Registration_OB


class RegistrationPage:

    def __init__(self, driver_object):
        global driver
        global ob_cfg_path
        global ob_json_path
        global excel_path
        driver = driver_object
        ob_json_path = ".\\Objects\\Registration_OB.json"
        ob_cfg_path = "./Objects/Registration_OB.cfg"
        excel_path = ".\\TestData\\TestData.xlsx"

    def enter_username(self):
        logger = Base.set_Logger()
        driver.find_element_by_css_selector(
            Config_Reader.read_Config_Data(ob_cfg_path, "Registration", "username"))\
            .send_keys(Excel_Reader.read_Excel_Data(excel_path, "Tester", "Username"))
        logger.info('Enter Username')

    def enter_password(self):
        logger = Base.set_Logger()
        driver.find_element_by_css_selector(
            Json_Reader.read_Json_Data(ob_json_path, "Registration.password"))\
            .send_keys(Excel_Reader.read_Excel_Data(excel_path, "Tester", "Password"))
        logger.info('Enter Password')

    def enter_confirm_password(self):
        logger = Base.set_Logger()
        driver.find_element_by_css_selector(
            Json_Reader.read_Json_Data(ob_json_path, "Registration.confirm_password_textbox"))\
            .send_keys(Excel_Reader.read_Excel_Data(excel_path, "Tester", "Password"))
        logger.info('Enter Confirm Password')

    def enter_email(self):
        logger = Base.set_Logger()
        driver.find_element_by_css_selector(Registration_OB.Registration["email_textbox"])\
            .send_keys(Excel_Reader.read_Excel_Data(excel_path, "Tester", "Email"))
        logger.info('Enter Email')
