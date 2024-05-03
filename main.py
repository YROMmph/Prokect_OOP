
class Appointment:
    def __init__(self, day, time, description):
        self.day = day
        self.time = time
        self.description = description

class AppointmentBook:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def get_appointments(self):
        return self.appointments

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for appointment in self.appointments:
                f.write(f"{appointment.day},{appointment.time},{appointment.description}\n")

    def load_from_file(self, filename):
        self.appointments = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                day, time, description = line.strip().split(',')
                self.appointments.append(Appointment(day, time, description))

    def sort_appointments(self):
        self.appointments.sort(key=lambda x: (x.day, x.time))

    def search_appointments(self, day=None, week=None):
        if day:
            return [a for a in self.appointments if a.day == day]
        elif week:
            return [a for a in self.appointments if a.day in week]
        else:
            return self.appointments
        
class ConsoleView:
    def __init__(self):
        pass

    def show_appointments(self, appointments):
        for appointment in appointments:
            print(f"{appointment.day} {appointment.time} - {appointment.description}")

    def ask_for_appointment(self):
        day = input("Enter day: ")
        time = input("Enter time: ")
        description = input("Enter description: ")
        return Appointment(day, time, description)

    def ask_for_filename(self):
        return input("Enter filename: ")

    def show_message(self, message):
        print(message)

class AppointmentPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            print("1. Make an appointment")
            print("2. Read appointments")
            print("3. Save appointments to file")
            print("4. Load appointments from file")
            print("5. Sort appointments")
            print("6. Search appointments")
            print("7. Quit")
            choice = input("Enter choice: ")

            if choice == "1":
                appointment = self.view.ask_for_appointment()
                self.model.add_appointment(appointment)
                self.view.show_message("Appointment added successfully")
            elif choice == "2":
                appointments = self.model.get_appointments()
                self.view.show_appointments(appointments)
            elif choice == "3":
                filename = self.view.ask_for_filename()
                self.model.save_to_file(filename)
                self.view.show_message("Appointments saved to file successfully")
            elif choice == "4":
                filename = self.view.ask_for_filename()
                self.model.load_from_file(filename)
                self.view.show_message("Appointments loaded from file successfully")
            elif choice == "5":
                self.model.sort_appointments()
                self.view.show_message("Appointments sorted successfully")
            elif choice == "6":
                day = input("Enter day (or leave blank for week): ")
                week = input("Enter week (or leave blank for day): ")
                if day:
                    appointments = self.model.search_appointments(day=day)
                elif week:
                    appointments = self.model.search_appointments(week=week)
                else:
                    appointments = self.model.search_appointments()
                self.view.show_appointments(appointments)
            elif choice == "7":
                break
            else:
                self.view.show_message("Invalid choice")

if __name__ == "__main__":
    model = AppointmentBook()
    view = ConsoleView()
    presenter = AppointmentPresenter(model, view)
    presenter.run()