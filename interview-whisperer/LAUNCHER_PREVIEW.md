# 🎯 Interview Whisperer Launcher - Visual Preview

## Window Layout

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                             ┃
┃              🎯 Interview Whisperer                         ┃
┃        AI-Powered Interview Copilot                         ┃
┃           (100% Local & Private)                            ┃
┃                                                             ┃
┃  ┌───────────────────────────────────────────────────┐     ┃
┃  │  System Status                                    │     ┃
┃  │                                                   │     ┃
┃  │  Ready Status:    ✅ Ready to start!             │     ┃
┃  │  🤖 Ollama:       ✅ Connected                    │     ┃
┃  │  📄 Documents:    ✅ 5 files processed            │     ┃
┃  │                                                   │     ┃
┃  │                            🔄 Refresh Status      │     ┃
┃  └───────────────────────────────────────────────────┘     ┃
┃                                                             ┃
┃  ┌───────────────────────────────────────────────────┐     ┃
┃  │        📁 Manage Documents                        │     ┃
┃  └───────────────────────────────────────────────────┘     ┃
┃                                                             ┃
┃  ┌───────────────────────────────────────────────────┐     ┃
┃  │        🎯 Start Interview Mode                    │     ┃
┃  └───────────────────────────────────────────────────┘     ┃
┃                                                             ┃
┃  ┌───────────────────────────────────────────────────┐     ┃
┃  │              ⚙️ Settings                          │     ┃
┃  └───────────────────────────────────────────────────┘     ┃
┃                                                             ┃
┃  ─────────────────────────────────────────────────────     ┃
┃  📂 Documents folder: /home/user/interview-whisperer/...   ┃
┃  💡 Click 'Manage Documents' to add your materials         ┃
┃                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Color Scheme

### Dark Theme
- **Background**: `#1e1e2e` (deep navy)
- **Panels**: `#2a2a3e` (medium navy)
- **Elements**: `#363650` (light navy)
- **Text Primary**: `#ffffff` (white)
- **Text Secondary**: `#b4b4c8` (light gray)

### Accent Colors
- **Blue Button**: `#89b4fa` (Manage Documents)
- **Green Button**: `#a6e3a1` (Start Interview - ready state)
- **Yellow Warning**: `#f9e2af` (attention needed)
- **Red Alert**: `#f38ba8` (errors)

## Status States

### System Ready ✅
```
Ready Status:    ✅ Ready to start!
🤖 Ollama:       ✅ Connected
📄 Documents:    ✅ 5 files processed
```
**Start Interview Mode button**: ENABLED (green)

### Ollama Not Available ⚠️
```
Ready Status:    ⚠️ Ollama not available
🤖 Ollama:       ❌ Not installed
📄 Documents:    ✅ 5 files processed
```
**Start Interview Mode button**: DISABLED (grayed out)

### Documents Not Ready ⚠️
```
Ready Status:    📄 Please add documents first
🤖 Ollama:       ✅ Connected
📄 Documents:    📂 No documents (0 files)
```
**Start Interview Mode button**: DISABLED (grayed out)

### Initial Loading
```
Ready Status:    Initializing...
🤖 Ollama:       Checking...
📄 Documents:    Checking...
```

## Button Interactions

### 📁 Manage Documents
- **Default**: Blue background (`#89b4fa`)
- **Hover**: Slightly darker
- **Click**: Opens document manager window
- **Always enabled**

### 🎯 Start Interview Mode
- **Default**: Green background (`#a6e3a1`) when ready
- **Disabled**: Gray background when not ready
- **Hover**: Slightly darker (when enabled)
- **Click**: Launches copilot interface
- **Smart enabling**: Only works when system is ready

### ⚙️ Settings
- **Default**: Dark gray background (`#363650`)
- **Hover**: Medium gray
- **Click**: Opens settings panel
- **Always enabled**

### 🔄 Refresh Status
- **Small button** in status panel
- **Click**: Updates all status indicators
- **Auto-refresh**: On launch

## Typography

- **Title**: Arial 24pt Bold - `🎯 Interview Whisperer`
- **Subtitle**: Arial 11pt Regular - Feature description
- **Section Headers**: Arial 12pt Bold - `System Status`
- **Status Labels**: Arial 10pt Regular - Status items
- **Button Text**: Arial 14pt Bold (main), 12pt (settings)
- **Footer**: Arial 9pt Regular - Help text

## Spacing & Layout

- **Window Size**: 600x550 pixels (fixed, not resizable)
- **Padding**: 20px around main container
- **Button Height**: Large (15px vertical padding)
- **Section Gaps**: 15-20px between sections
- **Status Items**: 3px spacing between lines

## User Experience Flow

### First Launch
1. Window opens, shows "Initializing..." status
2. After 500ms, status checks run automatically
3. Likely shows: "Please add documents first"
4. User clicks "Manage Documents"
5. Adds PDFs/documents
6. Returns to launcher, clicks "Refresh Status"
7. When ready: "Start Interview Mode" becomes enabled

### Daily Use
1. Launch application
2. Status checks automatically
3. If ready: Click "Start Interview Mode"
4. Interview copilot launches

## Accessibility Features

- **Large, Clear Buttons**: Easy to click (15px padding)
- **High Contrast**: Dark background, bright text
- **Visual Indicators**: Emoji + text for status
- **Helpful Messages**: Always guides next step
- **Cursor Changes**: Hand pointer on hover
- **Keyboard Navigation**: Tab through buttons
- **Screen Reader Friendly**: Clear text labels

## Future Enhancements

- [ ] Animated status indicators
- [ ] System tray integration
- [ ] Keyboard shortcuts
- [ ] Recent documents list
- [ ] Quick actions menu
- [ ] Theme customization
- [ ] Window position memory
- [ ] Notification support
