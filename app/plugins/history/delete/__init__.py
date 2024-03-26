from app.command.base_command import BaseCommand

class DeleteCommand(BaseCommand):
    def execute(self, *args):
        if len(args) == 0:
            print("You have to declare an index after the delete command.")
        elif len(args) > 1:
            print("You can declare only one index after the delete command.")
        else:
            try:
                index = int(args[0])
                # Proceed with deletion if the provided index is valid
                if not self.history_instance.delete_history(index - 1):  # Adjusting index to be 0-based
                    print("Unable to delete record. Please check the index or CSV file.")
            except ValueError:
                print("Error: Index must be an integer.")
