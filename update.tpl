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

      <!-- Main hero unit for a primary marketing message or call to action -->

      <div class="hero-unit text-center" style="padding:45px">
          <form action="/update/{{email}}" method="GET"> 
          <br>
          <br>
   	     <h4> You are already signed up to get updates about </h4>
   	     <a class="text-error"><h4>{{lState}}</h4></a>
		Choose from the list to update
		<br>
            <select name="state" required>
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
<!--                <option value="Gujarat">Gujarat</option> UNTIL FIGURE OUT THE UX FOR THIS -->
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
            <br>
            <button class="btn btn-danger btn-large" type="submit" name="save" value="1">Update State!!</button> 
          </form>
              
      </div> <!-- hero class -->
    
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
