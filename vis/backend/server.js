const express = require('express')
const sqlite = require('sqlite3').verbose()

const app = express()

// Open database
let db = new sqlite.Database('../craigslistVehicles.db', sqlite.OPEN_READONLY,
  err => {
    if (err) {
      console.error(err.message)
    }
    console.log('Connected to db')
  }
)

let sql = `
  SELECT *
  FROM Vehicle
  LIMIT 1000`

app.get('/', (req, res) => {
  out = []
  db.all(sql, [], (err, rows) => {
    if (err) {
      throw err
    }
    rows.forEach(row => {
      out.push(row)
    })
   res.status(200).json(out);
   return
  })
  res.status(400);
});

app.listen(2000, () => {
  console.log(`Server started on port 2000`);
});