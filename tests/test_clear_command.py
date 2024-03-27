from unittest.mock import patch
import pytest
from app.plugins.history.clear import ClearCommand

@pytest.fixture
def mocked_calculation_history():
    """Fixture to mock CalculationHistory and its methods."""
    with patch('app.calculation_history.CalculationHistory') as mocked_calc_history:
        mocked_instance = mocked_calc_history.return_value
        # Mock any methods as needed, e.g., clear_history
        yield mocked_instance

# Test executing the clear command without arguments
def test_clear_command_no_args(mocked_calculation_history, capsys):
    clear_command = ClearCommand()
    clear_command.history_instance = mocked_calculation_history
    clear_command.execute()
    
    # Verify clear_history was called
    mocked_calculation_history.clear_history.assert_called_once()
    
    captured = capsys.readouterr()
    assert "Calculation history cleared." in captured.out

# Test executing the clear command with arguments
def test_clear_command_with_args(mocked_calculation_history, capsys):
    clear_command = ClearCommand()
    clear_command.history_instance = mocked_calculation_history
    clear_command.execute("unexpected_argument")
    
    # Verify clear_history was not called
    mocked_calculation_history.clear_history.assert_not_called()
    
    captured = capsys.readouterr()
    assert "The clear command does not accept any arguments." in captured.out
