# app/plugins/calculation/add.py
from app.command.base_command import BaseCommand

class AddCommand(BaseCommand):

    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = sum(numbers)
            operation = " + ".join(args) + f" = {result}"
            self.history_instance.add_record(operation, result)
            return result
        except ValueError:
            return "Error: All arguments must be numbers."
