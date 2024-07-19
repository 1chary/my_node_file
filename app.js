const express = require("express")
const app = express()
const path = require("path")
const cors = require("cors")

const { open } = require("sqlite");
const sqlite3 = require("sqlite3");

const dbPath = path.join(__dirname,"mydata.db")

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
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

app.get("/data/", async(request,response) => {
    const getQueryResults = `
    select *
    from user_details
    `
    const results = await db.all(getQueryResults)
    response.send(results)
})

// get with respect to id

app.get("/data/:id/" ,async(request,response) => {
    const { id } = request.params;
    const wrtId = `
    select *
    from user_details
    where id = ${id}
    `
    const details = await db.get(wrtId);
    response.send(details)
})


// insert the data in the database through api
app.post("/data/", async(request,response) => {
    const details = request.body;
    const {name,imageUrl,city} = details;
    const insertData = `
    INSERT INTO user_details(name,image_url,city) 
    VALUES (
        '${name}',
        '${imageUrl}',
        '${city}'
    );
    `;
    const dbResponse = await db.run(insertData)
    const getId =  dbResponse.lastID
    response.send({id: getId})
})
  
// update the data using id 
app.post("/data/:id", async(request,response) => {
    const {id} = request.params;
    const {name} = request.body
    const updateName = `
    UPDATE user_details
    SET name = '${name}'
    WHERE id = ${id}
    `;
    await db.run(updateName)
    response.send('Name Updated Successfully')
})

initializeTheServer()