from unittest.mock import patch, MagicMock
import pytest
from app.plugins.history.load import LoadCommand

# Fixture for a mocked instance of CalculationHistory
@pytest.fixture
def mocked_calculation_history():
    with patch('app.calculation_history.CalculationHistory') as mocked_calc_history:
        mocked_instance = mocked_calc_history.return_value
        mocked_instance.history_df = MagicMock()
        yield mocked_instance

# Test: CSV exists and contains data
def test_load_command_with_data(mocked_calculation_history, capsys):
    # Setup
    mocked_calculation_history.load_history.return_value = True
    mocked_calculation_history.history_df.empty = False
    mocked_calculation_history.history_df.to_string.return_value = "Mocked Calculations"
    
    # Execute
    load_command = LoadCommand()
    load_command.history_instance = mocked_calculation_history
    load_command.execute()
    
    # Assert
    captured = capsys.readouterr()
    assert "Calculations:" in captured.out
    assert "Mocked Calculations" in captured.out

# Test: CSV exists but is empty
def test_load_command_empty(mocked_calculation_history, capsys):
    # Setup
    mocked_calculation_history.load_history.return_value = True
    mocked_calculation_history.history_df.empty = True
    
    # Execute
    load_command = LoadCommand()
    load_command.history_instance = mocked_calculation_history
    load_command.execute()
    
    # Assert
    captured = capsys.readouterr()
    assert "No calculations in history." in captured.out

# Test: CSV does not exist
def test_load_command_no_csv(mocked_calculation_history, capsys):
    # Setup
    mocked_calculation_history.load_history.return_value = False
    
    # Execute
    load_command = LoadCommand()
    load_command.history_instance = mocked_calculation_history
    load_command.execute()
    
    # Assert
    captured = capsys.readouterr()
    assert "Unable to load history. No CSV file present." in captured.out
