def extract_salary(salary_info):
    if salary_info and 'from' in salary_info:
        return salary_info['from'] or 0
    return 0

def process_vacancy(vacancy):
    return {
        'name': vacancy['name'],
        'salary': extract_salary(vacancy['salary']),
        'employer': vacancy['employer']['name']
    }

def process_vacancies(vacancies_data):
    return [process_vacancy(vacancy) for vacancy in vacancies_data['items']]