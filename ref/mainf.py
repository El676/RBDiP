from databasef import init_db, get_plant

def main():
    init_db()  
    plant_name = input("Введите растение: ")
    
    plant = get_plant(plant_name)
    
    if not plant:
        print("Растение не найдено!")
    else:
        print(f"Название: {plant['name']}")
        print(f"Сложность: {plant['difficulty']}")
        print(f"Полив: {plant['watering']}")
        print(f"Освещение: {plant['light']}")

if __name__ == "__main__":
    main()