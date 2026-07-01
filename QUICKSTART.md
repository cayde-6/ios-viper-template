# ⚡ Quick Start Guide

Get up and running with Swift Module Template in 5 minutes.

## Prerequisites Check

```bash
# Check Python version (need 3.8+)
python3 --version

# Check Xcode version (need 15.0+)
xcodebuild -version

# Install cookiecutter
pip install cookiecutter
```

## Step 1: Generate Project (1 min)

```bash
cookiecutter gh:cayde-6/swift-module-template
```

Answer the prompts:
```
project_name [iOSApp]: MyApp
organization_name [Your Organization]: MyCompany
author_name [Your Name]: John Doe
# ... press Enter for defaults on remaining prompts
```

## Step 2: Open in Xcode (1 min)

```bash
cd MyApp

# If xcodegen is installed (recommended)
open MyApp.xcodeproj

# If not, install xcodegen first
brew install xcodegen
xcodegen generate
open MyApp.xcodeproj
```

## Step 3: Build & Run (1 min)

In Xcode:
1. Select a simulator (iPhone 15)
2. Press `⌘R` (or click the Play button)
3. Watch your app launch! 🎉

## Step 4: Explore the Code (2 min)

### Check out the example VIPER module

**Navigate to:** `MyApp/Sources/Modules/MainScreen/`

You'll see 5 files:
- `MainScreenModule.swift` - Assembly
- `MainScreenView.swift` - SwiftUI view
- `MainScreenViewModel.swift` - State (@Observable)
- `MainScreenPresenter.swift` - Business logic
- `MainScreenRouter.swift` - Navigation

### Understand the flow

```
User Interaction → View → Presenter → ViewModel → View Updates
                              ↓
                           Router (Navigation)
```

## Next Steps

### Create Your First Module

If you included Claude agents, use Claude Code:

```
"Create a Profile module with user name and avatar"
```

Or copy the example manually:

```bash
cd MyApp/Sources/Modules
cp -R MainScreen Profile
# Rename all MainScreen references to Profile
```

### Add Dependencies

#### Swift Package Manager (Recommended)

In Xcode:
```
File → Add Package Dependencies...
```

Popular packages:
- Alamofire: `https://github.com/Alamofire/Alamofire.git`
- Kingfisher: `https://github.com/onevcat/Kingfisher.git`

#### CocoaPods

```bash
cd MyApp
pod init
# Edit Podfile
pod install
open MyApp.xcworkspace  # Note: workspace, not project
```

### Run Tests

Press `⌘U` in Xcode or:

```bash
xcodebuild test \
  -scheme MyApp \
  -destination 'platform=iOS Simulator,name=iPhone 15'
```

### Setup Git Remote

```bash
git remote add origin git@github.com:yourusername/myapp.git
git push -u origin main
```

## Common First Tasks

### 1. Change App Icon

1. Open `Assets.xcassets`
2. Select `AppIcon`
3. Drag your icons (1024x1024 recommended for all)

### 2. Update Bundle ID

In Xcode:
1. Select project in Navigator
2. Select your target
3. General tab → Bundle Identifier
4. Change to your domain (e.g., `com.mycompany.myapp`)

### 3. Change App Name

In Xcode:
1. Select project
2. Select target
3. General tab → Display Name
4. Or edit `Info.plist` → `CFBundleDisplayName`

### 4. Add Permissions (if needed)

Edit `Sources/Resources/Info.plist`:

```xml
<!-- Camera permission -->
<key>NSCameraUsageDescription</key>
<string>We need camera access to take photos</string>

<!-- Location permission -->
<key>NSLocationWhenInUseUsageDescription</key>
<string>We need your location to show nearby places</string>
```

## Troubleshooting

### "No such module" error

```bash
# Clean and rebuild
⌘⇧K  # Clean
⌘B   # Build
```

### Simulator not showing

```bash
# Reset simulators
xcrun simctl erase all
```

### Build fails

```bash
# Delete derived data
rm -rf ~/Library/Developer/Xcode/DerivedData
# Rebuild
⌘B
```

### Cookiecutter fails

```bash
# Update cookiecutter
pip install --upgrade cookiecutter

# Retry with verbose output
cookiecutter gh:cayde-6/swift-module-template --verbose
```

## Learning Resources

### Architecture
- Read [.claude/knowledge/viper-pattern.md]({{cookiecutter.project_slug}}/.claude/knowledge/viper-pattern.md)
- Understand separation of concerns
- Learn protocol-oriented programming

### Claude Agents
- Explore [.claude/agents/AGENTS-SYSTEM.md]({{cookiecutter.project_slug}}/.claude/agents/AGENTS-SYSTEM.md)
- Try agent commands
- Create custom agents

### Swift 6
- Study async/await patterns
- Learn about Sendable and actors
- Understand @MainActor

### Apple Resources
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Swift Documentation](https://swift.org/documentation/)
- [WWDC Videos](https://developer.apple.com/videos/)

## Example Projects

Check out these examples for inspiration:

### Minimal SwiftUI App
```bash
cookiecutter gh:cayde-6/swift-module-template --no-input \
  project_name="MinimalApp" \
  use_swiftui="yes" \
  use_uikit="no" \
  include_tests="no" \
  include_claude_agents="no"
```

### Full-Featured App
```bash
cookiecutter gh:cayde-6/swift-module-template --no-input \
  project_name="FullApp" \
  ios_deployment_target="17.0" \
  swift_version="6.0" \
  include_tests="yes" \
  include_ui_tests="yes" \
  include_claude_agents="yes"
```

## Keyboard Shortcuts (Xcode)

Essential shortcuts to know:

| Action | Shortcut |
|--------|----------|
| Build | `⌘B` |
| Run | `⌘R` |
| Test | `⌘U` |
| Clean | `⌘⇧K` |
| Find | `⌘F` |
| Find in Project | `⌘⇧F` |
| Open Quickly | `⌘⇧O` |
| Show/Hide Navigator | `⌘0` |
| Show/Hide Inspector | `⌘⌥0` |
| Documentation | `⌥ + Click` |

## Need Help?

- **Documentation**: Read [README.md](README.md) and [USAGE.md](USAGE.md)
- **Issues**: [GitHub Issues](https://github.com/cayde-6/swift-module-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/cayde-6/swift-module-template/discussions)

## What's Next?

1. ✅ Build your first feature
2. ✅ Write tests for it
3. ✅ Use Claude agents to speed up development
4. ✅ Deploy to TestFlight
5. ✅ Submit to App Store

**Happy coding! 🚀**
