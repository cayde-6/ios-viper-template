# Swift 6 & Structured Concurrency - Quick Reference

**⚡ Use `swift-concurrency` skill for detailed guidance**

The project has the `swift-concurrency` skill with 13 comprehensive references on actors, tasks, threading, migration, performance, testing, Core Data, and more.

**Invoke skill when discussing:** async/await, actors, @MainActor, Sendable, data races, Swift 6 migration, concurrency errors

## Swift 6 Key Changes

1. **Complete Data Race Safety** - Enforced at compile time
2. **Sendable Protocol** - Required for crossing isolation boundaries
3. **Actor Isolation** - Strict enforcement with `await` required
4. **@MainActor** - Required for UI code

## Common Patterns

### ViewModel (@MainActor)
```swift
@Observable
@MainActor
final class ViewModel {
    var title: String = ""
}
```

### Presenter (async operations)
```swift
@MainActor
protocol Presenter {
    func loadData() async
}

final class PresenterImpl: Presenter {
    @MainActor
    func loadData() async {
        viewModel.isLoading = true
        let data = await networkService.fetch()  // Off main actor
        viewModel.data = data  // Back on main actor
    }
}
```

### Service (actor for thread-safety)
```swift
actor NetworkService {
    private var cache: [URL: Data] = [:]

    func fetch(url: URL) async throws -> Data {
        if let cached = cache[url] { return cached }
        let data = try await URLSession.shared.data(from: url).0
        cache[url] = data
        return data
    }
}
```

### Task Groups (parallel operations)
```swift
await withThrowingTaskGroup(of: Result.self) { group in
    for item in items {
        group.addTask { await process(item) }
    }
    for try await result in group {
        results.append(result)
    }
}
```

## Migration Checklist

- [ ] Global vars → actors or @unchecked Sendable
- [ ] ViewModels → @MainActor
- [ ] Non-Sendable types → make Sendable or use only isolated values
- [ ] Task closures → check captured state
- [ ] Missing await → add for actor properties
- [ ] Closure sendability → mark @Sendable

## Quick Reference

### ✅ Do
- Use actors for shared mutable state
- Mark UI code @MainActor
- Make types Sendable when crossing boundaries
- Use structured concurrency (async let, task groups)
- Check Task.isCancelled
- Await actor-isolated members

### ❌ Don't
- Global mutable vars without protection
- Capture mutable state in Task
- Pass non-Sendable to actors
- Forget @MainActor on ViewModels
- Ignore cancellation

## Project Pattern

```swift
// ✅ Our VIPER pattern
@MainActor
protocol ExamplePresenter {
    func onAppear() async
}

@Observable
@MainActor
final class ExampleViewModel {
    var data: String = ""
}

actor ExampleService {
    func fetch() async -> Data { ... }
}
```

**For detailed patterns, error triage, and migration guide → use `swift-concurrency` skill**
