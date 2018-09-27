import codecs
import json

#http://beautifytools.com/excel-to-json-converter.php 
peopleDiv = [
        """col-md-4 col-sm-6 col-xs-6""",
        """col-md-4 col-sm-6 col-xs-6""",
        """col-md-4 col-sm-6 col-xs-6""",
        """col-md-6 col-md-push-1 col-sm-6 col-xs-6""",
        """col-md-6 col-md-pull-1 col-sm-12 col-xs-12"""
        """col-md-6 col-md-pull-1 col-sm-12 col-xs-12"""
        ]

leftDiv = """col-lg-5 col-lg-offset-1 col-sm-6 col-xs-12 item"""
rightDiv = """col-lg-5 col-sm-6 col-xs-12 item"""
prizeHtmlFront = """
                <div class="{div}"><img class="img-responsive" src="{img}" width="455px">
                    <h3 class="name"><img src="assets/img/trophy.svg" width="4.5%" id="trophy">{teamName}</h3>
                    <h6><strong>{prize}</strong> </h6>
                    <p class="description">{description}</p>
                    <div class="row" id="five-p">
                    </div>
                    """
htmlFront = """
                <div class="{div}"><img class="img-responsive" src="{img}" width="455px">
                <h3 class="name">{teamName}</h3>
                    <p class="description">{description}</p>
            """
personInfo = """
                        <div class="{div}">
                            <div class="author">
                                <h5 class="text-center name">{name}</h5>
                                <p class="text-center title">{school}, {userType}</p>
                            </div>
                        </div>
            """
htmlRear = """
                    <a class="btn btn-danger" role="button" href="{youtube}" id="webpage"><img src="assets/img/youtube.svg" width="21px" id="youtube"><strong>시연영상 </strong></a>
                    <a class="btn btn-danger" role="button" href="{github}" id="github"><img src="assets/img/gitlogo.svg" width="21px" id="gitlogo"> <strong>GitHub </strong></a>
                </div>
        """

firstColSchool = """
                <div class="col-lg-3 col-lg-offset-0 col-lg-push-0 col-md-3 col-md-offset-0 col-md-push-0 col-sm-4 col-sm-offset-0 col-sm-push-0 col-xs-10 col-xs-push-1 univ">
                    <img src="{img}" height="130px">
                    <h6 class="text-center name">{school}</h6></div>
                """
colSchool = """
                <div class="col-lg-3 col-md-3 col-sm-4 col-sm-push-0 col-xs-10 col-xs-push-1 univ">
                    <img src="{img}" height="130px"></a>
                    <h6 class="text-center name">{school}</h6></div>
                    """

teamDict = {}
data = json.load(codecs.open('data.txt', 'r', 'utf-8-sig'))

#gen team
for team in data["teamList"]:
    htmlf = ""
    htmlr = ""
    tdiv = ""
    descript = team["description"]
    if len(teamDict) %2 == 1:
        tdiv = rightDiv
    else:
        tdiv = leftDiv

    if "prize" in team:
        htmlf = prizeHtmlFront.format(img=team["img"], teamName=team["teamName"],
            prize=team["prize"], description=descript, div=tdiv)
    else:
        htmlf = htmlFront.format(img=team["img"], teamName=team["teamName"],
            description=descript, div=tdiv)

    htmlr = htmlRear.format(youtube=team["youtube"], github=team["github"])
    teamDict[team["teamName"]] = [[htmlf, htmlr], []]

for p in data["Peoples"]:
    pdiv = peopleDiv[len(teamDict[p["team"]][1])]
    phtml = personInfo.format(name=p["name"], school=p["school"],
                userType=p["type"], div=pdiv)
    teamDict[p["team"]][1].append(phtml)

for k in teamDict:
    v = teamDict[k]
    buf = ""
    buf += v[0][0]
    buf += "\n"
    for p in v[1]:
        buf += p
        buf += "\n"
    buf += v[0][1]
    buf += "\n"
#    print(buf)


#gen schoolImg
idx = 0
for sc in data["school"]:
    htmls = ""
    if idx % 4 == 0:
        htmls= firstColSchool.format(img=sc["img"], school=sc["name"])
    else:
        htmls= colSchool.format(img=sc["img"], school=sc["name"])
    print(htmls)

