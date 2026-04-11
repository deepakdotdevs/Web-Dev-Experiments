async function checkNews() {
    const text = document.getElementById("newsInput").value;
    const resultBox = document.getElementById("result");

    if (!text) {
        resultBox.innerText = "⚠️ Please enter some news!";
        return;
    }

    // Loading state
    resultBox.innerText = "⏳ Analyzing...";

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        let color = "white";

        if (data.prediction.includes("Real")) {
            color = "lightgreen";
        } else {
            color = "red";
        }

        resultBox.style.color = color;

        resultBox.innerHTML = `
            ${data.prediction} <br>
            <small>Confidence: ${data.confidence}%</small>
        `;

    } catch (error) {
        resultBox.innerText = "Error connecting to server";
        console.error(error);
    }
}