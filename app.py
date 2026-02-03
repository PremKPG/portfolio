from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        "name": "Prem Panjala",
        "role": "Certified Cloud Support Engineer",
        "experience": "1.5+ Years in Azure",
        "degree": "MSc in Computing",
        "skills": [
            {"category": "Cloud", "list": ["Azure(VMs, Storage, Virtual Desktop, Azure AD/Entra ID)", "AWS(EC2, S3, RDS)"]},
            {"category": "DevOps", "list": ["Terraform", "Docker", "Kubernetes", "Git", "CI/CD", "GithubActions"]},
            {"category": "Networking", "list": ["VNets", "DNS", "Firewalls", "Load Balancers", "TCP/IP", "VPNs"]},
            {"category": "Scripting", "list": ["Python", "Bash"]}
        ],
        "certifications": [
            {"name": "AZ-900", "title": "Azure Fundamentals"},
            {"name": "SC-900", "title": "Security, Compliance, and Identity Fundamentals"}
        ],
    }
    return render_template('index.html', **context)

@app.route('/health')
def health():
    return jsonify({"status": "up", "environment": os.getenv('FLASK_ENV', 'production')})

if __name__ == '__main__':
    app.run(debug=True)