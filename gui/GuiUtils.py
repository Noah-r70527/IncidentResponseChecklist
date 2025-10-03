from typing import Callable
import customtkinter as ctk

def create_label(parent_widget: ctk.CTkFrame, label_text: str) -> ctk.CTkLabel:
    label = ctk.CTkLabel(parent_widget, text=label_text)
    return label


def create_button(parent_widget: ctk.CTkFrame, button_text: str, button_command_func: Callable) -> ctk.CTkButton:
    button = ctk.CTkButton(parent_widget, text=button_text, command=button_command_func)
    return button


def create_checkbox(parent_widget: ctk.CTkFrame, on_value: int = 1, off_value: int = 1) -> ctk.CTkCheckBox:
    check_box = ctk.CTkCheckBox(parent_widget, onvalue=on_value, offvalue=off_value, text="")
    return check_box


def create_dropdown(parent_widget: ctk.CTkFrame, selection_list: list[str]) -> ctk.CTkComboBox:
    combo_box = ctk.CTkComboBox(parent_widget, values=selection_list)
    return combo_box


def create_entry(parent_widget: ctk.CTkFrame) -> ctk.CTkEntry:
    entry = ctk.CTkEntry(parent_widget)
    return entry


def create_frame(parent_widget: ctk.CTkFrame) -> ctk.CTkFrame:
    frame = ctk.CTkFrame(parent_widget)
    return frame