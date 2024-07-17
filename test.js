
function getTheValue(array,action) {
    if (action === "call") {
        const key = JSON.stringify(array)
        if (key in cache) {
            return cache[key]
        }
        else {
            const value = array.reduce((prev,current) => prev + current)
            cache[key] = value
            count += 1
            return cache[key]
        }
    }
    else {
        return count
    }
}


let fnName = "sum"
let actions = ["call","call","getCallCount","call","getCallCount"]
let values = [[2,2],[2,2],[],[1,2],[]]
let count = 0
let cache = {}
let storeResult = []
for (let i = 0; i < values.length; i++) {
    let result = getTheValue(values[i],actions[i])
    storeResult.push(result)
}
console.log(storeResult)