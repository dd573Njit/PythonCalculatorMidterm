from app.command.base_command import BaseCommand

class ClearCommand(BaseCommand):
    def execute(self, *args):
        if len(args) > 0:
            print("The clear command does not accept any arguments.")
        else:
            self.history_instance.clear_history()
            print("Calculation history cleared.")