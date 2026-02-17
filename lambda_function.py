def lambda_handler(event, context):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manmadh Kumar Reddy | Profile</title>
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
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

        /* Profile Image */
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

        /* Title under name */
        .title {
            font-size: 1.3em;
            color: var(--secondary-color);
            font-weight: 600;
            margin-bottom: 25px;
            font-family: 'Poppins', sans-serif;
        }

        /* Scrolling skills */
        .scrolling-skills {
            overflow: hidden;
            white-space: nowrap;
            border-top: 2px solid var(--primary-color);
            border-bottom: 2px solid var(--primary-color);
            background: #F0F2F5;
            color: var(--primary-color);
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
        @keyframes scrollLeft { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }

        /* Main content sections */
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

        /* Skills list */
        .skills-list {
            list-style-type: none;
            padding-left: 0;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 15px;
        }
        
        .skills-list li {
            margin-bottom: 12px;
            font-size: 1.1em;
            padding: 10px 15px;
            background-color: rgba(215, 204, 200, 0.1);
            border-radius: 6px;
            transition: all 0.3s ease;
        }
        
        .skills-list li:hover {
            background-color: rgba(141, 110, 99, 0.1);
            transform: translateX(5px);
        }
        
        .skills-list strong {
            color: var(--primary-color);
            font-family: 'Poppins', sans-serif;
        }

        /* Skills bars */
        .skill-container { 
            margin-bottom: 15px; 
        }
        
        .skill-label { 
            margin-bottom: 5px; 
            font-weight: 600; 
            color: var(--primary-color);
            font-family: 'Poppins', sans-serif;
        }
        
        .skill-bar { 
            background: var(--light-color); 
            border-radius: 10px; 
            overflow: hidden; 
            height: 12px; 
        }
        
        .skill-level { 
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color)); 
            height: 100%; 
            text-align: right; 
            padding-right: 10px; 
            color: var(--text-light); 
            font-weight: bold; 
            font-size: 0.8em;
            line-height: 12px;
        }

        /* Footer */
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

        /* Responsive */
        @media (max-width: 768px) {
            .profile-img { 
                width: 90%; 
                height: auto;
                max-height: 200px;
            }
            
            h1 { font-size: 2em; }
            
            .scrolling-skills { 
                font-size: 0.9em; 
                padding: 8px 0;
            }
            
            .skills-list {
                grid-template-columns: 1fr;
            }
            
            section {
                padding: 20px 0;
            }
            
            .contact a {
                margin: 0 10px;
                font-size: 1.5em;
            }
        }
        
        @media (max-width: 480px) {
            h1 { font-size: 1.8em; }
            
            .title {
                font-size: 1.1em;
            }
            
            .profile-img {
                border-width: 3px;
            }
        }
        /* Jump animation for icons */
            .jump {
            display: inline-block;
            animation: jump 2s ease-in-out infinite;
            }

        @keyframes jump {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-6px); }
            }

        .jump:nth-of-type(1) { animation-delay: 0s; }
        .jump:nth-of-type(2) { animation-delay: 0.2s; }
        .jump:nth-of-type(3) { animation-delay: 0.4s; }
        .jump:nth-of-type(4) { animation-delay: 0.6s; }
        .jump:nth-of-type(5) { animation-delay: 0.8s; }
        .jump:nth-of-type(6) { animation-delay: 1s; }
        .jump:nth-of-type(7) { animation-delay: 1.2s; }
        .jump:nth-of-type(8) { animation-delay: 1.4s; }

        .title i {
    font-size: 1.3em;
    vertical-align: middle;
    margin-right: 5px;
}

.n8n-icon {
    width: 20px;
    vertical-align: middle;
    margin-right: 5px;
}

.aws-icon {
    width: 28px;
    vertical-align: middle;
    margin-right: 6px;
}

.icon-img {
    width: 22px;
    vertical-align: middle;
    margin-right: 6px;
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
    <i class="devicon-linux-plain colored jump"></i> Linux &nbsp; | &nbsp;
    <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" class="jump aws-icon"> AWS | &nbsp;
    <img src="https://cdn-icons-png.flaticon.com/512/2721/2721291.png" class="jump icon-img"> DevOps  &nbsp; | &nbsp;
    <img src="https://cdn-icons-png.flaticon.com/512/2913/2913465.png" class="jump icon-img"> SRE &nbsp; | &nbsp;
    <img src="https://cdn-icons-png.flaticon.com/512/3063/3063822.png" class="jump icon-img"> Automation &nbsp; | &nbsp;
    <img src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png" class="jump icon-img"> Monitoring &nbsp; | &nbsp;
    <img src="https://cdn-icons-png.flaticon.com/512/3212/3212608.png" class="jump icon-img"> Networking &nbsp; | &nbsp;
    <img src="https://avatars.githubusercontent.com/u/45487711?s=200&v=4" class="jump n8n-icon"> n8n
            </div>



    <div class="scrolling-skills">
        <span>
            <i class="devicon-linux-plain colored"></i> Linux⚡ 
            <i class="devicon-amazonwebservices-original colored"></i> AWS ⚡ 
            <i class="fas fa-code-branch"></i> CI/CD ⚡ 
            <i class="fas fa-robot"></i> Automation ⚡ 
            <i class="fas fa-chart-line"></i> Monitoring ⚡ 
            <i class="devicon-docker-plain colored"></i> Docker ⚡ 
            <i class="devicon-kubernetes-plain colored"></i> Kubernetes ⚡ 
            <i class="devicon-terraform-plain colored"></i> Terraform ⚡ 
            <i class="devicon-n8n-plain colored"></i> n8n ⚡
            <i class="devicon-githubactions-plain colored"></i> GitHub Actions ⚡
            <i class="fas fa-network-wired"></i> Networking ⚡ 

        </span>
    </div>
    <main>
        <section id="about">
            <h2>About Me</h2>
            <p>I am a Cloud & DevOps Engineer with strong hands-on experience in Linux system administration, AWS cloud services, CI/CD pipeline implementation, infrastructure engineering, SRE practices, automation, and monitoring.

I have extensive experience managing and maintaining large-scale environments (1000+ servers) across both on-premises and cloud infrastructures, ensuring high availability, performance optimization, and operational excellence.

This portfolio is architected using AWS Lambda, API Gateway, and Route 53, demonstrating my expertise in serverless and scalable cloud-native architectures.</p>
        </section>

        <section id="skills">
            <h2>💡 Skills</h2>
            <ul class="skills-list">
                <li><strong>Operating Systems:</strong> Linux (Suse, Ubuntu, Amazon Linux)</li>
                <li><strong>Cloud Platforms:</strong> AWS (EC2, S3, IAM, VPC, EBS), OpenStack (Nova)</li>
                <li><strong>Automation & IaC:</strong> Bash Scripting, Terraform, N8N </li>
                <li><strong>Containers:</strong> Docker, Kubernetes</li>
                <li><strong>Infrastructure & Ops:</strong> Server Provisioning, Capacity Planning, Scaling, Backup & Recovery</li>
                <li><strong>Networking:</strong> TCP/IP, DNS, Subnetting, LAN/WAN</li>
                <li><strong>Monitoring & Support:</strong> Incident Management, RCA, SLA Support, Preventive Maintenance</li>
                <li><strong>Databases & Storage:</strong> Storage Expansion, Database Migration</li>
                <li><strong>Methodologies:</strong> Production Support, High Availability, Disaster Recovery</li>
            </ul>
        </section>

        <section id="projects">
            <h2>📂 Projects</h2>
            <div class="project">
                <h3>Serverless DevOps Portfolio</h3>
                <p>AWS Lambda + API Gateway + S3 + Route 53 based serverless portfolio.</p>
            </div>
            <div class="project">
                <h3>CI/CD Automation</h3>
                <p>Jenkins pipelines integrating GitHub, Docker, EC2, and automated deployments.</p>
            </div>
            <div class="project">
                <h3>Monitoring Stack</h3>
                <p>Prometheus, Grafana dashboards with alerts and performance monitoring.</p>
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