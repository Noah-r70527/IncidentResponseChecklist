from typing import Callable
import customtkinter as ctk
from customtkinter import CTkFont

from utils.WordDocCreator import WordDocCreator

def create_label(parent_widget: ctk.CTkFrame, label_text: str) -> ctk.CTkLabel:
    label = ctk.CTkLabel(parent_widget, text=label_text, font=("Arial", 15))
    return label


def create_button(parent_widget: ctk.CTkFrame, button_text: str, button_command_func: Callable) -> ctk.CTkButton:
    button = ctk.CTkButton(parent_widget, text=button_text, command=button_command_func)
    return button


def create_checkbox(parent_widget: ctk.CTkFrame, on_value: int = "Done", off_value: int = "Not Done") -> ctk.CTkCheckBox:
    check_box = ctk.CTkCheckBox(parent_widget, onvalue=on_value, offvalue=off_value, text="")
    return check_box


def create_dropdown(parent_widget: ctk.CTkFrame, selection_list: list[str]) -> ctk.CTkComboBox:
    combo_box = ctk.CTkComboBox(parent_widget, values=selection_list, state="readonly", font=("Arial", 20))
    return combo_box


def create_entry(parent_widget: ctk.CTkFrame) -> ctk.CTkEntry:
    entry = ctk.CTkEntry(parent_widget)
    return entry


def create_frame(parent_widget: ctk.CTkFrame) -> ctk.CTkFrame:
    frame = ctk.CTkFrame(parent_widget)
    return frame



def print_current_results(widget_in, checklist_type):
    output = []
    widgets = widget_in.winfo_children()
    for widget in widgets:
        if isinstance(widget, ctk.CTkFrame):
            label = widget.winfo_children()[0]
            content_label = widget.winfo_children()[1]

            match type(content_label):

                case ctk.CTkCheckBox:
                    check: ctk.CTkCheckBox = content_label
                    output.append(
                        {
                            label.cget("text"): "Done" if check.get() == 1 else "Not Done"
                        }
                    )

                case ctk.CTkComboBox:
                    dropbox: ctk.CTkComboBox = content_label
                    output.append(
                        {
                            label.cget("text"): dropbox.get()
                        }
                    )

                case ctk.CTkEntry:
                    entry: ctk.CTkEntry = content_label
                    output.append(
                        {
                            label.cget("text"): entry.get()
                        }
                    )
                case _:
                    print(f'Neither')

    with WordDocCreator("Output.docx", checklist_name=checklist_type) as document:
        document.write_output(output)