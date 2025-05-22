from database import init_db, get_plant

def main():
    init_db()
    plant_name = input("Введите растение: ")
    
    data = get_plant(plant_name)
    
    if not data:
        print("Растение не найдено!")
        return
    
    for row in data:
        print(row)

if __name__ == "__main__":
    main()