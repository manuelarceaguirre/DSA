"""
| Column          | Type    | Example Value         |
| --------------- | ------- | --------------------- |
| transaction\_id | string  | "T001"                |
| customer\_id    | string  | "C123"                |
| purchase\_date  | string  | "2025-05-01 09:15:00" |
| item            | string  | "  Socks   "          |
| quantity        | integer | 2                     |
| price           | double  | 9.99                  |
| coupon\_code    | string  | null / " SPRING2025"  |

Data Cleansing:
Trim whitespace from item and coupon_code columns.
Replace any null values in coupon_code with the string "NO_COUPON".
Remove duplicate rows (consider all columns for duplicates).
Data Enrichment:
Create a new column total_amount as quantity * price.
Create a new column purchase_date_ts as a proper timestamp type, converted from the string purchase_date.
"""
