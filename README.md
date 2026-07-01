# 📱 Swift Module Template

A modern, production-ready iOS application template built with **VIPER architecture**, **Swift 6**, and **Claude Code integration**.

## ✨ Features

### 🏗️ Architecture
- **VIPER Pattern** - Scalable, testable, and maintainable architecture
- **Protocol-Oriented** - Easy mocking and testing
- **Dependency Injection** - Clean component separation
- **Swift 6 Ready** - Modern concurrency with async/await and actors

### 🤖 Claude Code Integration
Pre-configured with 7 specialized AI agents:
- `viper-builder` - Generate new VIPER modules
- `swift6-auditor` - Check Swift 6 compliance and data race safety
- `architecture-reviewer` - Verify VIPER architecture patterns
- `ios-feature-implementer` - Implement iOS frameworks (StoreKit, MapKit, etc.)
- `troubleshooter` - Debug build and runtime errors
- `tabbar-orchestrator` - Manage TabBar structure
- `git-flow-manager` - Automate Git Flow workflow

### 📚 Knowledge Base
49 documentation files including:
- VIPER architecture patterns
- Swift 6 concurrency guides
- iOS 18+ framework documentation
- Apple Design Language guides
- Best practices and troubleshooting

### 🎨 UI Frameworks
- SwiftUI support
- UIKit support
- Hybrid SwiftUI/UIKit projects

### 🧪 Testing
- Unit tests setup
- UI tests setup
- Test-driven development ready

## 📋 Prerequisites

- **macOS** 14.0+
- **Xcode** 15.0+
- **Python** 3.8+
- **Cookiecutter** 2.0+ (`pip install cookiecutter`)
- **xcodegen** (optional, for automatic project generation: `brew install xcodegen`)

## 🚀 Quick Start

### 1. Generate Your Project

```bash
cookiecutter gh:cayde-6/swift-module-template
```

Or from local clone:

```bash
cookiecutter path/to/iOSApp/
```

### 2. Answer the Prompts

```
project_name [iOSApp]: MyAwesomeApp
organization_name [Your Organization]: Acme Inc
author_name [Your Name]: John Doe
bundle_identifier [com.acme.myawesomeapp]:
ios_deployment_target [18.0]: 17.0
swift_version [6.0]:
include_swiftui_previews [yes]:
include_tests [yes]:
include_claude_agents [yes]:
...
```

### 3. Open and Build

```bash
cd MyAwesomeApp
open MyAwesomeApp.xcodeproj  # or run xcodegen if project wasn't auto-generated
```

## 🎛️ Configuration Options

### Basic Settings
| Option | Description | Default |
|--------|-------------|---------|
| `project_name` | Display name of your app | iOSApp |
| `organization_name` | Your company/organization | Your Organization |
| `author_name` | Your name | Your Name |
| `bundle_identifier` | iOS bundle identifier | Auto-generated |
| `project_description` | Short description | A modern iOS application |

### Technical Settings
| Option | Description | Options |
|--------|-------------|---------|
| `ios_deployment_target` | Minimum iOS version | 15.0, 16.0, 17.0, **18.0** |
| `swift_version` | Swift language version | 5.9, 5.10, **6.0** |
| `use_swiftui` | Include SwiftUI support | **yes**, no |
| `use_uikit` | Include UIKit support | **yes**, no |

### Features
| Option | Description | Default |
|--------|-------------|---------|
| `include_swiftui_previews` | SwiftUI preview support | yes |
| `include_tests` | Unit tests | yes |
| `include_ui_tests` | UI tests | yes |
| `include_claude_agents` | Claude Code agents | yes |
| `include_viper_example_module` | Example VIPER module | yes |

### Architecture Components
| Option | Description | Default |
|--------|-------------|---------|
| `include_network_layer` | Networking layer with services | yes |
| `include_core_data` | Core Data stack | no |
| `include_keychain_wrapper` | Keychain wrapper | no |

### iOS Frameworks
| Option | Description | Default |
|--------|-------------|---------|
| `include_storekit` | In-app purchases | no |
| `include_mapkit` | Maps integration | no |
| `include_healthkit` | Health data access | no |

## 📁 Project Structure

```
MyAwesomeApp/
├── MyAwesomeApp/
│   └── Sources/
│       ├── Application/
│       │   ├── AppDelegate.swift
│       │   └── SceneDelegate.swift
│       ├── Modules/
│       │   └── MainScreen/          # Example VIPER module
│       │       ├── MainScreenModule.swift
│       │       ├── MainScreenView.swift
│       │       ├── MainScreenViewModel.swift
│       │       ├── MainScreenPresenter.swift
│       │       └── MainScreenRouter.swift
│       ├── Models/
│       ├── Network/
│       │   ├── Services/
│       │   └── Parsing/
│       ├── Extensions/
│       ├── UI/
│       └── Resources/
│           ├── Assets.xcassets/
│           ├── LaunchScreen.storyboard
│           └── Info.plist
├── MyAwesomeAppTests/
├── MyAwesomeAppUITests/
└── .claude/                          # Claude Code configuration
    ├── agents/                       # Specialized AI agents
    └── knowledge/                    # Documentation & guides
```

## 🏗️ VIPER Architecture

### Module Structure

Each feature is organized as a VIPER module with 5 components:

```swift
// 1. Module - Assembly point
final class ExampleModuleImpl {
    static func build() -> ExampleView {
        let viewModel = ExampleViewModel()
        let router = ExampleRouterImpl()
        let presenter = ExamplePresenterImpl(viewModel: viewModel, router: router)
        return ExampleView(viewModel: viewModel, presenter: presenter)
    }
}

// 2. View - SwiftUI view
struct ExampleView: View {
    @State private var viewModel: ExampleViewModel
    private let presenter: ExamplePresenter
}

// 3. ViewModel - UI state (@Observable)
@Observable
final class ExampleViewModel {
    var title: String = ""
}

// 4. Presenter - Business logic
protocol ExamplePresenter {
    func onAppear()
}

// 5. Router - Navigation
protocol ExampleRouter {
    func navigateTo(...)
}
```

## 🤖 Using Claude Code Agents

### Creating a New Module

```bash
# In Claude Code
"Create a Profile module with user info display"
```

The `viper-builder` agent will generate all 5 VIPER files automatically.

### Checking Swift 6 Compliance

```bash
"Check ProfilePresenter for Swift 6 compliance"
```

The `swift6-auditor` will scan for:
- Data race safety
- Sendable conformance
- @MainActor usage
- Actor isolation issues

### Implementing iOS Features

```bash
"Add Liquid Glass effect to the button"
```

The `ios-feature-implementer` will read Apple's documentation and implement the feature correctly.

### Architecture Review

```bash
"Review the Profile module architecture"
```

The `architecture-reviewer` will verify:
- VIPER pattern compliance
- Dependency injection
- Protocol usage
- Component responsibilities

## 🧪 Testing

### Run Unit Tests

```bash
⌘U in Xcode
# or
xcodebuild test -scheme MyAwesomeApp -destination 'platform=iOS Simulator,name=iPhone 15'
```

### Run UI Tests

```bash
# Select UI Test scheme in Xcode
⌘U
```

## 📦 Adding Dependencies

### Swift Package Manager (Recommended)

```
File → Add Package Dependencies...
```

### CocoaPods

```bash
pod init
# Edit Podfile
pod install
```

## 🔧 Customization

### Changing App Icon

1. Open `Assets.xcassets`
2. Select `AppIcon`
3. Drag your icons to the appropriate slots

### Updating Info.plist

Edit `Sources/Resources/Info.plist` to add:
- Privacy permissions
- URL schemes
- Background modes
- etc.

### Adding New Modules

```bash
# Using Claude Code
"Create a Settings module"

# Or manually copy MainScreen/ and rename files
```

## 🚀 Deployment

### App Store

1. Archive your app: `Product → Archive`
2. Distribute via App Store Connect
3. Follow Apple's submission guidelines

### TestFlight

1. Archive your app
2. Upload to App Store Connect
3. Add internal/external testers

## 🐛 Troubleshooting

### "Duplicate Info.plist" Error

If you see Xcode errors about duplicate Info.plist:
```bash
# Remove Info.plist from build phases
# Keep only in Resources folder
```

### xcodegen Not Found

```bash
brew install xcodegen
cd MyAwesomeApp
xcodegen generate
```

### Swift 6 Migration Issues

Use the `swift6-auditor` Claude agent:
```bash
"Check all files for Swift 6 compliance"
```

## 📚 Resources

### Documentation
- [VIPER Pattern Guide](.claude/knowledge/viper-pattern.md)
- [Swift 6 Concurrency](.claude/knowledge/swift6-concurrency.md)
- [Claude Agents System](.claude/agents/AGENTS-SYSTEM.md)

### External Resources
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Swift Evolution](https://github.com/apple/swift-evolution)
- [iOS Development Best Practices](https://github.com/futurice/ios-good-practices)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This template is available under the MIT License.

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/cayde-6/swift-module-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/cayde-6/swift-module-template/discussions)

## 🙏 Acknowledgments

- Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- Inspired by modern iOS best practices
- Powered by [Claude Code](https://claude.ai/code)

---

Made with ❤️ for the iOS community
