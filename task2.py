def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cat_dict = {"id": cat_id, "name": name, "age": age}
                    cats_list.append(cat_dict)
                else:
                    print(f"Пропущено рядок з некоректним форматом: {line.strip()}")
        return cats_list
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
        return []