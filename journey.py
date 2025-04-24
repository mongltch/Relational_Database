import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3


def enter_data():
    busNO = bus_number_entry.get()
    routeNO = route_number_entry.get()
    driverNO = driver_number_entry.get()
    day = day_entry.get()
    startTime = startTime_entry.get()
    finishTime = finishTime_entry.get()

    if busNO and routeNO and driverNO and day and startTime and finishTime:
        if int(startTime) <= 2300 and int(finishTime) <= 2300:

            conn = sqlite3.connect('SpeedyTravelDatabase.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Journey
            (Journey_No INTEGER, Bus_Number INTEGER, Route_No INTEGER, Driver_No INTEGER, Day_Of_Week TEXT, Start_Time INTEGER,
            Finish_Time INTEGER, PRIMARY KEY(Journey_No AUTOINCREMENT), FOREIGN KEY(Bus_Number) REFERENCES Buses (Bus_Number),
	        FOREIGN KEY(Driver_No) REFERENCES Driver (Driver_No), FOREIGN KEY(Route_No) REFERENCES Route (Route_Number))
                                                      
            '''
            conn.execute(table_create_query)

            #insert data

            data_insert_query = '''INSERT INTO Journey (Bus_Number, Route_No, Driver_No, Day_Of_Week, Start_Time, Finish_Time) VALUES (?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (busNO, routeNO, driverNO, day , startTime, finishTime)
            
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()

            


            #close connection
            conn.close()








            print('works')
        else:
            tkinter.messagebox.showwarning(title='Invalid Time', message= 'Invalid Time input. Please try again')
    else:
        tkinter.messagebox.showwarning(title='Complete Form', message= 'Must fill all sections before submission')


window = tkinter.Tk()

window.title('Buses Form')
frame = tkinter.Frame(window)
frame.pack()



journey_frame1 = tkinter.LabelFrame(frame, text= 'Journey')
journey_frame1.grid(row= 0 , column= 0, padx=20, pady=20)


bus_number_label = tkinter.Label(journey_frame1, text='Bus Number')
bus_number_label.grid(row= 0, column= 0)
bus_number_entry = tkinter.Entry(journey_frame1)
bus_number_entry.grid(row=1, column=0)

route_number_label = tkinter.Label(journey_frame1, text='Route Number')
route_number_label.grid(row= 0, column= 1)
route_number_entry = tkinter.Entry(journey_frame1)
route_number_entry.grid(row=1, column=1)

driver_number_label = tkinter.Label(journey_frame1, text='Driver Number')
driver_number_label.grid(row= 2, column= 0)
driver_number_entry = tkinter.Entry(journey_frame1)
driver_number_entry.grid(row=3, column=0)

day_label = tkinter.Label(journey_frame1, text='Day of week')
day_label.grid(row= 2, column= 1)
day_entry = tkinter.Entry(journey_frame1)
day_entry.grid(row=3, column=1)

startTime_label = tkinter.Label(journey_frame1, text='Journey Start Time \n(e.g. 14:00 = 1400)')
startTime_label.grid(row= 4, column= 0)
startTime_entry = tkinter.Entry(journey_frame1)
startTime_entry.grid(row=5, column=0)

finishTime_label = tkinter.Label(journey_frame1, text='Journey Finish Time \n(e.g. 16:30 = 1630)')
finishTime_label.grid(row= 4, column= 1)
finishTime_entry = tkinter.Entry(journey_frame1)
finishTime_entry.grid(row=5, column=1)


for widget in journey_frame1.winfo_children():
    widget.grid_configure(padx=10, pady= 5)


button = tkinter.Button(frame, text='Submit', command= enter_data)
button.grid(row= 3, column=0, sticky='news' , padx=20, pady=10)






window.mainloop()