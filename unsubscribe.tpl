<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>When is Dry Day</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="when is dry day" content="A simple email subscription service, away from the hassles of longin or account creation">
    <meta name="Anirudh singh shekhawat" content="also known as Acedip">

    <!-- Le styles -->
    <link href="./bs/css/bootstrap.css" rel="stylesheet">
    <style type="text/css">
      body {
        padding-top: 60px;
        padding-bottom: 40px;
        background-color: transparent;
      }
      html {
          background: #ffffcc url("./bs/img/480_home_page_final_2.jpg") no-repeat center bottom fixed;
          -webkit-background-size: 100% 100%;
          -moz-background-size: 100% 100%;
          -o-background-size: 100% 100%;
          background-size: 100% 100%;
      }
      /* For mobile */
      @media (max-width: 767px) {
          html {
			  background-image: url("./bs/img/480_home_page_final_2.jpg");
          }
      }
    </style>

    <link href="./bs/css/bootstrap-responsive.css" rel="stylesheet">
    
    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="ico/apple-touch-icon-57-precomposed.png">
    <link rel="shortcut icon" href="ico/favicon.png">
  </head>

  <body>

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
              <li><a href="http://stage.whenisdryday.in">Home</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

 <div class="container">
      <!-- Main hero unit for a primary marketing message or call to action -->
      <div class="hero-unit text-center">
              <form action="/unsubscribe/{{emailid}}" method="GET"> 
      			<br>
			<br>
        <p>We are really sad to see you go. Would you like to consider once again and not leave us? </p>
	        <p> <button name="cancel" value="0" onclick="location.href='http://stage.whenisdryday.in/wetdays.html';" class="btn btn-primary btn-large">Yes, Not Going Anywhere</button> </p>
    	    <p> <button name="save" value="1" class="btn btn-info">No, Screw you!!</button> </p>
    	</form>
      </div>      
</div>      
    
    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/jquery.js"></script>
    <script src="js/bootstrap-transition.js"></script>
    <script src="js/bootstrap-alert.js"></script>
    <script src="js/bootstrap-modal.js"></script>
    <script src="js/bootstrap-dropdown.js"></script>
    <script src="js/bootstrap-scrollspy.js"></script>
    <script src="js/bootstrap-tab.js"></script>
    <script src="js/bootstrap-tooltip.js"></script>
    <script src="js/bootstrap-popover.js"></script>
    <script src="js/bootstrap-button.js"></script>
    <script src="js/bootstrap-collapse.js"></script>
    <script src="js/bootstrap-carousel.js"></script>
    <script src="js/bootstrap-typeahead.js"></script>
  </body>
</html>
