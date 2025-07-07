from datetime import datetime, timedelta
import time
import re
import pytz

# Age Calculator
def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (birthdate.replace(year=today.year, month=today.month) - timedelta(days=today.day)).day

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Days Until Next Birthday
def days_until_birthday(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()
    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    return (next_birthday - today).days

# Meeting Scheduler
def schedule_meeting(current_dt_str, duration_hours, duration_minutes):
    current_dt = datetime.strptime(current_dt_str, "%Y-%m-%d %H:%M")
    end_time = current_dt + timedelta(hours=duration_hours, minutes=duration_minutes)
    return end_time

# Timezone Converter
def convert_timezone(date_time_str, from_tz_str, to_tz_str):
    from_tz = pytz.timezone(from_tz_str)
    to_tz = pytz.timezone(to_tz_str)
    naive_dt = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
    from_dt = from_tz.localize(naive_dt)
    to_dt = from_dt.astimezone(to_tz)
    return to_dt

# Countdown Timer
def countdown_timer(future_dt_str):
    future_dt = datetime.strptime(future_dt_str, "%Y-%m-%d %H:%M:%S")
    while True:
        now = datetime.now()
        if now >= future_dt:
            print("Time's up!")
            break
        remaining = future_dt - now
        print(f"Time remaining: {remaining}", end="\r")
        time.sleep(1)

# Email Validator
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return re.match(pattern, email) is not None

# Phone Number Formatter
def format_phone_number(phone_number):
    cleaned = re.sub(r'\D', '', phone_number)
    if len(cleaned) == 10:
        return f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"
    else:
        return "Invalid phone number"

# Password Strength Checker
def check_password_strength(password):
    length = len(password) >= 8
    upper = re.search(r'[A-Z]', password)
    lower = re.search(r'[a-z]', password)
    digit = re.search(r'\d', password)
    return all([length, upper, lower, digit])

# Word Finder
def find_word_occurrences(word, text):
    pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
    return pattern.findall(text)

# Date Extractor
def extract_dates(text):
    pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    return re.findall(pattern, text)

# Example usage
if __name__ == "__main__":
    # Age
    print("Age:", calculate_age("2000-05-15"))

    # Days until birthday
    print("Days until next birthday:", days_until_birthday("2000-05-15"))

    # Meeting scheduler
    print("Meeting ends at:", schedule_meeting("2025-07-07 10:00", 2, 30))

    # Timezone converter
    print("Converted time:", convert_timezone("2025-07-07 10:00", "Asia/Tashkent", "Europe/London"))

    # Email validation
    print("Valid email:", is_valid_email("example@mail.com"))

    # Phone number formatting
    print("Formatted number:", format_phone_number("1234567890"))

    # Password strength
    print("Password strength:", check_password_strength("StrongPass1"))

    # Word finder
    sample_text = "This is a test. This test is simple."
    print("Occurrences of 'test':", find_word_occurrences("test", sample_text))

    # Date extractor
    text_with_dates = "Important dates: 2025-07-07, 1999-12-31."
    print("Extracted dates:", extract_dates(text_with_dates))
