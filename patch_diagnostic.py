import re

with open('app/src/main/java/com/example/generator/SystemDiagnosticTracker.kt', 'r') as f:
    content = f.read()

content = content.replace(
    'android.os.Environment.DIRECTORY_DOWNLOADS + "/Quran Reels/ERROR"',
    'android.os.Environment.DIRECTORY_MOVIES + "/Quran Reels/ERROR"'
)

with open('app/src/main/java/com/example/generator/SystemDiagnosticTracker.kt', 'w') as f:
    f.write(content)

