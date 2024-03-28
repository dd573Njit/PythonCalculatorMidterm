# app/plugins/calculation/multiply.py
from app.command.base_command import BaseCommand
from app.logging_utility import LoggingUtility
import functools

class MultiplyCommand(BaseCommand):

    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = functools.reduce(lambda x, y: x * y, numbers)
            operation = " * ".join(args) + f" = {result}"
            self.history_instance.add_record(operation, result)
            LoggingUtility.info(result)
        except ValueError:
            LoggingUtility.error("Error: All arguments must be numbers.")
