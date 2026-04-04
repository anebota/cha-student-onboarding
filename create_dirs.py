import os

# Create directories
dirs = [
    'templates',
    'templates/student',
    'templates/administrator',
    'templates/donor',
    'templates/volunteer',
    'templates/community',
    'templates/admin',
    'static',
    'static/css',
    'static/js',
    'static/images'
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f"Created: {d}")

print("\nAll template and static directories created successfully!")
