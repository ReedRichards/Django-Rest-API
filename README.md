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

---
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

##### Example Request GET

```BASH
curl https://api.bvzzdesign.com/lonehen/about-page/1/
```

##### Example Response GET
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


##### Example Request PUT

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

##### Example Response PUT

TODO


---
---
### Email
```
/email/
```
remains for compatibility with other sites because I believe I use this api to send other emails from other domains.

sends email from rob@bvzzdesign.com to destination

##### Permissions
Any
###### Request type 
POST

##### Example Request POST
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
##### Example Response POST

TODO

---

### Checkout

```
/checkout/
```

create a charge to stripe

##### Permissions
Any
##### Request Type 
POST

##### Example Request POST
``` bash
curl
-d{
    "token":$token,
    "total":999,
}
-H "accept: application/json",
-H "Content-Type: application/json",
-X POST https://api.bvzzdesign.com/lonehen/checkout/
```

##### Example Response POST

TODO

---
---

### Press List

```
/press/
```

add or list press events


##### Permissions
Authenticated or Read Only
##### Request Type 
POST | GET

##### Example Request GET
``` bash
curl https://api.bvzzdesign.com/lonehen/press/
```

##### Example Response GET
```
[{"id":17,"press_image":"https://api.bvzzdesign.com/media/dda7d217-84f.jpg","press_descritption":"<p>
Lone Hen Winery is located in College Station and is owned by Steve and Vicki Kirkpatrick. Their firs
t vines of Blanc du Bois and Champanel were planted in 2004 on their ten acre lot where they live. Th
ey continued by planting Cabernet Sauvignon in 2006 and will be replanting with Lenoir soon. They cur
rently have 1.5 acres of vines and will have four acres of vineyard when completed. In 2009, Lone Hen
 Winery officially</p>","press_raw":{"object":"value","document":{"nodes":[{"nodes":[{"object":"text"
,"leaves":[{"object":"leaf","text":"Lone Hen Winery is located in College Station and is owned by Ste
ve and Vicki Kirkpatrick. Their first vines of Blanc du Bois and Champanel were planted in 2004 on th
eir ten acre lot where they live. They continued by planting Cabernet Sauvignon in 2006 and will be r
eplanting with Lenoir soon. They currently have 1.5 acres of vines and will have four acres of vineya
rd when completed. In 2009, Lone Hen Winery officially","marks":[]}]}],"isVoid":false,"data":{},"type
":"paragraph","object":"block"}],"object":"document","data":{}}},"owner":"bvzz"},{"id":40,"press_imag
e":"https://api.bvzzdesign.com/media/ea647651-9ee.jpg","press_descritption":"<p>NAVASOTA, Tex. (KBTX)
 - The Navasota Grimes County Chamber of Commerce is hosting its first Groovy Grapes Wine Walk in his
toric downtown Navasota on Saturday, April 15.</p><p></p><p></p><p>From 2 until 6 p.m., participants 
can enjoy a wide variety of Texas wines and snacks while touring local businesses</p>","press_raw":{"
object":"value","document":{"nodes":[{"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"NA
VASOTA, Tex. (KBTX) - The Navasota Grimes County Chamber of Commerce is hosting its first Groovy Grap
es Wine Walk in historic downtown Navasota on Saturday, April 15.","marks":[]}]}],"isVoid":false,"dat
a":{},"type":"paragraph","object":"block"},{"nodes":[{"object":"text","leaves":[{"object":"leaf","tex
t":"","marks":[]}]}],"isVoid":false,"data":{},"type":"paragraph","object":"block"},{"nodes":[{"object
":"text","leaves":[{"object":"leaf","text":"","marks":[]}]}],"isVoid":false,"data":{},"type":"paragra
ph","object":"block"},{"nodes":[{"object":"text","leaves":[{"object":"leaf","text":"From 2 until 6 p.
m., participants can enjoy a wide variety of Texas wines and snacks while touring local businesses","
marks":[]}]}],"isVoid":false,"data":{},"type":"paragraph","object":"block"}],"object":"document","dat
a":{}}},"owner":"bvzz"},{"id":41,"press_image":"https://api.bvzzdesign.com/media/8658c7ee-676.png","p
ress_descritption":"<p>Lone Hen Winery is located in College Station and is owned by Steve and Vicki 
Kirkpatrick. Their first vines of Blanc du Bois and Champanel were planted in 2004 on their ten acre 
lot where they live. They continued by planting Cabernet Sauvignon in 2006 and will be replanting wit
h Lenoir soon. They currently have 1.5 acres of vines and will have four acres of vineyard when compl
eted. In 2009, Lone Hen Winery officiall</p>","press_raw":{"object":"value","document":{"nodes":[{"no
des":[{"object":"text","leaves":[{"object":"leaf","text":"Lone Hen Winery is located in College Stati
on and is owned by Steve and Vicki Kirkpatrick. Their first vines of Blanc du Bois and Champanel were
 planted in 2004 on their ten acre lot where they live. They continued by planting Cabernet Sauvignon
 in 2006 and will be replanting with Lenoir soon. They currently have 1.5 acres of vines and will hav
e four acres of vineyard when completed. In 2009, Lone Hen Winery officiall","marks":[]}]}],"isVoid":
false,"data":{},"type":"paragraph","object":"block"}],"object":"document","data":{}}},"owner":"bvzz"}
]
```

##### Example Request POST
```
curl
-d{
    "press_image":base64(image.jpg),
    "press_descritption":"descritption of press",
    "press_raw":"raw text for rich text editor",
}
-H "accept: application/json",
-H "Content-Type: application/json",
-X POST https://api.bvzzdesign.com/lonehen/press/
```

##### Example Response POST

TODO

---
---

### Press Detail

```
/press/:id
```

get edit or delete existing press events


##### Permissions
Authenticated or Read Only
##### Request Type 
PUT | GET | DELETE

---
---

### Event
```
/event
```

get all events or add an event

##### Permissions
Authenticated or Read Only
##### Request Type 
GET POST

---
---

### Event Detail
```
/event/:id
```

edit or delete an event 

##### Permissions
Authenticated or Read Only
##### Request Type 
PUT DELETE

---
---
### blog
```
/blog/
```


get all blog posts or add an blog post

##### Permissions
Authenticated or Read Only
##### Request Type 
GET POST

---
---


### Blog Detail
```
/blog/:id
```

edit or delete a blog post

##### Permissions
Authenticated or Read Only
##### Request Type 
PUT DELETE

---
---
### Shop
```
/shop/
```


get all shop items or add a shop item

##### Permissions
Authenticated or Read Only
##### Request Type 
GET POST

---
---


###  Shop Detail
```
/shop/:id
```

edit or delete a shop item

##### Permissions
Authenticated or Read Only
##### Request Type 
PUT DELETE

---
---
 

### Makers Notes
```
/makersnotes/
```


get all makers notes items or add a makers notes item

##### Permissions
Authenticated or Read Only
##### Request Type 
GET POST

---
---


###  Makers notes  Detail
```
/makersnotes/:id
```

edit or delete a makersnotes item

##### Permissions
Authenticated or Read Only
##### Request Type 
PUT DELETE

---
---
 

 
 
