# 🎓 Web Development Course Portfolio

A beautiful, responsive GitHub Pages site showcasing my web development learning journey. This portfolio documents courses, projects, and skills acquired on the path to becoming a full-stack web developer.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

## 🌟 Features

- **Beautiful Landing Page**: Eye-catching design inspired by learning roadmaps
- **8 Course Modules**: Comprehensive coverage from basics to advanced topics
- **Responsive Design**: Looks great on desktop, tablet, and mobile
- **Easy Navigation**: Intuitive course structure with quick navigation
- **Automated Build**: Python script to generate and update all pages
- **GitHub Pages Ready**: Deploy-ready static site

## 📚 Course Modules

1. **HTML/CSS/JS** - Foundation of Web Development
2. **Git & GitHub** - Version Control Mastery
3. **React** - Modern Frontend Framework
4. **Backend Development** - Server-Side Programming
5. **Databases** - Data Storage & Management
6. **Frontend + Backend Integration** - Full-Stack Development
7. **Deployment & DevOps Basics** - Ship Your Applications
8. **Web Security** - Building Secure Applications

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Git
- A GitHub account

### Setup Instructions

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/yourusername/web-dev-courses.git
   cd web-dev-courses
   ```

2. **Run the build script** to generate all course pages:
   ```bash
   python build_courses.py
   ```

3. **Add your content** to each course folder:
   - Add notes in the `notes/` subdirectory
   - Add projects in the `projects/` subdirectory
   - Add exercises in the `exercises/` subdirectory

4. **Commit and push** to GitHub:
   ```bash
   git add .
   git commit -m "Initial course portfolio setup"
   git push origin main
   ```

5. **Enable GitHub Pages**:
   - Go to your repository settings
   - Navigate to "Pages" section
   - Select branch: `main`
   - Select folder: `/ (root)`
   - Click "Save"

Your site will be live at: `https://yourusername.github.io/repository-name/`

## 📁 Project Structure

```
web-dev-courses/
├── index.html                    # Main landing page
├── build_courses.py              # Build script
├── README.md                     # This file
├── .gitignore                   # Git ignore file
│
├── 01-html-css-js/
│   ├── index.html               # Course page
│   ├── README.md                # Course documentation
│   ├── notes/                   # Your course notes
│   ├── projects/                # Your projects
│   └── exercises/               # Practice exercises
│
├── 02-git-github/
│   └── ... (same structure)
│
├── 03-react/
│   └── ... (same structure)
│
├── 04-backend/
│   └── ... (same structure)
│
├── 05-databases/
│   └── ... (same structure)
│
├── 06-integration/
│   └── ... (same structure)
│
├── 07-deployment-devops/
│   └── ... (same structure)
│
└── 08-web-security/
    └── ... (same structure)
```

## 🛠️ Using the Build Script

The `build_courses.py` script automates the creation and updating of your course pages.

### Basic Usage

```bash
python build_courses.py
```

### What the Script Does

- ✅ Creates all course directories if they don't exist
- ✅ Generates/updates `index.html` in each course folder
- ✅ Generates/updates `README.md` in each course folder
- ✅ Creates subdirectories (`notes/`, `projects/`, `exercises/`)
- ✅ Maintains consistent styling and navigation across all pages

### When to Run the Script

- **Initial setup**: First time setting up the portfolio
- **After updates**: When you modify course information
- **Before deploying**: To ensure all pages are up-to-date

## 🎨 Customization

### Changing Colors

Edit the course colors in `build_courses.py`:

```python
COURSES = [
    {
        'id': '01-html-css-js',
        'color': '#ff5722',      # Primary color
        'color_end': '#ff9800',  # Gradient end color
        # ... other properties
    }
]
```

### Modifying Course Content

Update course details in the `COURSES` list in `build_courses.py`:

```python
{
    'title': 'Your Course Title',
    'subtitle': 'Course Subtitle',
    'description': 'Course description...',
    'topics': ['Topic 1', 'Topic 2', ...]
}
```

After making changes, run `python build_courses.py` to regenerate the pages.

### Styling Changes

- **Landing page**: Edit `index.html` directly
- **Course pages**: Modify the HTML template in `build_courses.py`'s `generate_course_html()` function

## 📝 Adding Your Content

### Adding Notes

Create markdown files in the `notes/` directory:

```bash
cd 01-html-css-js/notes
echo "# HTML Basics" > html-basics.md
```

### Adding Projects

Create project folders in the `projects/` directory:

```bash
cd 01-html-css-js/projects
mkdir portfolio-website
cd portfolio-website
# Add your project files here
```

### Adding Exercises

Add practice exercises to the `exercises/` directory:

```bash
cd 01-html-css-js/exercises
mkdir flexbox-practice
# Add exercise files
```

## 🌐 Deployment

### GitHub Pages (Recommended)

1. Push your code to GitHub
2. Go to repository Settings → Pages
3. Select `main` branch and `/ (root)` folder
4. Save and wait a few minutes
5. Your site will be live!

### Alternative Hosting

This is a static site and can be hosted on:
- **Netlify**: Drag and drop deployment
- **Vercel**: Connect your GitHub repo
- **Cloudflare Pages**: Fast global CDN
- **Any static hosting service**

## 🤝 Contributing

This is a personal learning portfolio, but suggestions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Design inspired by modern learning roadmaps
- Built with pure HTML, CSS, and JavaScript
- Fonts from Google Fonts (Syne & Karla)
- Icons and inspiration from the web development community

## 📧 Contact

Questions or suggestions? Feel free to:
- Open an issue
- Submit a pull request
- Reach out on [GitHub](https://github.com/yourusername)

---

**Happy Learning! 🚀**

Built with 💙 as part of my web development journey
