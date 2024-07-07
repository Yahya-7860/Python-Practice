import time
attempts = 1

timeTaken = 1

while attempts <= 5:
    print(f'Attemp {attempts} - time taken {timeTaken}')
    time.sleep(timeTaken)
    timeTaken *= 2
    attempts += 1
