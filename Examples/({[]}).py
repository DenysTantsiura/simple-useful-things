# ({[<>]})

import sys


class ChecP():
    def __init__(self, text, boundaries='({[<>]})') -> None:
        self.text = text
        self.sets = {}
        self._opens = ''
        self._closed = ''
        while len(boundaries):
            self._opens += boundaries[0]
            self._closed += boundaries[-1]
            boundaries = boundaries[1:-1]
 
    def check(self):
        stat = []
        idx = 0
        for char in self.text:
            if not len(stat) and char in self._closed:
                return False, idx
            if char in self._opens:
                stat.append(char)
            elif char in self._closed:
                if self._opens[self._closed.index(char)] != stat[-1]:
                    return False, idx
                else:
                    stat.pop()
            idx += 1
        return True

one_my_test = ChecP('qw er(ty{qwe<dfg[]dg>}dsg)re_ry')
print(one_my_test.check())

one_my_test = ChecP('qw er(ty{qwe)dfg>]dg>}dsg)re_ry')
print(one_my_test.check())

# another

class ValidationError(Exception):
    def __init__(self, *args: object, idx: int=None) -> None:
        self.idx = idx
        super().__init__(*args)


class Validator:
    def __init__(self) -> None:
        self.text = None
        self._opens = '([{<'
        self._closed = ')]}>'
        self._message = ''

    def balanced(self):
        stack = []
        errors = []
        for symbol_position, symbol in enumerate(self.text):
            if symbol in self._opens:
                stack.append((symbol_position, symbol))
            elif symbol in self._closed:
                position = self._closed.index(symbol)
                if stack and (self._opens[position] == stack[-1][1]):
                    stack.pop()
                else:
                    errors.append(symbol_position)

        if errors or stack:
            errors.extend([s[0] for s in stack])
            self._get_message('Unbalanced brackets', sorted(errors))
            raise ValidationError(self._message, idx=sorted(errors))

    def _get_message(self, base, error_details: list):
        result = (', '.join(f'at {error}' for error in error_details))
        self._message =f'{base}: {result}'

    def _get_mark_errors(self, indexes):
        marks = ['^' if i in indexes else ' ' for i in range(len(self.text))]
        return f'''{self.text}\n{''.join(marks)}'''

    def validate(self, text):
        self.text = text
        try:
            self.balanced()
        except ValidationError as error:
            print(self._get_mark_errors(error.idx), file=sys.stderr)
        
if __name__ == '__main__':
    input_text = '}qw er(ty{qwe<dfg[]dg>}dsg)re_ry}'
    valid = Validator()
    if valid.validate(text=input_text):
        print(input_text)
