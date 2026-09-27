requirements_content = """flask
requests
pytest
"""

with open("requirements.txt", "w") as f:
    f.write(requirements_content)

print("requirements.txt created.")