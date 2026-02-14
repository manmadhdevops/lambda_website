def lambda_handler(event, context):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Manmadh Kumar Reddy | DevOps Engineer</title>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">

<style>
:root {
    --primary:#1f2937;
    --accent:#3b82f6;
    --bg:#f3f4f6;
    --card:#ffffff;
}

body {
    margin:0;
    font-family:'Poppins',sans-serif;
    background:var(--bg);
    color:#333;
}

/* Animated Gradient Header */
header {
    background:linear-gradient(-45deg,#1f2937,#3b82f6,#111827,#2563eb);
    background-size:400% 400%;
    animation:gradientMove 12s ease infinite;
    color:white;
    text-align:center;
    padding:60px 20px;
    position:relative;
}

@keyframes gradientMove {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

h1 {
    margin:10px 0;
    font-size:2.8em;
    font-weight:700;
}

.profile-img {
    width:220px;
    height:220px;
    border-radius:50%;
    object-fit:cover;
    border:4px solid white;
    box-shadow:0 10px 25px rgba(0,0,0,0.3);
    margin-top:15px;
}

.title {
    margin-top:20px;
    font-size:1.2em;
}

.title i {
    color:#ffd700;
    margin-right:6px;
}

/* Scrolling skills */
.scrolling {
    background:#111827;
    color:#fff;
    padding:12px;
    overflow:hidden;
    white-space:nowrap;
}
.scrolling span {
    display:inline-block;
    padding-left:100%;
    animation:scroll 20s linear infinite;
}
@keyframes scroll {
    0%{transform:translateX(0);}
    100%{transform:translateX(-100%);}
}

/* Sections */
main {
    max-width:1100px;
    margin:40px auto;
    padding:0 20px;
}

section {
    margin-bottom:50px;
}

h2 {
    border-left:5px solid var(--accent);
    padding-left:15px;
    margin-bottom:25px;
}

/* Cards */
.card {
    background:var(--card);
    padding:25px;
    border-radius:12px;
    box-shadow:0 10px 30px rgba(0,0,0,0.08);
    transition:0.3s;
}

.card:hover {
    transform:translateY(-8px);
    box-shadow:0 20px 40px rgba(0,0,0,0.15);
}

/* Skill bars */
.skill {
    margin-bottom:15px;
}

.skill-bar {
    background:#e5e7eb;
    border-radius:20px;
    overflow:hidden;
    height:12px;
}

.skill-level {
    background:linear-gradient(90deg,#3b82f6,#2563eb);
    height:100%;
}

/* Contact */
.contact a {
    font-size:2em;
    margin:0 15px;
    color:var(--primary);
    transition:0.3s;
}

.contact a:hover {
    color:var(--accent);
    transform:scale(1.2);
}

footer {
    text-align:center;
    padding:20px;
    background:#111827;
    color:white;
}

/* Responsive */
@media(max-width:768px){
    h1{font-size:2em;}
    .profile-img{width:180px;height:180px;}
}
</style>
</head>

<body>

<header>
    <h1>🚀 Manmadh Kumar Reddy</h1>
    <img src="https://manmadhreddy.s3.us-east-1.amazonaws.com/Profile_Pic4.jpg" class="profile-img">
    <div class="title">
        <i class="fab fa-linux"></i> Linux |
        <i class="fab fa-aws"></i> AWS |
        <i class="fas fa-network-wired"></i> Networking |
        <i class="fas fa-infinity"></i> DevOps |
        <i class="fas fa-robot"></i> Automation |
        <i class="fas fa-project-diagram"></i> n8n |
        <i class="fas fa-chart-line"></i> Monitoring
    </div>
</header>

<div class="scrolling">
<span>
Linux ⚡ AWS ⚡ CI/CD ⚡ Docker ⚡ Kubernetes ⚡ Terraform ⚡ Python ⚡ GitHub Actions ⚡ Networking ⚡ n8n ⚡
</span>
</div>

<main>

<section>
<h2>👨‍💻 About Me</h2>
<div class="card">
Cloud & DevOps Engineer with hands-on experience in Linux administration, AWS cloud architecture, CI/CD pipelines, SRE practices, automation, monitoring, and infrastructure engineering. Portfolio hosted using AWS Lambda.
</div>
</section>

<section>
<h2>💡 Technical Skills</h2>

<div class="skill">
Linux
<div class="skill-bar"><div class="skill-level" style="width:90%"></div></div>
</div>

<div class="skill">
AWS
<div class="skill-bar"><div class="skill-level" style="width:85%"></div></div>
</div>

<div class="skill">
CI/CD
<div class="skill-bar"><div class="skill-level" style="width:80%"></div></div>
</div>

<div class="skill">
Automation & n8n
<div class="skill-bar"><div class="skill-level" style="width:88%"></div></div>
</div>

</section>

<section>
<h2>📂 Projects</h2>

<div class="card">
<h3>Serverless Portfolio</h3>
AWS Lambda + API Gateway + S3 + Route 53 architecture.
</div>

<br>

<div class="card">
<h3>CI/CD Automation</h3>
Jenkins pipelines integrated with GitHub, Docker & EC2.
</div>

<br>

<div class="card">
<h3>Monitoring Stack</h3>
Prometheus + Grafana dashboards with alerting.
</div>

</section>

<section>
<h2>📫 Contact</h2>
<div class="contact">
<a href="mailto:reddy.manmadh@gmail.com"><i class="fas fa-envelope"></i></a>
<a href="https://www.linkedin.com/in/manmadh-reddy-89b35017" target="_blank"><i class="fab fa-linkedin"></i></a>
<a href="https://github.com/manmadhdevops" target="_blank"><i class="fab fa-github"></i></a>
</div>
</section>

</main>

<footer>
© 2026 Manmadh Kumar Reddy | DevOps Engineer
</footer>

</body>
</html>
"""
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html; charset=UTF-8"},
        "body": html
    }
