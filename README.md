# REST API DOCS

This project is a work in progress and will constantly be growing. The name lonehen stems from the name of the orgin project but has now grown to be the base name for the api and therefore will be the name out of convenience. The "core" app is the app for lonehen winery and "lonehen" is the settings of the project. Although it is a bit confusing its a pain to change and a waste of time currently because I am the only one using this.  Maybe someday this will change. 
## Base Api Url
```
https://api.bvzzdesign.com
```
## LoneHen Docs
### Lonehen endpoint
```
/lonehen
```

### About Page
```
/about-page/1/
```

entries for the about page on lonehen.com

##### Permissions
Authenticated or Read Only 
Owner or Read Only
##### Request Type   
GET | PUT 

##### example request GET

```BASH
curl https://api.bvzzdesign.com/lonehen/about-page/1/
```

##### example response GET
```json
{"id":1,"about_title":"Located in College Station, Texas, Lone Hen Winery is a real
ly great winery with lots of awesome stuff going on. If you like wine, check this ou
t.","about_description":"<p>Steve and I sat on the upstairs porch, and thought, &quo
t;Wouldn&#x27;t it be great to grow grapes and run a winery?&quot; We had always had
 an organic garden and we thought - &quot;This will just be a bigger garden&quot;. T
hat was about 10 years ago. Our goal was and still is - to join the long tradition o
f farmers and gardeners who grow and eat locally produced foods. To that end, Lone H
en Winery creates sparkling wines made in a modified traditional method utilizing es
tate grown and Texas sourced grapes. We hope to have everything figured out in about
 3 to 4 generations, but we will certainly enjoy the process of learning! Come join 
us in our quest!</p>","about_raw":{"object":"value","document":{"nodes":[{"nodes":[{
"object":"text","leaves":[{"object":"leaf","text":"Steve and I sat on the upstairs p
orch, and thought, \"Wouldn't it be great to grow grapes and run a winery?\" We had 
always had an organic garden and we thought - \"This will just be a bigger garden\".
 That was about 10 years ago. Our goal was and still is - to join the long tradition
 of farmers and gardeners who grow and eat locally produced foods. To that end, Lone
 Hen Winery creates sparkling wines made in a modified traditional method utilizing 
estate grown and Texas sourced grapes. We hope to have everything figured out in abo
ut 3 to 4 generations, but we will certainly enjoy the process of learning! Come joi
n us in our quest!","marks":[]}]}],"isVoid":false,"data":{},"type":"paragraph","obje
ct":"block"}],"object":"document","data":{}}},"owner":"bvzz"}
```


##### example request PUT

```BASH
curl 
-d{
    "about_title": "title",
    "about_description": "description",
    "about_raw": "raw value"

}
-H "accept: application/json",
-H "Content-Type: application/json",
-H "Authorization: Token $Token"
-X PUT https://api.bvzzdesign.com/lonehen/about-page/ 
```

##### example response PUT
TODO


### Email
```
/email/
```
remains for compatibility with other sites because I believe I use this api to send other emails from other domains.

sends email from rob@bvzzdesign.com to destination

##### Permissions
Any

##### example request POST
```bash
curl 
-d{
    "from": "from",
    "message": "description",
    "to": "example@email.com"

}
-H "accept: application/json",
-H "Content-Type: application/json",
-X PUT https://api.bvzzdesign.com/lonehen/email/
```
##### example response POST
TODO

