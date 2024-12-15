# -*- coding: utf-8 -*-
"""
This program converts a CSV file to a fixed-length TXT file.
It uses a settings file written in JSON, which contains the structure of the CSV file and the desired output formatting.
"""

import json
import csv
import argparse
from pathlib import Path
from datetime import datetime

def pad_value(value: str, length: str, type: str):
    """
    This function adds padding to a string.

    Args:
        value (str): Original string.
        length (str): Fixed length.
        type (str): Type of padding: 'full', 'half', 'date' or 'digits'.

    Returns:
        str: String with padding.
    """

    if type == "full":
        padding = '　'
    elif type == "half" or type == "date":
        padding = ' '
    elif type == "digits":
        padding = '0'
        return value.rjust(length, padding)
    else:
        raise ValueError(f"Unknown padding type: {type}")
    
    return value.ljust(length, padding)
    
def format_date(date_string: str, original_format: str):
    """
    This function formats date string to %Y/%m/%d format.

    Args:
        date_string (str): A string with date.
        original_format (str): A string with date format like %Y/%m/%d.

    Returns:
        str: YYYYMMDD-like formatted date string if successful, 'ERROR' otherwise.
    """

    try:
        date_obj = datetime.strptime(date_string, original_format)
        return date_obj.strftime('%Y%m%d')
    except ValueError:
        return 'ERROR'

def main():
    """
    The main function.

    Returns:
        int: The final result code.
    """

    # Create argument parser
    parser = argparse.ArgumentParser(description='This script converts CSV file to a fixed-length TXT one.')
    parser.add_argument('settings_path', type=Path, help='Path to the settings (JSON) file')
    parser.add_argument('csv_path', type=Path, help='Path to the CSV file')
    parser.add_argument('txt_path', type=Path, help='Path to the TXT output file')

    # Parse arguments
    args = parser.parse_args()
    settings_path, csv_path, txt_path = args.settings_path, args.csv_path, args.txt_path

    # Read JSON with settings
    print('\nReading settings file...')

    try:
        with open(settings_path, 'r', encoding='utf-8') as file:
            settings = json.load(file)
            original_date_format, column_settings = settings['original_date_format'], settings['columns']

            print(f"Settings: original_date_format={original_date_format} column_settings=")
            print(column_settings)
    except:
        print(f"Failed at reading the settings file: {settings_path}")
        return 1
    
    print('Done!\n')
    
    # Read CSV file
    print('Reading CSV file...')

    try:
        with open(csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            columns = reader.fieldnames

            print('Header: ')
            print(columns)
            print('Done!\n')

            # Write to TXT with fixed length
            print('Writing to TXT file...')

            try:
                with open(txt_path, 'w', encoding='utf-8') as txtfile:
                    for index, row in enumerate(reader, start=1):
                        formatted_row = []

                        for column in columns:
                            if column in column_settings:
                                current_column_settings = column_settings[column]

                                print(f"Parsing column: row={index}\ttype={current_column_settings['type']}\tlength={current_column_settings['length']}\tvalue={row[column]}")

                                if current_column_settings['type'] == 'date':
                                    formatted_date = format_date(row[column], original_date_format)
                                    formatted_row.append(pad_value(formatted_date, current_column_settings['length'], current_column_settings['type']))
                                else:
                                    formatted_row.append(pad_value(row[column], current_column_settings['length'], current_column_settings['type']))
                            else:
                                print(f"Failed at finding the column: {row[column]}")
                                return 1
                        
                        txtfile.write(''.join(formatted_row) + '\n')

                print('Done!\n')
                return 0

            except:
                print(f"Failed at writing the TXT file: {txt_path}")
                return 1
    except:
        print(f"Failed at reading the CSV file: {csv_path}")
        return 1

if __name__ == "__main__":
    main()
