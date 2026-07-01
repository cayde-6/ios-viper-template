# Git Flow Workflow

This project uses a simplified Git Flow with two main branches.

## Branch Structure

```
main     - Production-ready code, always stable (protected)
develop  - Development branch, integration branch (default)
```

## Branch Types

### Feature Branches
**Pattern:** `feature/название`
**From:** `develop`
**Merge to:** `develop`
**Purpose:** New functionality

```bash
git checkout develop
git pull origin develop
git checkout -b feature/profile-screen
# ... work ...
git push origin feature/profile-screen
# Create PR: feature/profile-screen → develop
```

### Fix Branches
**Pattern:** `fix/название`
**From:** `develop`
**Merge to:** `develop`
**Purpose:** Bug fixes during development

```bash
git checkout develop
git pull origin develop
git checkout -b fix/crash-on-startup
# ... work ...
git push origin fix/crash-on-startup
# Create PR: fix/crash-on-startup → develop
```

### Hotfix Branches
**Pattern:** `hotfix/название`
**From:** `main`
**Merge to:** `main` AND `develop`
**Purpose:** Critical production fixes

```bash
git checkout main
git pull origin main
git checkout -b hotfix/critical-crash
# ... work ...
git push origin hotfix/critical-crash
# Create 2 PRs:
# 1. hotfix/critical-crash → main
# 2. hotfix/critical-crash → develop
```

### Refactor Branches
**Pattern:** `refactor/название`
**From:** `develop`
**Merge to:** `develop`
**Purpose:** Code refactoring without new features

### Docs Branches
**Pattern:** `docs/название`
**From:** `develop`
**Merge to:** `develop`
**Purpose:** Documentation updates only

## Workflow Steps

### 1. Start New Work

```bash
# Always start from develop (unless hotfix)
git checkout develop
git pull origin develop

# Create branch with descriptive name
git checkout -b feature/user-authentication
```

### 2. Work & Commit

```bash
# Make changes
git add .
git commit -m "Add login screen with form validation"

# Multiple commits OK
git commit -m "Add password reset flow"
```

### 3. Push & Create PR

```bash
# Push feature branch
git push origin feature/user-authentication

# Create Pull Request using gh CLI
gh pr create \
  --base develop \
  --head feature/user-authentication \
  --title "Add user authentication" \
  --body "Implements login, logout, and password reset"
```

### 4. After Merge

```bash
# Switch back to develop
git checkout develop
git pull origin develop

# Delete local feature branch
git branch -d feature/user-authentication

# Delete remote branch (usually auto-deleted by GitHub)
git push origin --delete feature/user-authentication
```

## Release Process

When `develop` is stable and ready for production:

```bash
# Create PR: develop → main
gh pr create \
  --base main \
  --head develop \
  --title "Release v1.0.0" \
  --body "Production release"

# After merge, tag the release
git checkout main
git pull origin main
git tag -a v1.0.0 -m "Release 1.0.0"
git push origin v1.0.0
```

## Naming Conventions

### Branch Names
- Use lowercase
- Use hyphens (not underscores)
- Be descriptive but concise
- Examples:
  - ✅ `feature/profile-screen`
  - ✅ `fix/login-crash`
  - ✅ `refactor/viper-modules`
  - ❌ `feature/new_stuff`
  - ❌ `fix/bug`

### Commit Messages
Follow conventional commits:

```
<type>: <description>

[optional body]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code refactoring
- `docs`: Documentation only
- `style`: Code style changes (formatting)
- `test`: Adding tests
- `chore`: Build/config changes

**Examples:**
```bash
git commit -m "feat: add user profile screen with avatar upload"
git commit -m "fix: resolve crash on nil user data"
git commit -m "refactor: extract networking layer to separate service"
git commit -m "docs: update README with setup instructions"
```

## Protected Branches

### main
- ✅ Require pull request
- ✅ Require status checks (if CI exists)
- ✅ Cannot force push
- ✅ Cannot delete

### develop (optional protection)
- ✅ Require pull request
- ⚠️ Can force push with approval
- ❌ Can delete (but shouldn't)

## Common Commands

### Check Current Status
```bash
git status
git branch -a  # Show all branches
```

### Update Local Branch
```bash
git checkout develop
git pull origin develop
```

### Rebase Feature on Latest Develop
```bash
git checkout feature/my-feature
git rebase develop
# Resolve conflicts if any
git push --force-with-lease origin feature/my-feature
```

### View PR List
```bash
gh pr list
gh pr status
```

### Checkout PR Locally
```bash
gh pr checkout 123
```

## Emergency Procedures

### Revert Last Commit (not pushed)
```bash
git reset --soft HEAD~1
```

### Revert Last Commit (already pushed)
```bash
git revert HEAD
git push origin feature/my-feature
```

### Abandon Feature Branch
```bash
git checkout develop
git branch -D feature/abandoned-work
git push origin --delete feature/abandoned-work
```

### Sync Fork with Upstream
```bash
git remote add upstream https://github.com/original/repo.git
git fetch upstream
git checkout develop
git merge upstream/develop
git push origin develop
```

## Best Practices

1. **Keep branches short-lived** - Merge within 1-3 days
2. **Pull before push** - Always `git pull` before `git push`
3. **Commit often** - Small, atomic commits
4. **Descriptive names** - Branch and commit names should be clear
5. **Test before PR** - Ensure code builds and tests pass
6. **Review your own PR** - Check diff before asking for review
7. **Delete merged branches** - Keep repository clean
8. **Never commit secrets** - Use .gitignore for sensitive files
9. **Use PR templates** - Consistent PR descriptions
10. **Tag releases** - Use semantic versioning (v1.0.0)

## GitHub Settings

### Repository Settings
```
Settings → General → Default branch: develop
Settings → Branches → Branch protection rules:
  - main: Protected
  - develop: Default
```

### Branch Protection (main)
```
Branch name pattern: main
✅ Require a pull request before merging
✅ Require approvals: 1
✅ Dismiss stale PR approvals when new commits are pushed
✅ Require status checks to pass before merging
✅ Require branches to be up to date before merging
✅ Require conversation resolution before merging
✅ Do not allow bypassing the above settings
✅ Restrict who can push to matching branches
```

### Auto-delete Branches
```
Settings → General → Pull Requests
✅ Automatically delete head branches
```

## Troubleshooting

### "Your branch is behind 'origin/develop'"
```bash
git pull origin develop
```

### "Your branch and 'origin/feature' have diverged"
```bash
# If you're the only one on this branch:
git pull --rebase origin feature/my-feature

# If others are working on it:
git pull origin feature/my-feature
# Resolve merge conflicts
```

### Accidentally committed to develop
```bash
# Create new branch with current work
git branch feature/accidental-work

# Reset develop to match origin
git checkout develop
git reset --hard origin/develop

# Switch to new branch
git checkout feature/accidental-work
git push origin feature/accidental-work
```

### Need to update PR with new commits
```bash
# Just push more commits to the same branch
git checkout feature/my-feature
git commit -m "Address review feedback"
git push origin feature/my-feature
# PR automatically updates
```
