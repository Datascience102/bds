#!/usr/bin/env python3
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

files = [
    'courses.html',
    'machine-learning-fundamentals.html',
    'big-data-spark.html',
    'sql-data-analysis.html',
    'data-visualization-tableau.html',
    'deep-learning-tensorflow.html',
    'course-detail.html'
]

replacements = [
    ('$49', '₹49'),
    ('$39', '₹39'),
    ('$69', '₹69'),
    ('$89', '₹89'),
    ('$129', '₹129'),
    ('$149', '₹149'),
]

for filename in files:
    if not os.path.exists(filename):
        print(f"Skipping {filename} - file not found")
        continue
    
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Updated {filename}')

print("All price symbols updated successfully!")
