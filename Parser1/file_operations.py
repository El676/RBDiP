import csv

def save_to_csv(data, filename):
    fieldnames = ['name', 'salary', 'employer']
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        print(f"Ошибка при сохранении файла: {e}")