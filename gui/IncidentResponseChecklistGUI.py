import customtkinter as ctk
from gui.GuiUtils import *
from utils.WordDocCreator import WordDocCreator
import json

class IrcApp:
    def __init__(self, master, checklist_name):

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=5)
        self.main_frame.columnconfigure(0, weight=1)

        self.name_label = ctk.CTkLabel(self.main_frame, text=checklist_name)
        self.name_label.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)

        self.checklist_frame = ctk.CTkFrame(self.main_frame, border_width=1, border_color="black")
        self.checklist_frame.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)


        with open('test.json', 'r') as json_file:
            data = json.load(json_file)

            for widget in data:
                if widget.get("ContentWidget") and widget.get("LabelText"):
                    frame = ctk.CTkFrame(self.checklist_frame)
                    frame.pack(side=ctk.TOP, fill="both", expand=True)
                    match widget.get("ContentWidget"):

                        case "Entry":
                            label = create_label(frame, widget.get("LabelText"))
                            label.pack(side=ctk.LEFT, padx=5, pady=5)
                            entry = create_entry(frame)
                            entry.pack(side=ctk.RIGHT, padx=5, pady=5)

                        case "Checkbox":
                            label = create_label(frame, widget.get("LabelText"))
                            label.pack(side=ctk.LEFT, padx=5, pady=5)
                            checkbox = create_checkbox(frame, on_value=1, off_value=0)
                            checkbox.pack(side=ctk.RIGHT, padx=5, pady=5)

                        case "Dropdown":
                            label = create_label(frame, widget.get("LabelText"))
                            label.pack(side=ctk.LEFT, padx=5, pady=5)
                            selection_list = widget.get("Selections")
                            dropdown = create_dropdown(frame, selection_list=selection_list)
                            dropdown.pack(side=ctk.RIGHT, padx=5, pady=5)

                        case _:
                            print(f'Invalid widget type received: {widget}')



        button = ctk.CTkButton(self.checklist_frame, text="Output", command=lambda: print_current_results(self.checklist_frame))
        button.pack(side=ctk.BOTTOM, padx=5, pady=5)



        # label_test = create_label(frame1, "This is a test of entry:")
        # entry_test = create_entry(frame1)
        # label_test.pack(side=ctk.LEFT, padx=5, pady=5)
        # entry_test.pack(side=ctk.RIGHT, padx=5, pady=5)
        #
        # frame2 = create_frame(self.checklist_frame)
        # frame2.pack(fill="x", expand=True)
        # label_test2 = create_label(frame2, "This is a test of combobox:")
        # dropdown_test2 = create_dropdown(frame2, ["Option 1", "Option 2"])
        # label_test2.pack(side=ctk.LEFT, padx=5, pady=5)
        # dropdown_test2.pack(side=ctk.RIGHT, padx=5, pady=5)



