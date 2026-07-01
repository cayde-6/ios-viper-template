#!/usr/bin/env python3
"""Pre-generation hook for iOS VIPER template validation."""

import re
import sys


def validate_project_name(project_name):
    """Validate project name contains only allowed characters."""
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9 \-]*$', project_name):
        print(f"ERROR: '{project_name}' is not a valid project name.")
        print("Project name must start with a letter and contain only letters, numbers, spaces, and hyphens.")
        sys.exit(1)


def validate_bundle_identifier(bundle_id):
    """Validate bundle identifier format."""
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9\-]*(\.[a-zA-Z][a-zA-Z0-9\-]*)+$', bundle_id):
        print(f"ERROR: '{bundle_id}' is not a valid bundle identifier.")
        print("Bundle identifier must be in reverse domain format (e.g., com.company.app).")
        sys.exit(1)


def validate_ios_version(version):
    """Validate iOS deployment target version."""
    valid_versions = ["15.0", "16.0", "17.0", "18.0"]
    if version not in valid_versions:
        print(f"ERROR: '{version}' is not a valid iOS deployment target.")
        print(f"Valid versions: {', '.join(valid_versions)}")
        sys.exit(1)


def validate_swift_version(version):
    """Validate Swift version."""
    valid_versions = ["5.9", "5.10", "6.0"]
    if version not in valid_versions:
        print(f"ERROR: '{version}' is not a valid Swift version.")
        print(f"Valid versions: {', '.join(valid_versions)}")
        sys.exit(1)


def validate_ui_framework_selection():
    """Validate at least one UI framework is selected."""
    use_swiftui = "{{ cookiecutter.use_swiftui }}" == "yes"
    use_uikit = "{{ cookiecutter.use_uikit }}" == "yes"

    if not use_swiftui and not use_uikit:
        print("ERROR: You must select at least one UI framework (SwiftUI or UIKit).")
        sys.exit(1)


def main():
    """Run all validation checks."""
    project_name = "{{ cookiecutter.project_name }}"
    bundle_id = "{{ cookiecutter.bundle_identifier }}"
    ios_version = "{{ cookiecutter.ios_deployment_target }}"
    swift_version = "{{ cookiecutter.swift_version }}"

    print(f"🔍 Validating project configuration...")
    print(f"   Project: {project_name}")
    print(f"   Bundle ID: {bundle_id}")
    print(f"   iOS: {ios_version}+ | Swift: {swift_version}")

    validate_project_name(project_name)
    validate_bundle_identifier(bundle_id)
    validate_ios_version(ios_version)
    validate_swift_version(swift_version)
    validate_ui_framework_selection()

    print("✅ All validations passed!")


if __name__ == "__main__":
    main()
