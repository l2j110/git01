import calendar

html_cal = calendar.HTMLCalendar()

html_output = html_cal.formatmonth(2025, 10)

print(html_output)