import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer= csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow('Name', 'Age', 'Email ID', "Contact Number")

        writer.writerow(info_list)

if __name__== '__main__':
    condition = True
while(condition):
                student= input("Enter student info in the following format name, age, email id, contact number: ")
                print(f'student info is: {student}')
                
                student_info_list= student.split ( )
                print(student_info_list)

                print("\n The entered information is: \n name:{}, \n age: {}, \n email id: {}, \n contact_number: {}".format(student_info_list[1], student_info_list[2], student_info_list[3]))
                check: input("Is the information entered correct? yes or no")

                if check== 'yes':
                    write_into_csv(student_info_list)

condition_check= input('Enter information about another student: ')
if condition_check == "yes":
    condition= True

elif condition_check == "no":
        condition= False
elif condition_check == "no":
     print("\n Please re-enter the values: ")
