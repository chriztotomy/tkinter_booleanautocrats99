from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Password Manager")
root.geometry("500x400")
root.minsize(600, 400)
root.maxsize(600, 400)

frame = Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.50, rely=0.50, relwidth=0.98, relheight=0.45, anchor = "n")

mysql = sqlite3.connect("passmanager.db")
cursor = mysql.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS paswd (
                       app_name text,
                        email_id text,
                        password text
                        )
""")


mysql.commit()

mysql.close()

def submit():
    #connect to database
    mysql = sqlite3.connect("passmanager.db")
    cursor = mysql.cursor()

    #Insert Into Table
    if url.get()!="" and email_id.get()!="" and password.get()!="":
        cursor.execute("INSERT INTO paswd VALUES (:url, :email_id, :password)",
            {
                'url': url.get(),
                'email_id': email_id.get(),
                'password': password.get()
            }
        )
        # Commit changes
        mysql.commit()
        # Close connection
        mysql.close()
        # Message box
        messagebox.showinfo("Info", "Record Added in Database!")

        # After data entry clear the text boxes
        url.delete(0, END)
        email_id.delete(0, END)
        password.delete(0, END)

    else:
        messagebox.showinfo("Alert", "Please fill all details!")
        conn.close()

def query():
    #set button text
    query_btn.configure(text="Hide Records", command=hide)
    # connect to database
    mysql = sqlite3.connect("passmanager.db")
    cursor = mysql.cursor()

    #Query the database
    cursor.execute("SELECT *, oid FROM paswd")
    records = cursor.fetchall()
    #print(records)

    p_records = ""
    for record in records:
            p_records += str(record[0])+ " " + str(record[1])+ " " + str(record[2]) + " " + str(record[3])+ "\n"
        #print(record)

    query_label['text'] = p_records
    # Commit changes
    mysql.commit()

    # Close connection
    mysql.close()

def delete():
    # connect to database
    conn = sqlite3.connect("passmanager.db")
    cursor = conn.cursor()

    #Query the database
    t = delete_id.get()
    if(t!=""):
        cursor.execute("DELETE FROM manager where oid = " + delete_id.get())
        delete_id.delete(0, END)
        messagebox.showinfo("Alert", "Record %s Deleted" %t)
    else:
        messagebox.showinfo("Alert", "Please enter record id to delete!")

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

def update():
    t = update_id.get()
    if(t!=""):
        global edit
        edit = Tk()
        edit.title("Update Record")
        edit.geometry("500x400")
        edit.minsize(450, 300)
        edit.maxsize(450, 300)

        #Global variables
        global app_name_edit, url_edit, email_id_edit, password_edit

        # Create Text Boxes
        app_name_edit = Entry(edit, width=30)
        app_name_edit.grid(row=0, column=1, padx=20)
        url_edit = Entry(edit, width=30)
        url_edit.grid(row=1, column=1, padx=20)
        email_id_edit = Entry(edit, width=30)
        email_id_edit.grid(row=2, column=1, padx=20)
        password_edit = Entry(edit, width=30)
        password_edit.grid(row=3, column=1, padx=20)

        # Create Text Box Labels
        app_name_label_edit = Label(edit, text="Application Name:")
        app_name_label_edit.grid(row=0, column=0)
        url_label_edit = Label(edit, text="URL:")
        url_label_edit.grid(row=1, column=0)
        email_id_label_edit = Label(edit, text="Email Id:")
        email_id_label_edit.grid(row=2, column=0)
        password_label_edit = Label(edit, text="Password:")
        password_label_edit.grid(row=3, column=0)
        submit_btn = Button(edit, text = "Generate")
        submit_btn.grid(row = 3, column=2, pady=5, padx=15, ipadx=35)


        # Create Save Button
        submit_btn_edit = Button(edit, text="Save Record", command=change)
        submit_btn_edit.grid(row=4, column=0, columnspan=2, pady=5, padx=15, ipadx=135)

        # connect to database
        conn = sqlite3.connect("passmanager.db")
        cursor = conn.cursor()

        # Query the database
        cursor.execute("SELECT * FROM manager where oid = " + update_id.get())
        records = cursor.fetchall()

        for record in records:
            app_name_edit.insert(0, record[0])
            url_edit.insert(0, record[1])
            email_id_edit.insert(0, record[2])
            password_edit.insert(0, record[3])

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

    else:
        messagebox.showinfo("Alert", "Please enter record id to update!")


url = Entry(root, width=30)
url.grid(row=1, column=1, padx=20)
email_id = Entry(root, width=30)
email_id.grid(row=2, column=1, padx=20)
password = Entry(root, width=30)
password.grid(row=3, column=1, padx=20)
delete_id = Entry(root, width=20)
delete_id.grid(row=6, column=1, padx=20)
update_id = Entry(root, width=20)
update_id.grid(row=7, column=1, padx=20)


url_label = Label(root, text = "URL:")
url_label.grid(row=1, column=0)
email_id_label = Label(root, text = "Email Id:")
email_id_label.grid(row=2, column=0)
password_label = Label(root, text = "Password:")
password_label.grid(row=3, column=0)
submit_btn = Button(root, text = "Generate")
submit_btn.grid(row = 3, column=3, pady=5, padx=15, ipadx=35)
#delete_label = Label(root, text = "Delete Record#:")
#delete_label.grid(row=6, column=1)


submit_btn = Button(root, text = "Add Record", command = submit)
submit_btn.grid(row = 5, column=0, pady=5, padx=15, ipadx=35)


query_btn = Button(root, text = "Show Records")
query_btn.grid(row=5, column=1, pady=5, padx=5, ipadx=35)


delete_btn = Button(root, text = "Delete Record")
delete_btn.grid(row=6, column=0, ipadx=30)


update_btn = Button(root, text = "Update Record")
update_btn.grid(row=7, column=0, ipadx=30)


global query_label
query_label = Label(frame, anchor="nw", justify="left")
query_label.place(relwidth=1, relheight=1)

def main():
    root.mainloop()

if __name__ == '__main__':
    main()

#root.mainloop()
