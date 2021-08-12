# [Make a smart webcam in JavaScript with a TensorFlow.js pre-trained Machine Learning model](https://codelabs.developers.google.com/codelabs/tensorflowjs-object-detection?hl=en&continue=https%3A%2F%2Fcodelabs.developers.google.com%2F%3Fcat%3Dmachinelearning#0)

## What you'll build

* Create a webpage that uses machine learning directly in the web browser via TensorFlow.js to classify and detect common objects, (yes, including more than one at a time), from a live webcam stream.
* Supercharge your regular webcam to identify objects and get the coordinates of the bounding box for each object it finds
* Highlight the found object in the video stream

## What you'll learn

* How to load a pre-trained TensorFlow.js model
* How to grab data from a live webcam stream and draw it to canvas
* How to classify an image frame to find the bounding box(es) of any object(s) the model has been trained to recognize
* How to use the data passed back from the model to highlight found objects

## TensorFlow.js

* Where can it be used
  * Client side in the web browser
  * Server side and even IoT devices like Raspberry Pi using Node.js
  * Desktop apps using Electron
  * Native mobile apps using React Native
  * backend
    * WebGL on GPU
    * Web Assembly (WASM) on CPU
    * CPU
* [Powers and features](https://codelabs.developers.google.com/codelabs/tensorflowjs-object-detection?hl=en&continue=https%3A%2F%2Fcodelabs.developers.google.com%2F%3Fcat%3Dmachinelearning#1)

## Pre-trained models

* wrapped in an easy to user class
* [Models for JS](https://www.tensorflow.org/js/models)
* [TensorFlow Hub](https://tfhub.dev/s?deployment-format=tfjs)
* Transfer learning
  * the practice of transferring information learnt from one machine learning task, to another similar example

### COCO-SSD

* a pre-trained object detection ML model
  * localize abd identify multiple objects in a single image
  * recognizes 90 common everyday objects
* COCO (Common Objects in Context) dataset
  * contains over 200,000 labeled images
* [SSD (Single Shot Multibox Detection)](https://towardsdatascience.com/understanding-ssd-multibox-real-time-object-detection-in-deep-learning-495ef744fab)

## Get set up

* Glitch.com or Codepen.io
* skeleton
  * HTML page (index.html)
  * Stylesheet (style.css)
  * JS code (script.js)
* there is an added import in the HTML file for the TensorFlow.js library

```HTML
<!-- Import TensorFlow.js library -->
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs/dist/tf.min.js" type="text/javascript"></script>
```

## Populate the HTML skeleton

* A title for the page
* Some descriptive text
* A button to enable the webcam
* **A video tag to render the webcam stream to**
* a section tag: the demo space
  * id="demos"
  * class="invisible"
* a script tag: import TF and COCO-SSD

## Add style

* styles for the HTML elements
* CSS classes

## Create JS skeleton

* Referencing key DOM elements
  * const video = document.getElementById('webcam')
* Check for webcam support
  * getUserMedia
  * if webcam supported, add event listener to button for when user wants to activate it to call enableCam function which we will define in the next step.
    * addEventListener('click', enableCam);
* Fetching the webcam stream
* **getElementById.classList.remove**
* **navigator**: The navigator object contains information about the browser

## Machine Learning model usage

* Loading the model
* Before we can use COCO-SSD class we must wait for it to finish loading.

```JavaScript
cocoSsd.load().then(function (loadedModel) {
  model = loadedModel;
  // Show demo section now model is ready to use.
  demosSection.classList.remove('invisible');
});
```

* Note: cocoSsd is an external object loaded from our index.html script tag import

## HTML

```HTML
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello World - TensorFlow.js</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
  </head>  
  <body>
    <h1>TensorFlow.js Hello World</h1>
    
    <p id="status">Awaiting TF.js load</p>

    <!-- Import TensorFlow.js library -->
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@2.0.0/dist/tf.min.js" type="text/javascript"></script>
    <!-- *** Import tfjs-vis - optional *** -->
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs-vis/dist/tfjs-vis.umd.min.js"></script>
    <!-- Import the page's JavaScript to do some stuff -->
    <script src="/script.js" defer></script>
  </body>
</html>
```

## CSS

```CSS
body {
  font-family: helvetica, arial, sans-serif;
  margin: 2em;
}

h1 {
  font-style: italic;
  color: #FF6F00;
}
```

## JS

```JavaScript
const status = document.getElementById('status');
status.innerText = 'Loaded TensorFlow.js - version: ' + tf.version.tfjs;
```

## Notes

* JS
  * interpreted by **browsers** with JS engine
    * JS code -> JS engine -> machine code
* JS Engine
  * V8: Chrome, IE
  * Firefox: Spidermonkey
* Can you use JS everywhere?
  * Mobile
  * Desktop
  * Server
* Runtime environment (RTE)
  * the environment in which a program or application is executed.
  * It's the hardware and software infrastructure that supports the running of a particular codebase in real time
  * Node.js
    * allow us to run JS on a machine (build standalone applications)
    * JS engine (V8)
    * HTTP module: to be used on the server side
    * npm (node package manager)
* Full Stack Development
  * Frontend: JS
    * React
    * Angular
  * Web Application Framework
    * Django for Python
    * Express.js
  * Backend
    * Node.js
  * Database
    * mongoDB
  * MERN (mongoDB, express.js, react, node.js)
  * MEAN (mongoDB, express.js, angular, node.js)
