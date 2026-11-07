import subprocess

commands = [
    ["git", "add", "."],
    ["git", "commit", "-m", "ben10"],
    ["git", "push", "origin", "main"]
] 

for cmd in commands:
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=False
    )
print(result.stdout)
print(result.stderr)
print("hello world")