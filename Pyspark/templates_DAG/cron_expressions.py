"""
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 6) (Sunday=0)
│ │ │ │ │
│ │ │ │ │
* * * * *

| Schedule                      | Cron Expression | Meaning                            |
| ----------------------------- | --------------- | ---------------------------------- |
| Every minute                  | `* * * * *`     | Runs every minute                  |
| Every 5 minutes               | `*/5 * * * *`   | Every 5 minutes                    |
| Every hour                    | `0 * * * *`     | At the top of every hour           |
| Every day at midnight         | `0 0 * * *`     | At 00:00 every day                 |
| Every day at 6 AM             | `0 6 * * *`     | At 06:00 every day                 |
| Every Sunday at 5 PM          | `0 17 * * 0`    | At 17:00 every Sunday              |
| Every Monday at 9 AM          | `0 9 * * 1`     | At 09:00 every Monday              |
| 1st of month at 3 AM          | `0 3 1 * *`     | On the 1st of every month at 03:00 |
| Weekdays at 8 AM              | `0 8 * * 1-5`   | At 08:00 Mon–Fri                   |
| Every 15th and 30th           | `0 0 15,30 * *` | At midnight on the 15th and 30th   |
| Every 10th minute in 6th hour | `*/10 6 * * *`  | Every 10 minutes between 6:00–6:59 |
"""


