import { NotificationHandler } from './notificationHandler';
import { environment } from './environments/environment';
import firebase from 'firebase/app';
import "firebase/auth";
import 'firebase/firestore';
import { User } from 'mytrack-data-classes';

console.log("Hello TS");

firebase.initializeApp(environment.firebase);
const email = "yupeng-31" + "@mytrackplus.org";
const password = "123456";
firebase.auth().signInWithEmailAndPassword(email, password);
const db = firebase.firestore();

async function sendHealthNotifications(){
    const user = await User.getByID(firebase.auth().currentUser.uid, db);
    // console.log(user.prefs["sunday"]);
    // NotificationHandler.sendContextBasedNotification(user);
}

sendHealthNotifications();

let notifType = NotificationHandler.getNotificationType();