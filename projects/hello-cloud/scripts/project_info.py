from datetime import datetime

# Project information
project_name = "Hello Cloud"
author = "Cristofer"
aws_services = ["EC2", "S3", "IAM", "Nginx"]
date = datetime.now().strftime("%Y-%m-%d")

# Output file path
output_file = "../output/project_info.txt"

# File content
content = f"""
Project Name: {project_name}
Author: {author}
Date: {date}

AWS Services Used:
- {aws_services[0]}
- {aws_services[1]}
- {aws_services[2]}
- {aws_services[3]}
"""

# Write to file
with open(output_file, "w") as file:
    file.write(content)

print("project_info.txt created successfully.")
