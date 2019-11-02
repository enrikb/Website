from behave import *

use_step_matcher("re")


@given("test got started")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('test started\n')


@when("bla")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('bla\n')

@then("tadaaa")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('tadaaaaaa\n')