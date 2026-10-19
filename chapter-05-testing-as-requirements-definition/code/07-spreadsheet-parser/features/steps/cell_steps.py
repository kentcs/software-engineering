import math

from behave import when, then

from cells import parse


@when('I type "{entry}" into a cell')
def type_into_cell(context, entry):
    # Do the action and keep what happened: a value or an error.
    context.entry = entry
    context.value = None
    context.error = None
    try:
        context.value = parse(entry)
    except ValueError as error:
        context.error = error


@then("the cell holds the number {number}")
def cell_holds_number(context, number):
    assert context.error is None, f"{context.entry!r} was rejected"
    expected = float(number)
    assert math.isclose(context.value, expected, rel_tol=1e-12, abs_tol=1e-12), \
        f"{context.entry!r} gave {context.value!r}, expected {expected!r}"


@then("the cell is rejected as not a number")
def cell_is_rejected(context):
    assert context.error is not None, \
        f"{context.entry!r} was accepted as {context.value!r}"
