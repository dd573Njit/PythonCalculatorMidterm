# PythonCalculatorMidterm

## Project Description:
This is a Python-based modular application for arithmetic calculation. It also supports a dynamic plugin system feature. It includes the App class responsible for loading plugins and executing commands through a CommandHandler mechanism. The application contains different arithmetic operations like add, subtract, divide and multiply through its plugin system. The plugin folder contains all these arithmetic operations as commands and is loaded dynamically and registered using the CommandHandler. It also provides a calculation history management feature, allowing users to load, save, clear, and delete historical calculation records via a singleton instance of a CalculationHistory class. The calculation record is also saved in a .csv file using panda library. Additionally, the project employs a LoggingUtility class for comprehensive logging across the application. The project's structure enables easy scalability, allowing for adding more complex operations or functionalities by adding new plugins.

## Configuration
- **logging.conf:** This configuration sets up a basic logger with a console handler that configure logging. It defines the format for log messages and the date format. [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/logging.conf)
- **.env:** For managing environment variables, we are using a .env file. Libraries like dotenv can load these variables at runtime.
- **pytest.ini:** This configuration specifies the minimum pytest version, default options to use when running pytest, and the directory where test files are located. [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/pytest.ini)

## Different Patterns Used:
- **Singleton Pattern:** 'CalculationHistory' class uses the singleton pattern. This is done using '__new__' method and private class variable '_instance' to hold singleton instance. When a new instance is requested, the class checks if an insatnce already exists, if not it creates one. [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/calculation_history.py)
- **Command Pattern:** The 'CommandHandler' and 'Command' abstract class (ABC) implement the command pattern, which means this pattern encapsulates a request as an object and allows parameterization of clients with queues, request and operations. [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/command/__init__.py)
- **Factory Method Pattern:** 'load_plugin_commands(self, path, package)' in 'App' class acts as a factory method that creates 'Command' object without specifying the exact class of objects that will be created. [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/__init__.py)
- **Static Class:** 'LoggingUtility' class contains all static method for logging info, warning and error messages which will be used by every classes in the project. Every method has '@staticmethod' decorator. [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/logging_utility.py) 

## Environment Variables
In the 'CalculationHistory' class, the environment variable 'HISTORY_FILE_PATH' is used to determine the file path for storing and reading the calculation history. The load_dotenv() function call at the beginning of the initialize method loads environment variables from a .env file into the environment. The line self.history_file = os.getenv('HISTORY_FILE_PATH', 'calculation_history.csv') attempts to read the value of the HISTORY_FILE_PATH environment variable. If the variable is defined (has been successfully loaded from the .env file or is otherwise set in the environment), its value will be used as the path to the history file. If the variable is not set, a default value of 'calculation_history.csv' is used. The self.history_file variable, now holding the path to the history file, is used throughout the CalculationHistory class to read from and write to the calculation history. [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/calculation_history.py)

## Look Before You Leap (LBYL) and Easier to Ask for Forgiveness than Permission (EAFP)
- **Easier to Ask for Forgiveness than Permission (EAFP)** 
  - App class [here](https://github.com/kaw393939/midterm-2024-calc/blob/main/app/__init__.py)
  - CommandHandler class [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/command/__init__.py)
  - AddCommand class [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/plugins/calculations/add/__init__.py)
  - DivideCommand class [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/plugins/calculations/divide/__init__.py)
  - MultiplyCommand class [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/plugins/calculations/multiply/__init__.py)
  - SubtractCommand class [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/plugins/calculations/subtract/__init__.py)
  - DeleteCommand class [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/plugins/history/delete/__init__.py)
- **Look Before You Leap (LBYL)**
  - CalculationHistory class [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/calculation_history.py)
  - ClearCommand class [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/plugins/history/clear/__init__.py)
  - DeleteCommand class [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/plugins/history/delete/__init__.py)
  - LoadCommand class [here](https://github.com/dd573Njit/PythonCalculatorMidterm/blob/main/app/plugins/history/load/__init__.py)