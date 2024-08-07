const express = require("express")
const app = express()
const bodyParser = require('body-parser');
const bcrypt = require("bcrypt")
const jwt = require("jsonwebtoken")
const path = require("path")
const cors = require("cors")

const { open } = require("sqlite");
const sqlite3 = require("sqlite3");

const dbPath = path.join(__dirname,"mydata.db")
app.use(bodyParser.json());
app.use(cors());

let db = null;

const initializeTheServer = async () => {
    try {
        db = await open({
            filename: dbPath,
            driver: sqlite3.Database,
        });
        app.listen(3001, () => {
            console.log("Server is running at http://localhost:3001")
        })
    }
    catch(e) {
        console.log(`DB: ERROR ${e.message}`);
        process.exit(1)
    }
}

//get all the data //

app.get("/users/", async(request,response) => {
    const getQueryResults = `
    select *
    from users
    `
    const results = await db.all(getQueryResults)
    response.send(results)
})

// insert the data in the table using request body 

app.post("/signUp/", async (request,response) => {
    const {name,password} = request.body;
    const hashedPassword = await bcrypt.hash(password,10)
    const checkUsernameAvailable = `
    SELECT name
    FROM users
    WHERE name = '${name}';
    `;
    const queryResults = await db.get(checkUsernameAvailable)
    if (queryResults === undefined) {
        const insertNewUser = `
        INSERT INTO users(name,password)
        VALUES (
            '${name}',
            '${hashedPassword}'
        );
        `;
        await db.run(insertNewUser)
        response.send("user added successfully");
    }
    else {
        response.status = 400;
        response.send("user already exists");
    }
})


// check if the user available in the database or not 

app.post("/login", async(request,response) => {
    const {name,password} = request.body;
    const dbUser = `
    SELECT *
    FROM users
    WHERE name = '${name}';
    `;
    const checkAvailability = await db.get(dbUser)
    if (checkAvailability === undefined) {
        response.status(400);
        response.send("Invalid user")
    }
    else {
        const comparePassword = await bcrypt.compare(password,checkAvailability.password);
        if (comparePassword === true) {
            const payLoad = {
                username: name,
            }
            const jwtToken = jwt.sign(payLoad, "my_token");
            response.send({jwtToken})
        }
        else {
            response.status(400);
            response.send("Invalid Password")
        }
    }
})

app.get("/check" , async(request,response) => {
    let query = `
        SELECT *
        FROM session_management
    `
    const result = await db.all(query)
    response.send(result)
})

// checking session management 
app.post("/sessions", async(request,response) => {
    let time = new Date()
    let date = time.getDate().toString()
    let month = (time.getMonth()+1).toString()
    let year = time.getFullYear().toString()
    let check = date + month + year
    ;
    const insertIntoTable = `
    INSERT INTO session_management(in_time)
    VALUES (${check});`;
    await db.run(insertIntoTable)
    response.send("Added in time")
})


app.post("/open", async(request,response) => {
    const {userInput} = request.body
    const url = await fetch(`https://api.openweathermap.org/data/2.5/weather?units=metric&q=${userInput}&appid=2fe74895e927cbe81e92169f1a159f12`)
    const data = await url.json()
    response.send(data)
})


initializeTheServer()