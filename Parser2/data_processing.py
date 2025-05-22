from typing import Dict, Any, List

def extract_salary(salary_info: Dict[str, Any] | None) -> int:
    if not salary_info or not isinstance(salary_info, dict):
        return 0
    return salary_info.get('from', 0) or 0  

def process_vacancy(vacancy: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'name': vacancy.get('name', 'Не указано'),
        'salary': extract_salary(vacancy.get('salary')),
        'employer': vacancy.get('employer', {}).get('name', 'Не указано')
    }

def process_vacancies(vacancies_data: Dict[str, Any] | None) -> List[Dict[str, Any]]:
    if not vacancies_data or not isinstance(vacancies_data, dict):
        return []
    items = vacancies_data.get('items', [])
    return [process_vacancy(v) for v in items if isinstance(v, dict)]