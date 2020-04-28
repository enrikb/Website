from behave import *


@then("i see 404 not found")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then i see 404 not found')


@when(u'i visit page /index')
def the_user_accesses_the_url(context):
    # full_url = urljoin(context.config.server_url, '/index')
    context.browser.visit('http://localhost:8000/index/')


@then(u'the url is /index')
def the_url_is(context):
    assert context.browser.url == 'http://localhost:8000/index/'


@then(u'the page contains clothes')
def the_page_contains_the_h1(context):
    assert context.browser.is_text_present('clothes')
