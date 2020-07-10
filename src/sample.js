"use strict";
exports.__esModule = true;
var cv = require("opencv4nodejs");
var img = cv.imread('./lenna.jpg');
var classifier = new cv.CascadeClassifier(cv.HAAR_FRONTALFACE_ALT2);
var grayImg = img.bgrToGray();
var result = classifier.detectMultiScale(grayImg);
if (!result.objects.length) {
    throw new Error('failed to detect faces');
}
var minDetections = 10;
result.objects.forEach(function (faceRect, i) {
    if (result.numDetections[i] < minDetections) {
        return;
    }
    var rect = cv.drawDetection(img, faceRect, {
        color: new cv.Vec3(255, 0, 0),
        segmentFraction: 4
    });
});
cv.imshowWait('result', img);
