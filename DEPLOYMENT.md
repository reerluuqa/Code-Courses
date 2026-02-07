# 🚀 Quick Deployment Guide

Get your GitHub Pages site live in 5 minutes!

## Step 1: Initial Setup

```bash
# Create a new repository on GitHub (e.g., "web-dev-courses")
# Then clone it locally:
git clone https://github.com/YOUR-USERNAME/web-dev-courses.git
cd web-dev-courses

# Copy all files from this project into your repository
# (index.html, build_courses.py, README.md, etc.)
```

## Step 2: Generate Course Pages

```bash
# Run the build script to create all course folders
python build_courses.py
```

You should see output like:
```
🚀 Building course structure...
✅ Created folder: 01-html-css-js/
...
✨ Build Complete!
```

## Step 3: Customize (Optional)

Edit `index.html` to add your GitHub link:
- Line ~394: Update the GitHub link in footer
- Add your name/information

## Step 4: Commit and Push

```bash
# Add all files
git add .

# Commit
git commit -m "Initial setup of web dev course portfolio"

# Push to GitHub
git push origin main
```

## Step 5: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Click **Pages** (left sidebar)
4. Under "Source":
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**

## Step 6: Visit Your Site! 🎉

Your site will be live at:
```
https://YOUR-USERNAME.github.io/web-dev-courses/
```

*(It may take 1-2 minutes for the site to build)*

## Adding Your Course Content

### Add Notes
```bash
cd 01-html-css-js/notes
# Create markdown files with your notes
echo "# HTML5 Basics" > html5-basics.md
```

### Add Projects
```bash
cd 01-html-css-js/projects
mkdir my-portfolio
cd my-portfolio
# Add your project files
```

### Add Exercises
```bash
cd 01-html-css-js/exercises
# Add practice exercises
```

## Updating Your Site

After making changes:
```bash
git add .
git commit -m "Add notes for HTML/CSS course"
git push origin main
```

GitHub Pages will automatically rebuild your site!

## Troubleshooting

**Site not showing up?**
- Wait 2-3 minutes after enabling GitHub Pages
- Check Settings → Pages to see if there are any errors
- Make sure your repository is public or you have GitHub Pro

**Changes not appearing?**
- GitHub Pages can take 1-2 minutes to rebuild
- Hard refresh your browser (Ctrl+Shift+R / Cmd+Shift+R)
- Check that you pushed your commits

**Want to test locally?**
```bash
# Use Python's built-in server
python -m http.server 8000

# Visit: http://localhost:8000
```

## Next Steps

✅ Customize colors and styling
✅ Add your course materials
✅ Create project showcases
✅ Share your portfolio!

---

**Need help?** Check the main [README.md](README.md) for detailed documentation.
