CUSTOM APP ICON
================

To add a custom icon to your Interview Whisperer app:

OPTION 1: Use Icon Composer (Mac only)
---------------------------------------
1. Create a 1024x1024 PNG image with your design
2. Open "Icon Composer" (part of Xcode tools)
3. Drag your PNG into Icon Composer
4. Export as "AppIcon.icns"
5. Place it in this Resources/ folder
6. Restart the app

OPTION 2: Use Online Icon Converter
------------------------------------
1. Create a 1024x1024 PNG image
2. Go to: https://cloudconvert.com/png-to-icns
3. Upload your PNG and convert to ICNS
4. Download "AppIcon.icns"
5. Place it in this Resources/ folder
6. Restart the app

OPTION 3: Use iconutil (Mac Terminal)
--------------------------------------
1. Create iconset folder:
   mkdir AppIcon.iconset

2. Create PNG files at different sizes:
   - icon_16x16.png
   - icon_32x32.png
   - icon_128x128.png
   - icon_256x256.png
   - icon_512x512.png
   - icon_1024x1024.png

3. Convert to icns:
   iconutil -c icns AppIcon.iconset -o AppIcon.icns

4. Place AppIcon.icns in this Resources/ folder

DESIGN SUGGESTIONS:
-------------------
- Use a microphone icon 🎤
- Use a target/bullseye icon 🎯
- Use speech bubbles 💬
- Keep it simple and recognizable
- Use blue/green colors (professional)

The app will use the system default icon until you add a custom one.
