from time import time as t
from datetime import date as d

ts = t()

print(f"Seconds since January 1, 1970: {ts:,.4f} or {ts:.2e} in scientific notation")
print(f"{d.fromtimestamp(ts):%b %d %Y}")
