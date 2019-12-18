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
	
our function call yeilds this result:

````
{

 "error": {

  "errors": [

   {

    "domain": "usageLimits",

    "reason": "dailyLimitExceededUnreg",

    "message": "Daily Limit for Unauthenticated Use Exceeded. Continued use requires signup.",

    "extendedHelp": "https://code.google.com/apis/console"

   }

  ],

  "code": 403,

  "message": "Daily Limit for Unauthenticated Use Exceeded. Continued use requires signup."

 }

}
````

Youll notice that something went wrong, the problem is that we dont have an API key.
To get a google API key, go to the google developers site and request an API key,
````https://console.developers.google.com/apis/credentials.````

Once you have the key, navigate tio the Library page. Select the API you want to use, and click 'enable'

<h3>New API call with our API key</h3>
Now well d our API call again, this time using our API key.
<br>
API Key = ````AIzaSyA7DxagTfSwLoumitSYqiaj5vBFTqXOcOM````
API call = ````https://www.googleapis.com/youtube/v3/search?channelId=UCJFp8uSYCjXOMnkUyb3CQ3Q&part=snippet&key=AIzaSyA7DxagTfSwLoumitSYqiaj5vBFTqXOcOM````

Now we should be getting some data!
This is the data that got returned
````{
 "kind": "youtube#searchListResponse",
 "etag": "\"j6xRRd8dTPVVptg711_CSPADRfg/xrzwjo555UqDuZP46ygzBVXkn_Q\"",
 "nextPageToken": "CAUQAA",
 "regionCode": "US",
 "pageInfo": {
  "totalResults": 467201,
  "resultsPerPage": 5
 },
 "items": [
  {
   "kind": "youtube#searchResult",
   "etag": "\"j6xRRd8dTPVVptg711_CSPADRfg/SCNlZxTPnx9vUSIjSpCQpj_luO4\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "5Sa9nYKiYg0"
   },
   "snippet": {
    "publishedAt": "2018-02-28T17:00:42.000Z",
    "channelId": "UCJFp8uSYCjXOMnkUyb3CQ3Q",
    "title": "The Original Orange Chicken by Panda Express",
    "description": "Reserve the One Top: http://bit.ly/2v0iast Get the recipe: https://tasty.co/recipe/original-orange-chicken-by-panda-express Buy the Tasty Cookbook Today: ...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/5Sa9nYKiYg0/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/5Sa9nYKiYg0/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/5Sa9nYKiYg0/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "Tasty",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"j6xRRd8dTPVVptg711_CSPADRfg/CBFWKg9pIZt2cDqFOoYSqh6D_Bs\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "MjVgIXccYXA"
   },
   "snippet": {
    "publishedAt": "2018-07-22T16:00:19.000Z",
    "channelId": "UCJFp8uSYCjXOMnkUyb3CQ3Q",
    "title": "The Most Fool-Proof Macarons You&#39;ll Ever Make",
    "description": "https://www.buzzfeed.com/marietelling/how-to-make-macarons?utm_term=.kkgkRxLmw#.ae7RewPg4 Get the recipe! - https://tasty.co/recipe/macarons Shop the ...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/MjVgIXccYXA/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/MjVgIXccYXA/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/MjVgIXccYXA/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "Tasty",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"j6xRRd8dTPVVptg711_CSPADRfg/M_Y8cgSo-yIDCRoVptE_ZuYO0FA\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "KLGSLCaksdY"
   },
   "snippet": {
    "publishedAt": "2016-10-27T01:00:00.000Z",
    "channelId": "UCJFp8uSYCjXOMnkUyb3CQ3Q",
    "title": "How To Cook With Cast Iron",
    "description": "This guide will make cooking with cast iron a breeze! Check us out on Facebook! - facebook.com/buzzfeedtasty MUSIC Promenade En Provence Licensed via ...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/KLGSLCaksdY/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/KLGSLCaksdY/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/KLGSLCaksdY/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "Tasty",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"j6xRRd8dTPVVptg711_CSPADRfg/Fe41OtBUjCV35t68y-E21BCpmsw\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "_eOA-zawYEA"
   },
   "snippet": {
    "publishedAt": "2016-02-25T22:23:40.000Z",
    "channelId": "UCJFp8uSYCjXOMnkUyb3CQ3Q",
    "title": "Chicken Pot Pie (As Made By Wolfgang Puck)",
    "description": "Read more! - http://bzfd.it/1XPgzLN Recipe! 2 pounds cooked boneless, skinless chicken, shredded Salt Freshly ground black pepper 4 tablespoons vegetable ...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/_eOA-zawYEA/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/_eOA-zawYEA/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/_eOA-zawYEA/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "Tasty",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"j6xRRd8dTPVVptg711_CSPADRfg/KDmoAcUWmeUj_VZXqc_egJ1Qhk4\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "F2SYDXV1W1w"
   },
   "snippet": {
    "publishedAt": "2017-03-24T22:00:03.000Z",
    "channelId": "UCJFp8uSYCjXOMnkUyb3CQ3Q",
    "title": "5-Cheese Mac &amp; Cheese as made by Lawrence Page",
    "description": "Here is what you'll need! FIVE-CHEESE MAC AND CHEESE as made by LAWRENCE PAGE Servings: 5 INGREDIENTS 1 box of elbow macaroni 1 12-ounce ...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/F2SYDXV1W1w/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/F2SYDXV1W1w/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/F2SYDXV1W1w/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "Tasty",
    "liveBroadcastContent": "none"
   }
  }
 ]
}
````

<h3>writing an API call script</h3>
<h4>Script planning</h4>
<ul>
	<li>Import all needed librarys</li>
	<li>Open the URL and read the API response</li>
	<li>Identify each data point in your JSON and print it to a spreadsheet</li>
</ul>


