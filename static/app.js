// Set constraints for the video stream
var constraints = { video: { facingMode: "user" }, audio: false };
// Define constants
const cameraView = document.querySelector("#camera--view"),
    cameraOutput = document.querySelector("#camera--output"),
    cameraSensor = document.querySelector("#camera--sensor"),
    cameraTrigger = document.querySelector("#camera--trigger")
// Access the device camera and stream to cameraView
function cameraStart() {
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function(stream) {
        track = stream.getTracks()[0];
        cameraView.srcObject = stream;
    })
    .catch(function(error) {
        console.error("Oops. Something is broken.", error);
    });
}
// Take a picture when cameraTrigger is tapped
cameraTrigger.onclick = function() {
    cameraSensor.width = cameraView.videoWidth;
    cameraSensor.height = cameraView.videoHeight;
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
    cameraOutput.src = cameraSensor.toDataURL("image/jpeg");
    cameraOutput.classList.add("taken");
    //uploadFile(cameraOutput.src);
    var imagefile = dataURLtoFile(cameraOutput.src, "image.jpeg");
    uploadFile(imagefile);
    //uploadFile("/home/becode2/Desktop/Zelus_Images/archive/archive_cleaned/vinted_test_only/dresses/1367721197.jpeg");
    setTimeout(function() {
        location.reload();
    }, 3000);
};

function uploadFile(file){
    if(file){
        var xhr = new XMLHttpRequest();
        var url = "/upload";
        xhr.open("POST", url, true);
        // xhr.setRequestHeader("Content-Type", "multipart/form-data");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                console.log(xhr.responseText);
            }
        };
        var formData = new FormData();
        formData.append("image", file);
        xhr.send(formData);
    }
}

function dataURLtoFile(dataurl, filename) {
 
    var arr = dataurl.split(','),
        mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), 
        n = bstr.length, 
        u8arr = new Uint8Array(n);
        
    while(n--){
        u8arr[n] = bstr.charCodeAt(n);
    }
    
    return new File([u8arr], filename, {type:mime});
}

// Start the video stream when the window loads
window.addEventListener("load", cameraStart, false);