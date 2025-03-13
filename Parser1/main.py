from api import get_vacancies
from data_processing import process_vacancies
from file_operations import save_to_csv

def main():
    region_id = 1  
    vacancies_data = get_vacancies(region_id)
    if vacancies_data:
        processed_data = process_vacancies(vacancies_data)
        save_to_csv(processed_data, 'vacancies.csv')
        print(f"Данные успешно сохранены в vacancies.csv для региона с ID {region_id}")

if __name__ == "__main__":
    main()