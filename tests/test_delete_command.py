from unittest.mock import patch, MagicMock
import pytest
from app.plugins.history.delete import DeleteCommand

@pytest.fixture
def mocked_calculation_history():
    """Fixture to mock CalculationHistory and its delete_history method."""
    with patch('app.calculation_history.CalculationHistory') as mocked_calc_history:
        mocked_instance = mocked_calc_history.return_value
        mocked_instance.delete_history = MagicMock(return_value=True)
        yield mocked_instance

# Test executing the delete command without arguments
def test_delete_command_no_args(mocked_calculation_history, capsys):
    delete_command = DeleteCommand()
    delete_command.history_instance = mocked_calculation_history
    delete_command.execute()
    
    captured = capsys.readouterr()
    assert "You have to declare an index after the delete command." in captured.out

# Test executing the delete command with more than one argument
def test_delete_command_multiple_args(mocked_calculation_history, capsys):
    delete_command = DeleteCommand()
    delete_command.history_instance = mocked_calculation_history
    delete_command.execute("1", "2")
    
    captured = capsys.readouterr()
    assert "You can declare only one index after the delete command." in captured.out

# Test executing the delete command with a non-integer argument
def test_delete_command_non_integer(mocked_calculation_history, capsys):
    delete_command = DeleteCommand()
    delete_command.history_instance = mocked_calculation_history
    delete_command.execute("not_an_integer")
    
    captured = capsys.readouterr()
    assert "Error: Index must be an integer." in captured.out

# Test executing the delete command with a valid index
def test_delete_command_valid_index(mocked_calculation_history, capsys):
    delete_command = DeleteCommand()
    delete_command.history_instance = mocked_calculation_history
    delete_command.execute("1")  # Assuming an item exists at this index for deletion
    
    # Verify delete_history was called with the correct 0-based index
    mocked_calculation_history.delete_history.assert_called_once_with(0)
    
    captured = capsys.readouterr()
    # Depending on your implementation, assert a successful deletion message or check the absence of an error message
    assert "Unable to delete record." not in captured.out
