from behave import *
import time

@when("i visit page /register")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.visit('http://localhost:8000/register/')


@step("fill in form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.fill('username', 'devil666')
    context.browser.fill('first_name', 'Lucifer')
    context.browser.fill('last_name', 'Morningstar')
    context.browser.fill('email', 'luci@hell.burn')
    context.browser.fill('street', 'deathrow')
    context.browser.fill('housenumber', '666')
    context.browser.fill('plz', '66666')
    context.browser.fill('city', 'hottown')
    context.browser.fill('country', 'hell')
    context.browser.fill('password1', '666burnyou666badboy666')
    context.browser.fill('password2', '666burnyou666badboy666')


@step("press 'sign up'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_name('sign_up_btn').first.click()
    time.sleep(5)


@then("account is created in database")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("user will be on profile page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.browser.url)
    assert context.browser.url == 'http://localhost:8000/profile/'
