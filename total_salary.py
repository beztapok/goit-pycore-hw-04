def total_salary(path):
    """ Функція для обчислення загальної та середньої суми заробітної плати розробників. """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    # Розділення рядка на ім'я та зарплату
                    name, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Помилка при обробці даних: {line}")
                    continue
            
            total = sum(salaries)
            average = total / len(salaries) if salaries else 0
            return total, average
    except FileNotFoundError:
        print("Файл не знайдено, будь ласка, перевірте шлях до файлу.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

if __name__ == "__main__":
    path_to_file = "./salary_file.txt"  # Вкажіть правильний шлях до файлу
    total, average = total_salary(path_to_file)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

