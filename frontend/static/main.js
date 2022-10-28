$(() => {
  var firebase_config = {
    apiKey: "%%% API_KEY %%%",
    authDomain: "%%% AUTH_DOMAIN %%%",
  };
  firebase.initializeApp(firebase_config);

  var user_id_token = null;

  firebase.auth().onAuthStateChanged((user) => {
    if (user) {
      user.getIdToken().then((id_token) => {
        user_id_token = id_token;
        $('#display-name').text(user.displayName ? user.displayName : user.email);
        $('#logged-out').hide();
        $('#logged-in').show();
      });
    } else {
      user_id_token = null;
      $('#logged-in').hide();
      $('#logged-out').show();
    }
  });

  var ui_config = {
    'signInSuccessUrl': '/',
    'signInOptions': [
      firebase.auth.EmailAuthProvider.PROVIDER_ID,
    ],
  };
  var ui = new firebaseui.auth.AuthUI(firebase.auth());
  ui.start('#firebaseui-auth-container', ui_config);

  var sign_out_button = $('#sign-out');
  sign_out_button.click((event) => {
    event.preventDefault();
    firebase.auth().signOut().catch((error) => {
      console.log(error);
    });
  });
});
