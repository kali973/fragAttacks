import subprocess

result = subprocess.run(['pip', 'show', 'scapy'], capture_output=True, text=True)

output = result.stdout.strip()
for line in output.split('\n'):
    if line.startswith('Version:'):
        version = line.split(': ')[1]
        print(f"Scapy version: {version}")
        break
