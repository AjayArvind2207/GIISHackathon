var fireBase = fireBase || firebase;
var hasInit = false;
var firebaseConfig = {
  apiKey: "AIzaSyBxxmcKtYP0J1LMRn8egow2ldVDdooK5gc",
  authDomain: "quarantine-plus-plus.firebaseapp.com",
  projectId: "quarantine-plus-plus",
  storageBucket: "quarantine-plus-plus.appspot.com",
  messagingSenderId: "670957449467",
  appId: "1:670957449467:web:a0e3ed81217ab4b5aa405e",
  measurementId: "G-3BDYW6PKQH"
};
if (!hasInit) {
  firebase.initializeApp(firebaseConfig);
  hasInit = true;
}