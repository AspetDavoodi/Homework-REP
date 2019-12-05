class Classroom:

    def __init__(self, room_no, Max_Cap, Open_time, Close_time):

        self.Room_num = room_no
        self.Maximum_Capacity = int(Max_Cap)
        self.opening_time = Open_time
        self.closing_time = Close_time
        self.schedule = [] #add dictionaries to this list


    def checkMaxCap(self, NumofStudents):
        if int(NumofStudents) <= self.Maximum_Capacity:
            return True
        else:
            return False

    def CheckBookTime(self,StartofBooking, EndofBooking):
        if StartofBooking < self.opening_time or EndofBooking > self.closing_time:
            print ("Reservation cannot be made. Room is Closed at that time.")
            return False
        else:
            return True

    def isFree(self, Tstart, Tend):

        interference = 0

        for slot in self.schedule:
            if (int(Tstart) < int(slot["Start"]) or int(Tend) < int(slot["End"])) and (int(Tstart) > int(slot["Start"]) or int(Tend) > int(slot["End"])):
                interference += 1
            else:
                continue

        if interference == 0:
            return True
        else: return False


    def ReserveRoom(self, Tstart, Tend):
        if self.isFree(Tstart, Tend):
            timeslot = {"Start":Tstart, "End":Tend}
            self.schedule.append(timeslot)
            return True
        else:
            self.CheckBookTime(Tstart,Tend)



def main():

    Classroom1 = Classroom("608M", 35, "0800", "2200")

    start = input("Please enter the start time of your reservation in a 4 number form e.g.\n"
                  "- 1300 for 13:00\n"
                  "- 1330 for 13:30\n")
    end = input("Please enter the end time of your reservation in a 4 number form e.g.\n"
                "- 1300 for 13:00\n"
                "- 1330 for 13:30\n")

    while not (Classroom1.ReserveRoom(start, end)):
        print ("The room is booked for the time specified, please enter a new interval...")
        start = input("Please enter the start time of your reservation in a 4 number form e.g.\n"
                      "- 1300 for 13:00\n"
                      "- 1330 for 13:30\n")
        end = input("Please enter the end time of your reservation in a 4 number form e.g.\n"
                    "- 1300 for 13:00\n"
                    "- 1330 for 13:30\n")

    print (Classroom1.schedule)

main()