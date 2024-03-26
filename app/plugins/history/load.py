from app.command.base_command import BaseCommand

class LoadCommand(BaseCommand):
    def execute(self):
        success = self.history_instance.load_history()

        if success:
            if not self.history_instance.history_df.empty:
                print("Calculations:")
                print(self.history_instance.history_df.to_string(index=False))
            else:
                print("No calculations in history.")
        else:
            print("Unable to load history. No CSV file present.")
