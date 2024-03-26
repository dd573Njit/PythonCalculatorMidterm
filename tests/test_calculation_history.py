from unittest.mock import patch
import pytest
import pandas as pd
from app.calculation_history import CalculationHistory

@pytest.fixture
def mock_calculation_history(tmp_path):
    """Fixture to mock CalculationHistory with a temporary CSV file path."""
    with patch.object(CalculationHistory, 'initialize') as mock_init:
        instance = CalculationHistory()
        instance.history_file = tmp_path / "calculation_history.csv"
        instance.history_df = pd.DataFrame(columns=['Calculations'])
        yield instance

def test_singleton_property():
    """Test that CalculationHistory is a singleton class."""
    first_instance = CalculationHistory()
    second_instance = CalculationHistory()
    assert first_instance is second_instance

def test_add_record_and_save_history(mock_calculation_history):
    """Test adding a record and saving to history."""
    mock_calculation_history.add_record("2 + 2", "4")
    assert not mock_calculation_history.history_df.empty
    assert mock_calculation_history.history_df.iloc[0]['Calculations'] == "2 + 2"

    # Simulate saving to CSV and reloading to ensure persistence
    mock_calculation_history.save_history()
    mock_calculation_history.load_history()
    assert "2 + 2" in mock_calculation_history.history_df['Calculations'].values

def test_clear_history(mock_calculation_history):
    """Test clearing the history."""
    mock_calculation_history.add_record("2 + 2", "4")
    mock_calculation_history.clear_history()
    assert mock_calculation_history.history_df.empty

def test_delete_history_with_valid_index(mock_calculation_history):
    """Test deleting a history record by valid index."""
    mock_calculation_history.add_record("3 + 3", "6")
    mock_calculation_history.delete_history(0)
    assert mock_calculation_history.history_df.empty

def test_delete_history_with_invalid_index(mock_calculation_history, capsys):
    """Test attempting to delete a history record with an invalid index."""
    mock_calculation_history.add_record("3 + 3", "6")
    mock_calculation_history.delete_history(999)  # Invalid index
    captured = capsys.readouterr()
    assert "Invalid index for deletion" in captured.out

def test_load_history_when_no_csv_exists(mock_calculation_history, capsys):
    """Test loading history when no CSV file exists."""
    result = mock_calculation_history.load_history()
    captured = capsys.readouterr()
    assert "There is no CSV file" in captured.out
    assert result is False
