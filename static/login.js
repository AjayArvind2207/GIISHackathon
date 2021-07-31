// FirebaseUI config.
var uiConfig = {
  signInSuccessUrl: "/",
  signInOptions: [
    firebase.auth.GoogleAuthProvider.PROVIDER_ID,
  ],
};

firebase.auth().setPersistence(firebase.auth.Auth.Persistence.SESSION)
  .then(() => {
    var provider = new firebase.auth.GoogleAuthProvider();
    // In memory persistence will be applied to the signed in Google user
    // even though the persistence was set to 'none' and a page redirect
    // occurred.
    var ui = new firebaseui.auth.AuthUI(firebase.auth());
    return ui.start("#firebaseui-auth-container", uiConfig);
  })
  .catch((error) => {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
  });



