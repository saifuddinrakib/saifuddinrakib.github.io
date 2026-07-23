import re

# Read the CSS file
with open(r'd:\portfolio\checking\saifuddinrakib.github.io\assets\css\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix: Add pointer-events: auto to primary filter li elements
old_primary_li = """.projects-filter-primary li {
  cursor: pointer;
  display: inline-block !important;
  padding: 12px 30px;
  font-size: 13px !important;
  font-weight: 700 !important;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-radius: 50px;
  transition: all 0.3s ease;
  background: #ffffff !important;
  color: var(--portfolio-color) !important;
  border: 2px solid var(--portfolio-color);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);

  /* FIX 2: Ensure buttons sit on top of any overlapping headers/margins */
  position: relative;
  z-index: 51;
}"""

new_primary_li = """.projects-filter-primary li {
  cursor: pointer;
  display: inline-block !important;
  padding: 12px 30px;
  font-size: 13px !important;
  font-weight: 700 !important;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-radius: 50px;
  transition: all 0.3s ease;
  background: #ffffff !important;
  color: var(--portfolio-color) !important;
  border: 2px solid var(--portfolio-color);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);

  /* FIX: Ensure buttons sit on top of any overlapping headers/margins */
  position: relative;
  z-index: 150;
  pointer-events: auto !important;
}"""

content = content.replace(old_primary_li, new_primary_li)

# Also ensure the section title's ::after doesn't block clicks
old_title_after = """.projects-section .section-title h2::after {
  content: '';
  display: block;
  width: 80px;
  height: 3px;
  background: var(--portfolio-color);
  margin-left: 20px;
  border-radius: 2px;
}"""

new_title_after = """.projects-section .section-title h2::after {
  content: '';
  display: block;
  width: 80px;
  height: 3px;
  background: var(--portfolio-color);
  margin-left: 20px;
  border-radius: 2px;
  pointer-events: none;
}"""

content = content.replace(old_title_after, new_title_after)

# Write the updated content back
with open(r'd:\portfolio\checking\saifuddinrakib.github.io\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS file updated successfully!")
print("Changes made:")
print("1. Increased z-index from 51 to 150 in .projects-filter-primary li")
print("2. Added 'pointer-events: auto !important' to .projects-filter-primary li")
print("3. Added 'pointer-events: none' to .projects-section .section-title h2::after")
