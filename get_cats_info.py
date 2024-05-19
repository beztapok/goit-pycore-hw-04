def get_cats_info(path):
    cats_info = []

    # Використовуємо менеджер контексту with для безпечного читання файлу
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо зайві пробіли та розділяємо рядок за комою
                line = line.strip()
                id, name, age = line.split(',')

                # Створюємо словник з інформацією про кота
                cat_info = {
                    "id": id,
                    "name": name,
                    "age": age
                }

                # Додаємо словник до списку
                cats_info.append(cat_info)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    return cats_info

# Приклад використання функції
cats_info = get_cats_info("./get_cats.txt")
print(cats_info)
