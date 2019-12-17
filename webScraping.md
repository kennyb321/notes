<h1>Mining Social Media / Web Scraping</h1>

<h2>Using API's</h2>

You tell the API what data you want by including it in the URL.
Were going to request data feed of posts puyblished by the BuzzFeed Tasty YouTube page.
enter this into the URL
````https://www.googleapis.com/youtube/v3/search?channelId=UCJFp8uSYCjXOMnkUyb3CQ3Q&part=snippet.````
<br>
<h4>Anatomy of a API Call</h4>
<p><b>Base:</b>Indicates which API you are using<br>
<b>Parameters:</b>Tells the call which data you want to harvest and copnveys information about who is making the call.
</p>

<h4>Breadown of our API call</h4>
<dl>
	<dt>https://www.googleapis.com</dt>
		<dd>The base of our API call. Specifies that well be using googleapi </dd>
	<dt>/youtube</dt>
		<dd>specifies that well be using the youtube API</dd>
	<dt>/v3</dt>
		<dd>Specifies that well be using version3</dd>
	<dt>search?channelID=</dt>
		<dd>specifies the parameter of our search. We are using ythe channelID parameter</dd>
	<dt>UCJFp8uSYCjXOMnkUyb3CQ3Q&part=snippet.`</dt>
		<dd>The Youtube ChannelIF we are using</dd>
	</dl>
