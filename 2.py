with open('requirements.txt', 'r') as file:
    lines = file.readlines()

# Filter out lines that contain 'file://'
cleaned_lines = [line for line in lines if 'file://' not in line]

with open('cleaned_requirements.txt', 'w') as file:
    file.writelines(cleaned_lines)

print("Cleaned requirements.txt saved as 'cleaned_requirements.txt'")
