import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3


def enter_data():

    driverNo = bank_driverNO_entry.get()
    salary = salary_entry.get()
    bankName = bank_entry.get()
    accountNO = bank_accountNO_entry.get()
    sortCode = bank_sortNO_entry.get()

    if driverNo and salary and bankName and accountNO and sortCode:

        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS Bank_Account
        (BankACC_ID INTEGER, Driver_Number, Salary NUMERIC, Bank TEXT, Account_No INTEGER, Sort_Code TEXT,
	    PRIMARY KEY(BankACC_ID AUTOINCREMENT), FOREIGN KEY(Driver_Number) REFERENCES Driver(Driver_No))                                           
        '''
        conn.execute(table_create_query)

        #insert data

        data_insert_query = '''INSERT INTO Bank_Account (Driver_Number, Salary, Bank, Account_No, Sort_Code) VALUES (?, ?, ?, ?, ?)'''
        data_insert_tuple = (driverNo, salary, bankName, accountNO, sortCode)
        
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()

        


        #close connection
        conn.close()











        print('works')
    else:
        tkinter.messagebox.showwarning(title='Complete Form', message= 'Must fill all sections before submission')


window = tkinter.Tk()

window.title('Buses Form')
frame = tkinter.Frame(window)
frame.pack()


bank_account_frame1 = tkinter.LabelFrame(frame, text= 'Bank Account')
bank_account_frame1.grid(row= 0 , column= 0, padx=20, pady=20)


bank_driverNo_label = tkinter.Label(bank_account_frame1, text= 'Driver Number')
bank_driverNo_label.grid(row= 0, column= 0)
bank_driverNO_entry = tkinter.Entry(bank_account_frame1)
bank_driverNO_entry.grid(row=1, column=0)

salary_label = tkinter.Label(bank_account_frame1, text= 'Salary')
salary_label.grid(row= 0, column= 1)
salary_entry = tkinter.Entry(bank_account_frame1)
salary_entry.grid(row=1, column=1)

bank_label = tkinter.Label(bank_account_frame1, text= 'Bank')
bank_label.grid(row= 2, column= 0)
bank_entry = tkinter.Entry(bank_account_frame1)
bank_entry.grid(row=3, column=0)

bank_accountNO_label = tkinter.Label(bank_account_frame1, text= 'Bank Account Number')
bank_accountNO_label.grid(row= 2, column= 1)
bank_accountNO_entry = tkinter.Entry(bank_account_frame1)
bank_accountNO_entry.grid(row=3, column=1)

bank_sortNO_label = tkinter.Label(bank_account_frame1, text= 'Bank Sort Code')
bank_sortNO_label.grid(row= 4, column= 0)
bank_sortNO_entry = tkinter.Entry(bank_account_frame1)
bank_sortNO_entry.grid(row=5, column=0)


for widget in bank_account_frame1.winfo_children():
    widget.grid_configure(padx=10, pady= 5)


button = tkinter.Button(frame, text='Submit', command= enter_data)
button.grid(row= 3, column=0, sticky='news' , padx=20, pady=10)







window.mainloop()