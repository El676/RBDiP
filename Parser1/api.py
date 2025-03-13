import requests

def get_vacancies(region_id):
    url = "https://api.hh.ru/vacancies"
    params = {
        'area': region_id,  
        'per_page': 10    
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None
    