<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>When is Dry Day</title>
    <meta name="when is dry day" content="A simple email subscription service, away from the hassles of longin or account creation">
    <meta name="Anirudh singh shekhawat" content="also known as Acedip">

    <!-- Le Bootstrap styles -->
    <link href="./bs/css/bootstrap.css" rel="stylesheet">
    <link href="./bs/css/main.css" rel="stylesheet">
    <link href="./bs/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- Le Bootstrap Social Buttons and Font Awesome styles -->
	<link href="./bs/awesome/css/font-awesome.min.css" rel="stylesheet">
	<link href="./bs/awesome/css/font-awesome.css" rel="stylesheet">
	<link href="./bs/bsb/social-buttons.css" rel="stylesheet">
	<link href="./bs/bsb/social-buttons.less" rel="stylesheet">

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="ico/apple-touch-icon-57-precomposed.png">
    <link rel="shortcut icon" href="ico/favicon.png">

  </head>

  <body class="background">

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <!--<a class="brand" href="#">whenisdryday</a>-->
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="http://localhost:8080"><i class="icon-home"></i> Home</a></li>
              <li><a href="./about.html">About Us</a></li>
              <li><a href="./wetdays.html">Wet Days</a></li>
              <li><a href="#contact">All Dry Days</a></li>
              <li><a href="http://github.com/acedip/whenisdryday">+Code</a></li>
              <li><iframe src="//www.facebook.com/plugins/like.php?href=https%3A%2F%2Fwww.facebook.com%2FWhenisdryday&amp;width&amp;layout=button_count&amp;action=like&amp;show_faces=false&amp;share=true&amp;height=21&amp;appId=381968148649899" scrolling="no" frameborder="0" style="border:none; overflow:hidden; height:21px;" allowTransparency="true"></iframe>
              </li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

      <!-- Main hero unit for a primary marketing message or call to action -->

      <div class="hero-unit pull-right" style="padding:45px">
        
        <div class="span3 offset2">
          <a class="muted"><h5><br><br>DRY DAYS are as per the state/central government calendar, politial calendar and lunar calendar. </h5></a>
          <p><h5>We'll send you an email a day before the DRY DAY in your state</h5></p>
        </div>

        <div class="span4">
          <form class="text-center" action="/" method="GET">
            <h2 style="margin-bottom:5px">When is Dry Day?</h2>

<div id="status">
</div>

			<p>
			<button class="btn btn-facebook" onclick="fb_login();" type="submit"><i class="fa fa-facebook"></i> | Connect </button>
			<button class="btn btn-google-plus"><i class="fa fa-google-plus"></i> | Connect </button>
			<button class="btn btn-twitter"><i class="fa fa-twitter"></i> | Connect </button>
			</p>
			
            <input type="text" id="name" class="input-small" name="name" placeholder="Nick Name" style="width:94px">   
            <br>
            <input type="text" name="email"  placeholder="Email Address">
            <br>
            <select name="state" value="x">
              <option value="">Select A State</option>
              	<option value="Andaman and Nicobar Islands">Andaman and Nicobar Islands</option>
                <option value="Andhra Pradesh">Andhra Pradesh</option>
                <option value="Arunachal Pradesh">Arunachal Pradesh</option>
                <option value="Assam">Assam</option>
                <option value="Bihar">Bihar</option>
                <option value="Chandigarh">Chandigarh</option>
                <option value="Chhattisgarh">Chhattisgarh</option>
                <option value="Dadar and Nagar Haveli">Dadar and Nagar Haveli</option>
                <option value="Daman and Diu">Daman and Diu</option>
                <option value="Delhi">Delhi</option>
                <option value="Goa">Goa</option>
                <option value="Gujarat">Gujarat</option> 
                <option value="Haryana">Haryana</option>
                <option value="Himachal Pradesh">Himachal Pradesh</option>
                <option value="Jammu and Kashmir">Jammu and Kashmir</option>
                <option value="Jharkhand">Jharkhand</option>
                <option value="Karnataka">Karnataka</option>
                <option value="Kerala">Kerala</option>
                <option value="Lakshadeep">Lakshadeep</option>
                <option value="Madya Pradesh">Madya Pradesh</option>
                <option value="Maharashtra">Maharashtra</option>
                <option value="Manipur">Manipur</option>
                <option value="Meghalaya">Meghalaya</option>
                <option value="Mizoram">Mizoram</option>
                <option value="Nagaland">Nagaland</option>
                <option value="Orissa">Orissa</option>
                <option value="Punjab">Punjab</option>
                <option value="Rajasthan">Rajasthan</option>
                <option value="Sikkim">Sikkim</option>
                <option value="Tamil Nadu">Tamil Nadu</option>
                <option value="Tripura">Tripura</option>
                <option value="Uttar Pradesh">Uttar Pradesh</option>
                <option value="Uttaranchal">Uttaranchal</option>
                <option value="West Bengal">West Bengal</option>
            </select>
            <input type="hidden" name="verified" value="0">
            <br>
            <button class="btn btn-danger btn-large" type="submit" name="save" value="1">Say Cheers!!</button> 
            <a class="text-error"><h4>We Do Not Spam</h4></a>       
          </form>
        </div>
              
      </div> <!-- hero class -->

<!-- Le Facebook JS SDK
================================================== -->
 // Load the SDK asynchronously
  (function(thisdocument, scriptelement, id) {
    var js, fjs = thisdocument.getElementsByTagName(scriptelement)[0];
    if (thisdocument.getElementById(id)) return;
	
    js = thisdocument.createElement(scriptelement); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));
	
  window.fbAsyncInit = function() {
  FB.init({
    appId      : '381968148649899', //Your APP ID
    cookie     : true,  // enable cookies to allow the server to access 
                        // the session
    xfbml      : true,  // parse social plugins on this page
    version    : 'v2.1' // use version 2.1
  });

  // These three cases are handled in the callback function.
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });

  };
	
  // This is called with the results from from FB.getLoginStatus().
  function statusChangeCallback(response) {
    if (response.status === 'connected') {
      // Logged into your app and Facebook.
	  _i();
    } else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into this app.';
    }
  }  
  
  function _login() {
	FB.login(function(response) {
	   // handle the response
	   if(response.status==='connected') {
		_i();
	   }
	 }, {scope: 'public_profile,email'});
 }
 
 function _i(){
	 FB.api('/me', function(response) {
		document.getElementById("name").value = response.first_name;
		document.getElementById("email").value = response.email;
	});
 }

</script>

    
    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="./bs/js/jquery.js"></script>
    <script src="./bs/js/bootstrap-transition.js"></script>
    <script src="./bs/js/bootstrap-alert.js"></script>
    <script src="./bs/js/bootstrap-modal.js"></script>
    <script src="./bs/js/bootstrap-dropdown.js"></script>
    <script src="./bs/js/bootstrap-scrollspy.js"></script>
    <script src="./bs/js/bootstrap-tab.js"></script>
    <script src="./bs/js/bootstrap-tooltip.js"></script>
    <script src="./bs/js/bootstrap-popover.js"></script>
    <script src="./bs/js/bootstrap-button.js"></script>
    <script src="./bs/js/bootstrap-collapse.js"></script>
    <script src="./bs/js/bootstrap-carousel.js"></script>
    <script src="./bs/js/bootstrap-typeahead.js"></script>
  </body>
</html>
