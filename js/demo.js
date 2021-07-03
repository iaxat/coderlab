// fetch API face detection
// using https://rapidapi.com/inferdo/api/face-detection6/


fetch("https://microsoft-face1.p.rapidapi.com/detect?returnFaceId=true&recognitionModel=recognition_01&detectionModel=detection_01&returnFaceAttributes=age", {
	"method": "POST",
	"headers": {
		"content-type": "application/json",
		"x-rapidapi-host": "microsoft-face1.p.rapidapi.com"
	},
	"body": {
		"url": "http://www.hdwallpaperspulse.com/wp-content/uploads/2017/10/26/island-natural-wallpaper.jpg"
	}
})
.then(response => {
	console.log(response);
})
.catch(err => {
	console.error(err);
});
