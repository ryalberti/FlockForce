// imports
import signals from './test_json_244.json' assert {type: 'json'};
console.log(signals)

//functions
function loadInput (fileLocation){
    // const fs = require('fs');
    // fs.readFile(fileLocation, 'utf8', (err, data) => {
    //     const json = JSON.parse(data);
    //     console.log(json.posts);
    //   });

    fetch(fileLocation)
        .then((response) => response.json())
        .then((json) => console.log(json));

    // $.getJSON(fileLocation, function(json) {
    //     console.log(json); // this will show the info it in firebug console
    // });
}

function fillArray(jsonOb){
    const res_array =[];
    for (let i in JSONobject){
        res_array.push([i,JSONobject[i]]);
    }
}

console.log("test");
loadInput("http://localhost:3000/998")