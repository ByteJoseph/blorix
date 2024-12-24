import os
import subprocess

def run_command(command):
    
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running: {command}\n{e.stderr.decode()}")


print("Installing dependencies using pip...")
run_command("pip install -r requirements.txt")

print("Installing dependencies using pip3...")
run_command("pip3 install -r requirements.txt")


instance_dir = "instance"
if not os.path.exists(instance_dir):
    print(f"Directory '{instance_dir}' does not exist. Initializing database...")
    os.makedirs(instance_dir)
    run_command("flask db init")
else:
    db_files = [file for file in os.listdir(instance_dir) if file.endswith(".db")]
    if not db_files:
        print(f"No database files found in '{instance_dir}'. Initializing database...")
        run_command("flask db init")


print("Running flask db migrate...")
run_command("flask db migrate")

print("Running flask db upgrade...")
run_command("flask db upgrade")
