<!doctype html>
<head>
	<meta charset="utf-8">
	<link href='http://fonts.googleapis.com/css?family=Alegreya:400&subset=latin' rel='stylesheet' type='text/css'>
	<title>When is Dry Day ?</title>
	<style type='text/css'>
	body {
		background-color: #eee; /* I took an oath never to use flat white backgrounds. */
		text-rendering: optimizeLegibility;
		color: #222;
		margin: 0px;
		padding: 0px;
		margin-top: 5%;
		width: 100%;
		font-family: 'Alegreya'; /* Do you speak German? No? Then STOP USING HELVETICA. */
		text-align: center;
	}
	
	h1 {
		font-weight: normal;
		font-size: 60px;
		margin: 0px;
	}

	h2 {
		font-weight: normal;
  		font-size: 40px;
		margin-left:30%;
		text-align: left;
	}
	#main {
		margin: auto;
		width: 50em;
		text-align: center;
	}
		
	a, a:visited { color: inherit; }
	
	#by {
		color: #888;
	}
	
	em {
		font-style: normal;
		border: 1px solid red;
	}
	</style>
</head>

<body>
<form action="/insert" method="GET"> 
	<div id='main'>
   	     <h1>When is Dry Day</h1>
   	     <h2> For internal use only<br>Insert Dry Days info in db</h2>
   	     <p>Date format YYYY-MM-DD. For Eg 2012-01-01<br>
   	     	Sate in all lower case</p>
   	     
		<input type="text" name="drydate" placeholder="Dry Date" required style="width: 200px; padding: 8px" > <br>
		<input type="text" name="state" placeholder="State" required style="width: 200px; padding: 8px"> <br><br>
		
		<input type="submit" name="save" value="Save" style="width: 100px; padding: 5px; background-color: #3682B4; color: #FFFFFF; border-radius:10px">
		<p> You will never miss a Dry Day ever again. Well only if you have access to your emails. We don't plan to send guys with booze to your house. </p>
	</div>
</form>
</body>
</html>

