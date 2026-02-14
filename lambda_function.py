def lambda_handler(event, context):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Manmadh Kumar Reddy | DevOps Portfolio</title>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">

<style>
:root {
    --primary-color: #2B1B17;
    --secondary-color: #5D4037;
    --accent-color: #8D6E63;
    --background-color: #F5F5F5;
    --light-color: #D7CCC8;
    --text-light: #FFF;
}

body {
    font-family: 'Open Sans', sans-serif;
    margin:0;
    background: linear-gradient(-45deg, #F5F5F5, #EDE7E3, #F5F5F5);
    background-size:400% 400%;
    animation:bgMove 15s ease infinite;
    color: var(--primary-color);
    overflow-x:hidden;
}

@keyframes bgMove {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* Floating soft shapes */
body::before, body::after {
    content:"";
    position:fixed;
    width:400px;
    height:400px;
    border-radius:50%;
    background: radial-gradient(circle, rgba(141,110,99,0.15), transparent);
    z-index:-1;
    animation:floatShape 12s ease-in-out infinite;
}
body::before{top:-150px;left:-150px;}
body::after{bottom:-150px;right:-150px;animation-delay:6s;}

@keyframes floatShape {
    0%,100%{transform:translateY(0px);}
    50%{transform:translateY(40px);}
}

/* Header */
header {
    text-align:center;
    padding:50px 20px;
    border-bottom:3px solid var(--primary-color);
}

h1 {
    font-family:'Poppins', sans-serif;
    font-size:2.7em;
    position:relative;
}

h1::after {
    content:"";
    width:60%;
    height:4px;
    background:var(--accent-color);
    position:absolute;
    left:20%;
    bottom:-10px;
    border-radius:5px;
    animation:pulse 2s infinite;
}

@keyframes pulse {
    0%,100%{opacity:0.5;}
    50%{opacity:1;}
}

.profile-img {
    width:300px;
    height:250px;
    object-fit:cover;
    border-radius:15px;
    border:4px solid var(--primary-color);
    margin:30px auto;
    box-shadow:0 15px 30px rgba(0,0,0,0.15);
    transition:0.4s;
}
.profile-img:hover { transform:scale(1.05); }

.title {
    font-family:'Poppins', sans-serif;
    font-weight:600;
    margin-bottom:25px;
}

.scrolling-skills {
    background:var(--primary-color);
    color:var(--light-color);
    padding:12px 0;
    overflow:hidden;
    white-space:nowrap;
}
.scrolling-skills span {
    display:inline-block;
    padding-left:100%;
    animation:scroll 20s linear infinite;
}
@keyframes scroll {
    0%{transform:translateX(0);}
    100%{transform:translateX(-100%);}
}

main {
    max-width:1000px;
    margin:auto;
    padding:20px;
}

section {
    padding:40px 0;
    border-bottom:1px solid var(--light-color);
    opacity:0;
    transform:translateY(30px);
    animation:fadeUp 0.8s ease forwards;
}
section:nth-child(1){animation-delay:0.2s;}
section:nth-child(2){animation-delay:0.4s;}
section:nth-child(3){animation-delay:0.6s;}
section:nth-child(4){animation-delay:0.8s;}

@keyframes fadeUp {
    to{opacity:1;transform:translateY(0);}
}

h2 {
    font-family:'Poppins', sans-serif;
    border-bottom:2px solid var(--light-color);
    padding-bottom:10px;
}

/* Projects glass cards */
.project {
    background:rgba(255,255,255,0.6);
    backdrop-filter:blur(10px);
    padding:20px;
    margin-bottom:20px;
    border-radius:12px;
    border-left:4px solid var(--accent-color);
    transition:0.3s;
}
.project:hover {
    transform:translateY(-6px);
    box-shadow:0 15px 35px rgba(0,0,0,0.1);
}

/* Skills list */
.skills-list {
    list-style:none;
    padding:0;
}
.skills-list li {
    padding:12px 15px;
    margin-bottom:12px;
    background:rgba(215,204,200,0.2);
    border-radius:8px;
    transition:0.3s;
}
.skills-list li:hover {
    transform:translateX(6px);
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
}

/* Contact */
.contact a {
    font-size:2em;
    margin:0 15px;
    color:var(--primary-color);
    transition:0.3s;
}
.contact a:hover {
    color:var(--accent-color);
    transform:scale(1.2);
}

/* Footer */
footer {
    background:var(--primary-color);
    color:var(--light-color);
    text-align:center;
    padding:25px;
    margin-top:40px;
}
</style>
</head>

<body>

<header>
<h1>🚀 Manmadh Kumar Reddy</h1>

<img src="https://manmadhreddy.s3.us-east-1.amazonaws.com/Profile_Pic4.jpg"
class="profile-img">

<div class="title">
<i class="fab fa-linux"></i> Linux |
<i class="fab fa-aws"></i> AWS |
<i class="fas fa-network-wired"></i> Networking |
<i class="fas fa-infinity"></i> DevOps |
<i class="fas fa-robot"></i> Automation |
<i class="fas fa-chart-line"></i> Monitoring |
<i class="fas fa-project-diagram"></i> n8n
</div>

<div class="scrolling-skills">
<span>
Linux ⚡ AWS ⚡ CI/CD ⚡ Docker ⚡ Kubernetes ⚡ Terraform ⚡ GitHub Actions ⚡ Networking ⚡ Monitoring ⚡ Automation ⚡
</span>
</div>
</header>

<main>

<section>
<h2>About Me</h2>
<p>I am a Cloud and DevOps Engineer with strong hands-on experience in Linux administration,
AWS cloud services, CI/CD pipelines, infrastructure engineering, SRE practices,
automation, and monitoring. This portfolio is built using AWS Lambda.</p>
</section>

<section>
<h2>💡 Skills</h2>
<ul class="skills-list">
<li><strong>Operating Systems:</strong> Linux (Suse, Ubuntu, Amazon Linux)</li>
<li><strong>Cloud Platforms:</strong> AWS (EC2, S3, IAM, VPC, EBS)</li>
<li><strong>Automation & IaC:</strong> Bash, Terraform, n8n</li>
<li><strong>Containers:</strong> Docker, Kubernetes</li>
<li><strong>Networking:</strong> TCP/IP, DNS, Subnetting</li>
<li><strong>Monitoring:</strong> Prometheus, Grafana</li>
</ul>
</section>

<section>
<h2>📂 Projects</h2>

<div class="project">
<h3>Serverless DevOps Portfolio</h3>
<p>AWS Lambda + API Gateway + S3 + Route 53 based serverless portfolio.</p>
</div>

<div class="project">
<h3>CI/CD Automation</h3>
<p>Jenkins pipelines integrating GitHub, Docker, EC2 deployments.</p>
</div>

<div class="project">
<h3>Monitoring Stack</h3>
<p>Prometheus + Grafana dashboards with alerting and SLA monitoring.</p>
</div>

</section>

<section>
<h2>📫 Contact Me</h2>
<div class="contact">
<a href="mailto:reddy.manmadh@gmail.com"><i class="fas fa-envelope"></i></a>
<a href="https://linkedin.com" target="_blank"><i class="fab fa-linkedin"></i></a>
<a href="https://github.com/manmadhdevops" target="_blank"><i class="fab fa-github"></i></a>
</div>
</section>

</main>

<footer>
© 2026 Manmadh Kumar Reddy 🚀
</footer>

</body>
</html>
"""
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html
    }
