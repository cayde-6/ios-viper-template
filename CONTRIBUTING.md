# Contributing to iOS VIPER Template

Thank you for your interest in contributing to the iOS VIPER Template! This document provides guidelines for contributing to this project.

## 🎯 Ways to Contribute

- **Bug Reports** - Found an issue? Let us know!
- **Feature Requests** - Have an idea? We'd love to hear it!
- **Code Contributions** - Submit pull requests
- **Documentation** - Improve guides and examples
- **Knowledge Base** - Add iOS framework documentation
- **Claude Agents** - Enhance or create new agents

## 🚀 Getting Started

### 1. Fork & Clone

```bash
# Fork the repository on GitHub
git clone https://github.com/YOUR_USERNAME/ios-viper-template.git
cd ios-viper-template
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Make Changes

Follow the guidelines below for your type of contribution.

## 📝 Development Guidelines

### Project Structure

```
ios-viper-template/
├── cookiecutter.json           # Template configuration
├── hooks/
│   ├── pre_gen_project.py     # Validation
│   └── post_gen_project.py    # Post-processing
├── {{cookiecutter.project_slug}}/
│   ├── {{cookiecutter.project_name}}/
│   │   └── Sources/           # Template source files
│   └── .claude/               # Claude agents & knowledge
├── README.md
├── USAGE.md
└── CONTRIBUTING.md
```

### Adding New Configuration Options

1. **Update `cookiecutter.json`**

```json
{
  "new_option": ["yes", "no"]
}
```

2. **Update validation in `hooks/pre_gen_project.py`**

```python
def validate_new_option():
    value = "{{ cookiecutter.new_option }}"
    if value not in ["yes", "no"]:
        print("ERROR: Invalid value for new_option")
        sys.exit(1)
```

3. **Handle in `hooks/post_gen_project.py`**

```python
if "{{ cookiecutter.new_option }}" == "yes":
    # Enable feature
    pass
```

4. **Update documentation in `README.md`**

### Adding Template Files

1. **Place files in correct location**

```bash
# For Swift files
{{cookiecutter.project_slug}}/{{cookiecutter.project_name}}/Sources/...

# For tests
{{cookiecutter.project_slug}}/{{cookiecutter.project_name}}Tests/...

# For Claude agents
{{cookiecutter.project_slug}}/.claude/agents/...
```

2. **Use Jinja2 variables**

```swift
//  {{ cookiecutter.project_name }}
//  Created by {{ cookiecutter.author_name }}

import UIKit

class {{ cookiecutter.project_name }}Manager {
    // ...
}
```

3. **Common variables**

- `{{ cookiecutter.project_name }}` - Project display name
- `{{ cookiecutter.project_slug }}` - Directory name (lowercase, no spaces)
- `{{ cookiecutter.bundle_identifier }}` - iOS bundle ID
- `{{ cookiecutter.organization_name }}` - Company name
- `{{ cookiecutter.author_name }}` - Developer name
- `{{ cookiecutter.ios_deployment_target }}` - Min iOS version
- `{{ cookiecutter.swift_version }}` - Swift version

### Adding Claude Agents

1. **Create agent file in `.claude/agents/`**

```markdown
# Agent Name

## Purpose
Brief description of what this agent does.

## When to Use
- Trigger phrase 1
- Trigger phrase 2

## Knowledge Files
- knowledge/relevant-file.md

## Capabilities
- Capability 1
- Capability 2

## Example Usage
\```
User: "trigger phrase"
Agent: [performs action]
\```
```

2. **Add to `AGENTS-SYSTEM.md`**

```markdown
### N. agent-name
**Purpose:** One-line description

**When to use:**
- Keyword 1
- Keyword 2

**Knowledge:**
- file.md

**Capabilities:**
- What it can do
```

3. **Create knowledge files if needed**

```bash
.claude/knowledge/your-topic.md
```

### Adding iOS Framework Documentation

1. **Create file in `.claude/knowledge/xcode-knowledge/`**

```markdown
# Framework Name - Feature

## Overview
Brief description of the feature.

## Implementation

\```swift
// Example code
\```

## Best Practices
- Practice 1
- Practice 2

## Common Issues
- Issue 1: Solution
- Issue 2: Solution
```

2. **Update INDEX.md**

```markdown
## Framework Name
- [Feature Name](./Framework-Feature.md)
```

## 🧪 Testing Your Changes

### 1. Test Template Generation

```bash
# From parent directory
cookiecutter ios-viper-template/

# Or with specific config
cookiecutter ios-viper-template/ --no-input \
  project_name="TestApp" \
  ios_deployment_target="17.0"
```

### 2. Verify Generated Project

```bash
cd TestApp
xcodegen generate  # if xcodegen available
open TestApp.xcodeproj
# Build with ⌘B
# Run tests with ⌘U
```

### 3. Test Hooks

```bash
# Hooks run automatically during generation
# Check for errors in console output

# Test validation
# Try invalid inputs to verify pre_gen_project.py catches them
```

### 4. Test Claude Agents (if modified)

```bash
cd TestApp
# Start Claude Code
# Test agent commands
```

## 📋 Pull Request Process

### 1. Ensure Quality

- [ ] All template variables work correctly
- [ ] Generated project builds successfully
- [ ] Tests pass (if included)
- [ ] Documentation updated
- [ ] No hardcoded values (use Jinja2 variables)
- [ ] Follows Swift style guidelines
- [ ] Follows Python style guidelines (hooks)

### 2. Update Documentation

- [ ] README.md (if adding features)
- [ ] USAGE.md (if adding examples)
- [ ] Inline code comments
- [ ] Agent documentation (if modifying agents)

### 3. Create Pull Request

```bash
git add .
git commit -m "feat: add new feature"
git push origin feature/your-feature-name
```

Then create PR on GitHub with:
- Clear title
- Description of changes
- Screenshots (if UI changes)
- Testing steps

### 4. PR Title Convention

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat: add new feature`
- `fix: resolve bug`
- `docs: update documentation`
- `style: code formatting`
- `refactor: code restructuring`
- `test: add tests`
- `chore: maintenance tasks`

## 🐛 Reporting Bugs

### Before Submitting

1. Check [existing issues](https://github.com/cayde-6/ios-viper-template/issues)
2. Test with latest version
3. Verify it's not a configuration issue

### Bug Report Template

```markdown
**Describe the bug**
Clear description of the bug.

**To Reproduce**
Steps to reproduce:
1. Run cookiecutter with these options...
2. See error...

**Expected behavior**
What should happen.

**Environment:**
- macOS version:
- Python version:
- Cookiecutter version:
- Xcode version:

**Additional context**
Logs, screenshots, etc.
```

## 💡 Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the feature.

**Use Case**
Why is this feature needed?

**Proposed Solution**
How should it work?

**Alternatives Considered**
Other approaches you've thought about.
```

## 📚 Documentation Guidelines

### Markdown Style

- Use ATX-style headers (`#` not `===`)
- Use fenced code blocks with language tags
- Keep line length reasonable
- Use relative links for internal docs
- Include emoji for visual hierarchy (sparingly)

### Code Examples

```swift
// ✅ Good - Clear, commented, complete
class UserManager {
    /// Fetches user profile from server
    func fetchUser() async throws -> User {
        // Implementation
    }
}

// ❌ Bad - No context, incomplete
class Manager {
    func fetch() {
        // ???
    }
}
```

## 🎨 Code Style

### Swift

Follow [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/):

- Clear, concise naming
- Prefer methods and properties
- Use verb phrases for mutating methods
- Use noun phrases for non-mutating methods

### Python (Hooks)

Follow [PEP 8](https://pep8.org/):

```python
# ✅ Good
def validate_project_name(project_name: str) -> bool:
    """Validate project name format."""
    return bool(re.match(r'^[A-Z][A-Za-z0-9]*$', project_name))

# ❌ Bad
def validate(n):
    return re.match(r'^[A-Z][A-Za-z0-9]*$', n)
```

## 🏷️ Versioning

This project follows [Semantic Versioning](https://semver.org/):

- **Major** (X.0.0) - Breaking changes
- **Minor** (0.X.0) - New features (backward compatible)
- **Patch** (0.0.X) - Bug fixes

## ⚖️ License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🤝 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information

## 💬 Communication

- **Issues** - Bug reports and feature requests
- **Pull Requests** - Code contributions
- **Discussions** - General questions and ideas

## 🙏 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in relevant documentation

## 📞 Contact

- **GitHub Issues**: For bugs and features
- **GitHub Discussions**: For questions
- **Email**: [your-email] for private inquiries

---

Thank you for contributing! 🎉
