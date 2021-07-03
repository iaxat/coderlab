// Get the 'deepai' package here (Compatible with browser & nodejs):
//     https://www.npmjs.com/package/deepai
// All examples use JS async-await syntax, be sure to call the API inside an async function.
//     Learn more about async-await here: https://javascript.info/async-await

// Example posting a image URL:

const deepai = require('deepai'); // OR include deepai.min.js as a script tag in your HTML

deepai.setApiKey('quickstart-QUdJIGlzIGNvbWluZy4uLi4K');

(async function() {
    var resp = await deepai.callStandardApi("facial-recognition", {
            image: "https://1.bp.blogspot.com/-jCxX62XeFwY/XQpnctlnDEI/AAAAAAAABmc/vtvcFxfSaNAoS8_6NE-KrKzPWAHNjWhpgCEwYBhgL/s1600/Actress-Katrina-Kaif-Hot-High-Resolution-Mobile-Wallpapers-HD-029.jpg",
    });
    console.log(resp);
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
