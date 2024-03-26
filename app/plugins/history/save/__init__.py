from app.command.base_command import BaseCommand

class SaveCommand(BaseCommand):
    def execute(self, *args):
        if len(args) > 0:
            print("The save command does not accept any arguments.")
        else:
            self.history_instance.save_history()
            print("Calculation history saved.")