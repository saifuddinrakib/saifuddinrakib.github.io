# PowerShell script to fix the secondary filter hover issue
$filePath = "d:\portfolio\checking\saifuddinrakib.github.io\assets\css\style.css"
$content = Get-Content $filePath -Raw

# Fix 1: Update the .projects-filter-secondary container
$content = $content -replace `
  '(/\* 3\. Secondary Filter \(Robotics, Mechanical, IoT\) \*/\r?\n\.projects-filter-secondary \{\r?\n  padding: 0;\r?\n  margin: 0 0 50px 0;\r?\n  list-style: none;\r?\n  text-align: center;\r?\n  display: flex !important;\r?\n  flex-wrap: wrap;\r?\n  justify-content: center;\r?\n  align-items: center;\r?\n\r?\n  /\* Ensure secondary filters are also accessible \*/\r?\n  position: relative;\r?\n  z-index: 40;\r?\n\})', `
  '/* 3. Secondary Filter (Robotics, Mechanical, IoT) */
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
}'

# Fix 2: Update the .projects-filter-secondary li
$content = $content -replace `
  '(\.projects-filter-secondary li \{\r?\n  cursor: pointer;\r?\n  display: inline-block !important;\r?\n  padding: 8px 20px;\r?\n  font-size: 15px !important;\r?\n  font-weight: 600 !important;\r?\n  margin: 0 5px;)', `
  '.projects-filter-secondary li {
  cursor: pointer;
  display: inline-block !important;
  padding: 8px 20px;
  font-size: 15px !important;
  font-weight: 600 !important;
  margin: 0;'

# Fix 3: Add pointer-events and z-index to li
$content = $content -replace `
  '(\.projects-filter-secondary li \{[^\}]+  background: transparent !important;\r?\n\})', `
  '$1
  
  /* FIX: Ensure each button is fully clickable */
  pointer-events: auto;
  z-index: 101;
}'

# Save the file
$content | Set-Content $filePath -NoNewline

Write-Host "CSS file updated successfully!"
