var store = [{
        "title": "Trying Jekyll with GitHub Pages",
        "excerpt":"I just moved my main website to [GitHub pages][gh-pages]. GitHubpages is interesting, it uses the static page and blog generatorcalled [Jekyll][jekyll]. It supports Markdown and Textile formats bydefault. Now all my [site source][source] is hosted in the GitHub.My website never had any major content except the [ZCA book][zca]. Soit was...","categories": ["update"],
        "tags": [],
        "url": "http://localhost:4000/update/trying-jekyll-with-github-pages/",
        "teaser":null},{
        "title": "Go File Server",
        "excerpt":"Pro{% highlight go linenos %}package mainimport ( \"log\" \"net/http\" \"flag\" \"strconv\" \"os\")var port = flag.Int(\"port\", 9999, \"port number\")var dir = flag.String(\"dir\", \"\", \"directory to serve\")func main() { flag.Parse() wd, _ := os.Getwd() if *dir != \"\" { wd = *dir } fileinfo, fileerr := os.Stat(wd) if fileerr != nil {...","categories": ["golang"],
        "tags": [],
        "url": "http://localhost:4000/golang/go-file-server/",
        "teaser":null},{
        "title": "Parsing text files using Parsley",
        "excerpt":"I was looking for a parser library to convert a [wikisource text] intoother formats. The wikisource text contains Holy Bible translationinto Malayalam language known as \"Sathyavedapusthakam\".I found [Parsley] very interesting after watching the [PyCon talk] byits author. Parsley doesn't support Python 3 yet. Then, I used a[fork] to run my...","categories": ["python"],
        "tags": [],
        "url": "http://localhost:4000/python/parsing-text-files-using-parsley/",
        "teaser":null},{
        "title": "ഡിജിറ്റൽ സത്യവേദപുസ്തകം - ഭാഗം ൧",
        "excerpt":"ഏതാനും ചില ആഴ്ചകൾക്ക് മുമ്പ് വിക്കിഗ്രന്ഥശാലയിലുള്ള [സത്യവേദപുസ്തകത്തിന്റെ] അച്ചടിപ്പിഴവുകൾ തിരുത്തുന്നപ്രവൎത്തനത്തിൽ ഞാൻ ചേൎന്നു. അതിനെക്കുറിച്ച് ഇവിടെ എഴുതി തുടങ്ങുവാൻ ആഗ്രഹിക്കുന്നു. ഈ പ്രവൎത്തനംകുറച്ചുകൂടി വിപുലമാക്കുന്നതിന്റെ ഭാഗമായി \"[ഡിജിറ്റൽ സത്യവേദപുസ്തകം]\" എന്ന ഒരു വെബ്‌സൈറ്റുംഅതിനോടനുബന്ധിച്ച് ഒരു [ഗൂഗിൾ ഗ്രൂപ്പും] തുടങ്ങിവെച്ചു.[സത്യവേദപുസ്തകത്തിന്റെ]: https://ml.wikisource.org/wiki/ഉപയോക്താവ്:BaijuMuthukadan/പ്രവർത്തനങ്ങൾ[ഡിജിറ്റൽ സത്യവേദപുസ്തകം]: http://sathyavedapusthakam.in/[ഗൂഗിൾ ഗ്രൂപ്പും]: https://groups.google.com/d/forum/sathyavedapusthakam### സത്യവേദപുസ്തകത്തിന്റെ 1923 -നു മുമ്പ് അച്ചടിച്ച പതിപ്പ്വിക്കിഗ്രന്ഥശാലയിലുള്ള സത്യവേദപുസ്തകത്തിന്റെ ആദ്യ പതിപ്പ് 1910 -ലാണ് അച്ചടിച്ചതെന്ന് കരുതുന്നു.ആയതിനാൽ ഇതിന്റെ പകൎപ്പവകാശം തീൎന്നിട്ടുണ്ടാകും എന്ന്...","categories": ["bible"],
        "tags": [],
        "url": "http://localhost:4000/bible/sathyavedapusthakam-part-1/",
        "teaser":null},{
        "title": "Windows Commands",
        "excerpt":"I had kept these notes in a private wiki page for sometime.I hope moving it here will be helpful for searching.### Deleting a Service`sc delete servicename`To get name of the service that need to be deleted:1. Run `services.msc`1. Right click and get the service name### Checking whether a port is...","categories": ["technology"],
        "tags": [],
        "url": "http://localhost:4000/technology/windows-commands/",
        "teaser":null},{
        "title": "Setting up OpenVPN on AWS",
        "excerpt":"I had kept these notes in a private wiki page for sometime.I hope moving it here will be helpful for searching.### Create and upload RSA public key for SSH accessBy deafult, most of the Amazon Linux machines are accessed through SSHusing a public key.### Create a VPC with public and...","categories": ["technology"],
        "tags": [],
        "url": "http://localhost:4000/technology/openvpn-on-aws/",
        "teaser":null},{
        "title": "Selenium Page Objects Pattern",
        "excerpt":"I have added a [new chapter on Page Objects] in my documenabouttationfor Selenium with Python. Code in this chapter works and is quiteself-descriptive, but a little description wouldn’t hurt. If anyoneinterested, please send pull request in [Github]. If you want anexample implementation, I have one as part of my project...","categories": ["testing"],
        "tags": [],
        "url": "http://localhost:4000/testing/selenium-page-objects/",
        "teaser":null},{
        "title": "Keynote Speech on Test Automation using Pytest",
        "excerpt":"I delivered a [Keynote speech] on \"Test Automation Using Pytest\" at\"Non-Conventional Software Test Automation\" conference. Theconference was organized by a testing community. I selected Pytest asmy topic and the talk was well received. This was not really a Pythoncommunity, but when I asked how many knows Python, around 40% raisedtheir...","categories": ["testing"],
        "tags": [],
        "url": "http://localhost:4000/testing/keynote-speech-on-test-automation-using-pytest/",
        "teaser":null},{
        "title": "An Introduction to Go Programming",
        "excerpt":"[Go], also commonly referred to as **golang**, is a statically typed,compiled, garbage-collected, concurrent general purpose programminglanguage. Go is considered as an object oriented programming languageand it uses [object composition] instead of class inheritance. Go wasinitially developed at Google by [Robert Griesemer], [Rob Pike], and[Ken Thompson]. Go was publicly released as...","categories": ["golang"],
        "tags": [],
        "url": "http://localhost:4000/golang/an-introduction-to-go-programming/",
        "teaser":null},{
        "title": "(Template)",
        "excerpt":"Write text here","categories": ["template","jekyll"],
        "tags": [],
        "url": "http://localhost:4000/template/jekyll/template/",
        "teaser":null},{
        "title": "Go and Ember.js talk at GopherConIndia 2015",
        "excerpt":"I was very much excited to present at the first GopherCon Indiaconference. My talk was on 20th February around 3pm.Sourcegraph team was coordinating and writing live blog and JuliaPoladsky has written a blogabout my talk.I have uploaded more photos in my Google+postThe video of the talk is available in YouTube:...","categories": ["golang","emberjs"],
        "tags": [],
        "url": "http://localhost:4000/golang/emberjs/gopherconindia-2015-talk/",
        "teaser":null},{
        "title": "Golang workshops",
        "excerpt":"Recently I conducted couple of Go workshops. The first workshop wason February 27th at [NIT Calicut](http://www.nitc.ac.in) as part of[FOSSMeet'16](http://fossmeet.in) program. The second one was lastSaturday (April 16th) at NUMA Bangalore organized by[Hasgeek](https://hasgeek.com) as part of[Rootconf'16](https://rootconf.in/2016).The workshop at NIT was a 4 hour workshop and particpants werecomputer science students from various...","categories": ["golang","talk"],
        "tags": [],
        "url": "http://localhost:4000/golang/talk/golang-workshops/",
        "teaser":null},{
        "title": "Golang workshops at Sahrdaya & Reboot Calicut",
        "excerpt":"Those who following me or [Twitter] or [Facebook] might be alreadyseen my updates about Golang workshops at [Sahrdaya] college ofengineering and [Reboot Calicut].[Twitter]: https://twitter.com/nogenerics[Facebook]: https://facebook.com/BaijuMuthukadan[Sahrdaya]: http://www.sahrdaya.ac.in[Reboot Calicut]: http://rebootcalicut.comMy third Golang workshop was organized by Sahrdaya college ofengineering as part of the faculty development program. Particantswere mostly computer science teachers from...","categories": ["golang","talk"],
        "tags": [],
        "url": "http://localhost:4000/golang/talk/golang-workshop-sahrdaya-rebootcalicut/",
        "teaser":null},{
        "title": "Total 7 Golang workshops in 2016!",
        "excerpt":"Last update about my Golang workshops was in June 2016. In the last 6months many things happened in my life. I changed my job, afterworking 9 years and 7 months at ZeOmega joined Red Hat. Our secondson born in last August. Became co-organizer of Bangalore Golang usergroup and started organizing...","categories": ["golang","talk"],
        "tags": [],
        "url": "http://localhost:4000/golang/talk/total-7-golang-workshops/",
        "teaser":null},{
        "title": "Golang workshops for data scientists and students",
        "excerpt":"Last Saturday I conducted one more Go workshop in Bangalore. Themeetup was organized by [Practical DataScience](https://www.meetup.com/Practical-Data-Science-Workshops-Bangalore/)meetup group. [Bargava](https://twitter.com/bargava) took initiativeto organize this workshop. The meetup was hosted at Red Hat Bangaloreoffice. Some of my colleagues,[Zeeshan](https://twitter.com/@zee_10000), [SurajD](https://twitter.com/surajd_) and [SurajN](https://twitter.com/red_suraj) volunteered for the meetup.{% twitter https://twitter.com/nogenerics/status/860836058757558272 %}I received lots of nice[feedback](https://www.meetup.com/Practical-Data-Science-Workshops-Bangalore/events/238824064)for the...","categories": ["golang","talk"],
        "tags": [],
        "url": "http://localhost:4000/golang/talk/golang-workshops-data-scientists-students/",
        "teaser":null},{
        "title": "Installing Guile 2.2 on Fedora 26 using Guix",
        "excerpt":"Few days before I upgraded to Fedora 26. Fedora has a package named`guile22` which gives 2.2 version of Guile. But I wanted to try Guix.I noticed that there is [Guix package][guix-copr] in Copr repository.Then I enabled that repository and installed Guix.{% raw %}```bash# dnf copr enable lantw44/guix# dnf install guix```{%...","categories": ["scheme","guile"],
        "tags": [],
        "url": "http://localhost:4000/scheme/guile/guile2.2-on-fedora26/",
        "teaser":null},{
        "title": "Golang workshops at ICEFOSS 2017, FISAT",
        "excerpt":"Today was my 10th Golang workshop. It was organized by FISAT studentsand staff as part of [ICEFOSS 2017 annualevent](http://archive.is/sB3yS). There were around 40 participantsfor my Go workshop. All of them were computer science students fromvarious engineering colleges.{% twitter https://twitter.com/nogenerics/status/916628503834980353 %}Now I am writing this from a hotel in Angamaly. I...","categories": ["golang","talk"],
        "tags": [],
        "url": "http://localhost:4000/golang/talk/golang-workshops-icefoss-fisat/",
        "teaser":null}]
