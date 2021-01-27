documents_list = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}


def validate(doc_number=None, shelf_number=None):
    def check_doc_shelf(num):
        for value_list in directories.values():
            for doc in value_list:
                print(doc)
                if num != doc:
                    print("Документ не существует!")
                    break
                    check_doc()
            else:
                return True

        # for doc in documents_list:
        #     if doc['number'] == num:
        #         return True

    def check_shelf(num):
        if num in directories:
            return True
        else:
            print("Полка не существует!")

    if doc_number and not shelf_number:
        result = check_doc_shelf(doc_number)

    elif shelf_number and not doc_number:
        result = check_shelf(shelf_number)

    elif shelf_number and doc_number:
        result = check_shelf(shelf_number) and check_doc_shelf(doc_number)

    else:
        result = None

    return result


def get_people(documents):
    doc_number = input("Введите номер документа - ")
    doc_name = ""
    for document in documents:
        if doc_number == document["number"]:
            doc_name = document["name"]
            return doc_name


def get_shelf(directory):
    doc_number = input("Введите номер документа - ")
    shelf_name = ""
    for shelf in directory.keys():
        if doc_number in directory[shelf]:
            shelf_name = shelf
            return shelf_name


def get_list(documents):
    result_list = ""
    for people in documents:
        result = " ".join(f"{value}" for key, value in people.items())
        result_list += result + "\n"
    return result_list


def get_add(documents, directory):
    which_shelf = input("Введите номер полки - ")
    if which_shelf in directory.keys():
        type_doc = input("Введите наименование документа - ")
        doc_number = input("Введите номер документа - ")
        name_people = input("Введите ФИО - ")
        new_people = dict(type=type_doc, number=doc_number,
                          name=name_people)
        documents.append(new_people)
        list_doc = directory[which_shelf]
        list_doc.append(doc_number)
        directory[which_shelf] = list_doc
    else:
        print("Полка с таким номером не существует!")
        get_add(documents, directory)
    return documents, directory


def get_delete(documents, directory):
    doc_number = str(input("Введите номер документа - "))
    documents_new = [number_doc for number_doc in documents if
                     doc_number not in number_doc["number"]]

    for value_list in directory.values():
        for doc in value_list:
            if doc_number == doc:
                value_list.remove(doc)

    return documents_new, directory
    print(get_delete(documents_list, directories))


def get_move(directory):
    num_doc = input("Введите номер перемещаемого документа - ")
    num_shelf = input("Введите номер полки, на которую переместить "
                      "документ - ")
    result = validate(doc_number=num_doc, shelf_number=num_shelf)

    if result:
        for value_list in directory.values():
            for doc in value_list:
                if num_doc == doc:
                    value_list.remove(doc)

        for shelf_list in directory:
            for shelf in shelf_list:
                if num_shelf == shelf:
                    directory[shelf].append(num_doc)

        return directory
    get_move(directories)


def get_add_shelf(directory):
    num_new_shelf = input("Введите номер новой полки - ")
    for shelf_list in directory:
        for shelf in shelf_list:
            if num_new_shelf != shelf:
                directory[num_new_shelf] = []
                return directory


def main(documents, directory):
    while True:
        user_input = input('Введите команду - ')
        if user_input == 'p':
            doc_name = get_people(documents)
            if doc_name:
                print(doc_name)
            else:
                print("Введенный номер не существует!")
        elif user_input == 's':
            shelf_name = get_shelf(directories)
            if shelf_name:
                print(shelf_name)
            else:
                print("Введенный номер не существует!")
        elif user_input == 'l':
            print(get_list(documents))
        elif user_input == 'a':
            get_add(documents, directory)
        elif user_input == 'd':
            print(get_delete(documents_list, directories))
        elif user_input == 'm':
            print(get_move(directories))
        elif user_input == 'as':
            print(get_add_shelf(directories))
        elif user_input == 'q':
            break


main(documents_list, directories)
