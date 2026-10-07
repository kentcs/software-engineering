from nicegui import ui

ui.label('Hello NiceGUI!')
ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'))
# my_click_handler = lambda: ui.notify('You also clicked me!')

def my_click_handler():
    ui.notify('You also clicked me!')

ui.button('ALso click me!', on_click=my_click_handler)

ui.run()