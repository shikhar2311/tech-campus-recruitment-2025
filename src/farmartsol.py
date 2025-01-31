import sys
import os



# Ensure output directory exists

def extract_logs(date):
    output_file = os.path.join(OUTPUT_DIR, f"output_{date}.txt")
    
    with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as log_file, open(output_file, "w", encoding="utf-8") as out_file:
        for line in log_file:
            if line.startswith(date):
                out_file.write(line)
    
    print(f"Output for Logs {date} saved in {output_file}")

if __name__ == "__main__":
    LOG_FILE = "C:\\Users\\SHIKHAR\\Downloads\\logs_2024.log\\logs_2024.log"
    OUTPUT_DIR = "C:\\Users\\SHIKHAR\\Downloads\\logs_2024.log"

if len(sys.argv) > 1:
    date_arg = sys.argv[1]  # Get the argument
    extract_logs(date_arg)
else:
    print("Error: No date argument provided. Usage: python script.py YYYY-MM-DD")
    sys.exit(1)  # Exit the script
