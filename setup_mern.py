#!/usr/bin/env python3
"""
Setup script for MERN stack architecture
Creates backend and frontend directory structures
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create directories
print("Creating MERN stack directory structure...")

dirs = [
    'backend',
    'backend/src',
    'backend/src/config',
    'backend/src/models',
    'backend/src/controllers',
    'backend/src/routes',
    'backend/src/middleware',
    'backend/src/services',
    'backend/src/services/payment',
    'backend/src/services/email',
    'backend/src/services/auth',
    'backend/src/services/socket',
    'backend/src/utils',
    'frontend',
    'frontend/src',
    'frontend/src/components',
    'frontend/src/components/common',
    'frontend/src/components/auth',
    'frontend/src/components/dashboard',
    'frontend/src/pages',
    'frontend/src/pages/student',
    'frontend/src/pages/administrator',
    'frontend/src/pages/donor',
    'frontend/src/pages/volunteer',
    'frontend/src/pages/community',
    'frontend/src/context',
    'frontend/src/hooks',
    'frontend/src/services',
    'frontend/src/utils',
    'frontend/public'
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f"✓ Created: {d}")

print("\n" + "="*60)
print("✅ MERN stack directory structure created!")
print("="*60)
