import csv

def output_to_csv(csv_file_name: str, csv_file_content: list[dict[str, str]]) -> bool:

    try:
        with open(f'output/{csv_file_name}', "w", encoding="utf-8", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Step Description", "Step Results"])

            for row in csv_file_content:
                key, value = list(row.items())[0]
                writer.writerow([key, value])

        return True

    except Exception as e:
        print("Error:", e)
        return False
