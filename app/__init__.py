import os
import pkgutil
import importlib
import sys
from app.command import CommandHandler,Command
from app.command.menu_command import MenuCommand
from dotenv import load_dotenv

class App:
    def __init__(self):
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        self.load_commands()
    
    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)
            
    def load_commands(self):
        enabled_plugins = os.getenv('ENABLED_PLUGINS', '').split(',')

        # Dynamically load plugins
        plugins_package = 'app.plugins'
        for _, plugin_name, _ in pkgutil.iter_modules(['app/plugins']):
            if plugin_name in enabled_plugins:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                command_class = getattr(plugin_module, f'{plugin_name.capitalize()}Command')
                self.command_handler.register_command(plugin_name, command_class())
        
    def start(self):
        print("Type 'menu' to see available commands. Type 'exit' to exit.")
        menu_command = MenuCommand(self.command_handler)
        menu_command.execute()
        while True:
            command_input = input(">>> ").strip()
            match command_input:
                case "exit":
                    sys.exit(1)
                case "menu":
                    menu_command.execute()
                case _ if command_input:
                    command_name, *args = command_input.split()
                    if command_name in self.command_handler.commands:
                        self.command_handler.execute_command(command_name, *args)
                    else:
                        print(f"No such command: {command_name}")
                        sys.exit(1)


