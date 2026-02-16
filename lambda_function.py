def lambda_handler(event, context):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manmadh Kumar Reddy | Profile</title>

    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Devicon CDN (ONLY ADDITION) -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">

    <style>
        :root {
            --primary-color: #2B1B17;
            --secondary-color: #5D4037;
            --accent-color: #8D6E63;
            --background-color: #F5F5F5;
            --light-color: #D7CCC8;
            --text-dark: #2B1B17;
            --text-light: #FFF;
        }
        
        body {
            font-family: 'Open Sans', sans-serif;
            background-color: var(--background-color);
            color: var(--text-dark);
            margin: 0;
            padding: 0;
            text-align: center;
            line-height: 1.6;
        }
        
        header {
            padding: 30px 20px;
            background-color: var(--background-color);
            border-bottom: 3px solid var(--primary-color);
        }
        
        h1 { 
            margin: 8px 0; 
            font-size: 2.5em; 
            color: var(--primary-color);
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        
        h2 {
            color: var(--primary-color);
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            border-bottom: 2px solid var(--light-color);
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        
        h3 {
            color: var(--secondary-color);
            font-family: 'Poppins', sans-serif;
            font-weight: 500;
        }
        
        p { 
            margin: 4px 0 15px 0;
            font-size: 1.1em; 
            color: var(--secondary-color);
            font-family: 'Open Sans', sans-serif;
            line-height: 1.7;
        }

        .profile-img {
            width: 300px;          
            height: 250px;         
            object-fit: cover;     
            border-radius: 10px;   
            border: 4px solid var(--primary-color);
            display: block;
            margin: 0 auto 20px auto;
            box-shadow: 0 5px 15px rgba(43, 27, 23, 0.1);
        }

        .title {
            font-size: 1.3em;
            color: var(--secondary-color);
            font-weight: 600;
            margin-bottom: 25px;
            font-family: 'Poppins', sans-serif;
        }

        .scrolling-skills {
            overflow: hidden;
            white-space: nowrap;
            border-top: 2px solid var(--primary-color);
            border-bottom: 2px solid var(--primary-color);
            background: var(--primary-color);
            color: var(--light-color);
            font-weight: 600;
            padding: 12px 0;
            font-size: 1.1em;
            font-family: 'Poppins', sans-serif;
        }

        .scrolling-skills span {
            display: inline-block;
            padding-left: 100%;
            animation: scrollLeft 20s linear infinite;
        }

        @keyframes scrollLeft { 
            0% { transform: translateX(0); } 
            100% { transform: translateX(-100%); } 
        }

        main {
            max-width: 1000px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        section { 
            padding: 30px 0;  
            text-align: left; 
            border-bottom: 1px solid var(--light-color);
        }
        
        section:last-child {
            border-bottom: none;
        }
        
        .project { 
            margin-bottom: 20px; 
            padding: 15px;
            background-color: rgba(215, 204, 200, 0.1);
            border-radius: 8px;
            border-left: 4px solid var(--accent-color);
        }
        
        .contact a { 
            color: var(--primary-color); 
            margin: 0 15px; 
            font-size: 1.8em; 
            text-decoration: none;
            transition: all 0.3s ease;
            display: inline-block;
        }
        
        .contact a:hover {
            color: var(--accent-color);
            transform: translateY(-3px);
        }

        footer { 
            padding: 25px 15px; 
            background-color: var(--primary-color); 
            color: var(--light-color); 
            text-align: center; 
            margin-top: 40px;
            font-family: 'Poppins', sans-serif;
        }

        footer p {
            color: var(--light-color);
            margin: 0;
        }
    </style>
</head>

<body>
<header>
    <h1>🚀 Manmadh Kumar Reddy</h1>

    <img src="https://manmadhreddy.s3.us-east-1.amazonaws.com/Profile_Pic4.jpg"
         alt="Manmadh Kumar Reddy"
         class="profile-img">

    <div class="title">
        <i class="devicon-linux-plain colored"></i> Linux &nbsp; | &nbsp;
        <i class="devicon-amazonwebservices-original colored"></i> AWS &nbsp; | &nbsp;
        <i class="fas fa-infinity"></i> DevOps Engineer &nbsp; | &nbsp;
        <i class="fas fa-shield-alt"></i> SRE &nbsp; | &nbsp;
        <i class="fas fa-robot"></i> Automation &nbsp; | &nbsp;
        <i class="fas fa-chart-line"></i> Monitoring &nbsp; | &nbsp;
        <i class="fas fa-network-wired"></i> Networking &nbsp; | &nbsp;
        <i class="devicon-n8n-plain colored"></i> n8n
    </div>

    <div class="scrolling-skills">
        <span>
            <i class="devicon-linux-plain colored"></i> Linux⚡ 
            <i class="devicon-amazonwebservices-original colored"></i> AWS ⚡ 
            <i class="devicon-githubactions-plain colored"></i> CI/CD ⚡ 
            <i class="devicon-ansible-plain colored"></i> Automation ⚡ 
            <i class="devicon-grafana-original colored"></i> Monitoring ⚡ 
            <i class="devicon-docker-plain colored"></i> Docker ⚡ 
            <i class="devicon-kubernetes-plain colored"></i> Kubernetes ⚡ 
            <i class="devicon-terraform-plain colored"></i> Terraform ⚡ 
            <i class="devicon-n8n-plain colored"></i> n8n ⚡
            <i class="devicon-githubactions-plain colored"></i> GitHub Actions ⚡
            <i class="devicon-nginx-original colored"></i> Networking ⚡
        </span>
    </div>
</header>

<main>

<section id="about">
    <h2>About Me</h2>
    <p>I am a Cloud and DevOps Engineer with strong hands-on experience in Linux system administration,
    AWS cloud services, CI/CD pipelines, infrastructure engineering, SRE practices,
    automation, and monitoring. This portfolio is built using AWS Lambda + API Gateway + Route 53.</p>
</section>

<section id="skills">
    <h2>💡 Skills</h2>
    <ul class="skills-list">
        <li><strong>Operating Systems:</strong> Linux (Suse, Ubuntu, Amazon Linux)</li>
        <li><strong>Cloud Platforms:</strong> AWS (EC2, S3, IAM, VPC, EBS), OpenStack (Nova)</li>
        <li><strong>Automation & IaC:</strong> Bash Scripting, Terraform, N8N</li>
        <li><strong>Containers:</strong> Docker, Kubernetes</li>
        <li><strong>Infrastructure & Ops:</strong> Server Provisioning, Capacity Planning, Scaling</li>
        <li><strong>Networking:</strong> TCP/IP, DNS, Subnetting, LAN/WAN</li>
        <li><strong>Monitoring & Support:</strong> Incident Management, RCA, SLA Support</li>
        <li><strong>Databases & Storage:</strong> Storage Expansion, Database Migration</li>
        <li><strong>Methodologies:</strong> High Availability, Disaster Recovery</li>
    </ul>
</section>

<section id="projects">
    <h2>📂 Projects</h2>
    <div class="project">
        <h3>Serverless DevOps Portfolio</h3>
        <p>AWS Lambda + API Gateway + S3 + Route 53 based serverless portfolio.</p>
    </div>
</section>

<section id="contact">
    <h2>📫 Contact Me</h2>
    <div class="contact">
        <a href="mailto:reddy.manmadh@gmail.com" title="Email"><i class="fas fa-envelope"></i></a>
        <a href="https://www.linkedin.com/in/manmadh-reddy-89b35017" target="_blank" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/manmadhdevops" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
    </div>
</section>

</main>

<footer>
    <p>© 2026 Manmadh Kumar Reddy 🚀</p>
</footer>

</body>
</html>
"""
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html; charset=UTF-8"},
        "body": html
    }
