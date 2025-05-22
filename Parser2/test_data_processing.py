import pytest
from data_processing import extract_salary, process_vacancy, process_vacancies

class TestExtractSalary:
    
    def test_normal_salary(self):
        assert extract_salary({'from': 50000, 'to': 70000}) == 50000
        assert extract_salary({'from': 0, 'to': 100}) == 0
    
    def test_missing_fields(self):
        assert extract_salary({'to': 70000}) == 0  
        assert extract_salary({}) == 0  
    
    def test_invalid_input(self):
        assert extract_salary(None) == 0
        assert extract_salary("salary") == 0  
        assert extract_salary([]) == 0
        assert extract_salary({'from': None}) == 0  
class TestProcessVacancy:
    
    def test_complete_vacancy(self):
        vacancy = {
            'name': 'Python Dev',
            'salary': {'from': 100000},
            'employer': {'name': 'TechCo'}
        }
        assert process_vacancy(vacancy) == {
            'name': 'Python Dev',
            'salary': 100000,
            'employer': 'TechCo'
        }
    
    def test_missing_fields(self):
        assert process_vacancy({'name': 'Job'}) == {
            'name': 'Job',
            'salary': 0,
            'employer': 'Не указано'
        }
        assert process_vacancy({}) == {
            'name': 'Не указано',
            'salary': 0,
            'employer': 'Не указано'
        }

class TestProcessVacancies:
    
    def test_normal_case(self):
        data = {
            'items': [
                {'name': 'Dev', 'salary': None, 'employer': {'name': 'Company'}}
            ]
        }
        result = process_vacancies(data)
        assert len(result) == 1
        assert result[0]['salary'] == 0
    
    def test_invalid_structure(self):
        assert process_vacancies({}) == []  
        assert process_vacancies({'items': {}}) == []  
        assert process_vacancies(None) == []