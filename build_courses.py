#!/usr/bin/env python3
"""
GitHub Pages Course Builder
----------------------------
This script creates/updates course folder structure and index.html files
for your web development course portfolio.

Usage:
    python build_courses.py

What it does:
- Creates all course folders if they don't exist
- Generates/updates index.html files in each folder
- Adds a sample README.md in each folder
- Creates a consistent navigation structure
"""

import os
from pathlib import Path
from datetime import datetime

# Course configuration
COURSES = [
    {
        'id': '01-html-css-js',
        'number': '01',
        'title': 'HTML/CSS/JS',
        'subtitle': 'Foundation of Web Development',
        'description': 'Master the core technologies that power the web. Learn semantic HTML5, modern CSS3 with Flexbox and Grid, and JavaScript fundamentals including ES6+ features.',
        'color': '#ff5722',
        'color_end': '#ff9800',
        'topics': [
            'HTML5 Semantic Elements',
            'CSS Grid & Flexbox',
            'JavaScript ES6+',
            'DOM Manipulation',
            'Responsive Design',
            'CSS Animations & Transitions'
        ]
    },
    {
        'id': '02-git-github',
        'number': '02',
        'title': 'Git & GitHub',
        'subtitle': 'Version Control Mastery',
        'description': 'Learn essential version control with Git and collaboration workflows with GitHub. Understand branching strategies, pull requests, and team development practices.',
        'color': '#ffc107',
        'color_end': '#ffeb3b',
        'topics': [
            'Git Fundamentals',
            'Branching & Merging',
            'GitHub Workflows',
            'Pull Requests',
            'Collaborative Development',
            'Git Best Practices'
        ]
    },
    {
        'id': '03-react',
        'number': '03',
        'title': 'React',
        'subtitle': 'Modern Frontend Framework',
        'description': 'Build powerful, component-based user interfaces with React. Learn hooks, context, routing, and state management for creating dynamic web applications.',
        'color': '#2196f3',
        'color_end': '#03a9f4',
        'topics': [
            'React Components',
            'Hooks (useState, useEffect)',
            'React Router',
            'State Management',
            'Context API',
            'Performance Optimization'
        ]
    },
    {
        'id': '04-backend',
        'number': '04',
        'title': 'Backend Development',
        'subtitle': 'Server-Side Programming',
        'description': 'Explore server-side development with Node.js and Express. Build RESTful APIs, handle authentication, and implement business logic on the backend.',
        'color': '#9c27b0',
        'color_end': '#ba68c8',
        'topics': [
            'Node.js Fundamentals',
            'Express.js Framework',
            'RESTful API Design',
            'Authentication & Authorization',
            'Middleware',
            'Error Handling'
        ]
    },
    {
        'id': '05-databases',
        'number': '05',
        'title': 'Databases',
        'subtitle': 'Data Storage & Management',
        'description': 'Master both SQL and NoSQL databases. Learn data modeling, complex queries, indexing, and how to choose the right database for your application.',
        'color': '#e91e63',
        'color_end': '#f06292',
        'topics': [
            'SQL Databases (PostgreSQL/MySQL)',
            'NoSQL Databases (MongoDB)',
            'Database Design',
            'Query Optimization',
            'Indexing',
            'Transactions & ACID'
        ]
    },
    {
        'id': '06-integration',
        'number': '06',
        'title': 'Frontend + Backend Integration',
        'subtitle': 'Full-Stack Development',
        'description': 'Connect frontend and backend seamlessly. Learn to fetch data, handle CORS, manage state across the stack, and build complete full-stack features.',
        'color': '#009688',
        'color_end': '#26a69a',
        'topics': [
            'REST API Integration',
            'Fetch API & Axios',
            'CORS Configuration',
            'State Synchronization',
            'File Uploads',
            'Real-time Communication'
        ]
    },
    {
        'id': '07-deployment-devops',
        'number': '07',
        'title': 'Deployment & DevOps Basics',
        'subtitle': 'Ship Your Applications',
        'description': 'Learn to deploy applications to production. Understand cloud platforms, CI/CD pipelines, monitoring, and DevOps best practices.',
        'color': '#3f51b5',
        'color_end': '#5c6bc0',
        'topics': [
            'Cloud Platforms (AWS, Heroku, Vercel)',
            'CI/CD Pipelines',
            'Docker Basics',
            'Environment Variables',
            'Monitoring & Logging',
            'Performance Optimization'
        ]
    },
    {
        'id': '08-web-security',
        'number': '08',
        'title': 'Web Security',
        'subtitle': 'Building Secure Applications',
        'description': 'Understand web security fundamentals. Learn about common vulnerabilities, HTTPS, secure authentication, and how to protect your applications.',
        'color': '#4caf50',
        'color_end': '#66bb6a',
        'topics': [
            'OWASP Top 10',
            'XSS & CSRF Protection',
            'SQL Injection Prevention',
            'Secure Authentication',
            'HTTPS & SSL/TLS',
            'Security Headers'
        ]
    }
]


def generate_course_html(course, all_courses):
    """Generate HTML content for a course page"""
    
    # Generate navigation links
    nav_links = []
    for c in all_courses:
        active = 'active' if c['id'] == course['id'] else ''
        nav_links.append(f'<a href="../{c["id"]}/" class="{active}">{c["number"]}. {c["title"]}</a>')
    
    nav_html = '\n                '.join(nav_links)
    
    # Generate topics list
    topics_html = '\n                        '.join([f'<li>{topic}</li>' for topic in course['topics']])
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{course['title']} | Web Development Courses</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Karla:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --course-color: {course['color']};
            --course-color-end: {course['color_end']};
            --bg-primary: #f5f7fa;
            --text-primary: #1a1a2e;
            --text-secondary: #6b7280;
        }}

        body {{
            font-family: 'Karla', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
        }}

        .hero {{
            background: linear-gradient(135deg, var(--course-color), var(--course-color-end));
            color: white;
            padding: 6rem 2rem 4rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}

        .hero::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(0, 0, 0, 0.1) 0%, transparent 50%);
            pointer-events: none;
        }}

        .hero-content {{
            max-width: 800px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }}

        .course-number {{
            font-family: 'Syne', sans-serif;
            font-size: 1.2rem;
            font-weight: 600;
            opacity: 0.9;
            margin-bottom: 0.5rem;
            letter-spacing: 0.1em;
        }}

        h1 {{
            font-family: 'Syne', sans-serif;
            font-size: clamp(2.5rem, 5vw, 4rem);
            font-weight: 800;
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
        }}

        .subtitle {{
            font-size: 1.3rem;
            opacity: 0.95;
            margin-bottom: 1.5rem;
            font-weight: 300;
        }}

        .description {{
            font-size: 1.1rem;
            opacity: 0.9;
            max-width: 700px;
            margin: 0 auto;
            line-height: 1.7;
        }}

        nav {{
            background: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            position: sticky;
            top: 0;
            z-index: 100;
        }}

        .nav-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            align-items: center;
            overflow-x: auto;
            gap: 0.5rem;
        }}

        nav a {{
            padding: 1rem 1.2rem;
            color: var(--text-secondary);
            text-decoration: none;
            white-space: nowrap;
            font-weight: 500;
            font-size: 0.9rem;
            border-bottom: 3px solid transparent;
            transition: all 0.3s;
        }}

        nav a:hover {{
            color: var(--text-primary);
            background: rgba(0, 0, 0, 0.02);
        }}

        nav a.active {{
            color: var(--course-color);
            border-bottom-color: var(--course-color);
        }}

        .home-link {{
            margin-right: auto;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            color: var(--text-primary) !important;
            border: none !important;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 4rem 2rem;
        }}

        .content-section {{
            background: white;
            border-radius: 16px;
            padding: 3rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }}

        .content-section h2 {{
            font-family: 'Syne', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            color: var(--text-primary);
        }}

        .topics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin-top: 2rem;
        }}

        .topics-grid li {{
            list-style: none;
            padding: 1rem 1.5rem;
            background: linear-gradient(135deg, var(--course-color), var(--course-color-end));
            color: white;
            border-radius: 12px;
            font-weight: 500;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }}

        .topics-grid li:hover {{
            transform: translateY(-4px);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
        }}

        .info-box {{
            background: linear-gradient(135deg, rgba(255, 107, 107, 0.1), rgba(255, 193, 7, 0.1));
            border-left: 4px solid var(--course-color);
            padding: 1.5rem;
            border-radius: 8px;
            margin: 2rem 0;
        }}

        .info-box p {{
            margin: 0;
            color: var(--text-primary);
        }}

        footer {{
            text-align: center;
            padding: 3rem 2rem;
            color: var(--text-secondary);
            font-size: 0.9rem;
        }}

        @media (max-width: 768px) {{
            .hero {{
                padding: 4rem 1.5rem 3rem;
            }}

            .container {{
                padding: 2rem 1.5rem;
            }}

            .content-section {{
                padding: 2rem 1.5rem;
            }}

            .topics-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <nav>
        <div class="nav-container">
            <a href="../" class="home-link">← Home</a>
            {nav_html}
        </div>
    </nav>

    <div class="hero">
        <div class="hero-content">
            <div class="course-number">COURSE {course['number']}</div>
            <h1>{course['title']}</h1>
            <p class="subtitle">{course['subtitle']}</p>
            <p class="description">{course['description']}</p>
        </div>
    </div>

    <div class="container">
        <section class="content-section">
            <h2>📚 Key Topics Covered</h2>
            <ul class="topics-grid">
                {topics_html}
            </ul>
        </section>

        <section class="content-section">
            <h2>📝 Course Notes & Materials</h2>
            <div class="info-box">
                <p><strong>📌 Note:</strong> Add your course notes, projects, and learning materials to this folder. You can create markdown files, add code examples, or link to external resources.</p>
            </div>
            <p>This section will contain all the notes, code examples, and projects from the <strong>{course['title']}</strong> course. Stay tuned for updates!</p>
        </section>

        <section class="content-section">
            <h2>🚀 Projects</h2>
            <p>Practical projects and exercises completed during this course will be listed here. Each project demonstrates key concepts and skills learned.</p>
            <div class="info-box">
                <p><strong>💡 Tip:</strong> Create a separate folder for each project with its own README.md file explaining what you built and what you learned.</p>
            </div>
        </section>
    </div>

    <footer>
        <p>Last updated: {datetime.now().strftime('%B %d, %Y')} | Part of my Web Development Journey</p>
    </footer>
</body>
</html>'''
    
    return html_content


def generate_readme(course):
    """Generate README.md content for a course"""
    topics_md = '\n'.join([f'- {topic}' for topic in course['topics']])
    
    readme_content = f'''# {course['title']}

**Course {course['number']}:** {course['subtitle']}

## Overview

{course['description']}

## Topics Covered

{topics_md}

## Structure

```
{course['id']}/
├── index.html          # Course overview page
├── README.md           # This file
├── notes/              # Course notes and documentation
├── projects/           # Course projects
└── exercises/          # Practice exercises
```

## Getting Started

1. Review the course overview on the [main page](../index.html)
2. Check out the [index.html](./index.html) for detailed information
3. Explore the notes and projects folders

## Resources

- [MDN Web Docs](https://developer.mozilla.org/)
- [W3Schools](https://www.w3schools.com/)
- [freeCodeCamp](https://www.freecodecamp.org/)

---

*Part of my Web Development Journey - [View All Courses](../)*
'''
    
    return readme_content


def create_directory_structure(base_path='.'):
    """Create all course directories and files"""
    base_path = Path(base_path)
    created_folders = []
    updated_files = []
    
    print("🚀 Building course structure...\n")
    
    for course in COURSES:
        course_dir = base_path / course['id']
        
        # Create course directory
        if not course_dir.exists():
            course_dir.mkdir(parents=True)
            created_folders.append(course['id'])
            print(f"✅ Created folder: {course['id']}/")
        else:
            print(f"📁 Folder exists: {course['id']}/")
        
        # Create subdirectories
        for subdir in ['notes', 'projects', 'exercises']:
            sub_path = course_dir / subdir
            if not sub_path.exists():
                sub_path.mkdir(parents=True)
                print(f"   ├── {subdir}/")
        
        # Generate and write index.html
        html_content = generate_course_html(course, COURSES)
        html_path = course_dir / 'index.html'
        html_path.write_text(html_content, encoding='utf-8')
        updated_files.append(f"{course['id']}/index.html")
        print(f"   ├── index.html (updated)")
        
        # Generate and write README.md
        readme_content = generate_readme(course)
        readme_path = course_dir / 'README.md'
        readme_path.write_text(readme_content, encoding='utf-8')
        print(f"   └── README.md (updated)")
        print()
    
    # Summary
    print("\n" + "="*60)
    print("✨ Build Complete!")
    print("="*60)
    print(f"\n📊 Summary:")
    print(f"   • Folders created: {len(created_folders)}")
    print(f"   • Files updated: {len(updated_files)}")
    print(f"   • Total courses: {len(COURSES)}")
    
    if created_folders:
        print(f"\n🆕 New folders:")
        for folder in created_folders:
            print(f"   • {folder}")
    
    print(f"\n📝 Next steps:")
    print(f"   1. Review the generated index.html files")
    print(f"   2. Add your course materials to each folder")
    print(f"   3. Commit and push to GitHub")
    print(f"   4. Enable GitHub Pages in your repository settings")
    print(f"\n🌐 Your site will be live at:")
    print(f"   https://[your-username].github.io/[repository-name]/")
    print()


if __name__ == '__main__':
    create_directory_structure()
