from nicegui import ui

from calculator import Calculator

KEYS = [
    [('C', 'clear'), ('CE', 'clear_entry'), ('+/-', 'negate'), ('/', 'op')],
    [('7', 'digit'), ('8', 'digit'), ('9', 'digit'), ('*', 'op')],
    [('4', 'digit'), ('5', 'digit'), ('6', 'digit'), ('-', 'op')],
    [('1', 'digit'), ('2', 'digit'), ('3', 'digit'), ('+', 'op')],
    [('0', 'digit'), ('.', 'decimal'), ('=', 'equals')],
]

SYMBOLS = {'/': '÷', '*': '×', '-': '−'}


@ui.page('/')
def index():
    calc = Calculator()

    def refresh():
        display.set_text(calc.display)

    def press(label, kind):
        if kind == 'digit':
            calc.digit(label)
        elif kind == 'decimal':
            calc.decimal()
        elif kind == 'op':
            calc.operate(label)
        elif kind == 'equals':
            calc.equals()
        elif kind == 'negate':
            calc.negate()
        elif kind == 'clear':
            calc.clear()
        elif kind == 'clear_entry':
            calc.clear_entry()
        refresh()

    def on_key(e):
        if not e.action.keydown:
            return
        key = e.key.name
        if key in '0123456789' and len(key) == 1:
            press(key, 'digit')
        elif key == '.':
            press(key, 'decimal')
        elif key in ('+', '-', '*', '/'):
            press(key, 'op')
        elif key in ('=', 'Enter'):
            press('=', 'equals')
        elif key in ('Escape', 'c', 'C'):
            press('C', 'clear')

    ui.keyboard(on_key=on_key)

    with ui.column().classes('w-full items-center mt-10'):
        with ui.card().classes('w-80 gap-2 p-4'):
            display = ui.label('0').classes(
                'w-full text-right text-4xl font-mono bg-gray-100 rounded p-4 overflow-hidden'
            )
            with ui.element('div').classes('w-full grid grid-cols-4 gap-2'):
                for row in KEYS:
                    for label, kind in row:
                        if kind is None:
                            ui.element('div')
                            continue
                        color = 'orange' if kind in ('op', 'equals') else 'grey-8'
                        ui.button(
                            SYMBOLS.get(label, label),
                            on_click=lambda l=label, k=kind: press(l, k),
                        ).props(f'color={color} unelevated').classes(
                            'w-full text-xl h-14' + (' col-span-2' if kind == 'equals' else '')
                        )


ui.run(title='WebCalc', reload=False)
