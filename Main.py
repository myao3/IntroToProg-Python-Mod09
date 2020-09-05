# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Myao,09.01.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")


# Main Body of Script  ---------------------------------------------------- #
# Add Data Code to the Main body
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]

# Load data from file into a list of employee objects when script starts
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))


# Show user a menu of options
while (True):
    Eio.print_menu_items()
    strChoice= Eio.input_menu_options()

# Get user's menu option choice
    # Show user current data in the list of employee objects
    if strChoice == '1':
        Eio.print_current_list_items(lstTable)
        continue

    # Let user add data to the list of employee objects
    elif strChoice.strip() == '2':
        input_data = Eio.input_employee_data()
        print(input_data)
        lstTable.append(input_data)
        continue

    # let user save current data to file
    elif strChoice == '3':
        Fp.save_data_to_file("EmployeeData.txt", lstTable)
        print('Saved!')
        continue

    # Let user exit program
    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        break

    else:
        print('Oops!  That was no valid number.  Try again...')
        continue
# Main Body of Script  ---------------------------------------------------- #
