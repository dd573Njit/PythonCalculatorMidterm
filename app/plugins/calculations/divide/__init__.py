# app/plugins/calculation/divide.py
from app.command.base_command import BaseCommand

class DivideCommand(BaseCommand):

    def execute(self, *args):
        try:
            if len(args) != 2:
                return "Error: There can only be 2 arguments."
            dividend, divisor = map(float, args)
            result = dividend / divisor
            operation = " / ".join(args) + f" = {result}"
            self.history_instance.add_record(operation, result)
            return result
        except ValueError:
            return "Error: All arguments must be numbers."
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
