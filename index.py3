
<!DOCTYPE html><html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Did You Know?</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #222;
        margin: 0;
        flex-direction: column;
        font-family: 'Montserrat', sans-serif;
    }
    .container {
        position: relative;
        max-width: 600px;
    }
    .image {
        width: 100%;
        display: block;
    }
    .overlay {
        position: absolute;
        bottom: 0;
        width: 100%;
        padding: 40px 20px;
        background: linear-gradient(to top, rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0));
        color: white;
        text-align: center;
        box-sizing: border-box;
    }
    .heading {
        font-size: 28px;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.9);
        margin-bottom: 10px;
    }
    .subtext {
        font-size: 22px;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.9);
    }
</style>

</head>
<body>
    <div class="container">
        <img src="https://image-us.samsung.com/us/smartphones/galaxy-s25/Gallery/PA1/PA1-01-Navy-1600x1200.jpg" alt="Samsung S25" class="image">
        <div class="overlay">
            <div class="heading">Samsung S25</div>
            <div class="heading">Did you know?</div>
            <p class="subtext">Samsung S25 is the first phone that when it scratches, it fixes itself without mechanics.</p>
        </div>
    </div>
</body>
</html>
