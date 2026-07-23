import re

# Read the CSS file
with open(r'd:\portfolio\checking\saifuddinrakib.github.io\assets\css\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Add gap, increase z-index, and add pointer-events to .projects-filter-secondary
old_secondary_container = """/* 3. Secondary Filter (Robotics, Mechanical, IoT) */
.projects-filter-secondary {
  padding: 0;
  margin: 0 0 50px 0;
  list-style: none;
  text-align: center;
  display: flex !important;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;

  /* Ensure secondary filters are also accessible */
  position: relative;
  z-index: 40;
}"""

new_secondary_container = """/* 3. Secondary Filter (Robotics, Mechanical, IoT) */
.projects-filter-secondary {
  padding: 0;
  margin: 0 0 50px 0;
  list-style: none;
  text-align: center;
  display: flex !important;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 10px;

  /* FIX: Ensure secondary filters are fully accessible and on top */
  position: relative;
  z-index: 100;
  pointer-events: auto;
}"""

content = content.replace(old_secondary_container, new_secondary_container)

# Fix 2: Change margin and add pointer-events to .projects-filter-secondary li
old_secondary_li = """.projects-filter-secondary li {
  cursor: pointer;
  display: inline-block !important;
  padding: 8px 20px;
  font-size: 15px !important;
  font-weight: 600 !important;
  margin: 0 5px;
  transition: all 0.3s ease;
  position: relative;
  text-transform: capitalize;
  color: var(--text-light) !important;
  background: transparent !important;
}"""

new_secondary_li = """.projects-filter-secondary li {
  cursor: pointer;
  display: inline-block !important;
  padding: 8px 20px;
  font-size: 15px !important;
  font-weight: 600 !important;
  margin: 0;
  transition: all 0.3s ease;
  position: relative;
  text-transform: capitalize;
  color: var(--text-light) !important;
  background: transparent !important;
  
  /* FIX: Ensure each button is fully clickable */
  pointer-events: auto;
  z-index: 101;
}"""

content = content.replace(old_secondary_li, new_secondary_li)

# Write the updated content back
with open(r'd:\portfolio\checking\saifuddinrakib.github.io\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS file updated successfully!")
print("Changes made:")
print("1. Added 'gap: 10px' to .projects-filter-secondary")
print("2. Changed z-index from 40 to 100 in .projects-filter-secondary")
print("3. Added 'pointer-events: auto' to .projects-filter-secondary")
print("4. Changed margin from '0 5px' to '0' in .projects-filter-secondary li")
print("5. Added 'pointer-events: auto' and 'z-index: 101' to .projects-filter-secondary li")
