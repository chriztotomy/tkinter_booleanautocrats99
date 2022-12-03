from tkinter import *
root = Tk()
root.title("Password Manager")
#conn = sqlite3.connect("passmanager.db")
#cursor = conn.cursor()

#cursor.execute(""" CREATE TABLE IF NOT EXISTS manager (
#                       app_name text,
#                        email_id text,
#                        password text
#                        )
#""")

#Create Text Boxes
app_name = Entry(root, width=30)
app_name.grid(row=0, column=1, padx=20)
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

#Create Text Box Labels
app_name_label = Label(root, text = "Application Name:")
app_name_label.grid(row=0, column=0)
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

#Create Submit Button
submit_btn = Button(root, text = "Add Record")
submit_btn.grid(row = 5, column=0, pady=5, padx=15, ipadx=35)

#Create a Query Button
query_btn = Button(root, text = "Show Records")
query_btn.grid(row=5, column=1, pady=5, padx=5, ipadx=35)

#Create a Delete Button
delete_btn = Button(root, text = "Delete Record")
delete_btn.grid(row=6, column=0, ipadx=30)

#Create a Update Button
update_btn = Button(root, text = "Update Record")
update_btn.grid(row=7, column=0, ipadx=30)

#Create a Label to show responses
#global query_label
#query_label = Label(frame, anchor="nw", justify="left")
#query_label.place(relwidth=1, relheight=1)

def main():
    root.mainloop()

if __name__ == '__main__':
    main()

#root.mainloop()
