# VIPER Pattern Guide

## Overview

VIPER is an architectural pattern used in this project for building modular, testable iOS applications.

## Components

### View
- SwiftUI view
- Renders UI based on ViewModel state
- Forwards user actions to Presenter
- Uses `@State private var viewModel`
- Immutable reference to `presenter`

```swift
struct ExampleView: View {
    @State private var viewModel: ExampleViewModel
    private let presenter: ExamplePresenter

    var body: some View {
        Text(viewModel.title)
            .onAppear { presenter.onAppear() }
    }
}
```

### Interactor (Presenter in our case)
- Contains business logic
- Updates ViewModel
- Coordinates with Router and Services
- Protocol-based for testability

```swift
protocol ExamplePresenter {
    var viewModel: ExampleViewModel { get }
    func onAppear()
}

final class ExamplePresenterImpl: ExamplePresenter {
    let viewModel: ExampleViewModel
    private let router: ExampleRouter

    func onAppear() {
        // Business logic here
        viewModel.title = "Loaded"
    }
}
```

### Presenter (ViewModel in our case)
- UI state container
- Uses `@Observable` macro
- No business logic
- Updated by Interactor/Presenter

```swift
@Observable
final class ExampleViewModel {
    var title: String = ""
    var isLoading: Bool = false
}
```

### Entity (Models)
- Data structures
- Located in `Elvi/Sources/Models/`
- Domain-specific (Auth, Email, etc.)

### Router
- Navigation logic
- Weak reference to UINavigationController
- Creates and presents new modules

```swift
protocol ExampleRouter {
    func navigateToDetail()
}

final class ExampleRouterImpl: ExampleRouter {
    weak var navigationController: UINavigationController?

    func navigateToDetail() {
        let detailView = DetailModuleImpl.build()
        // Navigation logic
    }
}
```

## Module Builder Pattern

Every module has a `XxxModuleImpl` class with a `static func build()`:

```swift
final class ExampleModuleImpl {
    static func build(
        navigationController: UINavigationController? = nil
    ) -> ExampleView {
        let viewModel = ExampleViewModel()
        let router = ExampleRouterImpl(navigationController: navigationController)
        let presenter = ExamplePresenterImpl(viewModel: viewModel, router: router)
        return ExampleView(viewModel: viewModel, presenter: presenter)
    }
}
```

## Key Principles

1. **Single Responsibility** - Each component has one job
2. **Dependency Injection** - Dependencies passed through constructors
3. **Protocol-Based** - Easy to test and mock
4. **Immutability** - Prefer immutable references where possible
5. **Weak References** - Avoid retain cycles with UINavigationController

## When to Use

- Creating new features/screens
- Need testability
- Complex business logic
- Multiple navigation paths

## Anti-Patterns to Avoid

❌ Business logic in View
❌ Direct ViewModel updates from View
❌ Strong references to UINavigationController
❌ God objects (too many responsibilities)
❌ Skipping protocols (makes testing hard)
