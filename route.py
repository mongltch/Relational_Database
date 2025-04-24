import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3


def enter_data():
    routeNO = route_number_entry.get()
    starting_point = starting_point_entry.get()
    destination = destination_entry.get()
    miles = length_spinBox.get()
    if routeNO and starting_point and destination and miles:
        print('hi')

        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS Route
            (Route_Number INTEGER, Starting_Point TEXT, Destination TEXT, Length_Miles INTEGER, 
            PRIMARY KEY(Route_Number)) '''

        conn.execute(table_create_query)

        

        data_insert_query = '''INSERT INTO Route (Route_Number, Starting_Point, Destination, Length_Miles) VALUES (?, ?, ?, ?)'''
        data_insert_tuple = (routeNO, starting_point, destination, miles)
        
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()

        


        #close connection
        conn.close()



    else:
        tkinter.messagebox.showwarning(title='Complete Form', message= 'Must fill all sections before submission')

window = tkinter.Tk()

window.title('Buses Form')
frame = tkinter.Frame(window)
frame.pack()


route_frame1 = tkinter.LabelFrame(frame, text= 'Route Information')
route_frame1.grid(row= 0 , column= 0, padx=20, pady=20)

route_number_label = tkinter.Label(route_frame1, text= 'Route Number')
route_number_label.grid(row= 0, column= 0)
route_number_entry = tkinter.Entry(route_frame1)
route_number_entry.grid(row=1, column=0)


starting_point_label = tkinter.Label(route_frame1, text= 'Starting Point')
starting_point_label.grid(row= 0, column= 1)
starting_point_entry = tkinter.Entry(route_frame1)
starting_point_entry.grid(row=1, column=1)


destination_label = tkinter.Label(route_frame1, text='Destination')
destination_label.grid(row=2, column=0)
destination_entry = tkinter.Entry(route_frame1)
destination_entry.grid(row=3, column=0)


length_label = tkinter.Label(route_frame1, text='Length in Miles')
length_label.grid(row=2, column=1)
length_spinBox = tkinter.Spinbox(route_frame1, from_=10,  to= 'infinity')
length_spinBox.grid(row = 3, column= 1)

for widget in route_frame1.winfo_children():
    widget.grid_configure(padx=10, pady= 5)


button = tkinter.Button(frame, text='Submit', command= enter_data)
button.grid(row= 3, column=0, sticky='news' , padx=20, pady=10)








window.mainloop()