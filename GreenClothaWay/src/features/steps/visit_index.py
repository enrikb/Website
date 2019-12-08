from behave import *
from urllib.parse import urljoin

use_step_matcher("re")


@then("i see /index page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then i see /index page')


@then("i see 404 not found")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then i see 404 not found')


@when(u'i visit page /index')
def the_user_accesses_the_url(context):
    # full_url = urljoin(context.config.server_url, '/index')
    context.browser.visit(context.get_url('/index'))


@then(u'the url is /index')
def the_url_is(context):
    path_info = context.browser.url.replace(context.config.server_url, '')
    assert path_info == '/index'


@then(u'the page contains clothes')
def the_page_contains_the_h1(context):
    page_h1 = context.browser.find_by_tag('clothes').first
    assert 'clothes' == page_h1.text, "Page should contain h1 '%s', has '%s'" % ('clothes', page_h1.text)


@given(u'the user is shown the login page')
def the_user_is_shown_the_login_page(context):
    return the_url_is(context, '/accounts/login/')


@then(u'the user is shown the home page')
def the_user_is_shown_the_home_page(context):
    return the_url_is(context, '/')
