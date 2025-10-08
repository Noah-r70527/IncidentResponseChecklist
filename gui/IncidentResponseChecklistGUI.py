from gui.GuiUtils import *
import json

class IrcApp:

    def __init__(self, master, checklist_name):

        self.finalize_button = None
        self.ctkVars = []
        self.total_steps = 0
        self.enable_report = ctk.BooleanVar()
        self.enable_report.set(False)
        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=10)
        self.main_frame.columnconfigure(0, weight=1)

        self.name_label = ctk.CTkLabel(self.main_frame, text=checklist_name, font=("Arial", 40))
        self.name_label.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)

        self.checklist_frame = ctk.CTkScrollableFrame(self.main_frame, border_width=1, border_color="black")
        self.checklist_frame.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)
        self.init_gui(checklist_name)


    def update_var_completion(self, label_text: str):
        found = False
        for entry in self.ctkVars:
            if label_text in entry:
                found = True

        if not found:
            self.ctkVars.append(
                {label_text: "Done"}
            )

        if len(self.ctkVars) >= self.total_steps:
            self.enable_report.set(True)

    def toggle_finalize_button_state(self, *args):
        if self.enable_report.get():
            self.finalize_button.configure(state="normal")
        else:
            self.finalize_button.configure(state="disabled")

    def init_gui(self, checklist_name):

        with open('test.json', 'r') as json_file:
            data = json.load(json_file)

            for widget in data:
                required = widget.get("Required")
                if required == "True": self.total_steps += 1
                if widget.get("ContentWidget") and widget.get("LabelText"):
                    frame = ctk.CTkFrame(self.checklist_frame, fg_color="transparent")
                    frame.pack(side=ctk.TOP, fill="x", expand=True, padx=5)
                    frame.grid_rowconfigure(0, weight=1)
                    frame.grid_columnconfigure(0, weight=1)
                    frame.grid_columnconfigure(1, weight=2)

                    match widget.get("ContentWidget"):

                        case "Entry":
                            entry_var = ctk.Variable()
                            text = widget.get("LabelText")
                            label = create_label(frame, text)
                            label.grid(row=0, column=0, sticky="nsw", padx=1, pady=1)
                            entry = create_entry(frame, entry_var)
                            entry.grid(row=0, column=1, sticky="nse", padx=1, pady=1)
                            if required == "True":
                                entry_var.trace_add(
                                "write",
                                lambda var_name, index, mode, label_text=text:
                                self.update_var_completion(label_text))

                        case "Checkbox":
                            checkbox_var = ctk.Variable()
                            text = widget.get("LabelText")
                            label = create_label(frame, text)
                            label.grid(row=0, column=0, sticky="nsw", padx=1, pady=1)
                            checkbox = create_checkbox(frame, on_value=1, off_value=0, ctkVar=checkbox_var)
                            checkbox.grid(row=0, column=1, sticky="nse", padx=1, pady=1)
                            if required == "True":
                                checkbox_var.trace_add(
                                "write",
                                lambda var_name, index, mode, label_text=text:
                                self.update_var_completion(label_text)
                            )

                        case "Dropdown":
                            dropdown_var = ctk.Variable()
                            text = widget.get("LabelText")
                            label = create_label(frame, text)
                            label.grid(row=0, column=0, sticky="nsw", padx=1, pady=1)
                            selection_list = widget.get("Selections")
                            dropdown = create_dropdown(frame, selection_list=selection_list, ctkVar=dropdown_var)
                            dropdown.grid(row=0, column=1, sticky="nse", padx=1, pady=1)
                            if required == "True":
                                dropdown_var.trace_add(
                                "write",
                                lambda var_name, index, mode, label_text=text:
                                self.update_var_completion(label_text))

                        case _:
                            print(f'Invalid widget type received: {widget}')

        self.finalize_button = ctk.CTkButton(self.checklist_frame, text="Finalize Report", state="disabled",
                               command=lambda: print_current_results(self.checklist_frame, checklist_name))
        self.finalize_button.pack(side=ctk.BOTTOM, padx=5, pady=5)
        self.enable_report.trace_add("write", self.toggle_finalize_button_state)

