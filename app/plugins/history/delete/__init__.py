from app.command.base_command import BaseCommand
from app.logging_utility import LoggingUtility

class DeleteCommand(BaseCommand):
    def execute(self, *args):
        if len(args) == 0:
            LoggingUtility.warning("You have to declare an index after the delete command.")
        elif len(args) > 1:
            LoggingUtility.warning("You can declare only one index after the delete command.")
        else:
            try:
                index = int(args[0])
                # Proceed with deletion if the provided index is valid
                if not self.history_instance.delete_history(index - 1):  # Adjusting index to be 0-based
                    LoggingUtility.warning("Unable to delete record. Please check the index or CSV file.")
                else:
                    LoggingUtility.info("Record deleted.")
            except ValueError:
                LoggingUtility.error("Error: Index must be an integer.")