import json

with open('CD925_3rdLevel_Qualification.json') as json_data:
    DATA = json.load(json_data)

    VALUE = DATA["dataset"]["value"]
    BIRTHPLACE = DATA["dataset"]["dimension"]["Birthplace"]["category"]["label"]
    FIELD_OF_STUDY = DATA["dataset"]["dimension"]["Field of Study"]["category"]["label"]
    SEX = DATA["dataset"]["dimension"]["Sex"]["category"]["label"]
    # COUNTRY = DATA["dataset"][""]
    CENSUS_YEAR = DATA["dataset"]["dimension"]["Census Year"]["category"]["label"]

    f = open("CD925.csv", 'w+')
    f.write('"Birthplace", "Field of study", "Sex"\n')
    i = 0
    for s in SEX:
        for bp in BIRTHPLACE:
            f.write('"' + SEX[s] + '", "' + BIRTHPLACE[bp]
            + '", "' + str(SEX[i])
            + '", "' + str("" + SEX[i + 1])
            + '", "' + str(SEX[i + 2]) + '"\n')
            i = i + 3
    f.close()

    # print(CENSUS_YEAR)
    # print(DATA)
