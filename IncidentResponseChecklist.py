from gui.IncidentResponseChecklistGUI import *
from tkinter import PhotoImage, TclError

if __name__ == "__main__":
    try:
        root = ctk.CTk()
        root.title("IR Checklist Tool")
        root.geometry("800x400")

        try:
            icon_image = PhotoImage(file="assets/ndrtechlogo.png")
            root.iconphoto(True, icon_image)

        except TclError:
            print("Failed to set icon.")

        app = IrcApp(root, checklist_name="Ransomware", input_file="test.json")
        root.mainloop()

    except ModuleNotFoundError as e:
        input(f'Missing a module: {e}. Trying running pip -r requirements.txt and then run the script again.')

    except FileNotFoundError as e:
        input(f'Error occurred during initialization: {e}')

    except Exception as e:
        input(f'Unhandled exception occurred.: {e}')
