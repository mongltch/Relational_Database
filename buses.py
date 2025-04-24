import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3

def validateDate(date):
    if int(date[5:7]) > 12:
        return False
    elif int(date[8:10]) > 32:
        return False
    elif int(date[0:4]) > 2025:
        return False
    return True

def enter_data():
    registrationNO = registration_entry.get()
    registrationYear = registration_year_entry.get()
    seatingCap = seating_capacity_spinBox.get()
    lastServiced = last_serviced_entry.get()
    lastMOTED = last_MOTED_entry.get()
    if registrationNO and registrationYear and seatingCap and lastServiced and lastMOTED:
        if validateDate(lastServiced) == True and validateDate(lastMOTED) == True:
            print('Reg No:', registrationNO, 'Year: ', registrationYear, 'Seating Capacity: ', seatingCap)
            print('Last Serviced: ', lastServiced, 'Last MOTED: ', lastMOTED)

            #connect to sqlite3

            conn = sqlite3.connect('SpeedyTravelDatabase.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Buses
            (Bus_Number INTEGER, Registration_Number INTEGER UNIQUE, Seating_Capacity INTEGER, Last_Serviced TEXT, Last_MOTED TEXT,
                PRIMARY KEY("Bus_Number" AUTOINCREMENT))                                            
            '''
            conn.execute(table_create_query)

            #insert data

            data_insert_query = '''INSERT INTO Buses (Registration_Number, Registration_Year, Seating_Capacity, Last_Serviced, Last_MOTED) VALUES (?, ?, ?, ?, ?)'''
            data_insert_tuple = (registrationNO, registrationYear, seatingCap, lastServiced,lastMOTED)
            
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()

            


            #close connection
            conn.close()










        else:
            tkinter.messagebox.showwarning(title='Invalid Date', message= 'Invalid Date input. Please try again')
    else:
        tkinter.messagebox.showwarning(title='Complete Form', message= 'Must fill all sections before submission')

window = tkinter.Tk()

window.title('Buses Form')
frame = tkinter.Frame(window)
frame.pack()

#first frame of buses
bus_info_frame1 = tkinter.LabelFrame(frame, text= 'Bus Information')
bus_info_frame1.grid(row= 0 , column= 0, padx=20, pady=20)

#registration label + entry in frame 1
registration_Number_label = tkinter.Label(bus_info_frame1, text= 'Registration Number')
registration_Number_label.grid(row= 0, column= 0)
registration_entry = tkinter.Entry(bus_info_frame1)
registration_entry.grid(row=1, column=0)

#year of reg
registration_year_label = tkinter.Label(bus_info_frame1, text='Year of Registration')
registration_year_entry = tkinter.Entry(bus_info_frame1)
registration_year_label.grid(row=0, column=1)
registration_year_entry.grid(row=1, column=1)

#seating capacity
seating_capacity_label = tkinter.Label(bus_info_frame1, text='Seating Capacity')
seating_capacity_label.grid(row=2, column=0)
seating_capacity_spinBox = tkinter.Spinbox(bus_info_frame1, from_=10,  to= 'infinity')
seating_capacity_spinBox.grid(row = 3, column= 0)

#Last date serviced 
last_serviced_label = tkinter.Label(bus_info_frame1, text= 'Last Serviced (yyyy-mm-dd)')
last_serviced_entry = tkinter.Entry(bus_info_frame1)
last_serviced_label.grid(row= 2, column=1)
last_serviced_entry.grid(row=3, column=1)

#last date moted 
last_MOTED_label = tkinter.Label(bus_info_frame1, text= "Last MOT'ed(yyyy-mm-dd) ")
last_MOTED_entry = tkinter.Entry(bus_info_frame1)
last_MOTED_label.grid(row= 4, column=0)
last_MOTED_entry.grid(row=5, column=0)


#spacing
for widget in bus_info_frame1.winfo_children():
    widget.grid_configure(padx=10, pady= 5)


button = tkinter.Button(frame, text='Submit', command= enter_data)
button.grid(row= 3, column=0, sticky='news' , padx=20, pady=10)
























window.mainloop()