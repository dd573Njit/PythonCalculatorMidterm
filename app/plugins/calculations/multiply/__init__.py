# app/plugins/calculation/multiply.py
from app.command.base_command import BaseCommand
import functools

class MultiplyCommand(BaseCommand):

    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = functools.reduce(lambda x, y: x * y, numbers)
            operation = " * ".join(args) + f" = {result}"
            self.history_instance.add_record(operation, result)
            return result
        except ValueError:
            return "Error: All arguments must be numbers."
