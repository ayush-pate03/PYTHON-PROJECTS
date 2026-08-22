import time

print("================================")
print("       COUNTDOWN TIMER")
print("================================")

# Take time from user
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# Convert everything to seconds
total_seconds = minutes * 60 + seconds

# Countdown
while total_seconds >= 0:

    minutes_left = total_seconds // 60
    seconds_left = total_seconds % 60

    # Display timer
    print(
        f"\rTime Remaining: {minutes_left:02d}:{seconds_left:02d}",
        end=""
    )

    # Wait for 1 second
    time.sleep(1)

    # Reduce time
    total_seconds -= 1

# Timer finished
print("\n\n⏰ TIME'S UP!")
print("Countdown completed.")