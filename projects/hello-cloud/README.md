Hello Cloud ☁️

Overview

Hello Cloud is a hands-on beginner project built to practice core AWS and cloud fundamentals through real infrastructure setup.

The project demonstrates how to deploy a simple web service using an EC2 instance with Nginx and how to host static content using Amazon S3.

This project is part of my learning path toward entry-level cloud and IT roles.

⸻

Architecture

The project uses the following components:
	•	Amazon EC2
	•	Linux instance (Free Tier eligible)
	•	Nginx web server
	•	Public HTTP access (port 80)
	•	SSH access restricted to my IP (port 22)
	•	Amazon S3
	•	Static website hosting enabled
	•	Public access limited to the required HTML object
	•	Used to store and serve static content
	•	IAM
	•	Used to manage permissions securely
	•	Public access controlled through bucket policies and Block Public Access settings

⸻

Project Structure

projects/hello-cloud/
├── README.md
├── PLAN.md
├── s3-static/
│   └── index.html
├── scripts/
│   └── project_info.py
└── output/
    └── project_info.txt   (generated file, not versioned)


⸻

What I Learned

Through this project, I practiced and understood:
	•	How to launch and secure an EC2 instance
	•	How security groups work (public vs restricted access)
	•	How to configure and run Nginx on Linux
	•	How static website hosting works in Amazon S3
	•	The difference between source code and generated output
	•	Basic Git workflow and repository organization

⸻

Python Script

The project_info.py script generates a text file with basic project metadata such as:
	•	Project name
	•	Author
	•	Date
	•	AWS services used

The generated file is placed in the output/ directory, which is intentionally excluded from version control using .gitignore.

⸻

Notes
	•	All resources were selected within the AWS Free Tier.
	•	This project focuses on understanding fundamentals rather than production readiness.
	•	The goal is learning by doing, not deploying a commercial application.

⸻

Author

Cristofer

Aspiring Cloud / IT professional
Currently building hands-on experience with AWS, Linux, Git, and Python.

⸻

