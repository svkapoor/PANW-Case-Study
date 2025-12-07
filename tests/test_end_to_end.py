import sys
import json
import pytest
from unittest.mock import patch
from main import main
from journal import storage

@pytest.fixture
def mock_storage(tmp_path):
    # Create a temporary file for the database
    d = tmp_path / "data"
    d.mkdir()
    p = d / "entries.json"
    # Initialize with empty list
    p.write_text("[]")
    return str(p)

def test_add_command(mock_storage, capsys):
    # Patch the DATA_PATH in the storage module so we don't overwrite real data
    with patch.object(storage, 'DATA_PATH', mock_storage):
        test_text = "I feel amazing today"
        
        # Simulate 'python main.py add "I feel amazing today"'
        with patch.object(sys, 'argv', ["main.py", "add", test_text]):
            main()
            
        captured = capsys.readouterr()
        assert "Saved entry with tag:" in captured.out
        
        # Verify content in the mock file
        with open(mock_storage, 'r') as f:
            entries = json.load(f)
        
        assert len(entries) == 1
        assert entries[0]['text'] == test_text
        assert 'tag' in entries[0]
        # We assume the model works (it's loaded in main -> sentiment), 
        # checking the tag value might be flaky if model changes, 
        # but we can check if it's a string.
        assert isinstance(entries[0]['tag'], str)

def test_summary_command(mock_storage, capsys):
    with patch.object(storage, 'DATA_PATH', mock_storage):
        # Pre-populate some data
        initial_data = [
            {"text": "First entry", "tag": "neutral", "date": "2023-01-01"},
            {"text": "Second entry", "tag": "happy", "date": "2023-01-02"}
        ]
        with open(mock_storage, 'w') as f:
            json.dump(initial_data, f)
            
        # Simulate 'python main.py summary'
        with patch.object(sys, 'argv', ["main.py", "summary"]):
            main()
            
        captured = capsys.readouterr()
        output = captured.out
        
        assert "First entry" in output
        assert "Second entry" in output
        assert "Tag: neutral" in output
        assert "Tag: happy" in output

def test_clear_command(mock_storage, capsys):
    with patch.object(storage, 'DATA_PATH', mock_storage):
        # Pre-populate
        with open(mock_storage, 'w') as f:
            json.dump([{"text": "foo"}], f)
            
        # Simulate 'python main.py clear'
        with patch.object(sys, 'argv', ["main.py", "clear"]):
            main()
            
        captured = capsys.readouterr()
        assert "Cleared all entries." in captured.out
        
        # Verify file is effectively empty (storage.py writes {}, which load_entries reads as [])
        with open(mock_storage, 'r') as f:
            content = json.load(f)
            
        # storage.py clear_entries writes {}
        assert content == {}
        
        # Verify load_entries handles it
        assert storage.load_entries() == []

# --- Edge Case Tests ---

def test_no_arguments(capsys):
    """Test running the script with no arguments prints usage."""
    with patch.object(sys, 'argv', ["main.py"]):
        main()
    captured = capsys.readouterr()
    assert "Usage: python3 main.py" in captured.out

def test_add_missing_text(capsys):
    """Test 'add' command without providing text."""
    with patch.object(sys, 'argv', ["main.py", "add"]):
        main()
    captured = capsys.readouterr()
    assert "Error: No text provided" in captured.out

def test_unknown_command(capsys):
    """Test providing an unknown command."""
    with patch.object(sys, 'argv', ["main.py", "unknown_command"]):
        main()
    captured = capsys.readouterr()
    # The script currently does nothing for unknown commands, so output should be empty
    assert captured.out == ""

def test_summary_empty_database(mock_storage, capsys):
    """Test 'summary' when the database exists but is empty."""
    with patch.object(storage, 'DATA_PATH', mock_storage):
        # The fixure creates an empty file "[]"
        with patch.object(sys, 'argv', ["main.py", "summary"]):
            main()
        captured = capsys.readouterr()
        assert "No entries yet." in captured.out

def test_summary_corrupted_file(mock_storage, capsys):
    """Test 'summary' when the JSON file is corrupted."""
    with patch.object(storage, 'DATA_PATH', mock_storage):
        # Overwrite with invalid JSON
        with open(mock_storage, 'w') as f:
            f.write("{ invalid json content }")
            
        with patch.object(sys, 'argv', ["main.py", "summary"]):
            main()
            
        # storage.load_entries returns [] on error, so main should print "No entries yet."
        captured = capsys.readouterr()
        assert "No entries yet." in captured.out
