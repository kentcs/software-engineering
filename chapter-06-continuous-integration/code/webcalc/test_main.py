"""Simulate WebCalc button clicks without starting a browser.

Run with either:
    python3 -m pytest -v test_main.py
    python3 test_main.py

NiceGUI's user_simulation is the same mechanism used by its pytest user
fixture. Using it directly lets these tests also run from main.
These checks exercise Python UI handlers, not browser layout or JavaScript.
"""

import asyncio
from pathlib import Path

APP_FILE = Path(__file__).with_name('main.py')


async def check_display(user, expected):
    from nicegui import ui

    # A button marked "5" must not count as a displayed result of "5".
    await user.should_see(kind=ui.label, content=expected)
    labels = user.find(ui.label).elements
    assert len(labels) == 1, 'Expected exactly one calculator display'
    actual = next(iter(labels)).text
    assert actual == expected, f'Expected display {expected!r}, got {actual!r}'


async def click_and_check(checkpoints):
    from nicegui import ui
    from nicegui.testing import UserInteraction, user_simulation

    async with user_simulation(main_file=APP_FILE) as user:
        await user.open('/')
        await check_display(user, '0')
        for buttons, expected in checkpoints:
            for text in buttons:
                matches = {button for button in user.find(ui.button).elements
                           if button.text == text}
                assert len(matches) == 1, f'Expected one button labeled {text!r}'
                UserInteraction(user, matches, text).click()
            await check_display(user, expected)


def test_page_starts_with_zero():
    asyncio.run(click_and_check([]))


def test_addition_buttons_update_display():
    asyncio.run(click_and_check([(['2', '+', '3', '='], '5')]))


def test_subtraction_button_is_connected():
    asyncio.run(click_and_check([(['3', '\u2212', '8', '='], '-5')]))


def test_multiplication_button_is_connected():
    asyncio.run(click_and_check([(['6', '\u00d7', '7', '='], '42')]))


def test_division_button_is_connected():
    asyncio.run(click_and_check([(['7', '\u00f7', '2', '='], '3.5')]))


def test_decimal_button():
    asyncio.run(click_and_check([
        (['.', '2', '5'], '0.25'),
        (['+', '.', '5', '='], '0.75'),
    ]))


def test_sign_button():
    asyncio.run(click_and_check([
        (['1', '2', '+/-'], '-12'),
        (['+/-'], '12'),
    ]))


def test_clear_button_discards_pending_calculation():
    asyncio.run(click_and_check([
        (['9', '+', '4', 'C'], '0'),
        (['2', '='], '2'),
    ]))


def test_clear_entry_button_keeps_pending_calculation():
    asyncio.run(click_and_check([
        (['9', '+', '4', '5', 'CE'], '0'),
        (['2', '='], '11'),
    ]))


def test_error_is_displayed_and_next_digit_recovers():
    asyncio.run(click_and_check([
        (['8', '\u00f7', '0', '='], 'Error'),
        (['7'], '7'),
        (['+', '2', '='], '9'),
    ]))


def test_digit_after_result_starts_new_entry():
    asyncio.run(click_and_check([
        (['2', '+', '3', '='], '5'),
        (['7'], '7'),
    ]))


def test_chained_operations_update_display():
    asyncio.run(click_and_check([
        (['2', '+', '3', '\u00d7'], '5'),
        (['4', '='], '20'),
    ]))


def main():
    # Run inside pytest so NiceGUI uses its test environment in both modes.
    import pytest
    return pytest.main(['-v', str(Path(__file__).resolve())])


if __name__ == '__main__':
    raise SystemExit(main())
