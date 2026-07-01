# Troubleshooting Guide

## Build Errors

### "Cannot find type 'UINavigationController' in scope"

**Problem:** Module files are importing `Foundation` instead of `UIKit`

**Solution:** Change imports in all `*Module.swift` files:
```swift
// ❌ Wrong
import Foundation

// ✅ Correct
import UIKit
```

**Affected files:**
- `*Module.swift` files in all modules

### "duplicate output file Info.plist"

**Problem:** Xcode is trying to generate Info.plist while we have a custom one

**Solution:**
1. Set `GENERATE_INFOPLIST_FILE = NO` in build settings
2. Ensure `INFOPLIST_FILE = Elvi/Sources/Resources/Info.plist`
3. Add `Sources/Resources/Info.plist` to `membershipExceptions` in project.pbxproj

### "Multiple commands produce Info.plist"

**Problem:** Info.plist is being copied as a resource and processed

**Solution:** Add exception in `project.pbxproj`:
```
membershipExceptions = (
    Sources/Resources/Info.plist,
);
```

## Runtime Errors

### App shows blank screen

**Check:**
1. SceneDelegate is calling correct module: `TabBarModuleImpl.build()`
2. Window is set as key and visible: `window.makeKeyAndVisible()`
3. Console logs show module initialization

### Tab content not showing

**Check:**
1. Builder closure in TabBarDependencies returns correct module
2. Module `build()` method creates all components
3. View's `body` has actual content

### Navigation not working

**Check:**
1. Router has `weak var navigationController: UINavigationController?`
2. NavigationController is passed to module builder
3. Each tab has `NavigationStack` wrapper

## Observable Pattern Issues

### ViewModel changes not updating UI

**Problem:** View not observing ViewModel correctly

**Solution:** Ensure View uses `@State private var viewModel`:
```swift
struct ExampleView: View {
    @State private var viewModel: ExampleViewModel  // Must be @State

    init(viewModel: ExampleViewModel) {
        _viewModel = State(wrappedValue: viewModel)  // Correct initialization
    }
}
```

### "Published changes from background threads"

**Problem:** ViewModel updated from background thread

**Solution:** Use `@MainActor` in Presenter:
```swift
@MainActor
func loadData() async {
    viewModel.isLoading = true
    // async work
    viewModel.isLoading = false
}
```

## Xcode Project Issues

### Files not compiling after moving

**Problem:** Xcode uses file system synchronization

**Solution:**
1. Files are auto-discovered in `Elvi/` folder
2. No need to manually add to project
3. Clean build folder: `Cmd+Shift+K`

### Simulator deployment target errors

**Problem:** Deployment target mismatch

**Solution:** Use available simulator:
```bash
# List available simulators
xcrun simctl list devices

# Use iPhone 17 or another available device
xcodebuild -destination 'platform=iOS Simulator,name=iPhone 17'
```

## Common Mistakes

### 1. Forgetting to call presenter.onAppear()

```swift
// ❌ Missing onAppear
var body: some View {
    Text(viewModel.title)
}

// ✅ Correct
var body: some View {
    Text(viewModel.title)
        .onAppear { presenter.onAppear() }
}
```

### 2. Strong reference to UINavigationController

```swift
// ❌ Causes retain cycle
var navigationController: UINavigationController?

// ✅ Weak reference
weak var navigationController: UINavigationController?
```

### 3. Business logic in View

```swift
// ❌ Wrong - logic in View
var body: some View {
    Button("Load") {
        viewModel.data = loadData()  // Don't do this!
    }
}

// ✅ Correct - delegate to Presenter
var body: some View {
    Button("Load") {
        presenter.loadData()
    }
}
```

### 4. Not using protocol for Presenter

```swift
// ❌ Hard to test
private let presenter: ExamplePresenterImpl

// ✅ Protocol-based, testable
private let presenter: ExamplePresenter
```
