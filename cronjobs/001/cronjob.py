from emailer import send_mail
from days_count import days_count
import sys

def cronjob(dry_run: bool):
    if dry_run == True:
        days = days_count()
        print("".join(days))

        print("I would have run! But i sure didnt")
        sys.exit()
    else:
        days = days_count()
        print(days)
        send_mail(days)


if __name__ == "__main__":
    cronjob(False)

