const fs = require("fs");
const axios = require("axios");
const { createCanvas, loadImage } = require("canvas");

const IMAGE_URL = "https://image-us.samsung.com/us/smartphones/galaxy-s25/Gallery/PA1/PA1-01-Navy-1600x1200.jpg?$default-400-jpg$";

async function editImage() {
    const response = await axios({ url: IMAGE_URL, responseType: "arraybuffer" });
    const imageBuffer = Buffer.from(response.data, "binary");

    const img = await loadImage(imageBuffer);
    const canvas = createCanvas(img.width, img.height);
    const ctx = canvas.getContext("2d");

    ctx.drawImage(img, 0, 0);

    // Gradient Overlay
    const gradient = ctx.createLinearGradient(0, img.height - 100, 0, img.height);
    gradient.addColorStop(0, "rgba(0, 0, 0, 0.8)");
    gradient.addColorStop(1, "rgba(0, 0, 0, 0)");

    ctx.fillStyle = gradient;
    ctx.fillRect(0, img.height - 100, img.width, 100);

    // Title Box
    ctx.fillStyle = "#ff4500";
    ctx.fillRect(20, img.height - 90, 200, 50);

    // Text
    ctx.font = "bold 24px Arial";
    ctx.fillStyle = "white";
    ctx.fillText("Did you know?", 30, img.height - 55);
    ctx.font = "bold 20px Arial";
    ctx.fillText("Samsung S25 can fix scratches itself!", 30, img.height - 25);

    fs.writeFileSync("edited_image.png", canvas.toBuffer("image/png"));
    console.log("Image edited successfully!");
}

editImage();
