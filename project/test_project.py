import pytest
from project import (
    display_todo_list,
    mark_complete,
    save_to_file,
    load_from_file,
)

# Assuming your_todo_module is the module where your functions are defined

@pytest.fixture
def sample_todo_list():
    return [
        ["Task 1", "High", "Incomplete"],
        ["Task 2", "Medium", "Incomplete"],
        ["Task 3", "Low", "Complete"],
    ]

def test_display_todo_list(capsys, sample_todo_list):
    display_todo_list(sample_todo_list)
    captured = capsys.readouterr()
    assert "Task 1" in captured.out
    assert "Medium" in captured.out
    assert "Complete" in captured.out



def test_mark_complete(sample_todo_list, monkeypatch):
    # Mocking user input using monkeypatch
    monkeypatch.setattr('builtins.input', lambda _: "1")  # Mocking task index input

    mark_complete(sample_todo_list)

    assert sample_todo_list[-1][2] == "Complete"  # Check if the last task is marked as complete

def test_save_to_file(tmp_path, sample_todo_list):
    file_path = tmp_path / "test_todo_list.txt"
    save_to_file(sample_todo_list, filename=str(file_path))
    loaded_todo_list = load_from_file(filename=str(file_path))
    assert loaded_todo_list == sample_todo_list

def test_load_from_file(tmp_path, sample_todo_list):
    file_path = tmp_path / "test_todo_list.txt"
    save_to_file(sample_todo_list, filename=str(file_path))
    loaded_todo_list = load_from_file(filename=str(file_path))
    assert loaded_todo_list == sample_todo_list
