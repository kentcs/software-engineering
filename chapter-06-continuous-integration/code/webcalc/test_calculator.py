"""Tests of Calculator without a browser or NiceGUI.

Run with either:
    python3 -m pytest -v test_calculator.py
    python3 test_calculator.py
"""

from calculator import Calculator


def enter(calc, text):
    """Enter a nonnegative number using the public calculator operations."""
    for character in text:
        if character == '.':
            calc.decimal()
        else:
            calc.digit(character)


def test_initial_display_is_zero():
    calc = Calculator()
    assert calc.display == '0'


def test_enter_multiple_digits():
    calc = Calculator()
    enter(calc, '123')
    assert calc.display == '123'


def test_leading_zeros_do_not_accumulate():
    calc = Calculator()
    enter(calc, '0007')
    assert calc.display == '7'


def test_decimal_can_start_a_number():
    calc = Calculator()
    enter(calc, '.25')
    assert calc.display == '0.25'


def test_second_decimal_point_is_ignored():
    calc = Calculator()
    enter(calc, '1.2.3')
    assert calc.display == '1.23'


def test_entry_is_limited_to_twelve_digits():
    calc = Calculator()
    enter(calc, '1234567890123')
    assert calc.display == '123456789012'


def test_decimal_point_does_not_count_toward_digit_limit():
    calc = Calculator()
    enter(calc, '123456.7890123')
    assert calc.display == '123456.789012'


def test_addition():
    calc = Calculator()
    enter(calc, '2')
    calc.operate('+')
    enter(calc, '3')
    calc.equals()
    assert calc.display == '5'


def test_subtraction_can_produce_a_negative_result():
    calc = Calculator()
    enter(calc, '3')
    calc.operate('-')
    enter(calc, '8')
    calc.equals()
    assert calc.display == '-5'


def test_multiplication():
    calc = Calculator()
    enter(calc, '6')
    calc.operate('*')
    enter(calc, '7')
    calc.equals()
    assert calc.display == '42'


def test_division_can_produce_a_fraction():
    calc = Calculator()
    enter(calc, '7')
    calc.operate('/')
    enter(calc, '2')
    calc.equals()
    assert calc.display == '3.5'


def test_decimal_addition_has_a_readable_display():
    calc = Calculator()
    enter(calc, '0.1')
    calc.operate('+')
    enter(calc, '0.2')
    calc.equals()
    assert calc.display == '0.3'


def test_negate_changes_sign_and_changes_it_back():
    calc = Calculator()
    enter(calc, '12.5')
    calc.negate()
    assert calc.display == '-12.5'
    calc.negate()
    assert calc.display == '12.5'


def test_negating_zero_leaves_zero():
    calc = Calculator()
    calc.negate()
    assert calc.display == '0'


def test_negative_operand():
    calc = Calculator()
    enter(calc, '4')
    calc.negate()
    calc.operate('*')
    enter(calc, '3')
    calc.equals()
    assert calc.display == '-12'


def test_operations_evaluate_left_to_right():
    # A basic calculator evaluates 2 + 3 before applying * 4.
    calc = Calculator()
    enter(calc, '2')
    calc.operate('+')
    enter(calc, '3')
    calc.operate('*')
    assert calc.display == '5'
    enter(calc, '4')
    calc.equals()
    assert calc.display == '20'


def test_second_operator_replaces_the_pending_operator():
    calc = Calculator()
    enter(calc, '8')
    calc.operate('+')
    calc.operate('-')
    enter(calc, '3')
    calc.equals()
    assert calc.display == '5'


def test_clear_discards_a_pending_operation():
    calc = Calculator()
    enter(calc, '9')
    calc.operate('+')
    enter(calc, '4')
    calc.clear()
    assert calc.display == '0'
    enter(calc, '2')
    calc.equals()
    assert calc.display == '2'


def test_clear_entry_preserves_the_pending_operation():
    calc = Calculator()
    enter(calc, '9')
    calc.operate('+')
    enter(calc, '45')
    calc.clear_entry()
    assert calc.display == '0'
    enter(calc, '2')
    calc.equals()
    assert calc.display == '11'


def test_digit_after_equals_starts_a_new_number():
    calc = Calculator()
    enter(calc, '2')
    calc.operate('+')
    enter(calc, '3')
    calc.equals()
    enter(calc, '7')
    assert calc.display == '7'
    calc.equals()
    assert calc.display == '7'


def test_decimal_after_equals_starts_a_new_number():
    calc = Calculator()
    enter(calc, '2')
    calc.operate('+')
    enter(calc, '3')
    calc.equals()
    enter(calc, '.5')
    assert calc.display == '0.5'


def test_result_can_be_used_in_another_operation():
    calc = Calculator()
    enter(calc, '2')
    calc.operate('+')
    enter(calc, '3')
    calc.equals()
    calc.operate('*')
    enter(calc, '4')
    calc.equals()
    assert calc.display == '20'


def test_equals_without_an_operator_leaves_the_number():
    calc = Calculator()
    enter(calc, '17')
    calc.equals()
    assert calc.display == '17'


def test_division_by_zero_displays_error():
    calc = Calculator()
    enter(calc, '8')
    calc.operate('/')
    enter(calc, '0')
    calc.equals()
    assert calc.display == 'Error'
    calc.equals()
    calc.operate('+')
    calc.negate()
    assert calc.display == 'Error'


def test_digit_recovers_from_division_by_zero():
    calc = Calculator()
    enter(calc, '8')
    calc.operate('/')
    enter(calc, '0')
    calc.equals()
    assert calc.display == 'Error'
    enter(calc, '7')
    calc.operate('+')
    enter(calc, '2')
    calc.equals()
    assert calc.display == '9'


def test_decimal_recovers_from_division_by_zero():
    calc = Calculator()
    enter(calc, '8')
    calc.operate('/')
    enter(calc, '0')
    calc.equals()
    assert calc.display == 'Error'
    enter(calc, '.5')
    assert calc.display == '0.5'


def test_clear_entry_recovers_from_division_by_zero():
    calc = Calculator()
    enter(calc, '8')
    calc.operate('/')
    enter(calc, '0')
    calc.equals()
    assert calc.display == 'Error'
    calc.clear_entry()
    assert calc.display == '0'
    enter(calc, '6')
    calc.equals()
    assert calc.display == '6'


def main():
    # Run the same test functions pytest discovers, without importing pytest.
    tests = sorted((name, function) for name, function in globals().items()
                   if name.startswith('test_') and callable(function))
    failures = 0
    for name, function in tests:
        try:
            function()
        except Exception as error:
            failures += 1
            print(f'FAIL {name}: {type(error).__name__}: {error}')
        else:
            print(f'PASS {name}')
    print(f'{len(tests) - failures} passed, {failures} failed')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
