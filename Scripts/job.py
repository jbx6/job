import argparse
import os
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
        print()
        print(f"Description: {self.description}")
        print()
        print(f"Hourly Rate: ${self.hourly_rate}")
        print(f"Discount: {self.discount}%")
        print()
        print(f"Start Time: {self.start_time.strftime('%H:%M:%S')}")
        print(f"Finish Time: {self.finish_time.strftime('%H:%M:%S')}")
        print(f"Travel Time: {self.travel_time} hours")
        print()
        print(f"Notes:\n{self.notes}")
        print(f"Total Payment: ${self.calculate_payment():.2f}")

    def save_to_file(self, directory):
        filename = os.path.join(directory, f"{self.job_name}.txt")

        # Check if a file with the same name already exists
        if os.path.exists(filename):
            # If yes, append the date to the filename
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = os.path.join(directory, f"{self.job_name}_{timestamp}.txt")

        with open(filename, 'w') as file:
            file.write(f"Job: {self.job_name}\n")
            file.write(f"Date and Time: {self.start_time.strftime('%d-%m-%Y T %H:%M')}\n")
            file.write(f"Description: {self.description}\n")
            file.write(f"Hourly Rate: ${self.hourly_rate}\n")
            file.write(f"Discount: {self.discount}%\n")
            file.write(f"Start Time: {self.start_time.strftime('%H:%M:%S')}\n")
            file.write(f"Finish Time: {self.finish_time.strftime('%H:%M:%S')}\n")
            file.write(f"Travel Time: {self.travel_time} hours\n")
            file.write(f"Notes:\n{self.notes}\n")
            file.write(f"Total Payment: ${self.calculate_payment():.2f}\n")

        print(f"Task information saved to {filename}")

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

    # Specify the directory in the root directory (adjust the folder name as needed)
    root_directory = os.path.expanduser("~/Desktop/Jobs")  # You can change this to any directory you prefer
    logs_directory = os.path.join(root_directory, "Logs")

    # Create the directory if it doesn't exist
    os.makedirs(logs_directory, exist_ok=True)

    # Save the task information to a file
    task.save_to_file(logs_directory)

if __name__ == "__main__":
    main()
