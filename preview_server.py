def lambda_handler(event, context):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Manmadh Kumar Reddy Reddy Palle Palle Manmadh  | DevOps Portfolio</title>

    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">

    <style>
        body {
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
            background: #f4f6f8;
            color: #333;
            overflow-x: hidden;
        }

        header {
            background: #232f3e;
            color: white;
            padding: 60px 20px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        /* Decorative SVG background blob */
        .header-blob {
            position: absolute;
            pointer-events: none;
            inset: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            opacity: 0.18;
        }

        /* Profile Image */
        .profile-img {
            width: 170px;
            height: 170px;
            border-radius: 50%;
            border: 5px solid #ff9900;
            object-fit: cover;
            margin-top: 20px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.4);
            z-index: 2;
            position: relative;
        }

        nav {
            background: #ff9900;
            padding: 12px;
            text-align: center;
        }

        nav a {
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
            color: #232f3e;
        }

        section {
            max-width: 900px;
            margin: auto;
            padding: 40px 20px;
        }

        h2 {
            color: #232f3e;
        }

        /* Floating Icons */
        .icon {
            position: absolute;
            font-size: 42px;
            opacity: 0.7;
            animation: floatAnim linear infinite;
        }


        .tech-icon { font-size: 48px; opacity: 0.95 }

        /* Small rotation for variety */
        .spin-slow { animation: spin 12s linear infinite; }
        .spin-medium { animation: spin 9s linear infinite; }

        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        .aws { color: #ff9900; }
        .linux { color: #00b894; }
        .devops { color: #1f77b4; }
        .automation { color: #6c5ce7; }
        .monitoring { color: #e17055; }

        @keyframes floatAnim {
            0% { transform: translateY(0px) translateX(0px); }
            50% { transform: translateY(-25px) translateX(15px); }
            100% { transform: translateY(0px) translateX(0px); }
        }

        /* Wave separator */
        .wave {
            display: block;
            width: 100%;
            margin-top: -6px;
        }

        /* Skills */
        .skill-container {
            margin: 20px 0;
        }

        .skill-label {
            font-weight: bold;
        }

        .skill-bar {
            width: 100%;
            background: #ddd;
            border-radius: 25px;
            overflow: hidden;
            height: 25px;
        }

        .skill-level {
            height: 100%;
            background: linear-gradient(90deg, #1f77b4, #00b894);
            color: white;
            text-align: right;
            padding-right: 10px;
            line-height: 25px;
            font-weight: bold;
        }

        /* Projects */
        .project {
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-left: 5px solid #ff9900;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            transition: transform 220ms ease, box-shadow 220ms ease;
        }

        .project:hover { transform: translateY(-6px); box-shadow: 0 8px 22px rgba(0,0,0,0.14); }

        footer {
            background: #232f3e;
            color: white;
            text-align: center;
            padding: 20px;
        }
    </style>
</head>

<body>

<header>
    <svg class="header-blob" viewBox="0 0 800 400" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="g1" x1="0" x2="1">
                <stop offset="0%" stop-color="#ff9900"/>
                <stop offset="100%" stop-color="#6c5ce7"/>
            </linearGradient>
            <filter id="blur"><feGaussianBlur stdDeviation="40"/></filter>
        </defs>
        <g filter="url(#blur)">
            <path d="M0 120 Q160 20 300 140 T800 120 L800 400 L0 400 Z" fill="url(#g1)" opacity="0.9"/>
            <circle cx="95" cy="60" r="60" fill="#1f77b4" opacity="0.6"/>
            <circle cx="720" cy="80" r="40" fill="#00b894" opacity="0.5"/>
        </g>
    </svg>
    <!-- Floating Icons -->
    <i class="fab fa-aws icon aws tech-icon spin-medium" style="top:30px; left:40px; animation-duration:7s;"></i>
    <i class="fab fa-linux icon linux tech-icon" style="top:120px; left:200px; animation-duration:9s;"></i>
    <i class="fas fa-cogs icon devops tech-icon spin-slow" style="top:60px; right:80px; animation-duration:8s;"></i>
    <i class="fas fa-robot icon automation tech-icon" style="top:160px; right:220px; animation-duration:10s;"></i>
    <i class="fas fa-chart-line icon monitoring tech-icon" style="top:40px; right:350px; animation-duration:11s;"></i>
    <i class="fab fa-docker icon" style="top:220px; left:60px; color:#2496ED; animation-duration:10s;"></i>
    <i class="fab fa-kubernetes icon" style="top:40px; left:320px; color:#326CE5; animation-duration:12s;"></i>
    <i class="fas fa-cloud icon" style="top:200px; right:380px; color:#8ec5ff; animation-duration:9s;"></i>
    <i class="fas fa-server icon" style="top:260px; right:120px; color:#ffd166; animation-duration:8s;"></i>

    <h1>🚀 Manmadh Kumar Reddy</h1>

    <img src="https://manmadhreddy.s3.us-east-1.amazonaws.com/Profile_Pic.jpg"
         alt="Manmadh Kumar Reddy"
         class="profile-img">

    <p>Linux | AWS | DevOps Engineer | SRE | Automation | Monitoring</p>

    <!-- Social / badges row -->
    <div style="margin-top:14px; z-index:2; position:relative;">
        <a href="#projects" style="color:white; margin:0 8px; text-decoration:none; font-weight:600;">Explore Projects</a>
        <span style="display:inline-block; width:10px;"></span>
        <a href="https://github.com/" target="_blank" style="color:white; margin:0 8px;"><i class="fab fa-github"></i></a>
        <a href="https://www.linkedin.com/" target="_blank" style="color:white; margin:0 8px;"><i class="fab fa-linkedin"></i></a>
    </div>
</header>

<nav>
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
</nav>

<section id="about">
    <h2>👋 About Me</h2>
    <p>
        I am a DevOps Engineer with strong hands-on experience in Linux system administration,
        AWS cloud services, CI/CD pipelines, infrastructure engineering, SRE practices,
        automation, and monitoring. This portfolio is fully serverless using AWS Lambda.
    </p>
</section>

<section id="skills">
    <h2>💡 Skills</h2>

    <div class="skill-container">
        <div class="skill-label">Linux Administration</div>
        <div class="skill-bar"><div class="skill-level" style="width:90%">90%</div></div>
    </div>

    <div class="skill-container">
        <div class="skill-label">AWS Cloud</div>
        <div class="skill-bar"><div class="skill-level" style="width:85%">85%</div></div>
    </div>

    <div class="skill-container">
        <div class="skill-label">CI/CD Pipelines</div>
        <div class="skill-bar"><div class="skill-level" style="width:80%">80%</div></div>
    </div>

    <div class="skill-container">
        <div class="skill-label">Automation</div>
        <div class="skill-bar"><div class="skill-level" style="width:90%">90%</div></div>
    </div>

    <div class="skill-container">
        <div class="skill-label">Monitoring & SRE</div>
        <div class="skill-bar"><div class="skill-level" style="width:85%">85%</div></div>
    </div>
</section>

<svg class="wave" viewBox="0 0 1440 60" xmlns="http://www.w3.org/2000/svg"><path fill="#232f3e" d="M0,0 C360,80 1080,-40 1440,20 L1440,60 L0,60 Z"></path></svg>

<section id="projects">
    <h2>📂 Projects</h2>

    <div class="project">
        <h3>Serverless DevOps Portfolio <span style="float:right; color:#999;"><i class="fas fa-laptop-code"></i></span></h3>
        <p>AWS Lambda + API Gateway + S3 + Route 53 based serverless portfolio.</p>
    </div>

    <div class="project">
        <h3>CI/CD Automation <span style="float:right; color:#999;"><i class="fas fa-project-diagram"></i></span></h3>
        <p>Jenkins pipelines integrating GitHub, Docker, EC2, and automated deployments.</p>
    </div>

    <div class="project">
        <h3>Monitoring Stack <span style="float:right; color:#999;"><i class="fas fa-chart-area"></i></span></h3>
        <p>Prometheus, Grafana dashboards with alerts and performance monitoring.</p>
    </div>

    <div class="project">
        <h3>Infrastructure as Code</h3>
        <p>Terraform modules and reusable CloudFormation templates for repeatable infra.</p>
    </div>
</section>

<footer>
    <p>© 2026 Manmadh Kumar Reddy 🚀</p>
</footer>

</body>
</html>
"""
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html; charset=UTF-8"
        },
        "body": html
    }
