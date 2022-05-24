class Restaurant:

    # def __init__(self, data):
    #     self.id = data[0]
    #     self.hooli_number = data[1]
    #     self.name = data[2]
    #     self.contact_phone = data[3]

    def __init__(self, data):
        if data is None:
            self.__id = None
            self.__hooli_number = None
            self.__name = None
            self.__contact_phone = None
        else:
            self.__id = data[0]
            self.__hooli_number = data[1]
            self.__name = data[2]
            self.__contact_phone = data[3]

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_hooli_number(self):
        return self.__hooli_number

    def set_hooli_number(self, hooli_number):
        self.__hooli_number = hooli_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_contact_phone(self):
        return self.__contact_phone

    def set_contact_phone(self, contact_phone):
        self.__contact_phone = contact_phone

    def to_string(self):
        return {"id": self.__id,
                "hooli_number": self.__hooli_number,
                "name": self.__name,
                "contact_phone": self.__contact_phone}
