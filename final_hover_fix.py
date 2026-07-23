# Final comprehensive fix for filter hover issues
# This script will add ALL necessary CSS properties to ensure clickability

with open(r'd:\portfolio\checking\saifuddinrakib.github.io\assets\css\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Add cursor: pointer !important and user-select to primary filter li
old_primary_li_hover = """.projects-filter-primary li:hover {
  transform: translateY(-2px);
  background: rgba(19, 133, 126, 0.1) !important;
}"""

new_primary_li_hover = """.projects-filter-primary li {
  cursor: pointer !important;
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
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}

.projects-filter-primary li:hover {
  transform: translateY(-2px);
  background: rgba(19, 133, 126, 0.1) !important;
  cursor: pointer !important;
}"""

# Find and replace the primary filter li section
import re
pattern = r'\.projects-filter-primary li \{[^}]+\}\s*\.projects-filter-primary li:hover \{[^}]+\}'
content = re.sub(pattern, new_primary_li_hover, content, flags=re.DOTALL)

# Add cursor and user-select to secondary filter li
old_secondary_li = """.projects-filter-secondary li {
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

new_secondary_li = """.projects-filter-secondary li {
  cursor: pointer !important;
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
  pointer-events: auto !important;
  z-index: 101;
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}

.projects-filter-secondary li:hover {
  color: var(--portfolio-color) !important;
  cursor: pointer !important;
}"""

# Replace secondary filter li
content = content.replace(old_secondary_li, new_secondary_li)

# Write back
with open(r'd:\portfolio\checking\saifuddinrakib.github.io\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ CSS updated with comprehensive hover fixes!")
print("Changes:")
print("1. Added cursor: pointer !important to all filter buttons")
print("2. Added user-select: none to prevent text selection interference")
print("3. Added pointer-events: auto !important")
print("4. Added cursor: pointer !important to :hover states")
print("\nPlease refresh your browser (Ctrl+F5) to clear cache and test!")
