from Base import Base
import os
import hashlib
from behave.model_core import Status
import allure


def before_all(context):
    # Script generates new json file for every execution in Reports folder, so clear reports folder before execution
    # os.remove("Reports")

    # By default all driver binaries are saved to user.home/.wdm folder.
    # You can override this setting and save binaries to project.root/.wdm.
    os.environ['WDM_LOCAL'] = '1'

    dir_path = './Reports'
    for f in os.listdir(dir_path):
        os.remove(os.path.join(dir_path, f))

    file = open("Logs/info_log.txt", "w")
    file.close()
    environment = context.config.userdata.get("environment")
    Base.set_Environment(environment)
    Base.set_Logger()


# This method will remove duplicate lines from log file and create final_log.txt file
def after_all(context):
    logger = Base.set_Logger()
    output_file_path = "Logs/final_log.txt"
    input_file_path = "Logs/info_log.txt"

    completed_lines_hash = set()

    output_file = open(output_file_path, "w")

    for line in open(input_file_path, "r"):
        hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        if hashValue not in completed_lines_hash:
            output_file.write(line)
            completed_lines_hash.add(hashValue)
    output_file.close()

    # Generate Allure report after execution
    try:
        # os.system('cmd /k "allure serve .\Reports"')
        # os.system('cmd /k "allure generate .\Reports --clean -o .\Reports\%allure-reports%"')
        os.system('cmd /k "allure generate .\Reports --clean"')
        logger.info("Skip allure report try block")
    except:
        logger.info("Could not run Assure command")


def before_scenario(context, scenario):
    browser = context.config.userdata.get("browser")
    Base.set_Driver(browser)
    context.driver = Base.get_Driver()
    return context.driver


def after_scenario(context, scenario):
    context.driver.quit()


def after_step(context, step):
    if step.status == Status.failed:
        allure.attach(
            context.driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)


# before_all(context)
# after_all(context)
# before_feature(context, feature)
# after_feature(context, feature)
# before_scenario(context, scenario)
# after_scenario(context, scenario)
# before_tag(context, tag)
# after_tag(context, tag)
# before_step(context, step)
# after_step(context, step)

# This file name must always be Environment.py
