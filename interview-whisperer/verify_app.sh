#!/bin/bash

# Interview Whisperer - App Bundle Verification Script

echo "🔍 Verifying Interview Whisperer.app bundle..."
echo ""

APP_PATH="/home/user/interview-whisperer/Interview Whisperer.app"
ERRORS=0

# Check if .app exists
if [ ! -d "$APP_PATH" ]; then
    echo "❌ App bundle not found at: $APP_PATH"
    exit 1
fi

echo "✅ App bundle exists"

# Check directory structure
echo ""
echo "📁 Checking directory structure..."

if [ ! -d "$APP_PATH/Contents" ]; then
    echo "❌ Missing Contents/ directory"
    ((ERRORS++))
else
    echo "✅ Contents/ directory"
fi

if [ ! -d "$APP_PATH/Contents/MacOS" ]; then
    echo "❌ Missing Contents/MacOS/ directory"
    ((ERRORS++))
else
    echo "✅ Contents/MacOS/ directory"
fi

if [ ! -d "$APP_PATH/Contents/Resources" ]; then
    echo "❌ Missing Contents/Resources/ directory"
    ((ERRORS++))
else
    echo "✅ Contents/Resources/ directory"
fi

# Check required files
echo ""
echo "📄 Checking required files..."

if [ ! -f "$APP_PATH/Contents/Info.plist" ]; then
    echo "❌ Missing Info.plist"
    ((ERRORS++))
else
    echo "✅ Info.plist"
fi

if [ ! -f "$APP_PATH/Contents/PkgInfo" ]; then
    echo "❌ Missing PkgInfo"
    ((ERRORS++))
else
    echo "✅ PkgInfo"
fi

if [ ! -f "$APP_PATH/Contents/MacOS/launcher" ]; then
    echo "❌ Missing launcher executable"
    ((ERRORS++))
else
    echo "✅ launcher executable"

    # Check if launcher is executable
    if [ ! -x "$APP_PATH/Contents/MacOS/launcher" ]; then
        echo "   ⚠️  launcher is not executable (fixing...)"
        chmod +x "$APP_PATH/Contents/MacOS/launcher"
        echo "   ✅ Fixed permissions"
    else
        echo "   ✅ launcher has correct permissions"
    fi
fi

# Check Info.plist validity
echo ""
echo "📋 Checking Info.plist validity..."

if command -v plutil &> /dev/null; then
    if plutil -lint "$APP_PATH/Contents/Info.plist" &> /dev/null; then
        echo "✅ Info.plist is valid XML"
    else
        echo "❌ Info.plist has syntax errors"
        ((ERRORS++))
    fi
else
    echo "⚠️  plutil not available (can't validate Info.plist)"
fi

# Check project files
echo ""
echo "🔗 Checking project files..."

if [ ! -d "app" ]; then
    echo "❌ Missing app/ directory"
    ((ERRORS++))
else
    echo "✅ app/ directory"
fi

if [ ! -f "app/launcher.py" ]; then
    echo "❌ Missing app/launcher.py"
    ((ERRORS++))
else
    echo "✅ app/launcher.py"
fi

if [ ! -f "requirements.txt" ]; then
    echo "❌ Missing requirements.txt"
    ((ERRORS++))
else
    echo "✅ requirements.txt"
fi

# Summary
echo ""
echo "=" * 50
if [ $ERRORS -eq 0 ]; then
    echo "✅ All checks passed!"
    echo ""
    echo "🎯 Your app is ready to use!"
    echo ""
    echo "To launch:"
    echo "  1. Open Finder"
    echo "  2. Navigate to: /home/user/interview-whisperer/"
    echo "  3. Double-click 'Interview Whisperer.app'"
    echo ""
    echo "First time: Right-click → Open → Click 'Open'"
    echo ""
    echo "📖 See MAC_APP_GUIDE.md for detailed instructions"
else
    echo "❌ Found $ERRORS error(s)"
    echo ""
    echo "Please fix the errors above before using the app."
fi

exit $ERRORS
