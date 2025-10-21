# Incident Response Checklist Tool

The **Incident Response Checklist Tool** is a lightweight Python application that helps security teams manage and document incident response procedures in a consistent, structured way.  
It uses simple JSON files to build interactive checklists dynamically and exports the results into a formatted Word document for reporting and review.

---

## Features

- **Dynamic GUI generation** – the interface is automatically built from JSON configuration files.  
- **Customizable checklists** – create new scenarios (ransomware, phishing, data breach, etc.) by writing a short JSON file.  
- **Automatic report creation** – exports results into a formatted Word document using `python-docx`.  
- **Modern, simple interface** – built with `CustomTkinter` for a clean user experience.  
- **Built-in error handling** – informative pop-ups and graceful exception handling.

---

## How It Works

1. The tool reads a JSON file that defines each checklist step.  
2. Each step specifies what to display in the GUI:

   ```json
   {
     "Step": "1",
     "LabelText": "Describe the step to take",
     "ContentWidget": "Checkbox" | "Entry",
     "Required": "True" | "False"
   }
   ```
3. The GUI (`IrcApp`) builds input fields and checkboxes dynamically from this data.  
4. When complete, the responses can be exported to a Word document through the `WordDocCreator` class.

---

## Example JSON File

Here’s a simple example for a ransomware response checklist:

```json
[
  {
    "Step": "1",
    "LabelText": "List all affected systems, devices, and network shares",
    "ContentWidget": "Entry",
    "Required": "True"
  },
  {
    "Step": "2",
    "LabelText": "Confirm ransomware infection (e.g., encrypted files, ransom note, alerts)",
    "ContentWidget": "Checkbox",
    "Required": "False"
  }
]
```

You can create additional files in the same format for other scenarios such as phishing, data breaches, or malware infections.

---

## Installation

1. Clone or download this repository.  
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:

   ```bash
   python IncidentResponseChecklist.py
   ```
---

## File Overview

| File | Description |
|------|--------------|
| `IncidentResponseChecklist.py` | Application entry point. Creates the main window, initializes the GUI, and handles runtime errors. |
| `IncidentResponseChecklistGUI.py` | Builds the dynamic GUI from the JSON input. |
| `WordDocCreator.py` | Handles Word document creation and table formatting. |
| `*.json` | Checklist definition files for different incident scenarios. |

---

## Example Output

When you export to Word, the tool creates:
- A heading with the checklist name  
- A two-column table with **Step Description** and **Step Results**  
- A confirmation message when the document is saved successfully  

---

## Extending the Tool

To add new incident types:

1. Create a JSON file in the same structure as the example above.  
2. Save it in the project directory.  
3. Select the file in the popup,


The tool will automatically generate a new interface and report format based on your file.

---

## Contributing

Contributions and suggestions are welcome.  
You can extend the tool by adding new checklist templates, improving the GUI layout, or expanding reporting capabilities.

---

## License

This project is available for internal and educational use.  
Please provide attribution if you reuse or adapt the code.
