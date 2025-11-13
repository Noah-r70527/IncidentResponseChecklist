import csv

def output_to_csv(csv_file_name: str, csv_file_content: list[dict[str, str]]) -> bool:

    try:
        with open(f'output/{csv_file_name}', "w", encoding="utf-8", newline='') as csv_file:
            headers = csv_file_content[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=headers, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(csv_file_content)
            return True

    except Exception as e:
        return False
