def incorrectPasscodeAttempts(passcode, attempts):
    count = 0
    for attempt in attempts:
        if attempt != passcode:
            count += 1
            if count == 10:
                return True
        else:
            count = 0
    return False
