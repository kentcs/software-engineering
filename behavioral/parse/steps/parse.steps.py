from calc import parse

@given('we have a string "{s}"')
def step_impl(context, s):
    context.string = s


@when('we call the parse function with that string')
def step_impl(context):
    context.value = parse(context.string)


@then('we should get a {n}')
def step_impl(context, n):
    n = float(n)
    n0 = n - 0.000000001
    n1 = n + 0.000000001
    assert n0 <= context.value <= n1
