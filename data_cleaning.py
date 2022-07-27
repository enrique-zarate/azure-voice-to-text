from datetime import datetime, date

now = date.today()

#for enty in entities
dicc = {
    "entities": [
        {
            "text": "me duele la cabeza",
            "category": "dolor-cabeza",
            "offset": 0,
            "length": 18,
            "confidenceScore": 1
        },
        {
            "text": "me duele la panza",
            "category": "dolor-panza",
            "offset": 21,
            "length": 17,
            "confidenceScore": 1
        }
    ]
}


# for i in entities:
#     d= entities["entities"][0]["text"]
#     f= entities["entities"][1]["text"]
#     #print(d)
#     #print(f)

# sin_1 = entities["entities"][0]["text"]
# cat_1 = entities["entities"][0]["category"]
# sin_2 = entities["entities"][1]["text"]
# cat_2 = entities["entities"][1]["category"]

def clean_dict(dic):
    cleaned = {}
    
    # for enti in dic["entities"]:
    #     cleaned["text"] = enti["entities"][0]["text"] 
    #     cleaned["category"]= enti["entities"][0]["category"]
    #     print(cleaned)
    # return cleaned
    for count, values in enumerate(dic['entities']):
        # print(count)
        # print(values)
        #print('sintoma:',count, values['text'])

        cleaned["symptoms"] = values['text']
        cleaned["category"] = values['category']
        # print(cleaned)
    # cleaned["text"] = dic["entities"][0]["text"] 
    # cleaned["category"]= dic["entities"][0]["category"]
    # cleaned["text"] = dic["entities"][1]["text"]
    # cleaned["category"]= dic["entities"][1]["category"]
 

# my_dict = {'sintoma': [],
# 'categoria': [],
# 'fecha': []
# }
# def add_to_dic():
#     my_dict['sintoma'].append(sin_1)
#     my_dict['sintoma'].append(sin_2)
#     my_dict['categoria'].append(cat_1)
#     my_dict['categoria'].append(cat_2)
#     my_dict['fecha'].append(now)
#     my_dict['fecha'].append(now)
# add_to_dic()

# new_date = datetime(2019, 2, 28,)
# print(new_date)
# full_dates = '1/1/17'
# objDate = datetime.strptime(full_dates, '%m/%d/%y')
# print(objDate)


# for full_date in full_dates:

#print(my_dict)

if __name__ == "__main__":
    clean_dict(dicc)


