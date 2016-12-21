var j = document.createElement("script");
j.src = chrome.extension.getURL("lib/jquery.js");
//j.src = "https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"
(document.head || document.documentElement).appendChild(j);

var g = document.createElement("script");
g.src = chrome.extension.getURL("lib/gmail.js");
(document.head || document.documentElement).appendChild(g);

var s = document.createElement("script");
s.src = chrome.extension.getURL("main.js");
(document.head || document.documentElement).appendChild(s);

var imgUrl = chrome.extension.getURL("images/ic_extension_2x.png");
var i = document.createElement("input");
i.setAttribute("type", "hidden");
i.setAttribute("id", "--action-img-url");
i.setAttribute("value", imgUrl);
(document.body || document.documentElement).appendChild(i);