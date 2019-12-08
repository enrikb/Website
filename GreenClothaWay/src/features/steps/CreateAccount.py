from behave import *

use_step_matcher("re")


@given("User is on create account site")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given User is on create account site')


@step("all fields are filled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And all fields are filled')


@when("create account button gets pushed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When create account button gets pushed')


@then("process will fail")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then process will fail')


@step("inform the user that one must use a valid email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And inform the user that one must use a valid email')


@step("email allready exists in database")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And email allready exists in database')


@step("inform the user that every email is only to be registered once")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And inform the user that every email is only to be registered once')


@step("all fields except password are filled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And all fields except password are filled')


@step("inform the user that one must fill out all fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And inform the user that one must fill out all fields')


@step("all fields except name are filled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And all fields except name are filled')


@step("all fields except surname are filled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And all fields except surname are filled')


@step("all fields except e-mail are filled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And all fields except e-mail are filled')


@step("passwords in both fields are not the same")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And passwords in both fields are not the same')


@step("inform the user that one password is not equal to the other")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And inform the user that one password is not equal to the other')