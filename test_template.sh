#!/bin/bash
# Quick test script for iOS VIPER Template

set -e

echo "🧪 Testing iOS VIPER Template..."
echo ""

# Check if cookiecutter is installed
if ! command -v cookiecutter &> /dev/null; then
    echo "❌ cookiecutter not found!"
    echo "   Install: pip3 install cookiecutter"
    exit 1
fi

# Get template directory
TEMPLATE_DIR="$(cd "$(dirname "$0")" && pwd)"
PARENT_DIR="$(dirname "$TEMPLATE_DIR")"
TEST_PROJECT_NAME="TestiOSProject"

echo "📁 Template directory: $TEMPLATE_DIR"
echo "📁 Test project will be created in: $PARENT_DIR/$TEST_PROJECT_NAME"
echo ""

# Clean up old test project if exists
if [ -d "$PARENT_DIR/$TEST_PROJECT_NAME" ]; then
    echo "🗑️  Removing old test project..."
    rm -rf "$PARENT_DIR/$TEST_PROJECT_NAME"
fi

echo "🚀 Generating test project..."
echo ""

# Generate project with cookiecutter
cd "$PARENT_DIR"
cookiecutter "$TEMPLATE_DIR" --no-input \
    project_name="$TEST_PROJECT_NAME" \
    organization_name="Test Company" \
    author_name="Test Author" \
    ios_deployment_target="17.0" \
    swift_version="6.0"

echo ""
echo "✅ Test project generated!"
echo ""

# Check if project was created
if [ ! -d "$PARENT_DIR/testiOSProject" ]; then
    echo "❌ Project directory not found!"
    exit 1
fi

cd "testiOSProject"

echo "📋 Project structure:"
ls -la
echo ""

# Check for key files
echo "🔍 Checking key files..."
FILES_TO_CHECK=(
    "TestiOSProject/Sources/Application/AppDelegate.swift"
    "TestiOSProject/Sources/Application/SceneDelegate.swift"
    "TestiOSProject/Sources/Modules/MainScreen/MainScreenModule.swift"
    ".claude/agents/viper-builder.md"
)

for file in "${FILES_TO_CHECK[@]}"; do
    if [ -f "$file" ]; then
        echo "   ✅ $file"
    else
        echo "   ❌ $file (missing!)"
    fi
done

echo ""

# Try to generate Xcode project if xcodegen is available
if command -v xcodegen &> /dev/null; then
    echo "🔨 Generating Xcode project..."
    xcodegen generate

    if [ -f "TestiOSProject.xcodeproj/project.pbxproj" ]; then
        echo "   ✅ Xcode project generated successfully!"
        echo ""
        echo "🎉 Test successful!"
        echo ""
        echo "📝 Next steps:"
        echo "   1. cd $PARENT_DIR/testiOSProject"
        echo "   2. open TestiOSProject.xcodeproj"
        echo "   3. Build with ⌘B"
        echo ""
        echo "🗑️  To clean up: rm -rf $PARENT_DIR/testiOSProject"
    else
        echo "   ⚠️  Xcode project generation failed"
    fi
else
    echo "ℹ️  xcodegen not found (install: brew install xcodegen)"
    echo "   You'll need to create Xcode project manually"
    echo ""
    echo "✅ Template generation successful!"
    echo ""
    echo "📝 Next steps:"
    echo "   1. cd $PARENT_DIR/testiOSProject"
    echo "   2. Install xcodegen: brew install xcodegen"
    echo "   3. Run: xcodegen generate"
    echo "   4. open TestiOSProject.xcodeproj"
    echo ""
    echo "🗑️  To clean up: rm -rf $PARENT_DIR/testiOSProject"
fi

echo ""
echo "=" "==============================================="
echo "Template test complete!"
echo "================================================"
