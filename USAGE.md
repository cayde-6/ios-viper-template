# Usage Examples

## Basic Usage

### Generate a Simple Project

```bash
cookiecutter gh:cayde-6/ios-viper-template
```

Answer the prompts with default values or customize as needed.

## Advanced Usage

### Non-Interactive Mode

Create a config file `my-project.yaml`:

```yaml
default_context:
  project_name: "MyAwesomeApp"
  organization_name: "Acme Inc"
  author_name: "John Doe"
  bundle_identifier: "com.acme.myawesomeapp"
  ios_deployment_target: "17.0"
  swift_version: "6.0"
  include_swiftui_previews: "yes"
  include_tests: "yes"
  include_ui_tests: "yes"
  include_claude_agents: "yes"
  include_viper_example_module: "yes"
  use_swiftui: "yes"
  use_uikit: "no"
```

Then run:

```bash
cookiecutter gh:cayde-6/ios-viper-template --config-file my-project.yaml --no-input
```

### Override Single Values

```bash
cookiecutter gh:cayde-6/ios-viper-template \
  project_name="CoolApp" \
  ios_deployment_target="16.0"
```

### Use Specific Branch/Tag

```bash
# Use specific branch
cookiecutter gh:cayde-6/ios-viper-template --checkout develop

# Use specific tag
cookiecutter gh:cayde-6/ios-viper-template --checkout v1.0.0
```

## Common Scenarios

### Scenario 1: SwiftUI-Only Project

```yaml
use_swiftui: "yes"
use_uikit: "no"
include_swiftui_previews: "yes"
ios_deployment_target: "17.0"
swift_version: "6.0"
```

### Scenario 2: UIKit-Only Project

```yaml
use_swiftui: "no"
use_uikit: "yes"
include_swiftui_previews: "no"
ios_deployment_target: "15.0"
swift_version: "5.10"
```

### Scenario 3: Minimal Project (No Tests, No Agents)

```yaml
include_tests: "no"
include_ui_tests: "no"
include_claude_agents: "no"
include_viper_example_module: "no"
architecture_features:
  include_network_layer: "no"
```

### Scenario 4: Full-Featured Project

```yaml
include_tests: "yes"
include_ui_tests: "yes"
include_claude_agents: "yes"
include_viper_example_module: "yes"
architecture_features:
  include_network_layer: "yes"
  include_core_data: "yes"
  include_keychain_wrapper: "yes"
ios_frameworks:
  include_storekit: "yes"
  include_mapkit: "yes"
```

### Scenario 5: E-commerce App

```yaml
project_name: "ShopApp"
ios_deployment_target: "17.0"
swift_version: "6.0"
use_swiftui: "yes"
architecture_features:
  include_network_layer: "yes"
  include_keychain_wrapper: "yes"
ios_frameworks:
  include_storekit: "yes"
```

### Scenario 6: Health & Fitness App

```yaml
project_name: "FitTracker"
ios_deployment_target: "17.0"
swift_version: "6.0"
use_swiftui: "yes"
architecture_features:
  include_network_layer: "yes"
ios_frameworks:
  include_healthkit: "yes"
  include_mapkit: "yes"
```

## Post-Generation Tasks

### 1. After Generation - First Build

```bash
cd MyAwesomeApp

# If xcodegen was used
open MyAwesomeApp.xcodeproj

# If xcodegen wasn't installed
xcodegen generate  # or manually create project in Xcode
open MyAwesomeApp.xcodeproj

# Build the project
# Press ⌘B in Xcode
```

### 2. Adding Your First Feature Module

Using Claude Code:

```
"Create a Profile module with user avatar and settings"
```

Or manually:

```bash
# Copy example module
cp -R Sources/Modules/MainScreen Sources/Modules/Profile

# Rename files and update class names
# MainScreen → Profile in all files
```

### 3. Setting Up Git Remote

```bash
cd MyAwesomeApp
git remote add origin git@github.com:yourusername/myawesomeapp.git
git push -u origin main
```

### 4. Enabling Claude Code

If you included Claude agents:

```bash
# Claude Code will automatically detect .claude/ directory
# Start Claude Code in the project directory
claude-code

# Try commands like:
"Create a Settings module"
"Check code for Swift 6 compliance"
"Review architecture"
```

### 5. Adding Dependencies

#### Swift Package Manager

```
File → Add Package Dependencies...
```

Common packages:
- **Alamofire**: `https://github.com/Alamofire/Alamofire.git`
- **Kingfisher**: `https://github.com/onevcat/Kingfisher.git`
- **SwiftLint**: `https://github.com/realm/SwiftLint.git`

#### CocoaPods

```bash
pod init

# Edit Podfile
pod 'Alamofire'
pod 'Kingfisher'

pod install
open MyAwesomeApp.xcworkspace  # Note: .xcworkspace, not .xcodeproj
```

### 6. Running Tests

```bash
# Unit tests
⌘U in Xcode

# Or via command line
xcodebuild test \
  -scheme MyAwesomeApp \
  -destination 'platform=iOS Simulator,name=iPhone 15'
```

### 7. Building for Release

```bash
# In Xcode
Product → Archive

# Select distribution method:
# - App Store Connect
# - Ad Hoc
# - Enterprise
# - Development
```

## CI/CD Integration

### GitHub Actions

Create `.github/workflows/ios.yml`:

```yaml
name: iOS CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  build:
    runs-on: macos-latest

    steps:
    - uses: actions/checkout@v3

    - name: Select Xcode version
      run: sudo xcode-select -s /Applications/Xcode_15.0.app

    - name: Build
      run: xcodebuild build -scheme MyAwesomeApp -destination 'platform=iOS Simulator,name=iPhone 15'

    - name: Test
      run: xcodebuild test -scheme MyAwesomeApp -destination 'platform=iOS Simulator,name=iPhone 15'
```

### fastlane

```bash
# Install fastlane
brew install fastlane

# Initialize
cd MyAwesomeApp
fastlane init

# Create lanes in Fastfile
# See fastlane documentation for examples
```

## Tips & Tricks

### Regenerate Project File

If your `.xcodeproj` gets corrupted:

```bash
# If using xcodegen
xcodegen generate

# Otherwise, recreate manually in Xcode
```

### Update All Swift Files Headers

```bash
find . -name "*.swift" -exec sed -i '' 's/iOSApp/MyNewName/g' {} +
```

### Clean Derived Data

```bash
rm -rf ~/Library/Developer/Xcode/DerivedData
```

### Reset Simulators

```bash
xcrun simctl erase all
```

## Troubleshooting

### "No such module" Error

```bash
# Clean build folder
⌘⇧K in Xcode

# Clean derived data
rm -rf ~/Library/Developer/Xcode/DerivedData

# Rebuild
⌘B
```

### Signing Issues

1. Open project settings (⌘1)
2. Select your target
3. Signing & Capabilities tab
4. Select your team
5. Enable "Automatically manage signing"

### Claude Agents Not Working

```bash
# Verify .claude/ directory exists
ls -la .claude/

# Check agent files
ls -la .claude/agents/

# Restart Claude Code
```

## Next Steps

1. Read the [Architecture Documentation](.claude/knowledge/viper-pattern.md)
2. Explore [Claude Agents](.claude/agents/AGENTS-SYSTEM.md)
3. Check out [Apple's HIG](https://developer.apple.com/design/human-interface-guidelines/)
4. Join the community discussions

## Additional Resources

- [Xcode Keyboard Shortcuts](https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/xcode_help-command_shortcuts/)
- [Swift Style Guide](https://google.github.io/swift/)
- [iOS Security Guide](https://support.apple.com/guide/security/welcome/web)
