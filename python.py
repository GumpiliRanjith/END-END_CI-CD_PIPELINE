import subprocess

result = subprocess.run(
    ["git","push","origin","main"]
)

print(result.stdout)
print(result.stderr)