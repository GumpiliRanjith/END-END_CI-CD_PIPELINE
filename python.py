import subprocess

result = subprocess.run(
    ["git","add","."]
)

print(result.stdout)
print(result.stderr)