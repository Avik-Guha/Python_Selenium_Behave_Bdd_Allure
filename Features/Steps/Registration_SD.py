from behave import *
from Base import Base
from Pages import Registration_BC


@given(u'Launch application page')
def step_impl(context):
    context.driver.get(Base.get_Environment())


@when(u'User enters "{item}"')
def user_enters(context, item):
    registration_obj = Registration_BC.Registration(context.driver)

    if item == "username":
        registration_obj.enter_username()
    elif item == "password":
        registration_obj.enter_password()
    elif item == "email":
        registration_obj.enter_email()
    elif item == "confirm password":
        registration_obj.enter_confirm_password()

    Base.wait_for_seconds(2)
