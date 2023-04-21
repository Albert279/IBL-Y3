def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("Valid IPv4 address")
    else:
        print("Invalid IPv4 address")


def validate(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True


if __name__ == "__main__":
    main()