# [Firebase web codelab](https://firebase.google.com/codelabs/firebase-web#0)

* Sync data using Cloud Firestore and Cloud Storage for Firebase.
* Authenticate your users using **Firebase Authentication**.
* Deploy your web app on Firebase Hosting.
* Send notifications with **Firebase Cloud Messaging**.
* Collect your web app's performance data.

## Create and set up a Firebase project

* In the Firebase console, click Add Project, and then name your Firebase project FriendlyChat. Remember the **project ID** for your Firebase project.
* Firebase products that are available for web apps:
  * **Firebase Authentication** to easily allow your users to sign into your app.
  * Cloud Firestore to save structured data on the cloud and get instant notification when data changes.
  * Cloud Storage for Firebase to save files in the cloud.
  * Firebase Hosting to host and serve your assets.
  * **Firebase Cloud Messaging to send push notifications** and display browser popup notifications.
  * Firebase Performance Monitoring to collect user performance data for your app.

### Add a Firebase web app to the project

### Enable Google sign-in for Firebase Authentication

### Enable Cloud Firestore

### Enable Cloud Storage

## Import and configure Firebase

## Set up user sign-in

## Write messages to Cloud Firestore

* Cloud Firestore data is split into **collections, documents, fields, and subcollections**

## Read messages

* Synchronize messages

## Send images

* Save images to Cloud Storage

## **Show notifications**

* Add support for browser notifications
* Firebase Cloud Messaging (FCM) is a cross-platform messaging solution that lets you reliably deliver messages and notifications at no cost

### Whitelist the GCM Sender ID

* **web app manifest (manifest.json)**
  * gcm_sender_id: a hard-coded value indicating that FCM is authorized to send messages to this app

### Add the FCM service worker

### Get FCM device tokens

### Request permissions to show notifications

### Get your device token

### Send a notification to your device

## Cloud Firestore security rules

## Cloud Storage security rules

## Collect performance data

## Deploy your app using Firebase Hosting

* The hosting settings are specified under the hosting attribute (firebase.json):
* ```firebase deploy --except functions```
