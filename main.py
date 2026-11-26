
from abc import ABC, abstractmethod


# Interface
class Management(ABC):

    @abstractmethod
    def dashboard(self):
        pass


# Admin Class
class Admin(Management):

    def dashboard(self):
        print("\n--- Admin Dashboard ---")
        print("1. Add Manager")
        print("2. Remove Manager")
        print("3. View All Managers")
        print("4. Manage System")

    def manage_system(self):
        print("Admin is managing the system...")


# Manager Class
class Manager(Management):

    def dashboard(self):
        print("\n--- Manager Dashboard ---")
        print("1. Add Employee")
        print("2. Assign Task")
        print("3. View Employees")
        print("4. View Tasks")

    def assign_task(self):
        task = input("Enter task name: ")
        print(f"Task assigned successfully: {task}")


# Main Program
def main():

    print("===== Company Management System =====")
    print("1. Admin Login")
    print("2. Manager Login")

    choice = input("Select your role: ")

    if choice == "1":
        user = Admin()
        user.dashboard()

        action = input("Select an option: ")

        if action == "4":
            user.manage_system()
        else:
            print("Admin option selected.")

    elif choice == "2":
        user = Manager()
        user.dashboard()

        action = input("Select an option: ")

        if action == "2":
            user.assign_task()
        else:
            print("Manager option selected.")

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
