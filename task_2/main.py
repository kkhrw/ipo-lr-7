import json
print("start code")
file = "dump.json"
num = str(input("Введите необходимый код  квалификации"))
skills = False
with open(file, "r",encoding = "UTF-8") as file:
    data = json.load(file)
    for skill in data:
        if skill["model"] == "data.skill":
            skill_code = skill["fields"]["code"]
            skill_title = skill["fields"]["title"]
            skills = True

        for profession in data:
            if profession["model"]=="data.speciality":
                code_title = profession["fields"]["code"]
                if code_title in num:
                    prof_title = profession["fields"]["title"]
                    c_type_title = profession["fields"]["c_type"]    
        break

if not skills:
   print("=============== Не найдено ===============")   
else:
    print("=============== Найдено ===============")
    print(f" {code_title} >> Специальность {prof_title}, {c_type_title}")
    print(f" {skill_code} >> Квалификация {skill_title}")
print("end code")    