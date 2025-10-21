from gui.IncidentResponseChecklistGUI import *
from tkinter import filedialog, messagebox
from pathlib import Path
import time

TEMPLATE_FILE_PATH = os.path.join(Path(__file__).resolve().parent, r"assets\ChecklistTemplates")

if __name__ == "__main__":
    try:
        file_path = filedialog.askopenfilename(initialdir=TEMPLATE_FILE_PATH)
        root = ctk.CTk()
        root.title("IR Checklist Tool")
        root.geometry("800x400") # Initial size of program
        name = os.path.basename(file_path).split(".json")[0].capitalize() # Setting the name based on the input json file.

        app = IrcApp(root, checklist_name=name, input_file=file_path)
        root.mainloop()

    except ModuleNotFoundError as e:
        messagebox.showerror(title=e.name, message=f'Missing a module. '
                                                   f'Trying running pip -r requirements.txt '
                                                   f'and then run the script again.')

    except FileNotFoundError as e:
        messagebox.showerror(title=e.strerror, message=f'Could not find the input file.')

    except Exception as e:
        messagebox.showerror(title="Exception occurred..", message=f'Unhandled exception: {e}')

    finally:
        print(f'Finished running.. Closing')
        time.sleep(5)
