import os
import csv
import json
import argparse
from concurrent.futures import ThreadPoolExecutor
from faker import Faker
from tqdm import tqdm

fake = Faker()

def generate_mock_data(file_path, file_size_mb, batch_size=10000, file_format="csv"):
    """
    Generates a mock user data file (CSV or JSON) until it reaches the specified file size.
    
    :param file_path: Name of the output file
    :param file_size_mb: Target file size in megabytes
    :param batch_size: Number of rows to write in each batch (default: 10,000)
    :param file_format: Output file format ('csv' or 'json')
    """
    target_size = file_size_mb * 1024 * 1024  # Convert MB to bytes
    headers = ["id", "name", "email", "phone", "address", "city", "state", "zip", "country"]
    
    write_func = write_csv if file_format == "csv" else write_json

    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        if file_format == "csv":
            writer = csv.writer(file)
            writer.writerow(headers)  # Write CSV header

        file.seek(0, os.SEEK_END)  # Move to end to check size
        current_size = file.tell()
        user_id = 1

        # Progress bar
        with tqdm(total=target_size, unit="B", unit_scale=True, desc=f"Generating {file_format.upper()} File", dynamic_ncols=True, ascii=True, mininterval=0.5) as pbar:
            while current_size < target_size:
                with ThreadPoolExecutor() as executor:
                    data_buffer = [generate_user_record(user_id + i) for i in range(batch_size)]
                    executor.submit(write_func, file, data_buffer)

                user_id += batch_size
                
                # Check file size only after batch write
                file.seek(0, os.SEEK_END)
                new_size = file.tell()
                
                # Update progress bar
                pbar.update(new_size - current_size)
                current_size = new_size

        tqdm.write(f"\nGenerated {file_path} with an approximate size of {file_size_mb}MB.")  # Ensure message is visible

def generate_user_record(user_id):
    """Generates a fake user record."""
    return {
        "id": user_id,
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zip": fake.zipcode(),
        "country": fake.country()
    }

def write_csv(file, data_buffer):
    """Writes data buffer to CSV file."""
    writer = csv.writer(file)
    writer.writerows([list(record.values()) for record in data_buffer])

def write_json(file, data_buffer):
    """Writes data buffer to JSON file."""
    json.dump(data_buffer, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a mock user dataset.")
    parser.add_argument("--file", type=str, default="mock_users.csv", help="Output file name (default: mock_users.csv)")
    parser.add_argument("--size", type=int, default=10, help="File size in MB (default: 10MB)")
    parser.add_argument("--format", type=str, choices=["csv", "json"], default="csv", help="File format: csv or json (default: csv)")

    args = parser.parse_args()

    generate_mock_data(args.file, args.size, file_format=args.format)