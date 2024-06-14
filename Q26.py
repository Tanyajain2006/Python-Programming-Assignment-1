def prefix_suffix(string, prefix, suffix):
    print(f"The string {string} starts with prefix {prefix} : {string.startswith(prefix)}")
    print(f"The string {string} ends with suffix {suffix} : {string.endswith(suffix)}")

str = input("Enter the string: ")
pre = input("Enter prefix: ")
suf = input("Enter suffix: ")
prefix_suffix(str, pre, suf)