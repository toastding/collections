import smtplib

MY_EMAIL = "shumingting0@gmail.com"
MY_PASSWORD = "Star0258"
contact = []
final_contact = []
result = []
final_result = []
SEND_EMAIL = ''
email_list = []
i = 0


# compare two list then merge
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


# check if two list name are the same
def check_same(list1, list2):
    if list1[0] == list2[0]:
        return True


# Swap function
def swap_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# remove element from dictionary
def remove_key(d, key):
    r = dict(d)
    del r[key]
    return r


# open txt & apply to list
with open("通訊錄考題1.txt", mode="r", encoding="utf-8") as file:
    data = file.readlines()
    for i in data:
        list_split = i.split()
        # check email empty
        if len(list_split) < 4:
            list_split.append('empty')
            # check phone empty
            if len(list_split[2]) > 12:
                list_split = swap_positions(list_split, 2, 3)
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


# -----------------------------------SMTP------------------------------------ #
def send():
    global SEND_EMAIL, email_list, i
    name = input("Enter the name: ").capitalize()
    for i in range(len(result)):
        if name == result[i]['name']:
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
    if name == 'Exit':
        pass
    else:
        send()
# -----------------------------------SMTP------------------------------------ #


send()
