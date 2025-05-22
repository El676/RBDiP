import os
import csv
import pytest
from file_operations import save_to_csv

class TestSaveToCSV:
    
    def test_successful_save(self, tmpdir):
        test_data = [
            {'name': 'Job1', 'salary': 100, 'employer': 'Company1'},
            {'name': 'Job2', 'salary': 200, 'employer': 'Company2'}
        ]
        file_path = os.path.join(tmpdir, 'test.csv')
        assert save_to_csv(test_data, file_path) is True
        assert os.path.exists(file_path)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            assert len(rows) == 2
            assert rows[0]['name'] == 'Job1'
    
    def test_invalid_data(self, tmpdir):
        file_path = os.path.join(tmpdir, 'invalid.csv')
        
        assert save_to_csv(
            [{'name': 'Job'}], 
            file_path
        ) is False
        
        assert save_to_csv(
            [{'name': 123, 'salary': 'text', 'employer': None}],
            file_path
        ) is False
        
        assert save_to_csv([], file_path) is False
        assert save_to_csv(None, file_path) is False
    
    def test_file_errors(self, tmpdir):
        read_only_file = os.path.join(tmpdir, 'readonly.csv')
        with open(read_only_file, 'w') as f:
            f.write('test')
        os.chmod(read_only_file, 0o444)  
        
        valid_data = [{'name': 'Job', 'salary': 0, 'employer': 'Test'}]
        assert save_to_csv(valid_data, read_only_file) is False