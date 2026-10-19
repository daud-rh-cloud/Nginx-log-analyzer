nginx-log-analyzer
Small Python script that reads NGINX access logs and shows status codes, 5xx error rate, top IPs, top paths, total bytes and requests per hour. I made it to practice Python, OOP and Linux.

Written in Python 3 using only the built-in libraries.

3 ways to use it
One log file, report in the terminal:

python3 main.py access.log
One log file, report saved to a file:

python3 main.py access.log report.txt
A whole folder (works with rotated .gz logs too), one report per log file:

python3 main.py /var/log/nginx/ reports/
The reports folder has to exist first. On most systems you need to be in the adm group to read /var/log/nginx.

Example output
Status codes:
200               5
500               1
404               1
5xx Error rate: 20.00%

Top IPs:
192.0.2.10        4
203.0.113.7       3

Total Bytes Sent: 2718
How it works
Each line gets split on the " character first. A normal NGINX line gives 7 parts, so anything else is rejected. Doing it this way means user agents with spaces in them don't break the parsing. The timestamp is checked too, so a line with a broken time gets skipped instead of crashing the program.

Rejected lines are listed at the end of the report.

In folder mode, each report is named after the dates inside the log, for example analyzed.log..12-Oct-2026___16-Oct-2026. That way you can see which days a report covers from the name, and running it again on the same log doesn't make duplicates.

Files
main.py - starts everything, handles files, folders and gzip
Parsers.py - reads the lines and rejects bad ones
Models.py - LogEntry class, one parsed line
Analyzers.py - does the counting
Report.py - prints the report
Next
JSON output so other tools can read the results
Skip error.log files when reading a folder
Run it from cron and maybe send the numbers to Prometheus
