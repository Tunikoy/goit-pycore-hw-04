def total_salary(path):
    total_sum = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if ',' in line:
                    name, salary_str = line.strip().split(',')
                    try:
                        salary = float(salary_str)
                        total_sum += salary
                        count += 1
                    except ValueError:
                        print(f"Помилка: Не вдалося перетворити '{salary_str}' у число. Пропускаю рядок: {line.strip()}")
    
        if count > 0:
            average_salary = total_sum / count
        else:
            average_salary = 0
        
        return total_sum, average_salary
    
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return 0, 0

# Приклад використання:
if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")