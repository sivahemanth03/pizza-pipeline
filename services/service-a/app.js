const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    service: 'service-a',
    message: 'Pizza order service is running!'
  });
});

app.get('/api', (req, res) => {
  res.json({
    message: 'Welcome to the Pizza Order API',
    orders: ['Margherita', 'Pepperoni', 'BBQ Chicken']
  });
});

app.listen(PORT, () => {
  console.log(`Service A running on http://localhost:${PORT}`);
});