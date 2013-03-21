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
		margin-left: 20%;
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
<form action="/new" method="GET"> 
	<div id='main'>
   	     <h1>When is Dry Day</h1>
   	    <input type="text" name="first_name" placeholder="First Name" style="width: 200px; padding: 8px" > <br>
   	    <input type="text" name="last_name" placeholder="Last Name" style="width: 200px; padding: 8px" > <br> 
		<input type="text" name="email" placeholder="Email" required style="width: 200px; padding: 8px" > <br>
		<input type="text" name="state1" placeholder="State 1" required style="width: 200px; padding: 8px"> <br>
		<input type="text" name="state2" placeholder="State 2" style="width: 200px; padding: 8px"> <br>
		<input type="text" name="state3" placeholder="State 3" style="width: 200px; padding: 8px"> <br>
		<input type="hidden" name="verified" value="0" > <br>
		<br>
			
		<input type="submit" name="save" value="Sign Me Up" style="width: 100px; padding: 5px; background-color: #3682B4; color: #FFFFFF; border-radius:10px">
		<p> You will never miss a Dry Day ever again. Well only if you have access to your emails. We don't plan to send guys with booze to your house. </p>
	</div>
</form>
</body>
</html>

