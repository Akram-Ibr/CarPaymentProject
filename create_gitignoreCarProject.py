gitignore_content = """__pycache__/
*.pyc
.pytest_cache/
"""

with open(".gitignore", "w") as f:
    f.write(gitignore_content)

print(".gitignore created.")