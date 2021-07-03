// Get the 'deepai' package here (Compatible with browser & nodejs):
//     https://www.npmjs.com/package/deepai
// All examples use JS async-await syntax, be sure to call the API inside an async function.
//     Learn more about async-await here: https://javascript.info/async-await

// Example posting a image URL:

const deepai = require('deepai'); // OR include deepai.min.js as a script tag in your HTML

deepai.setApiKey('quickstart-QUdJIGlzIGNvbWluZy4uLi4K');

(async function() {
    var resp = await deepai.callStandardApi("facial-recognition", {
            image: "https://nkcf.org/wp-content/uploads/2017/11/people-880x480.jpg",
    });
    console.log(resp);
	jsonArrData = JSON.stringify(resp)
	console.log(jsonArrData)
	return resp
})()


// // Example posting file picker input image (Browser only):

// const deepai = require('deepai'); // OR include deepai.min.js as a script tag in your HTML

// deepai.setApiKey('quickstart-QUdJIGlzIGNvbWluZy4uLi4K');

// (async function() {
//     var resp = await deepai.callStandardApi("facial-recognition", {
//             image: document.getElementById('yourFileInputId'),
//     });
//     console.log(resp);
// })()


// // Example posting a local image file (Node.js only):
// const fs = require('fs');

// const deepai = require('deepai'); // OR include deepai.min.js as a script tag in your HTML

// deepai.setApiKey('quickstart-QUdJIGlzIGNvbWluZy4uLi4K');

// (async function() {
//     var resp = await deepai.callStandardApi("facial-recognition", {
//             image: fs.createReadStream("/path/to/your/file.jpg"),
//     });
//     console.log(resp);
// })()
