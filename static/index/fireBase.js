var fireBase = fireBase || firebase;
var hasInit = false;
var config = {
  apiKey: "AIzaSyD5DGSBbkYMqCfLRJQSFvVPtQ6Cw6dSF40",
  authDomain: "reformbar-a4b02.firebaseapp.com",
  projectId: "reformbar-a4b02",
  storageBucket: "reformbar-a4b02.appspot.com",
  messagingSenderId: "783205470099",
  appId: "1:783205470099:web:25e4f8b5c7ed369e96e266",
  measurementId: "G-YB39ZQSM0G",
};

if (!hasInit) {
  firebase.initializeApp(config);
  hasInit = true;
}
