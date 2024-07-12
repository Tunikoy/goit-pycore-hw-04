def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if ',' in line:
                    cat_id, name, age = line.strip().split(',')
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat_info)
    
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
    
    return cats_info

# Приклад використання:
cats_info = get_cats_info("cats_file.txt")
print(cats_info)