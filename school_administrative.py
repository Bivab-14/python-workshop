import csv

def write_info_csv(info_list):
    with open('student_info.csv','w+',newline= '') as csv_file:
        writer =csv.writer(csv_file)

        writer.writerow(info_list)

condition = True
while(condition):
    student_info=input("Enter student info in following format(Name Age Contact_no E-mail ID")
    print("Entered information" +student_info)

    student_info_list= student_info.split(' ')
    print("Entered split up information is"+ str(student_info_list))
    condition_check = input("Enter (yes/no) if you want to enter more information about another student")
    if condition_check = "yes":
        condition = True
    elif condition_check = "no":
        condition = False
