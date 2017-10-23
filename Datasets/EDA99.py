import json


with open('EDA99-Students_Enrolled_in_and_Entrants_to_Third_Level.json') as json_data:
    d = json.load(json_data)
    # d.value
    value = d["dataset"]["value"]

    label = d["dataset"]["dimension"]["Institution"]["category"]["label"]

    year = d["dataset"]["dimension"]["Year"]["category"]["label"]

    f = open('data.csv', 'w+')
    f.write('"Institution","Year","Full-time Enrolments to Third Level Courses (Number)","Part-time Enrolments to Third Level Courses (Number)","Entrants to Third Level Courses (Number)"\n')
    i = 0
    for lbl in label:
        for y in year:
            f.write('"' + label[lbl] + '", "' + year[y] + '", "' 
            + str(value[i]) 
            + '", "' + str("" + value[i + 1]) 
            + '", "' + str(value[i + 2]) + '"\n')
            i = i + 3

    f.close()
