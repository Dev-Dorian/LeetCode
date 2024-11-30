def reorderLogFiles(logs):
    digit_logs = []
    letter_logs = []
    for log in logs:
        if log[-1].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)
    letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    result = letter_logs + digit_logs
    return result


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
print(reorderLogFiles(logs))


log = "sdss 2 2 4 g7"
print(log[-2], log[-1].isdigit())
