#!/usr/bin/env python3
"""Post-generation hook for iOS VIPER template setup."""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def remove_file_or_dir(path):
    """Remove file or directory if it exists."""
    if os.path.isfile(path):
        os.remove(path)
        print(f"   ❌ Removed: {path}")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f"   ❌ Removed: {path}")


def cleanup_optional_features():
    """Remove files based on user selections."""
    print("\n🧹 Cleaning up optional features...")

    # Remove test targets if not included
    if "{{ cookiecutter.include_tests }}" == "no":
        remove_file_or_dir("{{ cookiecutter.project_name }}Tests")
        print("   ℹ️  Test target not included")

    if "{{ cookiecutter.include_ui_tests }}" == "no":
        remove_file_or_dir("{{ cookiecutter.project_name }}UITests")
        print("   ℹ️  UI Test target not included")

    # Remove Claude agents if not included
    if "{{ cookiecutter.include_claude_agents }}" == "no":
        remove_file_or_dir(".claude")
        print("   ℹ️  Claude agents not included")

    # Remove VIPER example if not included
    if "{{ cookiecutter.include_viper_example_module }}" == "no":
        remove_file_or_dir("{{ cookiecutter.project_name }}/Sources/Modules/MainScreen")
        print("   ℹ️  VIPER example module not included")

    # Remove network layer if not included
    if "{{ cookiecutter.architecture_features.include_network_layer }}" == "no":
        remove_file_or_dir("{{ cookiecutter.project_name }}/Sources/Network")
        print("   ℹ️  Network layer not included")


def create_xcode_project():
    """Create Xcode project using available tools."""
    print("\n📦 Creating Xcode project...")

    project_name = "{{ cookiecutter.project_name }}"

    # Check if xcodegen is available
    try:
        subprocess.run(["which", "xcodegen"], check=True, capture_output=True)
        print("   ✅ Using xcodegen to generate project...")

        # Generate project.yml for xcodegen
        create_project_yml()

        # Run xcodegen
        result = subprocess.run(["xcodegen", "generate"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ {project_name}.xcodeproj created successfully!")
            # Clean up project.yml after generation
            if os.path.exists("project.yml"):
                os.remove("project.yml")
            return True
        else:
            print(f"   ⚠️  xcodegen failed: {result.stderr}")
            return False

    except subprocess.CalledProcessError:
        print("   ℹ️  xcodegen not found")
        print("\n   📝 Manual setup required:")
        print(f"      1. Open Xcode")
        print(f"      2. File → New → Project")
        print(f"      3. Choose iOS App template")
        print(f"      4. Name it '{project_name}'")
        print(f"      5. Add existing source files to the project")
        print("\n   Or install xcodegen: brew install xcodegen")
        print("   Then run: xcodegen generate")
        return False


def create_project_yml():
    """Create project.yml for xcodegen."""
    project_name = "{{ cookiecutter.project_name }}"
    bundle_id = "{{ cookiecutter.bundle_identifier }}"
    ios_version = "{{ cookiecutter.ios_deployment_target }}"
    swift_version = "{{ cookiecutter.swift_version }}"

    project_yml = f"""
name: {project_name}
options:
  bundleIdPrefix: {'.'.join(bundle_id.split('.')[:-1])}
  deploymentTarget:
    iOS: {ios_version}
  xcodeVersion: "15.0"
  swiftVersion: "{swift_version}"

settings:
  base:
    SWIFT_VERSION: {swift_version}
    IPHONEOS_DEPLOYMENT_TARGET: {ios_version}

targets:
  {project_name}:
    type: application
    platform: iOS
    deploymentTarget: {ios_version}
    sources:
      - {project_name}/Sources
    resources:
      - {project_name}/Sources/Resources
    info:
      path: {project_name}/Sources/Resources/Info.plist
      properties:
        CFBundleDisplayName: {project_name}
        CFBundleIdentifier: {bundle_id}
        CFBundleShortVersionString: "1.0.0"
        CFBundleVersion: "1"
        UILaunchStoryboardName: LaunchScreen
        UIApplicationSceneManifest:
          UIApplicationSupportsMultipleScenes: false
          UISceneConfigurations:
            UIWindowSceneSessionRoleApplication:
              - UISceneConfigurationName: Default Configuration
                UISceneDelegateClassName: $(PRODUCT_MODULE_NAME).SceneDelegate
"""

    # Add test targets if included
    if "{{ cookiecutter.include_tests }}" == "yes":
        project_yml += f"""
  {project_name}Tests:
    type: bundle.unit-test
    platform: iOS
    sources:
      - {project_name}Tests
    dependencies:
      - target: {project_name}
"""

    if "{{ cookiecutter.include_ui_tests }}" == "yes":
        project_yml += f"""
  {project_name}UITests:
    type: bundle.ui-testing
    platform: iOS
    sources:
      - {project_name}UITests
    dependencies:
      - target: {project_name}
"""

    with open("project.yml", "w") as f:
        f.write(project_yml)

    print("   ✅ project.yml created")


def initialize_git():
    """Initialize git repository."""
    print("\n🔧 Initializing git repository...")

    try:
        subprocess.run(["git", "init"], check=True, capture_output=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit from iOS VIPER template"],
            check=True,
            capture_output=True
        )
        print("   ✅ Git repository initialized with initial commit")
    except subprocess.CalledProcessError as e:
        print(f"   ⚠️  Git initialization failed: {e}")


def print_next_steps():
    """Print next steps for the user."""
    project_name = "{{ cookiecutter.project_name }}"
    include_agents = "{{ cookiecutter.include_claude_agents }}" == "yes"

    print("\n" + "=" * 60)
    print(f"🎉 {project_name} created successfully!")
    print("=" * 60)

    print("\n📋 Next steps:")
    print(f"   1. cd {project_name}")

    if os.path.exists(f"{project_name}.xcodeproj"):
        print(f"   2. open {project_name}.xcodeproj")
    else:
        print(f"   2. Set up Xcode project (see instructions above)")

    print(f"   3. Build and run (⌘R)")

    if include_agents:
        print("\n🤖 Claude Code Integration:")
        print("   Your project includes specialized Claude agents:")
        print("   • viper-builder - Create new VIPER modules")
        print("   • swift6-auditor - Check Swift 6 compliance")
        print("   • architecture-reviewer - Verify VIPER architecture")
        print("   • ios-feature-implementer - Implement iOS features")
        print("   • troubleshooter - Debug build/runtime errors")
        print("   • tabbar-orchestrator - Manage TabBar structure")
        print("   • git-flow-manager - Automate Git Flow workflow")
        print("\n   See .claude/agents/AGENTS-SYSTEM.md for details")

    print("\n📚 Documentation:")
    print("   • README.md - Project overview and setup")
    print("   • .claude/knowledge/ - Architecture patterns and guides")

    print("\n💡 Tips:")
    print("   • Use VIPER pattern for new modules")
    print("   • Run tests before committing")
    print("   • Follow Swift 6 concurrency best practices")

    print("\n" + "=" * 60)


def main():
    """Run all post-generation tasks."""
    print("\n🚀 Setting up your iOS project...")

    cleanup_optional_features()
    create_xcode_project()
    initialize_git()
    print_next_steps()


if __name__ == "__main__":
    main()
