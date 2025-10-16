def get_cats_info(path):
    cats_info = []
    
    with open(path, 'r', encoding="utf-8") as file:
        lines = [el.strip() for el in file]
        
        for line in lines:
            cat_info = line.split(',')
            cats_info.append({
                'id': cat_info[0],
                'name': cat_info[1],
                'age': cat_info[2]
            })
    return cats_info

try:
    cats_info = get_cats_info("task_2\cats_file.txt")
    print(cats_info)
except Exception as err:
    print(err)