def total_salary(path):
    total = 0

    with open(path, 'r', encoding="utf-8") as file:
        lines = [el.strip() for el in file.readlines()]
        for line in lines:
            salary = line.split(',')[1]
            total += int(salary)
    
    average = round(total / len(lines))

    return (total, average)

try:
    total, average = total_salary("task_1\salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except Exception as err:
    print("Ошибка:", err)
    
