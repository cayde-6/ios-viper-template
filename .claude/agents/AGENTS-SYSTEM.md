# Specialized Agents System

This project uses specialized sub-agents for specific tasks. The main Claude instance orchestrates these agents.

## Available Agents

### 1. viper-builder
**Purpose:** Create new VIPER modules following project architecture

**When to use:**
- "Create a new module called X"
- "Add a Profile module"
- "Build a Login screen using VIPER"

**Knowledge:**
- viper-pattern.md
- tabbar-architecture.md (if adding to TabBar)

**Capabilities:**
- Creates Module.swift, View.swift, ViewModel.swift, Presenter.swift, Router.swift
- Wires dependencies correctly
- Follows project naming conventions
- Adds to TabBar if requested

**Example invocation:**
```
Main: User wants Profile module
→ Launch viper-builder agent with "Create Profile module with user info display"
→ Agent creates all 5 VIPER files
→ Returns list of created files
Main: Verify files and inform user
```

---

### 2. swift6-auditor
**Purpose:** Check code for Swift 6 compliance and data race safety

**When to use:**
- "Check this code for Swift 6"
- "Is this code data race safe?"
- "Review concurrency issues"
- User mentions: @MainActor, Sendable, actor isolation

**Knowledge:**
- swift6-concurrency.md
- swift-concurrency skill (13 reference files)

**Capabilities:**
- Scans code for data races
- Checks Sendable conformance
- Verifies @MainActor usage
- Identifies isolation issues
- Suggests fixes with before/after examples

**Example invocation:**
```
Main: User asks "check Presenter for Swift 6"
→ Launch swift6-auditor with file path
→ Agent reads file, checks against Swift 6 rules
→ Returns checklist with ✅/❌ and fixes
Main: Show report to user
```

---

### 3. architecture-reviewer
**Purpose:** Verify code follows project VIPER architecture

**When to use:**
- "Review this module"
- "Does this follow our architecture?"
- "Check if this is correct VIPER"

**Knowledge:**
- viper-pattern.md
- tabbar-architecture.md
- Project VIPER patterns

**Capabilities:**
- Checks component responsibilities
- Verifies dependency injection
- Validates protocol usage
- Checks for anti-patterns
- Ensures @MainActor on ViewModels

**Example invocation:**
```
Main: User asks "review Statistics module"
→ Launch architecture-reviewer with module path
→ Agent checks all 5 files against VIPER rules
→ Returns violations and suggestions
Main: Present findings to user
```

---

### 4. ios-feature-implementer
**Purpose:** Implement iOS framework features (StoreKit, MapKit, Liquid Glass, etc.)

**When to use:**
- "Add Liquid Glass effect"
- "Implement in-app purchases"
- "Add Visual Intelligence"
- Any xcode-knowledge framework mention

**Knowledge:**
- xcode-knowledge/INDEX.md (keyword lookup)
- Relevant xcode-knowledge/*.md files

**Capabilities:**
- Reads appropriate Apple framework guide
- Implements feature with official patterns
- Adds necessary imports and setup
- Follows Apple best practices

**Example invocation:**
```
Main: User asks "add liquid glass to button"
→ Launch ios-feature-implementer with "Liquid Glass on button in SwiftUI"
→ Agent reads SwiftUI-Implementing-Liquid-Glass-Design.md
→ Implements glassEffect() with proper modifiers
→ Returns code with explanation
Main: Apply code and explain to user
```

---

### 5. troubleshooter
**Purpose:** Diagnose and fix build/runtime errors

**When to use:**
- Build errors reported
- Runtime crashes
- "Why doesn't this work?"
- Xcode errors

**Knowledge:**
- troubleshooting.md
- Project-specific patterns

**Capabilities:**
- Identifies error type
- Searches troubleshooting.md for known issues
- Suggests fixes with steps
- Can apply fixes if requested

**Example invocation:**
```
Main: User reports "duplicate Info.plist error"
→ Launch troubleshooter with error message
→ Agent searches troubleshooting.md
→ Finds solution: update membershipExceptions
→ Returns fix steps
Main: Apply fix and verify
```

---

### 6. tabbar-orchestrator
**Purpose:** Add/modify TabBar structure and tabs

**When to use:**
- "Add a new tab"
- "Change tab icons"
- "Reorder tabs"

**Knowledge:**
- tabbar-architecture.md
- viper-pattern.md (for tab module)

**Capabilities:**
- Updates TabBarDependencies
- Modifies TabItem enum
- Creates new tab modules if needed
- Updates TabBarView

**Example invocation:**
```
Main: User asks "add Profile tab"
→ Launch tabbar-orchestrator with "Add Profile as 4th tab"
→ Agent updates TabItem.swift
→ Agent updates TabBarDependencies
→ Agent coordinates with viper-builder to create ProfileModule
→ Returns changes made
Main: Verify and inform user
```

---

### 7. git-flow-manager
**Purpose:** Automate Git Flow workflow with branch management and PR creation

**When to use:**
- "Create a feature branch for X"
- "Start working on Y"
- "Create PR for this work"
- "Merge and clean up branch"
- "Make a hotfix"
- User wants to follow git workflow

**Knowledge:**
- git-flow.md
- Project git workflow patterns

**Capabilities:**
- Creates feature/fix/hotfix/refactor branches with correct naming
- Ensures on correct base branch (develop/main)
- Commits changes with conventional commit messages
- Pushes branches to remote
- Creates PRs with gh CLI (base: develop or main)
- Merges and cleans up branches after PR
- Handles hotfix dual-merge (main + develop)
- Tags releases with semantic versioning

**Example invocation:**
```
User: "Start working on profile screen"
Main → git-flow-manager("Create feature branch for profile screen")
     → Agent checks current branch
     → Switches to develop and pulls latest
     → Creates feature/profile-screen
     → Returns branch name and next steps

User: "Create PR for this"
Main → git-flow-manager("Create PR for current branch")
     → Agent checks current branch (feature/profile-screen)
     → Commits any staged changes
     → Pushes to origin
     → Creates PR: feature/profile-screen → develop
     → Returns PR URL
```

**Workflow automation:**
```
User: "Complete this feature and merge"
Main → git-flow-manager("Complete and merge feature")
     → Agent creates PR if not exists
     → Waits for/merges PR
     → Switches back to develop
     → Pulls latest develop
     → Deletes feature branch (local + remote)
     → Returns summary
```

---

## Agent Orchestration Patterns

### Sequential Execution
When tasks depend on each other:
```
User: "Create Profile module and add it as a tab"

Main → viper-builder("Create Profile module")
     → Wait for completion
     → tabbar-orchestrator("Add Profile to TabBar")
     → Verify both completed
     → Inform user
```

### Parallel Execution
When tasks are independent:
```
User: "Check Statistics module for Swift 6 and architecture issues"

Main → swift6-auditor("Check Statistics module") ║
     ║ architecture-reviewer("Review Statistics")  ║
     ↓ Wait for both
     → Combine reports
     → Present to user
```

### Iterative Refinement
When agent needs to fix issues:
```
User: "Create Login module"

Main → viper-builder("Create Login module")
     → swift6-auditor("Check created files")
     → If issues found:
        → viper-builder("Fix issues: [list]")
        → swift6-auditor("Re-check")
     → Done when all ✅
```

### Multi-Agent Collaboration
Complex tasks requiring multiple agents:
```
User: "Add Liquid Glass Settings tab with subscriptions"

Main → viper-builder("Create Settings module")
     → ios-feature-implementer("Add Liquid Glass to Settings")
     → ios-feature-implementer("Add StoreKit subscriptions")
     → tabbar-orchestrator("Add Settings tab")
     → architecture-reviewer("Review entire flow")
     → If issues: fix and re-verify
```

---

## Agent Communication Protocol

### Input Format
```json
{
  "task": "Create Profile module",
  "context": {
    "existing_modules": ["Home", "Statistics", "Settings"],
    "add_to_tabbar": true
  },
  "requirements": [
    "Display user name and email",
    "Show avatar",
    "Edit button"
  ]
}
```

### Output Format
```json
{
  "status": "completed",
  "files_created": [
    "ProfileModule.swift",
    "ProfileView.swift",
    "ProfileViewModel.swift",
    "ProfilePresenter.swift",
    "ProfileRouter.swift"
  ],
  "files_modified": [
    "TabBarDependencies.swift",
    "TabItem.swift"
  ],
  "issues": [],
  "next_steps": [
    "Run build to verify",
    "Test navigation to Profile tab"
  ]
}
```

---

## Decision Tree for Agent Selection

```
User Request
    │
    ├─ Contains "create module" / "new module"
    │  → viper-builder
    │
    ├─ Contains "Swift 6" / "data race" / "concurrency"
    │  → swift6-auditor
    │
    ├─ Contains "review" / "check architecture"
    │  → architecture-reviewer
    │
    ├─ Contains iOS feature (Liquid Glass, StoreKit, etc.)
    │  → ios-feature-implementer
    │
    ├─ Contains "tab" / "tabbar"
    │  → tabbar-orchestrator
    │
    ├─ Contains error message / "doesn't work"
    │  → troubleshooter
    │
    ├─ Contains "branch" / "PR" / "merge" / "feature" / "commit"
    │  → git-flow-manager
    │
    └─ Complex multi-step task
       → Main orchestrates multiple agents
```

---

## Benefits

### For Users
- ✅ Faster task completion (parallel agents)
- ✅ Specialized expertise per domain
- ✅ Consistent results (agents follow same patterns)
- ✅ Less errors (agents validate each other)

### For Main Agent
- ✅ Smaller context per agent (focused knowledge)
- ✅ Reusable agent definitions
- ✅ Easier to extend (add new agents)
- ✅ Clear separation of concerns

### For Project
- ✅ Enforces architecture patterns
- ✅ Knowledge encoded in agents
- ✅ Onboarding new devs easier
- ✅ Consistent code quality

---

## Adding New Agents

To add a new specialized agent:

1. **Identify the domain** - What specific task/knowledge area?
2. **Define scope** - What can agent do? What can't it do?
3. **Assign knowledge** - Which .md files does it need?
4. **Create trigger patterns** - What keywords invoke this agent?
5. **Define I/O format** - Input parameters, output structure
6. **Add to decision tree** - When to use this agent?
7. **Document orchestration** - How it works with other agents

Example:
```markdown
### 7. test-runner
**Purpose:** Run tests and verify functionality

**When to use:**
- "Run tests"
- "Test this module"

**Knowledge:**
- Project test patterns
- XCTest best practices

**Capabilities:**
- Runs xcodebuild test
- Parses test results
- Reports failures with context
```

---

## Implementation Notes

Agents are implemented using Claude Code's Task tool with specific prompts that:
1. Load relevant knowledge files
2. Focus on single responsibility
3. Return structured output
4. Can be run in parallel when possible

Main Claude instance:
- Analyzes user request
- Selects appropriate agent(s)
- Launches with Task tool
- Coordinates multiple agents
- Combines results
- Presents to user
