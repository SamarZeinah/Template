from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import numpy as np
import joblib

app = FastAPI()

# Render the index.html template on root URL


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    content = """
    <html>
    <head>
        <title>Mastercard Stock Price Prediction</title>
    </head>
    <body>
        <h1>Mastercard Stock Price Prediction</h1>
        <form method="post">
            <label for="open_price">Open Price:</label>
            <input type="text" id="open_price" name="open_price"><br><br>
            <label for="high_price">High Price:</label>
            <input type="text" id="high_price" name="high_price"><br><br>
            <label for="low_price">Low Price:</label>
            <input type="text" id="low_price" name="low_price"><br><br>
            <label for="volume">Volume:</label>
            <input type="text" id="volume" name="volume"><br><br>
            <input type="submit" value="Predict">
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=content)

# Handle prediction request


@app.post("/", response_class=HTMLResponse)
async def predict(request: Request, open_price: float = Form(...), high_price: float = Form(...),
                  low_price: float = Form(...), volume: float = Form(...)):
    # Load the trained model
    loaded_model = joblib.load("trained_model.pkl")
    # Make prediction using the model
    prediction = loaded_model.predict(
        np.array([[open_price, high_price, low_price, volume]]))[0]
    result = f"<h2>Predicted Close Mastercard Stock Price: {prediction}</h2>"
    return HTMLResponse(content=result)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
