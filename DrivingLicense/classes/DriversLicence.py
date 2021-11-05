from datetime import date, timedelta

class DriversLicence():

    def convert_dob_to_age(self, year, month, day):
        # dob, convert it to age
        if year > 0 and month > 0 and day > 0:
            today = date.today() #Today's date
            birthday = date(year, month, day)  #Birth date

            #Calculate age
            age = (today - birthday) // timedelta(days=365.2425)

            return age
        # Cannot convert negative distance
        else:
            return 0

    """
     * User eligible to apply for a full licence if they are 17 or over. If they are under 17, they are not eligible.
     * They must also already have a provisional licence
     * 
     * @param age - users current age
     * @param provisionalLicence - if they have a provisional licence
     * @return string informing them if they can apply
    """
    def can_driver_apply_for_full_licence(self, age, provisional_licence ):
        if age < 17:
            outcome = "You are NOT eligible to apply for a driving license"
        elif age >17 or provisional_licence == True:
            outcome = "You are eligible to apply for a driving license"
        elif age >17 or provisional_licence == False:
            outcome = "You are NOT eligible to apply for a driving license"
        else:
            outcome = "Cannot be determined."

        return outcome


if __name__ == '__main__':
    print("******                               *******    ")
    print("****** Driving Licence Application   *******    ")
    year = int(input("Please enter your year of birth (in format yyyy): "))
    month = int(input("Please enter your month of birth (in format 1-12): "))
    day = int(input("Please enter your day of birth (in format 1-31): "))
    pl = bool(input("Do you have a provisional licence? (True / False):  "))

    drivers_licence = DriversLicence()
    age = drivers_licence.convert_dob_to_age(year, month, day);
    print("You are : ", age, " years old.")

    print(drivers_licence.can_driver_apply_for_full_licence(age, pl))