import smtplib

MY_EMAIL = "shumingting0@gmail.com"
MY_PASSWORD = "Star0258"
contact = []
final_contact = []
result = []
final_result = []
SEND_EMAIL = ''
email_list = []


# def merge_dict(dict1, dict2):
#     dict3 = {**dict1, **dict2}
#     for key, value in dict3.items():
#         if key in dict1 and key in dict2:
#             if dict1[key] == dict2[key]:
#                 dict3[key] = value
#             else:
#                 dict3[key] = value, dict1[key]
#     return dict3

def merge_list(list1, list2):
    if list1[0] == list2[0]:
        if list2[2] == list1[2]:
            list2[2] = list1[2]
        else:
            list2[2] = list1[2] + ',' + list2[2]
        if list2[3] == list1[3]:
            list2[3] = list1[3]
        else:
            list2[3] = list1[3] + ',' + list2[3]
    return list2


def check_same(list1, list2):
    if list1[0] == list2[0]:
        return True


# open txt & apply to list
with open("通訊錄考題1.txt", mode="r", encoding="utf-8") as file:
    data = file.readlines()
    for i in data:
        list_split = i.split()
        contact.append(list_split)
    new_contact = sorted(contact, key=lambda x: (x[0], x[2]))


# merge different information
    for i in range(len(new_contact)-1):
        final = merge_list(new_contact[i], new_contact[i+1])
        # print(final)
        final_contact.append(final)


# remove duplicated information
    for i in range(len(final_contact)-1):
        if check_same(final_contact[i], final_contact[i+1]):
            final_contact[i].clear()

    list3 = [x for x in final_contact if x != []]

# apply to dic

with open('contact.txt', mode='w') as file:
    for i in list3:
        contact_dic = {
            "name": i[0],
            "gender": i[1],
            "phone": i[2],
            "email": i[3]
        }
        file.write(str(contact_dic) + '\n')
        # print(contact_dic)

        result.append(contact_dic)
    # print(result)

# -----------------------------------SMTP------------------------------------ #
    name = input("Enter the name: ").capitalize()
    for i in range(len(result)):
        if result[i]['name'] == name:
            SEND_EMAIL = result[i]['email']
            email_list = SEND_EMAIL.split(',')
            for item in email_list:
                SEND_EMAIL = item
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=SEND_EMAIL,
                        msg=f"Subject:Information\n\n{result[i]['name'], result[i]['gender'], result[i]['phone'], result[i]['email']}"
                    )
# -----------------------------------SMTP------------------------------------ #


# a = [{'name': 'Ally', 'gender': 'F', 'phone': '0937-456-922', 'email': 'alpy@eastek.com.tw'},
#      {'name': 'Ally', 'gender': 'F', 'phone': '0955-189-229', 'email': 'ally@eastek.com.tw'},
#      {'name': 'Ally', 'gender': 'F', 'phone': '0951-189-229', 'email': 'alky@eastek.com.tw'},
#      {'name': 'Ally', 'gender': 'F', 'phone': '0951-189-229', 'email': 'aley@eastek.com.tw'},
#      {'name': 'Carl', 'gender': 'M', 'phone': '0926-296-207', 'email': 'carlyang@eastek.com.tw'}
#      ]


# for i in range(len(a) - 1):
#     if a[i]['name'] == a[i + 1]['name']:
#         final = merge_dict(a[i], a[i + 1])
#     else:
#         final_result.append(final)
#         final_result.append(a[i+1])
#
#
# print(final_result)

# Concatenate Similar Key values
# Using loop
# for i in range(len(result) - 1):
#     if result[i]['name'] == result[i + 1]['name']:
#         final = merge_dict(result[i], result[i + 1])
#         final_result.append(final)
#     else:
#         final_result.append(result[i+1])
#
#
# print(final_result[0])
