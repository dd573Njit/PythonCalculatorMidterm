# app/plugins/calculation/subtract.py
from app.command.base_command import BaseCommand

class SubtractCommand(BaseCommand):

    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = numbers[0] - sum(numbers[1:])
            operation = " - ".join(args) + f" = {result}"
            self.history_instance.add_record(operation, result)
            return result
        except ValueError:
            return "Error: All arguments must be numbers."
