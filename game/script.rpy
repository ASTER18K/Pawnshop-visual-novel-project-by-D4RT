﻿##############################################################################
# 
#
# 2022-02-24
#
# 스토리 원본은 도저히 못 찾겠다.
# 찾는대로 작업 들어갈 예정이지만 찾을 수 있을지 미지수..
# 
# D4RT GAMES MEMBERS
# 이동현
# 이재겸
# 이현수
# 김성연
# 조현동
# 강우진
# 김찬엽
# 곽태양
# 이재준
#
#
##############################################################################


# last build is 2017-02-17

# 게임에서 사용할 캐릭터 정의
# 인물을 정의 할때 ???의 경우에는 정의 문자 뒤에 q를 붙입시다. 색 코드도 같이 맞춰두세요.
# w-우진 s-설아 sq-설아"???" m-미아 mq-미아"???"


define w = Character('우진', color="#8E8E8E")
define s = Character('설아', color="#FFA4F2")
define sq = Character('???', color="#FFA4F2")
define m = Character('미아', color="#c0d2e4")
define mq = Character('???', color="#c0d2e4")


#배경사진
image bg firework = "firework.jpg"
image bg room = "room.jpg"
image bg road1 = "road1.jpg"
image bg school = "class.jpg"
image bg jdp = "JDP.jpg"

#미아 사진
image m st = "17.png"
image m worry = "18.png"
image m het = "20.png"
image m angry = "m-angry.png"
image m angry2 = "m-stangry2.png"
image m convic = "m-convic.png"
image m happy = "m-happy.png"
image m happy2 = "m-happy2.png"
image m hmm = "m-hmm2.png"
image m serious = "m-serious.png"
image m stangry = "m-stangry.png"


# start
label start:

    "이 게임의 내용에서 나오는 인물과 장소는 모두 픽션입니다."
    "몇몇 장소는 실제 장소를 기반으로 한 곳도 있습니다."
    "아직 완벽하게 만들어지지 않은 테스트 빌드 입니다."

    scene bg firework

    "//화재가 일어나고 있다.//"

    "..."
    
    "....."
    
    "......."
    
    "........."
    
    w "엄마...아빠...누나..."
    
    w "누가... 구해주세요..."
    
    w "가족이 안에..."
    
    w "가족이......"
    
    sq "우진아..."
    
    sq "우진아...."
    
    sq "우진아!!!!"

    scene bg room
    
    "//우진이가 눈을 떠보니 방에 있다//"
    
    w "설아.. 누나???"
    
    s "우진아.. 너 또 울고있어"
    
    w "어....?"
    
    s "또 그 꿈이지? 또.. 그 꿈 때문에.."
    
    s "미안해... 내가... 미안해... 나만 살아서..."
    
    s "나 같은것만 멀쩡하게 살아 돌아와서..."
    
    "(내 앞에서 눈물을 흘리며 사과를 구하는 사람은.. 나의 친누나이다.)"
    
    "(나는 작년 겨울 크리스마스때 화재로 누나 빼고 모든것을 잃었다.)"
    
    "(그 일은 나에게 큰 트라우마를 심어주었다)"
    
    "(그날의 일은 나에게 잊을 수 없는 일이다... 부모님과... 행복했던 내 모든 것을 뺏어간 그 일을... 잊을 수 없다...)"
    
    "(잊으려고 노력하지만 부모님마저 기억속에서 지워져버릴까 두렵다.)"
    
    s "우진아... 울지마..."
    
    s "그때... 내가 아프지만 않았더라면..."
    
    "(지금 미안함을 호소하는 누나도 화재의 피해자다.)"
    
    "(화재 당일 새벽 누나는 몸이 아파 집에서 쉬고 있었다.)"
    
    "(내가 별자리 사진을 찍으러 갔을 시간에 화재가 시작되어서 내가 도착 할 떄쯤에는... 우리집은 이미 되돌릴수 없었다.)"
    
    "(나는 밖에서 불타는 우리집을 보고만 있었다...)"
    
    "(타오르는 불길속으로 소리를 질러 부모님과 누나를 불러보아도 아무 반응도 없었다.)"
    
    "(결국 누나는 소방관에서 구출되고 부모님은 구출되지 못하였다...)"
    
    "(누나는 항상 부모님을 구하지 못했다며 나에게 항상 미안하다고 한다.)"
    
    "(솔직히 누나 잘못은 없다.)"
    
    "(내가 사진만 찍으러 가지 않았다면 불이 크게 번지지도 않았을 것이다...)"
    
    "(아니면 내가 나가기전에 제대로 확인이라도 했다면...)"
    
    "(따스한 손길이 내 볼에 닿기전까지 나는 트라우마에 시달렸다.)"
    
    s "우진아... 울지마..."
    
    w "누나가 살아 돌아온 것만으로 다행이라고 생각해..."
    
    w "누나 잘못 아니야... 살아 돌아와서 고마워..."
    
    w "아침부터 우울하게되서 미안... 늦겠다 준비하자"
    
    s "응... 아침 준비해뒀으니까 어서 준비하자"
    
    "(나는 어떻게 해야할까... 역시 잊으려고 노력해야하나...)"
    
    "(화재로 인해 악몽을 자주 꾸게된다...)"
    
    w "누나 가게준비는 어떻게 됐어?"
    
    s "잘 되었어 오늘부터 열심히 해야지."
    
    w "감정 잘 할 수 있겠어?? 또 사고 치는건 아닐까..."
    
    s "흐음... 믿지 못하는 걸까?"
    
    w "그건 아닌데... 그냥 걱정되서."
    
    s "걱정은 고맙지만 누나가 다 알아서 잘할테니까 두고봐!"
    
    "(오늘은 부모님이 운영하던 전당포를 누나가 운영하기로 한 날이다.)"
    
    "(집안에서 대대로 내려오던 전당포는 화재 이후 누나가 부모님을 이어가 계속 운영을 하기로 했다.)"
    
    "(사실 누나의 고집으로 반 강제적으로 계속 운영을 하기로 했다.)"
    
    "(게다가 누나가 전당포를 계속하게 된 이유는 생계유지이기도 하고, 남은게 돈과 전당포 뿐 이었다.)"
    
    s "맞다! 오늘 아침부터 손님에게 전화가 왔었어!"
    
    s "???를 담보로 하신다고 했었어."
    
    s "사정이 많으신분 같아 말이 좀 길어지긴 했지만 오늘 4시에 방문하기로 했어."
    
    w "알았어 난 학교 때문에 늦어질수도 있으니까 감정은 누나에게 맡길게."
    
    s "나도 공부 많이 했다고!!"
    
    "(철없이 웃는 누나가 불안하기만 하다.)"
    
    w "무슨 일 있으면 연락하고. 나 다녀올게!"
    
    s "잘 다녀와!"
    
    #파트1 끝
    
    #파트2 시작

    scene bg road1
    
    "//등교길//"
    
    w "(그 일을 잊고 싶지만 기억이라는건 그런걸 쉽게 허락해주지 않는다.)"
    
    w "하아. 아침부터 피곤하네."
    
    "//찰칵 소리가난다.//"
    
    w "응?"

    show m st

    w "(셔터소리에 놀라 뒤를 돌아보자 셔터소리의 주인과 눈이 마주쳤다.)"
    
    w "(셔터소리의 주인은 짧은 파란 단발머리를 한 소녀였다.)"
    
    w "(나는 시선을 빼앗기고 말았다.)"
    
    w "(파란머리의 소녀는 신중한 표정으로 우리집을 촬영하고 있었다.)"
    
    w "저...기요??"

    show m het
    
    mq "아..."
    
    w "저기..."
    
    mq "아... 하- 하- 하- "
    
    w "저기 방금 사진 찍으신거죠...?"
    
    mq "아 하 하 그게 말이죠.."
    
    w "아침부터 남의 집 사진을 찍고 있는 이유를 여쭤봐도 될까요?"
    
    mq "아하...그게...죄송합니다!!!"

    hide m het
    
    "(죄송하다는 말과 함께 소녀는 도망을 가버렸다.)"
    
    w "...허?"
    
    "(당황스럽다. 아니 어이가 없달까...)"
    
    "(아침부터 남의 집을 촬영하는 소녀라니 아침부터 피곤한일이 들꺼 같은 예감이 들었다.)"

    scene bg school

    "//2-3 교실//"
    
    "(웅성거리는 교실 새학기는 새로운 친구들과의 만남과 새로운 환경의 떨림이 가득하다.)"
    
    "(나도 한때 그렇게 느낄때가 있었다. 하지만 다 부질 없는 것이다.)"
    
    "(어짜피 내년이 되면 모두 떨어지고 잊혀질것이다.)"
    
    "(잊혀지고.....)"
    
    "(잊혀진다...)"
    
    "(올해도 학교에서는 조용히 지내고 싶다.)"
    
    w "하아..."

    show m st
    
    mq "여어~ 즐거운 새학기 아침부터 한숨을 쉬고 있는 너는 이름이 뭐니?"
    
    "(갑자기 건네온 말에 나는 뒤를 돌아봤고 어디선가 본적이 있는 듯한 파란색 단발머리 소녀)"
    
    "(그리고 그녀의 목에 걸려있는 카메라와 목소리가 오늘 아침에 본 것 같았다.)"
    
    w "너는..."
    
    mq "아...?"
    
    "(눈을 마주치자 활기차게 말을 건네던 소녀는 당황했는지 말을 잇지 못했다.)"
    
    w "너 오늘 아침에..."
    
    mq "어... 그게 말입니다..."
    
    mq "저는 2학년 3반인데 반을 잘못들어왔네요 하 하..."
    
    w "여기 2학년 3반 맞습니다만..."
    
    w "우리 어디선가 본적이 있는거 같죠?"
    
    mq "그런가요 하하 제가 강한 인상이긴하죠 하 하 그럼 전 이만 수업준비하러 가보겠습니다..."
    
    mq "하 하..."
    
    w "오늘 아침에 오리집 사진찍던..."
    
    mq "그...럴리가요 저는 처음 뵙네요. 하 하"

    hide m st
    
    mq "그럼 실례했습니다"

    "(말이 끝나게 무섭게  소녀는 도망가기 시작했다)"
    
    w "어딜가 이 도촬범아!!"
    
    "(나도 모르게 소리를 질러 버렸고 약속한듯 반 아이들의 시선이 주목된다.)"

    show m angry
    
    mq "뭐? 도촬범? 누가보면 내가 너라도 찍은줄 알겠다!"
    
    mq "부탁이니깐 오해할만한 발언 좀 하지마!"
    
    w "그럼 우리집은 왜 찍은 건데?"
    
    mq "너네집...?"
    
    w "그래 우리집을 왜 찍었냐고 도.촬.범.아."
    
    mq "알겠어 미안해 미안하니깐 제발 도촬범이라고는 하지 말아줘..."
    
    w "하아... 너도 참 피곤한 사람이구나."
    
    mq "하...하..."
    
    "(주목받은 시선탓일까 시선을 회피하고 굳어버린듯한 이 소녀에게 물어보고 싶은것은 것은 많지만 그럴 분위기가 아니다.)"
    
    w "알겠으니깐 가서 앉아 종칠 시간 됐어"
    
    mq "진짜 미안해 나중에 다 하나부터 설명할게..."
    
    w "알았어 어서 너 자리로 돌아가줄래?"
    
    "(돌아가라는 말이 끝나기 무섭게 내 옆자리로 와서 앉는다.)"

    show m het
    
    w "내 옆에 앉으란 소리는 안했는데...?"
    
    mq "너는 분명 니자리로 돌아가라 했어"
    
    w "그랬지"
    
    mq "너 상황파악이 안되니??"
    
    w "설마..."
    
    mq "내가 너 옆자리야"
    
    "(이제 조용한 학교생활은 꿈도 못꾸는 건가...)"
    
    w "우리 지금 엄청난 주목을 받오 있는거 같은데..."
    
    mq "괜찮지 않아? 새학기인데 모두들한테 얼굴도 바로 익혀주고"
    
    "(긍정적이라고 해야 하나 바보 같다고 해야하나...)"
    
    mq "내 이름도 아직 소개를 안했구나 나는 미아라고해 너는?"
    
    w "서우진"
    
    m "기억했어 내 이름도 잊지 않아야 한다?"
    
    w "그건 무리일지도..."
    
    "(몸시 귀찮다. 잘못걸렸다... 잘못걸린게 틀림없다...)"
    
    "(이것도 혹시 악몽의 일종이 아닐까...)"
    
    "(아침에 우리집을 촬영하던 도촬범하고 같은 학교, 같은 반, 내 옆자리라니...)"
    
    "(이건 악몽이디... 악몽임에 틀림 없을거다.)"
    
    w "하아..."
    
    m "한숨은 그만...!"
    
    w "아..네..."
    
    "(빨리 집으로 돌아가고 싶다.)"

    hide bg school
    
    #파트 2 끝
    
    #파트 3 시작

    scene bg school
    
    "(수업의 끝을 알리는 종이 울려온다.)"
    
    w "하아.. 드이어 끝났구나"

    show m st
    
    m "한숨 쉬지 말라고 했지??"
    
    m "젊은 녀석이 왜이리 기운이 없어 새학기 처럼 좋은날이 어디있다고!"
    
    m "난 오늘 급한 약송이 있어서 먼저 가볼게 좀 이따 봐!"

    hide m st
    
    "(하아... 제멋대로인 성격 정말 멀리하고 싶어진다.)"
    
    w "잠만...? 내일보자는게 아니라 좀 있다가??"
    
    "(불안하다...)"
    
    w "아니겠지..."
    
    w "아닐거야..."
    
    w "(우리집을 촬영하던 소녀라... 뭔가 불안하다.)"
    
    w "설마..."
    
    w "(아니길 바라면서 달리기 시작했다.)"

    show bg jdp
    
    "//집//"
    
    w "누나!!!!"
    
    s "우진이 왔구나"
    
    w "누나 손님! 오기로한 손님 어디 계셔?!"
    
    s "아직 안 오셨는데..."

    w "아... 그래"

    s "우진아 괜찮아..? 너 오늘 이상해... 평소랑 다르다고 해야하나...?"

    s "혹시 오날 아침 일 때문에 그런거야...?"

    s "미안해 우진아..."

    "(누나는 금방이라도 울거 같은 표정으로 말을 한다.)"

    w "아니야... 그런거 아니고..."

    mq "저기요~ 저 오늘 방문하기로 한 사람인데..."

    "(띠링 하는 소리와 함께 문이 열리자 오늘 나를 괴롭혀왔던 목소리가 들려온다.)"

    w "하... 진짜네..."

    m "어 나보다 먼저 와 있었네 다시 안녕~"

    w "하아... 진짜 너였구나"

    m "오옷~ 예상 하고 있었다는건가!"
    
    m "생각보다 눈치 빠른 녀셕이군... 훗"

    s "우진이 친구니? 우진이에게도 이렇게 예쁜 친구가 있었구나"

    m "네! 오늘 반에서 우진이와 짝꿍이 된 미아라고 합니다! 처음뵙겠습니다!"

    s "붙임성이 좋은 아이구나"

    w "어... 악연인지 인연인지 그냥 반친구라고 하자..."

    w "그나저나 너가 여긴 왜 방문한거야"

    m "나? 돈이 급해서... 전당포에서 돈 좀 빌릴려고 했어..."

    w "그래?"

    w "혹시 아침에 우리집 사진을 찍은거 하고 상관이 있어??"

    m "그건... 그냥 사진으로 남기고 싶었어. 방법이 이것 밖에는 없는거 같아서..."

    w "사진으로 우리 전당포를 찍어서 뭘 남기겠다는 건데??"

    "(갑자기 미아의 분위기가 바뀌었다. 방금전까지 활발하던 미아는 어디가고 곧 울거 같은 표정을 한 미아로 바뀌었다. )"

    s "우진아! 너 친구한테 왜 이리 공격적인거야!"

    w "아니... 뭐..."

    w "잘못한거 같긴하네 미안해..."

    m "아니야... 그래서 이 카메라로 돈을 빌릴 수 있을까...?"

    "(미아가 꺼낸 카메라는 빨간로고가 붙은 상당히 고가의 카메라였다...)"

    w "그 카메라야??"

    m "응... 우리 아버지 카메라인데 이것밖에 돈 될만한게 없더라고..."

    m "그래서 이 카메라로 빌릴수 있을까 싶어서 전화 해본거였어"

    m "그때 전화 받으신건 언니분 맞으시죠??"

    s "어? 어... 내가 받았어..."

    w "근데 너 혼자 온거면 조금 곤란할거 같은데..."

    w "부모님이 동행하지 않으면 법적으로 거래가 불가능하거든..."

    m "부모님... 그게...."

    m "혼자서는 어떻게 할 수 없을까??"

    "(미아는 크게 놀란듯 하다.)"

    "(미아는 갑자기 울기 시작했다.)"

    w "법적으로 그런거라... 나한테 어찌한들..."

    m "그럴 수가..."

    "(내가 또 실수를 한거일까? 이젠 나도 모르겠다...)"

    m "너도 미성년자잖아..."

    w "난 전당포 관리인이 아니야"

    m "그래도 너라면 어떻게 안될까?? 제발 부탁이야... 이제 더 이상 갈곳도 없어..."

    m "부탁이야..."

    w "미안하지만 그건 힘들어"

    s "많이 급한건가 보구나"

    m "정말 힘들어요... 아버지 병원비가 정말 급해요..."

    s "우진아 잠깐만 와볼래?"

    "(곤란하다... 급한건 알겠지만 정말 짐덩어리 같다.)"

    "(굳이 내가 해결해줘야 할 문제도 아니고...)"

    s "우진아... 저 아이하고 오늘 만난 친구야??"

    w "이래저래 아침부터 피곤하게 만났지..."

    s "그래.. 일단 저 아이 이야기 좀 들어보는게 어떨까?"

    w "...."

    w "알겠어"

    "(솔직히 들어준다고 해도 어찌할 도리가 없다고 생각했다.)"

    s "미아라고 했지? 잠깐 괜찮으면 여기와서 앉아줄래?"

    m "네..."

    m "죄송합니다... 갑자기 울어버려서..."

    s "괜찮아... 아버지 병원비라니 어떤 상황인지 괜찮다면 자세히 이야기 해줄 수 있겠니?"

    m "네"

    m "저는 아버지와 둘이 살고 있어요. 어머니는 어릴때... 기억조차 없어요. 돌아가셨다고 들었어요"

    m "아버지는 소방관이세요. 예전에 화재를 진압하시다가..."

    m "쓰러지셨는데 그날 이후 몸 상태가 급격히 안좋아지셔서는... 지금 병원에 계세요..."

    m "아버지가 쓰러지고 나서는 연금으로 생계를 유지하면서 아버지 치료를 받고 계신데"

    m "이번에 또 쓰러져서 수술을 하게 됐는데, 수술비가 너무 큰 바람에..."

    m "돈이 필요하지만 어떻게 구할 방법이 없었어요... 그래서 여길 왔는데, 여기서도..."

    "(미아의 사정은 충분히 이해했다. 도와주고 싶지만... 법이라는 벽이 있어 도와주기 힘들다)"

    "(아니면 법이라는 이유로 도와주기 귀찮은거 일지도...)"

    "(미아의 이야기를 듣다보니 과거의 일이 떠오른다...)"

    "(불타는 집...)"

    s "우진아!"

    s "우진아!!!"

    s "우진아 괜찮아??"

    s "미아야 잠깐만 기다려봐"

    "(누나가 내 손을 잡고 전당포 안에 있는 방으로 끌고 갔다.)"

    s "우진아... 넌 미아를 믿을 수 있니?"





    

    



    
    
    
    
    
    
    
    
    
    
    
    
    

    return
