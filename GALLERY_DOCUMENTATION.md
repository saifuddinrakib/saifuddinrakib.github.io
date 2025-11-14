# Photo Gallery Documentation

## Overview
The photo gallery is a fully functional image carousel with navigation controls, keyboard support, touch/swipe functionality, and responsive design.

## Current Features
- ✅ Image navigation with previous/next buttons
- ✅ Dot indicator navigation
- ✅ Keyboard navigation (left/right arrow keys)
- ✅ Touch/swipe support for mobile devices
- ✅ Image preloading for smooth transitions
- ✅ Fade transition effects
- ✅ Responsive design for all screen sizes
- ✅ Hover effects and visual feedback
- ✅ Transition protection (prevents rapid clicking issues)
- ✅ Auto-play capability (configurable)
- ✅ Easy image configuration system
- ✅ Accessibility features (alt text, ARIA labels)

## How to Add More Images

### Step 1: Add Images to the Images Folder
1. Add your new image files to the `assets/img/achievements/` folder
2. Use standard web formats (JPG, PNG, WebP)
3. Recommended maximum width: 800px for optimal loading

### Step 2: Update the Gallery Configuration
In `assets/js/main.js`, find the `galleryConfig` object and add your new images:

```javascript
var galleryConfig = {
  images: [
    {
      src: 'assets/img/achievements/NRF.jpg',
      alt: 'NRF Achievement',
      title: 'National Robotics Foundation Competition'
    },
    {
      src: 'assets/img/achievements/NRF_hackathon.jpg',
      alt: 'NRF Hackathon Achievement',
      title: 'NRF Hackathon Winner'
    },
    {
      src: 'assets/img/achievements/Techfest.jpg',
      alt: 'Techfest Achievement', 
      title: 'Techfest Competition Award'
    },
    // Add new images here:
    {
      src: 'assets/img/achievements/your-new-image.jpg',
      alt: 'Your Image Description',
      title: 'Your Image Title'
    }
  ],
  fadeSpeed: 200,
  autoPlay: false,
  autoPlayDelay: 5000
};
```

### Step 3: Update the HTML Dots
In `index.html`, add corresponding dots for each new image in the gallery section:

```html
<div class="gallery-dots">
  <span class="gallery-dot active" data-index="0"></span>
  <span class="gallery-dot" data-index="1"></span>
  <span class="gallery-dot" data-index="2"></span>
  <!-- Add new dots for additional images: -->
  <span class="gallery-dot" data-index="3"></span>
  <span class="gallery-dot" data-index="4"></span>
</div>
```

## Configuration Options

### Auto-play Settings
To enable auto-play, change the configuration:
```javascript
var galleryConfig = {
  // ... images array ...
  autoPlay: true,        // Enable auto-play
  autoPlayDelay: 5000   // 5 seconds between transitions
};
```

### Transition Speed
Adjust the fade speed (in milliseconds):
```javascript
var galleryConfig = {
  // ... images array ...
  fadeSpeed: 300  // Slower transitions (default: 200)
};
```

## File Structure
```
assets/
├── css/
│   └── style.css          # Gallery styles
├── js/
│   └── main.js           # Gallery functionality
└── img/
    └── achievements/     # Gallery images folder
        ├── NRF.jpg
        ├── NRF_hackathon.jpg
        └── Techfest.jpg
```

## Browser Support
- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 11+
- ✅ Edge 79+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## Accessibility Features
- ARIA labels on navigation buttons
- Alt text for all images
- Title attributes for additional context
- Keyboard navigation support
- Focus indicators for keyboard users

## Troubleshooting

### Images Not Loading
1. Check file paths in the `galleryConfig.images` array
2. Ensure images exist in the specified folders
3. Verify image file extensions match the configuration

### Navigation Not Working
1. Ensure jQuery is loaded before main.js
2. Check browser console for JavaScript errors
3. Verify all HTML elements have correct IDs and classes

### Mobile Touch Issues
1. Ensure the device supports touch events
2. Check that the swipe distance threshold is appropriate
3. Test on actual devices, not just browser dev tools

## Performance Tips
1. Optimize image sizes (recommend max 800px width)
2. Use modern image formats (WebP when possible)
3. Keep the number of images reasonable (< 20 for best performance)
4. Enable image compression for web delivery
