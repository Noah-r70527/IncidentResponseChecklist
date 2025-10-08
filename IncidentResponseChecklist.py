from gui.IncidentResponseChecklistGUI import *

if __name__ == "__main__":
    try:
        root = ctk.CTk()
        root.title("IR Checklist Tool")
        root.geometry("600x600")
        app = IrcApp(root, checklist_name="Ransomware")
        root.mainloop()

    except ModuleNotFoundError as e:
        input(f'Missing a module: {e}. Trying running pip -r requirements.txt and then run the script again.')

    except FileNotFoundError as e:
        input(f'Error occurred during initialization: {e}')

    except Exception as e:
        input(f'Unhandled exception occurred.: {e}')
