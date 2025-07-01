// index.js
const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

app.post('/query', async (req, res) => {
    try {
        const { question } = req.body;

        if (!question) {
            return res.status(400).json({ error: "Question chahiye!" });
        }

        // Flask ko call karo
        const response = await axios.post(
            'http://localhost:5000/ask',
            { question }
        );

        res.json({
            question: question,
            answer: response.data.answer
        });

    } catch (error) {
        res.status(500).json({
            error: "Server error: " + error.message
        });
    }
});

app.listen(3000, () => {
    console.log('✅ Node.js running on http://localhost:3000');
});

