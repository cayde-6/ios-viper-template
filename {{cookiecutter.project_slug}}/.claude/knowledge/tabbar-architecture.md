# TabBar Architecture

## Overview

The TabBar uses a special dependency injection pattern to enable lazy loading of tab modules.

## TabBarDependencies

Contains builder closures for each tab:

```swift
struct TabBarDependencies {
    let homeBuilder: () -> AnyView
    let statisticsBuilder: () -> AnyView
    let settingsBuilder: () -> AnyView

    static func makeDefault() -> TabBarDependencies {
        TabBarDependencies(
            homeBuilder: {
                AnyView(HomeModuleImpl.build())
            },
            statisticsBuilder: {
                AnyView(StatisticsModuleImpl.build())
            },
            settingsBuilder: {
                AnyView(SettingsModuleImpl.build())
            }
        )
    }
}
```

## Lazy Module Creation

Modules are created only when tabs are selected:

```swift
TabView(selection: $viewModel.selectedTab) {
    Tab("Home", systemImage: "house.fill", value: TabItem.home) {
        NavigationStack {
            dependencies.homeBuilder()  // Created here!
        }
    }
}
```

**Benefits:**
- ✅ Faster app startup
- ✅ Lower memory usage
- ✅ Modules created on-demand
- ✅ Easy to add/remove tabs

## Adding a New Tab

1. **Create the module** following VIPER pattern

2. **Add TabItem case** in `Models/TabBar/TabItem.swift`:
```swift
enum TabItem: String, CaseIterable {
    case home = "Home"
    case profile = "Profile"  // New tab
    case settings = "Settings"

    var icon: String {
        case .profile: return "person.fill"
    }
}
```

3. **Update TabBarDependencies** in `Modules/TabBar/TabBarDependencies.swift`:
```swift
struct TabBarDependencies {
    let profileBuilder: () -> AnyView  // Add builder

    static func makeDefault() -> TabBarDependencies {
        TabBarDependencies(
            profileBuilder: {
                AnyView(ProfileModuleImpl.build())
            }
        )
    }
}
```

4. **Add Tab in TabBarView**:
```swift
Tab(TabItem.profile.rawValue, systemImage: TabItem.profile.icon, value: TabItem.profile) {
    NavigationStack {
        dependencies.profileBuilder()
    }
}
```

## TabBarEnvironment

Provides SwiftUI Environment keys for passing state:

```swift
@Environment(\.tabBarViewModel) private var tabBarViewModel
```

Use this to access TabBar state from child views.

## Navigation in Tabs

Each tab has its own `NavigationStack`:
- Independent navigation history
- Separate back button behavior
- Can push multiple screens

To navigate within a tab:
```swift
// In Router
func navigateToDetail() {
    let detailView = DetailModuleImpl.build(
        navigationController: navigationController
    )
    // Push to navigation controller
}
```
