import argparse
from datetime import datetime

class Task:
    def __init__(self, job_name, description, hourly_rate, start_time=None, finish_time=None, travel_time=0, discount=0):
        self.job_name = job_name
        self.description = description
        self.hourly_rate = hourly_rate
        self.start_time = start_time
        self.finish_time = finish_time
        self.travel_time = travel_time
        self.discount = discount
        self.notes = ""

    def add_notes(self, notes):
        self.notes += notes + "\n"

    def calculate_payment(self):
        if self.start_time is None or self.finish_time is None:
            return 0

        total_time = (self.finish_time - self.start_time).total_seconds() / 3600
        total_payment = total_time * self.hourly_rate

        total_payment += self.travel_time

        total_payment -= total_payment * (self.discount * 0.01)

        return total_payment

    def display_task_info(self):
        print(f"Job: {self.job_name}")
        print(f"Date and Time: {self.start_time.strftime('%d-%m-%Y T %H:%M')}")
        print(f"Description: {self.description}")
        print(f"Hourly Rate: ${self.hourly_rate}")
        print(f"Discount: {self.discount}%")
        print(f"Start Time: {self.start_time.strftime('%H:%M:%S')}")
        print(f"Finish Time: {self.finish_time.strftime('%H:%M:%S')}")
        print(f"Travel Time: {self.travel_time} hours")
        print(f"Notes:\n{self.notes}")
        print(f"Total Payment: ${self.calculate_payment():.2f}")

def main():
    parser = argparse.ArgumentParser(description="Task Logging CLI")
    parser.add_argument("job_name", type=str, help="Name of the job")
    parser.add_argument("description", type=str, help="Description of the job")
    parser.add_argument("hourly_rate", type=float, help="Hourly rate for the job")
    parser.add_argument("--start_time", type=str, help="Start time in 'YYYY-MM-DD HH:MM:SS' format")
    parser.add_argument("--finish_time", type=str, help="Finish time in 'YYYY-MM-DD HH:MM:SS' format")
    parser.add_argument("--travel_time", type=float, default=0, help="Travel time for the job")
    parser.add_argument("--discount", type=float, default=0, help="Discount percentage for the job")

    args = parser.parse_args()

    start_time = datetime.strptime(args.start_time, '%Y-%m-%d %H:%M:%S') if args.start_time else None
    finish_time = datetime.strptime(args.finish_time, '%Y-%m-%d %H:%M:%S') if args.finish_time else None

    task = Task(args.job_name, args.description, args.hourly_rate, start_time, finish_time, args.travel_time, args.discount)
    task.display_task_info()

if __name__ == "__main__":
    main()
