import os
import pkgutil
import importlib
import sys
from app.command import CommandHandler, Command
from dotenv import load_dotenv

class App:
    def __init__(self):
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        print("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)
            
    def show_menu(self):
        print("Available commands:")
        # List all registered commands
        for command_name in self.command_handler.commands.keys():
            print(f"- {command_name}")

    def load_plugins(self):
        plugins_package = 'app.plugins'
        calculation_path = os.path.join(plugins_package.replace('.', '/'), 'calculations')
        history_path = os.path.join(plugins_package.replace('.', '/'), 'history')
        other_plugins_path = plugins_package.replace('.', '/')
        
        self.load_plugin_commands(calculation_path, f'{plugins_package}.calculations')
        self.load_plugin_commands(history_path, f'{plugins_package}.history')
        
        self.load_plugin_commands(other_plugins_path,f'{plugins_package}')

                    
    def load_plugin_commands(self, path, package):
        if not os.path.exists(path):
            print(f"Directory '{path}' not found.")
            return
        for _, plugin_name, _ in pkgutil.iter_modules([path]):
            try:
                plugin_module = importlib.import_module(f'{package}.{plugin_name}')
                command_instance = getattr(plugin_module, f'{plugin_name.capitalize()}Command')()
                self.command_handler.register_command(plugin_name, command_instance)
                print(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
            except ImportError as e:
                print(f"Error importing plugin {plugin_name}: {e}")

        

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                print(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        self.load_plugins()
        self.show_menu()
        print("Application started. Type 'exit' to exit.")
        while True:
            input_line = input(">>> ").strip()
            if input_line == "":
                continue
            parts = input_line.split()
            command_name = parts[0]
            args = parts[1:]

            if command_name == "menu":
                self.show_menu()
                continue

            try:
                self.command_handler.execute_command(command_name, *args)
            except KeyError:
                print(f"Unknown command: {command_name}")
                sys.exit(1)