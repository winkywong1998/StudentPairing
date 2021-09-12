class Student:

    def __init__(self, name, we_chat_id, major, purpose, pref):
        # Basic variable
        self.name = name
        self.we_chat_id = we_chat_id
        # Variable used to pair
        self.major = major
        self.purpose = purpose
        self.pref = pref

    def __str__(self):
        return "Name: " + self.name \
               + "\nWeChat ID:" + self.we_chat_id \
               + "\nMajor: " + self.major \
               + "\nPurpose: " + self.purpose \
               + "\nPreference: " + self.pref
