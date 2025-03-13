import requests

def get_vacancies():
    url = "https://api.hh.ru/vacancies"
    response = requests.get(url)
    data = response.json()
    return data

def process_vacancies(data):
    result = []
    for item in data['items']:
        if item['salary']:
            salary = item['salary']['from'] or 0
        else:
            salary = 0
        result.append({
            'name': item['name'],
            'salary': salary,
            'employer': item['employer']['name']
        })
    return result

def save_to_file(data, filename):
    with open(filename, 'w') as f:
        for item in data:
            f.write(f"{item['name']}, {item['salary']}, {item['employer']}\n")

def main():
    data = get_vacancies()
    processed_data = process_vacancies(data)
    save_to_file(processed_data, 'vacancies.txt')

main()