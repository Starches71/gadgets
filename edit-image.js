const fs = require('fs');
const canvas = require('canvas');
const axios = require('axios');
const path = require('path');

// Define the image URL
const imageUrl = 'https://image-us.samsung.com/us/smartphones/galaxy-s25/Gallery/PA1/PA1-01-Navy-1600x1200.jpg';

// Setup canvas and context
const { createCanvas, loadImage } = canvas;
const canvasWidth = 800; // Set width of the image canvas
const canvasHeight = 800; // Set height of the image canvas
const canvasInstance = createCanvas(canvasWidth, canvasHeight);
const ctx = canvasInstance.getContext('2d');

// Load the image
axios({
  url: imageUrl,
  responseType: 'arraybuffer',
})
  .then((response) => {
    loadImage(response.data).then((image) => {
      // Draw the image onto the canvas
      ctx.drawImage(image, 0, 0, canvasWidth, canvasHeight);

      // Apply a gradient overlay
      const gradient = ctx.createLinearGradient(0, canvasHeight, 0, canvasHeight - 50);
      gradient.addColorStop(0, 'rgba(0, 0, 0, 0.98)');
      gradient.addColorStop(0.5, 'rgba(0, 0, 0, 0.7)');
      gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = gradient;
      ctx.fillRect(0, canvasHeight - 50, canvasWidth, 50);

      // Add the text box with a gradient title and fact text
      ctx.fillStyle = 'white';
      ctx.font = 'bold 18px Poppins';
      ctx.textAlign = 'center';

      // Title box (rounded gradient)
      const titleWidth = 250;
      const titleHeight = 40;
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(50, 0);
      ctx.lineTo(titleWidth - 50, 0);
      ctx.lineTo(titleWidth, 50);
      ctx.lineTo(50, titleHeight);
      ctx.closePath();
      ctx.clip();
      const gradientTitle = ctx.createLinearGradient(0, 0, 1, 0);
      gradientTitle.addColorStop(0, '#ff8c00');
      gradientTitle.addColorStop(1, '#ff4500');
      ctx.fillStyle = gradientTitle;
      ctx.fillRect(30, 10, titleWidth - 60, titleHeight - 20);

      // Add "Did you know?" inside the title box
      ctx.fillStyle = 'white';
      ctx.font = 'bold 18px Poppins';
      ctx.fillText('Did you know?', canvasWidth / 2, canvasHeight - 30);

      // Add fact text below title
      ctx.font = 'bold 14px Poppins';
      ctx.fillText('Samsung S25 is the first phone that when it scratches, it fixes itself without mechanics.', canvasWidth / 2, canvasHeight - 70);

      // Save image to a file
      const outputFile = path.join(__dirname, 'edited_image.png');
      const buffer = canvasInstance.toBuffer('image/png');
      fs.writeFileSync(outputFile, buffer);
      console.log('Image has been saved as "edited_image.png".');
    });
  })
  .catch((err) => {
    console.error('Error downloading or processing the image:', err);
  });
