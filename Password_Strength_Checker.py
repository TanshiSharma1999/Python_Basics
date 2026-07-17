
def length_check(password):
    return len(password) >= 8


def upper_check(password):
    return any(ch.isupper() for ch in password)


def lower_check(password):
    return any(ch.islower() for ch in password)


def digit_check(password):
    return any(ch.isdigit() for ch in password)


def special_check(password):
    special = "!@#$%^&*()_+-=?.,"
    return any(ch in special for ch in password)
        
# ---------------- MAIN ----------------
password=input("Enter your password: ")
has_length = length_check(password)
has_upper = upper_check(password)
has_lower = lower_check(password)
has_digit = digit_check(password)
has_special = special_check(password)
score=0
if has_length:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1  

print("\n------ Password Report ------")

if score == 5:
    print("✅ Strong Password")
elif score >= 3:
    print("🟡 Medium Password")
else:
    print("🔴 Weak Password")

print("\nChecklist")

print(f"Length (8+)      : {'✔' if has_length else '✘'}")
print(f"Uppercase Letter : {'✔' if has_upper else '✘'}")
print(f"Lowercase Letter : {'✔' if has_lower else '✘'}")
print(f"Digit            : {'✔' if has_digit else '✘'}")
print(f"Special Character: {'✔' if has_special else '✘'}")

if score != 5:
    print("\nMissing:")

    if not has_length:
        print("- Password should contain at least 8 characters.")

    if not has_upper:
        print("- At least one uppercase letter.")

    if not has_lower:
        print("- At least one lowercase letter.")

    if not has_digit:
        print("- At least one digit.")

    if not has_special:
        print("- At least one special character.")