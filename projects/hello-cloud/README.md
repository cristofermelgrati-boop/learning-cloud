# Hello Cloud (AWS) — EC2 + Nginx + S3 Static Website

## Overview
Hello Cloud is a hands-on AWS project to practice cloud fundamentals by deploying:
- A public web server on an EC2 instance running Nginx
- A static website hosted on Amazon S3

This project focuses on core concepts: networking, security groups, SSH access, and least-privilege permissions.

## Architecture
- **EC2 (Amazon Linux)**: Hosts a basic HTTP web page served by **Nginx**
- **Security Group**:
  - **Inbound 22 (SSH)**: allowed only from my public IP
  - **Inbound 80 (HTTP)**: open to the internet (0.0.0.0/0)
- **S3 Bucket (Static Website Hosting)**:
  - Hosts `index.html`
  - Public access is limited to `s3:GetObject` for website content

## What I implemented
1. Launched an EC2 instance in **eu-north-1 (Stockholm)**
2. Created and used an SSH key pair to connect securely to the instance
3. Installed and started **Nginx**
4. Updated the default Nginx page to display a custom “Hello Cloud – Cristofer” page
5. Created an S3 bucket and enabled **Static Website Hosting**
6. Uploaded `index.html` and validated the public website endpoint

## Security notes
- SSH access is restricted to **my IP only**
- The S3 bucket is configured to expose only the required static objects
- This project applies the **Principle of Least Privilege**

## How to verify
### EC2 website
Open the EC2 public IPv4 in a browser:
- `http://<EC2_PUBLIC_IP>`

### S3 static website
Open the S3 website endpoint:
- `http://<BUCKET_NAME>.s3-website.<REGION>.amazonaws.com`

## Next improvements (Roadmap)
- Add a custom HTML/CSS page and basic assets (images)
- Automate provisioning (IaC) with Terraform later
- Add CloudWatch monitoring / logs
- Put CloudFront in front of S3 for HTTPS + caching
