# Publishing iOS VIPER Template to GitHub

Complete guide for publishing this Cookiecutter template to GitHub.

## 📋 Pre-Publishing Checklist

### 1. Update Configuration

Before publishing, update these files with your actual GitHub username:

**Files to update:**
- `README.md` - Replace `cayde-6` with your username
- `USAGE.md` - Replace `cayde-6` with your username
- `CONTRIBUTING.md` - Replace `cayde-6` with your username
- `QUICKSTART.md` - Replace `cayde-6` with your username

**Quick find & replace:**
```bash
# Replace in all markdown files
find . -name "*.md" -type f -exec sed -i '' 's/cayde-6/YOUR_GITHUB_USERNAME/g' {} +

# Verify changes
git diff
```

### 2. Verify Template Structure

```bash
# Check all required files exist
ls -la cookiecutter.json
ls -la hooks/
ls -la "{{cookiecutter.project_slug}}/"

# Test template generation locally
cd ..
cookiecutter iOSApp/ --no-input
cd TestiOSApp
xcodegen generate  # if xcodegen installed
open TestiOSApp.xcodeproj
```

### 3. Choose Repository Name

Recommended names:
- `ios-viper-template`
- `ios-viper-template`
- `swift-project-template`
- Custom name that reflects your template

## 🚀 Publishing Steps

### Step 1: Create GitHub Repository

```bash
# Option A: Using gh CLI (recommended)
gh repo create ios-viper-template --public \
  --description "Modern iOS application template with VIPER architecture and Claude Code integration"

# Option B: Via GitHub website
# Go to https://github.com/new
# Name: ios-viper-template
# Description: Modern iOS application template with VIPER architecture and Claude Code integration
# Visibility: Public
# Don't initialize with README (we have one)
```

### Step 2: Initialize Git (if not already)

```bash
cd ~/Projects/YourWorkspace/iOSApp

# Initialize git
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: iOS VIPER Template with VIPER architecture

- Cookiecutter template for iOS projects
- VIPER architecture pattern
- Swift 6 support
- 7 specialized Claude Code agents
- 49 knowledge base files
- Comprehensive documentation"
```

### Step 3: Push to GitHub

```bash
# Add remote (replace YOUR_USERNAME)
git remote add origin git@github.com:YOUR_USERNAME/ios-viper-template.git

# Or use HTTPS
git remote add origin https://github.com/YOUR_USERNAME/ios-viper-template.git

# Push to main branch
git branch -M main
git push -u origin main
```

### Step 4: Configure Repository Settings

On GitHub repository page:

1. **Add Topics** (Settings → Topics)
   - `ios`
   - `swift`
   - `viper-architecture`
   - `cookiecutter`
   - `template`
   - `xcode`
   - `ios-template`
   - `swift6`
   - `claude-code`

2. **Enable Features**
   - ✅ Issues
   - ✅ Discussions
   - ✅ Projects (optional)
   - ✅ Wiki (optional)

3. **Set Up Branch Protection** (Settings → Branches)
   - Protect `main` branch
   - Require pull request reviews
   - Require status checks

### Step 5: Create Release

```bash
# Tag first version
git tag -a v1.0.0 -m "Release v1.0.0

Features:
- VIPER architecture template
- Swift 6 support
- Claude Code integration with 7 agents
- iOS 15-18 support
- Comprehensive documentation
- Xcodegen integration"

# Push tags
git push origin --tags

# Create release on GitHub
gh release create v1.0.0 \
  --title "v1.0.0 - Initial Release" \
  --notes "First stable release of iOS VIPER Template"
```

### Step 6: Test Public Access

```bash
# Test from different directory
cd ~
cookiecutter gh:YOUR_USERNAME/ios-viper-template

# Verify it works
cd iOSApp
xcodegen generate
open iOSApp.xcodeproj
```

## 📝 Post-Publishing Tasks

### 1. Update README Badges

Add to top of `README.md`:

```markdown
[![GitHub release](https://img.shields.io/github/release/YOUR_USERNAME/ios-viper-template.svg)](https://github.com/YOUR_USERNAME/ios-viper-template/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Swift](https://img.shields.io/badge/Swift-6.0-orange.svg)](https://swift.org)
[![iOS](https://img.shields.io/badge/iOS-15.0+-green.svg)](https://developer.apple.com/ios/)
```

### 2. Create GitHub Pages (Optional)

```bash
# Create gh-pages branch
git checkout --orphan gh-pages
git rm -rf .

# Create simple index.html
cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>iOS VIPER Template</title>
    <meta http-equiv="refresh" content="0; url=https://github.com/YOUR_USERNAME/ios-viper-template">
</head>
<body>
    Redirecting to GitHub repository...
</body>
</html>
EOF

git add index.html
git commit -m "Add GitHub Pages redirect"
git push origin gh-pages

# Enable GitHub Pages in Settings → Pages
# Source: gh-pages branch
```

### 3. Submit to Template Galleries

Add your template to:

1. **Cookiecutter Templates List**
   - Fork https://github.com/cookiecutter/cookiecutter
   - Add to `README.md` under iOS section
   - Submit PR

2. **Awesome iOS**
   - Fork https://github.com/vsouza/awesome-ios
   - Add under "Templates" section
   - Submit PR

3. **Swift Package Index** (if applicable)
   - https://swiftpackageindex.com

### 4. Announce on Social Media

Share on:
- Twitter/X with hashtags: `#iOSDev #Swift #VIPER #Template`
- Reddit: r/iOSProgramming
- Dev.to / Medium (write blog post)
- LinkedIn

### 5. Create Documentation Website (Optional)

Using GitHub Pages with Jekyll:

```bash
# In main branch
mkdir docs
cd docs

# Create _config.yml
cat > _config.yml << 'EOF'
theme: jekyll-theme-cayman
title: iOS VIPER Template
description: Modern iOS application template with VIPER architecture
EOF

# Copy markdown files
cp ../README.md index.md
cp ../USAGE.md usage.md
cp ../QUICKSTART.md quickstart.md

git add docs/
git commit -m "Add documentation website"
git push

# Enable GitHub Pages in Settings
# Source: main branch /docs folder
```

## 🔄 Maintaining the Template

### Regular Updates

1. **Monitor Issues**
   - Respond to bug reports
   - Consider feature requests
   - Help users with problems

2. **Update Dependencies**
   - Keep iOS versions current
   - Update Swift version
   - Update Claude agents knowledge

3. **Release New Versions**
   ```bash
   # Make changes
   git add .
   git commit -m "feat: add new feature"

   # Tag new version
   git tag -a v1.1.0 -m "Release v1.1.0"
   git push origin main --tags

   # Create GitHub release
   gh release create v1.1.0
   ```

4. **Gather Feedback**
   - Create surveys
   - Monitor discussions
   - Track usage statistics (if possible)

### Versioning Guidelines

Follow [Semantic Versioning](https://semver.org/):

- `v1.0.0` → `v2.0.0` - Breaking changes (major)
  - Example: Change template structure, remove features

- `v1.0.0` → `v1.1.0` - New features (minor)
  - Example: Add new agents, add new configuration options

- `v1.0.0` → `v1.0.1` - Bug fixes (patch)
  - Example: Fix broken template generation, typos

## 📊 Analytics (Optional)

Track template usage:

1. **GitHub Stars** - Track repository popularity
2. **Clones** - Insights → Traffic → Git clones
3. **Download Stats** - Release download counts
4. **Issues/Discussions** - User engagement

## 🎯 Promotion Strategies

1. **Write Blog Posts**
   - "Building iOS Apps with VIPER"
   - "Getting Started with iOS VIPER Template"
   - "Claude Code Integration Guide"

2. **Create Video Tutorials**
   - YouTube walkthrough
   - Template demonstration
   - Feature highlights

3. **Share Use Cases**
   - Showcase apps built with template
   - Testimonials
   - Success stories

4. **Engage Community**
   - Answer questions promptly
   - Accept contributions
   - Give credit to contributors

## 🔒 Security

1. **Review Dependencies**
   - Keep hooks dependencies updated
   - Scan for vulnerabilities

2. **Template Security**
   - Don't include API keys
   - No hardcoded credentials
   - Safe default configurations

3. **Report Security Issues**
   - Add SECURITY.md
   - Provide contact for private reports

## 📞 Support Channels

1. **GitHub Issues** - Bug reports, feature requests
2. **GitHub Discussions** - Q&A, general discussion
3. **Email** - Private inquiries (add to README)
4. **Discord/Slack** (optional) - Real-time community

## ✅ Final Checklist

Before making repository public:

- [ ] All placeholder usernames updated
- [ ] LICENSE file present
- [ ] README.md complete and clear
- [ ] Template generates successfully
- [ ] Generated project builds in Xcode
- [ ] All documentation links work
- [ ] Repository topics added
- [ ] Release v1.0.0 created
- [ ] Tested public access via cookiecutter

## 🎉 Success!

Your template is now public and ready for the iOS community!

**Next Steps:**
1. Monitor first users' feedback
2. Fix any reported issues quickly
3. Iterate based on usage patterns
4. Celebrate your contribution! 🎊

---

**Template Repository**: https://github.com/YOUR_USERNAME/ios-viper-template
**Generated Projects**: Will use this template to build amazing iOS apps!
