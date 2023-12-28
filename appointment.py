
# Methods:









class Appointment:
    # __init__(): Constructor to initialize properties
    def __init__(self, day_of_week, start_time_hour):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    #Getters for each property
    def get_client_name(self):
        return self.__client_name

    def get_client_phone(self):
        return self.__client_phone

    def get_appt_type(self):
        return self.__appt_type

    def get_day_of_week(self):
        return self.__day_of_week

    def get_start_time_hour(self):
        return self.__start_time_hour

    #get_appt_type_desc(): Getter for translating appt_type to a text description
    def get_appt_type_desc(self):
        appt_type_desc = {0:"Available", 1:"Mens Cut", 2:"Ladies Cut", 3:"Mens Colouring", 4:"Ladies Colouring"}   
        return appt_type_desc.get(self.__appt_type)   
    
    #get_end_time_hour(): Getter for the end time of the appointment
    def get_end_time_hour(self):
        return str(self.__start_time_hour + 1)
    
    #setters for client_name, client_phone, and appt_type
    def set_client_name(self, new_client_name):
        self.__client_name = new_client_name
     
    def set_client_phone(self, new_client_phone):
        self.__client_phone = new_client_phone
    
    def set_appt_type(self, new_appt_type):
        self.__appt_type = new_appt_type

    #schedule(): Method to set client_name, client_phone, and appt_type properties
    def schedule(self, client_name, client_phone, appt_type):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type

    #cancel(): Method to reset client_name, client_phone, and appt_type properties
    def cancel(self):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0

    #format_record(): Method to return a string representation of an Appointment object
    def format_record(self):
        return str(self.__client_name) + "," + str(self.__client_phone) + "," + str(self.__appt_type) + "," + str(self.__day_of_week) + "," + str(self.__start_time_hour).zfill(2)

    #__str__(): Method to return a formatted string representation for display
    def __str__(self): 
        return "{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format(str(self.__client_name),
        str(self.__client_phone), str(self.__day_of_week), str(self.__start_time_hour).zfill(2) + ":00", str(self.__start_time_hour + 1).zfill(2) + ":00", self.get_appt_type_desc())