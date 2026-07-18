There is an Apache-style access log at /app/access.log. Parse the log and write a JSON report to /app/report.json.

The report must be a JSON object with exactly these keys:
- "total_requests": the total number of non-empty log lines
- "unique_ips": the number of distinct client IP addresses
- "top_path": the request path that appears most often

Success criteria:
1. /app/report.json exists and contains valid JSON.
2. The report contains exactly the keys "total_requests", "unique_ips", and "top_path".
3. "total_requests" is 6.
4. "unique_ips" is 3.
5. "top_path" is "/index.html".

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.