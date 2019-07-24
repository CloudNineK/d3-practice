const express = require('express')
const cors = require('cors')


const app = express()

// Allow CORS
app.use(cors())

// Open database
const sqlite = require('sqlite3').verbose()
let db = new sqlite.Database('./craigslistVehicles.db', sqlite.OPEN_READONLY,
  err => {
    if (err) {
      console.error(err.message)
    }
    console.log('Connected to db')
  }
)


app.get('/vehicles', (req, res) => {
  if (!req.query.id) {
    res.status(400);
    console.log("no ID")
  }

  let sql = `
    SELECT *
    FROM Vehicle
    LIMIT 1000`

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