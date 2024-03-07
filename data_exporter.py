import csv

def export_emails_to_csv(emails, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Email"])
        for email in emails:
            writer.writerow([email])
    print(f'Data exported to {file_path}')
