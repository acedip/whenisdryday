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
<form action="/update/{{email}}" method="GET"> 
	<div id='main'>
   	     <h1>When is Dry Day</h1>
   	     <h2> Here is a list of your existing states </h2>
   	     <a>state : </a><input type="text" name="state1" placeholder="State 1" value="{{lState[0]}}" style="width: 200px; padding: 8px"> <br>
   	     <a>state : </a><input type="text" name="state2" placeholder="State 2" value="{{lState[1]}}" style="width: 200px; padding: 8px"> <br>
   	     <a>state : </a><input type="text" name="state3" placeholder="State 3" value="{{lState[2]}}" style="width: 200px; padding: 8px"> <br>
		<br>
		<input type="submit" name="save" value="Update State" style="width: 100px; padding: 5px; background-color: #3682B4; color: #FFFFFF; border-radius:10px">
		<p> You will never miss a Dry Day ever again. Well only if you have access to your emails. We don't plan to send guys with booze to your house. </p>
	</div>
</form>
</body>
</html>

