from behave import *
from functools import wraps


def requires_process(func):
    @wraps(func)
    def wrapper(context, *args, **kwargs):
        if (not hasattr(context, "process")):
            raise AssertionError("No process started!")
        return func(context, *args, **kwargs)
    return wrapper

@given('The Connection Has Been Established With The Server')
@requires_process
def step_the_connection_has_been_established_with_the_server(context):
    pass

@then('the process must be terminated')
@requires_process
def step_the_process_must_be_terminated(context) -> None:
    if (context.process.isalive()):
        raise AssertionError("Process still running!")

@when('the expression provided is "{exp}"')
@requires_process
def step_the_expression_provided_is(context, exp: str) -> None:
    if (not context.process.run_command(exp)):
        raise AssertionError(f"It was no possible to run {exp}")

@then('the command must be successful')
@requires_process
def step_the_command_must_be_successful(context) -> None:
    if (not context.process.is_last_command_successful):
        raise AssertionError("The last command failed!!")

@then('the command must be unsuccessful')
@requires_process
def step_the_command_must_be_unsuccessful(context) -> None:
    if (context.process.is_last_command_successful):
        raise AssertionError("The last command was successful!!")

@then('the result should be equals to "{test_res}"')
@requires_process
def step_the_result_should_be_equals_to(context, test_res: str) -> None:
    if (float(context.process.last_result) != float(test_res)):
        raise AssertionError(f"Result {context.process.last_result} is not equals to {test_res}!!")

@then('the result should not be equals to "{test_res}"')
@requires_process
def step_the_result_should_not_be_equals_to(context, test_res: str) -> None:
    if (float(context.process.last_result) == float(test_res)):
        raise AssertionError(f"Result {context.process.last_result} is equals to {test_res}!!")

