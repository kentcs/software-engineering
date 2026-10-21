"""Four-function calculator logic, independent of the UI."""

OPERATORS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


class Calculator:
    def __init__(self):
        self.clear()

    def clear(self):
        self.display = '0'
        self.accumulator = None
        self.operator = None
        self.fresh = True  # next digit starts a new number

    def clear_entry(self):
        if self.display == 'Error':
            self.clear()
            return
        self.display = '0'
        self.fresh = True

    def digit(self, d):
        if self.display == 'Error':
            self.clear()
        if self.fresh:
            self.display = d
            self.fresh = False
        elif len(self.display.replace('-', '').replace('.', '')) < 12:
            self.display = d if self.display == '0' else self.display + d

    def decimal(self):
        if self.display == 'Error':
            self.clear()
        if self.fresh:
            self.display = '0.'
            self.fresh = False
        elif '.' not in self.display:
            self.display += '.'

    def negate(self):
        if self.display in ('0', 'Error'):
            return
        self.display = self.display[1:] if self.display.startswith('-') else '-' + self.display

    def operate(self, op):
        if self.display == 'Error':
            return
        if self.operator and not self.fresh:
            self._evaluate()
        else:
            self.accumulator = float(self.display)
        self.operator = op
        self.fresh = True

    def equals(self):
        if self.display == 'Error' or not self.operator:
            return
        self._evaluate()
        self.operator = None
        self.fresh = True

    def _evaluate(self):
        try:
            result = OPERATORS[self.operator](self.accumulator, float(self.display))
        except ZeroDivisionError:
            self.display = 'Error'
            self.accumulator = None
            self.operator = None
            return
        self.accumulator = result
        self.display = self._format(result)

    @staticmethod
    def _format(value):
        text = f'{value:.10g}'
        return text
