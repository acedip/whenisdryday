<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>When is Dry Day</title>
  <meta name="when is dry day" content="A simple email subscription service, away from the hassles of longin or account creation">
  <meta name="Anirudh singh shekhawat" content="also known as Acedip">
  <!-- Le styles -->
  <link href="./bs/css/bootstrap.css" rel="stylesheet">
  <link href="./bs/css/main.css" rel="stylesheet">
  <link href="./bs/css/bootstrap-responsive.css" rel="stylesheet">
  <!-- Fav and touch icons -->
  <link rel="apple-touch-icon-precomposed" sizes="144x144" href="ico/apple-touch-icon-144-precomposed.png">
  <link rel="apple-touch-icon-precomposed" sizes="114x114" href="ico/apple-touch-icon-114-precomposed.png">
  <link rel="apple-touch-icon-precomposed" sizes="72x72" href="ico/apple-touch-icon-72-precomposed.png">
  <link rel="apple-touch-icon-precomposed" href="ico/apple-touch-icon-57-precomposed.png">
  <link rel="shortcut icon" href="ico/favicon.png">
  <style type="text/css"></style>
</head>
<body class="otherbackground">

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
      <li><a href="http://whenisdryday.in">Home</a></li>
      <li><a href="./about">About Us</a></li>
      <li><a href="./wetdays">Wet Days</a></li>
      <li class="active"><a href="./alldrydays">All Dry Days</a></li>
      <li><a href="http://github.com/acedip/whenisdryday">+Code</a></li>
    </ul>
  </div><!--/.nav-collapse -->
</div>
</div>
</div>

<!-- Main hero unit for a primary marketing message or call to action -->
<div class="hero-unit text-center">
<h2 class="text-error">List of all Dry Days in all States</h2>

%for _s, sdata in smap.items():
<table class="table table-striped table-hover table-bordered table-condensed" boder="10">
<caption><h2 class="text-success">{{_s}}</h2></caption>
  <thead>
    <tr>
      <th>Dry Day</th>
      <th>Reason</th>
    </tr>
  </thead>
  %for rows in sdata:
    <tr>
      <td>{{rows.dd}}</td>
      <td>{{rows.reason}}</td>
    </tr>
  %end
  </table>
%end
</div> <!-- hero class -->

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
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-60498113-1', 'auto');
ga('send', 'pageview');

</script>
</body>
</html>
