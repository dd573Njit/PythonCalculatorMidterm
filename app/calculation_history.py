# calculation_history.py
import os
import pandas as pd
from dotenv import load_dotenv

class CalculationHistory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculationHistory, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        load_dotenv()
        self.history_file = os.getenv('HISTORY_FILE_PATH', 'calculation_history.csv')
        self.history_file = os.path.abspath(self.history_file)
        self.history_df = self.load_or_initialize_history()

    def load_or_initialize_history(self):
        if os.path.exists(self.history_file):
            return pd.read_csv(self.history_file)
        else:
            return pd.DataFrame(columns=['Calculations'])

    def add_record(self, operation, result):
        new_index = len(self.history_df)
        self.history_df.loc[new_index] = [operation]
        self.save_history()

    def save_history(self):
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
        self.history_df.to_csv(self.history_file, index=False)

    def load_history(self):
        if os.path.exists(self.history_file):
            self.history_df = pd.read_csv(self.history_file)
            print("Calculation history loaded.")
            return True
        else:
            print("There is no CSV file.")
            return False

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['Calculations'])
        self.save_history()

    def delete_history(self, index):
        if not os.path.exists(self.history_file) or self.history_df.empty:
            print("No history to delete.")
            return False  # Indicates no action was taken
        try:
            if index < 0 or index >= len(self.history_df):
                raise KeyError(f"Invalid index: {index}")
            self.history_df = self.history_df.drop(index).reset_index(drop=True)
            self.save_history()
            print("Record deleted.")
            return True
        except KeyError as e:
            print(f"Invalid index for deletion: {index + 1}.")
            return False
