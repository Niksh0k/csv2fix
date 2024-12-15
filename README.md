# CSV2Fix - The Ultimate Fixed-Length Converter

## English

This program converts a CSV file to a fixed-length TXT file. It uses a settings file written in JSON, which contains the structure of the CSV file and the desired output formatting.

**Usage:**

> python fixed_width_converter.py SETTINGS_PATH CSV_PATH OUTPUT_PATH

- SETTINGS_PATH - path to a settings file
- CSV_PATH - path to a CSV file
- OUTPUT_PATH - path to an output TXT file

**The settings file**

- original_date_format - date format
- columns - column settings
  - length - fixed length
  - type:
    - 'full' = full-width
    - 'half' = half-width
    - 'date' = date
    - 'digits' = half-width digits


## 日本語

このプログラムはCSVファイルを固定長のTXTファイルに変換できる。JSONで書かれた設定ファイルを使用し、その中にはCSVファイルの構造と望ましい出力フォーマットが含まれている。

**使い方**

> python fixed_width_converter.py SETTINGS_PATH CSV_PATH OUTPUT_PATH

- SETTINGS_PATH - 設定ファイルのパス
- CSV_PATH - CSVファイルのパス
- OUTPUT_PATH - 出力ファイルのパス

**設定ファイル**

- original_date_format - 日付のフォーマット
- columns - カラムの設定
  - length - 固定長
  - type:
    - 'full' = 全角
    - 'half' = 半角
    - 'date' = 日付
    - 'digits' = 半角数字
