import os
import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

    
def test_load_environment_variables():
    app = App()
    environment = app.get_environment_variable('ENVIRONMENT')
    assert environment is not None
    assert environment == 'PRODUCTION'

def test_plugin_loading(monkeypatch):
    # Mock the os.environ.get to return a specific plugin
    monkeypatch.setattr(os, 'environ', {'ENABLED_PLUGINS': 'add,subtract'})
    app = App()
    app.load_plugins()
    assert 'add' in app.command_handler.commands
    assert 'subtract' in app.command_handler.commands

def test_empty_input(capfd, monkeypatch):
    inputs = iter(['', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()