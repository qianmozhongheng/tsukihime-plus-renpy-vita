# 游戏的脚本可置于此文件中。
# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
$ forbid_saving = True
define a = Character(" 远野志贵",what_size=20,who_size=18,what_size_color="#006400",
what_font="tl/test.ttf")
define b = Character("我",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define c = Character("陌生少女",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define d = Character("路人a",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define e = Character("路人b",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define f = Character("路人c",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define g = Character("籁尾晶",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define h = Character("未知的声音",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define i = Character("远野秋叶",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define j = Character("熟悉的声音",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define k = Character("电视里的新闻播报声",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define l = Character("（伪）远野志贵",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define config.say_attribute_transition = dissolve(0.4)
define m = Character("陌生的少年",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define h1 = Character("秋叶",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define i1 = Character("琥珀",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define j1 = Character("叔父",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define k1= Character("爱尔奎特",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define l1= Character("罗亚",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define n1= Character("鹿",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define k1= Character("琥珀",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define k2= Character("翡翠",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define m1= Character("爱尔奎特·布伦史塔德",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define wy1= Character("弓冢五月",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")
define y1=Character("希耶尔",what_size=20,who_size=18,what_size_color="#620A0a",
what_font="tl/test.ttf")


define config.say_attribute_transition = dissolve(0.4)
############################################################################
#视频：
# 游戏在此开始。
label start:
    call screen start with  dissolve
label huanshi:
    show screen quick with  dissolve
    scene black with  dissolve
    "本闲话承接tsukihime本篇而成、"
    "请在完成tsukihime本篇的主要结局之后再来开启。"
    "那么，「幻视同盟」章节开始了哦！"
    stop music
    window hide
    show  genshi with  dissolve
    pause
    hide   genshi with  dissolve
    play  music "music/tmcd-0101_09.ogg"
    show  ima_14

    play  sound "audio/se03.ogg"
    "咻”的一声，志贵的刀刃"
    "掠过了他的右手。"
    "结束了。"
    play sound "audio/se04.ogg"
    "之后惨兮兮地，他直直倒向了地面。"
    scene black with  dissolve
    show  bg_61
    "学长如释重负般地深吸了一口气。"
    m " 「啊——」"
    "他——该说是、杀人犯，倒在地面动也不动。"
    "但感觉并没有死去，只是昏过去了而已。"
    "因为速度太快没有看清楚，但在切到手腕的那一刻，学长似乎用了什么招式使对方失去了知觉。"
    "我瞪瞪地看着，这犹如漫画般的一幕。"
    b  "「…………咦？」"
    "可…有些古怪呀。"
    "倒地杀人犯的手腕上既没有伤口，也不见有血迹渗出。"
    "不知为何，他一直昏睡着。"
    show shiki_03 at left
    with  dissolve
    m "「………？」"
    "不觉再次吃了一惊。"
    m "「小…晶？」"
    hide shiki_03
    with  dissolve
    "收起小刀，志贵学长把手伸向了瘫坐在地上的我，"
    b "「啊…哎、真、真是对不起！」"
    "我慌慌张张地握住学长的手、站了起来。"
    "还没有从刚刚的冲击里缓过神、哆哆嗦嗦地站也站不直，只能紧紧的抱着他的手臂。"
    "唔唔，真是丢死人了"
    b "「唔……啊，唔……」"
    "话也说不出来，只能不停晃动着脑袋，"
    "想说没有关系，又不想看躺在地上的家伙的脸。"
    "连是不是因为第一次被男生抱着也搞不清，"
    "整个人一片晕头转向，像在跳桑巴。"
    show shiki_04 at left
    with  dissolve
    m "「这样，还是出去一下吧。」"
    hide shiki_04
    with  dissolve
    play sound "audio/se07.ogg"
    "好像察觉到我有些不适，学长牵着我的手走离开了那里。 "
    scene bg_01c with blinds
    "直到把我领至学门、他转身准备离开，"
    show shiki_04 at left with  dissolve
    m "「吃了大苦头呢」"
    "什么嘛，那种若无其事的微笑。"
    hide shiki_04
    with  dissolve
    b "「啊——」"
    "一下子恶寒消失了，泪水在眼眶里直打转。"
    "这全是学长的错，都不做点表示，还悠哉悠哉的。"
    "算什么嘛，那种轻飘飘的一句话。"
    "都发生了那种事情却一言不发。"
    "至今为止的事情像是骗人似的，"
    "虽然觉得很蠢，但人却仍颤抖个不停。"

    "一如既往，之后我们一起去了餐厅，"
    "和第一次吃的草莓派比，这次的就逊色了些，不过没有办法呀。"
    "不过这也是没有办法的事呀。"
    "……唔，记得约莫三天前，"
    "我、籁尾晶，和一个陌生男人搭上了话，"
    "由此契机结识了远野志贵学长。"
    window hide
    stop  music
    scene black
    pause
    show  genshi
    with  dissolve
    pause
    show  one_a
    with  dissolve
    pause
    scene bg_60
    with  dissolve
    play music "audio/se08.ogg"
    "时至十二月末，街道上的氛围开始悄然改变。"
    "虽然繁华依旧，但浮华喧嚣的光景由于蒙上了一层阴影而变得杂乱。"
    "特别是过了二十五日之后，寂寥感久久徘徊在人流如潮的街道上。 "
    "还真是个矛盾异常的季节。"
    "圣诞结束后，再过几天就是除夕了。"
    "在这两个节日的夹缝中的这五天时间，让人觉得懒散而松弛。"
    b "「―-―-―-―」"
    b "「既然没有什么要做的事情，就到街道上去逛逛吧。」"
    "想稍稍独处一下，于是便从住所出发，晃到一站之遥的街区。"
    window hide
    scene black
    show  ima_06
    with  dissolve
    "―――这数日里发生了一些事。"
    "原本我的眼睛就和普通人不同，一个月前我又看到了奇怪的东西。"
    "无法判别关于谁的、离谱而诡异的景象。"
    "自己单手拿刀，若无其事地切割着、似乎是人类的尸体。"
    "……无法理解这个景象，"
    "只是自此之后、我变得不会笑了，"
    "或许还是能挤出一丝来迎合周围的人，"
    "但发自内心的笑容已无法再浮现。"
    b  "「………………真是的。」"
    b "「都应该已经习惯了那种奇怪的东西了才对啊」"
    "冥冥之中的改变悄然发生。"
    "仅仅几天后，我的世界已变得翻天覆地，只能说是很戏剧性吧。"
    b  "「确实,远野家的老宅好像有着不好的传闻」"
    "漫无目的，我边走边嘟囔着。"
    "心不在焉地逛着逛着、想要抑制着内心的亢奋。"
    hide ima_06
    show bg_60
    with  dissolve
    pause
    window hide
    show seo_01 at right
    with  dissolve
    c "「杀人什么的可不行啊！」"
    hide seo_01 with  dissolve
    b "「――――嗯。」"
    "从后面传来了不安的叫声"
    b "「怎么回事？」"
    "包括我在内，很多人都转过头去，"
    "一个中学生模样的少女站在那里、肩膀瑟瑟发抖着。"
    show seo_01 at right
    with  dissolve
    c  "「那个、虽然没有人知道！」"
    c  "「但大家都感到无所谓吗？」"
    c  "「那样可怕的事情！？」"
    hide seo_01 with  dissolve
    "少女的话好像在斥责所有的行人般。"
    d"「喂，你在说什么东西啊」"
    e "「什么？是你认识的人么？」"
    f "「年终的时候人很容易发神经的吧」"
    "停下脚步的人们冷眼看着少女，立刻又匆匆离开。"
    show seo_01 at right with  dissolve
    c  "「喂喂…等、等一下啊！这样真的不行的啊！」"
    hide seo_01 with  fade
    "少女依然站在人潮中，拼了命地大声喊叫。"
    "毫不在意周围投来的异样目光，"
    "她重复着这种怪异的行为。"
    b "「…………………」"
    "一定有什么缘由吧。"
    "整理了一下思绪，我走向了那个少女。"

    scene black
    window hide
    play music "audio/se08.ogg"
    hide black
    show bg_27a  with blinds

    "终于在远离人群的地方和她搭上了话。"
    show seo_01 at right with dissolve
    c "「那个…………」"
    hide seo_01 with  dissolve
    "少女不安地转着眼珠盯着我。"
    "黑色短发、乍一看像一个男孩子。"
    "朴实得体的着装，脖子上紧紧缠着围巾。"
    "可能是茶褐色围巾的缘故，感觉像只小狐狸"
    "――――还是，修正一下。"
    "少女应该有在意周围投来的怪异目光。"
    "因为她的脸已经羞得成了一个红富士，身子紧张地直打哆嗦，"
    "战战兢兢地的视线流露出了内向的性格，"
    "小巧的身体像个小动物。"
    "话说，还真看不出有在大街上大喊大叫的胆量。"
    show seo_02 at right with dissolve
    c "「那个…………」"
    "少女又重新嘀咕了一遍。"
    c "「你是，就要杀人的人吗？」"
    hide seo_02 with  dissolve
    "这话可是非同小可啊，"

    scene black
    window hide
    play music "audio/se23.ogg"
    hide black
    show bg_59  with blinds
    "自不用说，钓起了我的兴趣。"
    "总知换个地方，听听这曲折的故事好了"
    show seo_01 at right with dissolve
    "「……那个，我们学校是禁止来这里的呐」"
    hide seo_01 with  dissolve
    " 少女一边拘谨地说着，一边东张西望着。"
    "怎么说呢，真是和小狐狸一模一样。"
    b "「有监护人一起嘛，不要在意不要在意」"
    b "「来吧!」"
    b "「你不要站着了，快坐下来吧!」"
    "客套一番后，少女坐了下来。"
    b "「这里的草莓派可是好东西啊，但是男生一个人来点不是有些浪费了?」"
    b "「所以一直想着能够和女孩子一起来。」"
    "我叽里呱啦地对着沉默不语的少女说着。"
    "并不期待她的回应，只是想说所以说了。"
    b "「我来结账，所以想吃什么就点好了」"
    b "「倒是这种年纪了还不让进咖啡屋，到底是什么学校啊!」"
    show seo_02 at right with dissolve
    c "「--------」"
    hide seo_02 with  dissolve
    "她趴在那边，不安地望着我"
    "……真是没有办法，"
    "这种状况什么都问不出来嘛。"
    b "「这样吧，和我点一样的怎么样？」"
    b "「正好我也是红茶党的,没什么大关系吧。」"
    "向着姗姗来迟的服务生要了个特大草莓派两杯柠檬红茶、"
    "还有一进店就相中的木莓奶油蛋糕和特制芝士蛋糕。"
    show seo_02 at right with dissolve
    c "「--------」"
    c "「嗯」"
    hide seo_02 with  dissolve
    "少女用菜单遮着脸，不好意思地望着我。"
    "渴求地眨巴着眼睛。"
    "原来如此。不是自满，"
    "我很能读出对方无言的要求。"
    b "「啊啊、等一下，芝士蛋糕两只」"
    "服务生记录下之后退了出去。"
    b "「怎么，喜欢芝士蛋糕吗？」"
    show seo_02 at right with dissolve
    c "「嗯，我喜欢木莓」"
    c "「--------」"
    hide seo_02 with  dissolve
    "少女直接了当地说道。"
    "――――接着。"
    "重振下颓势，开始进入正题。"
    show seo_01 at right with dissolve
    c "「那么，来说一说刚刚到底怎么回事吧，」"
    c "「我觉得你不是那种会去恶作剧的性格」"
    hide seo_01 with  dissolve
    b "「――――是的。@我不擅长开玩笑」"
    show seo_01 at right with dissolve
    c "「确实」"
    c "「刚刚那种笑话可不好笑呢？」"
    hide seo_01 with  dissolve
    b "「那个,不觉得可笑吗？」"
    show seo_01 at right with dissolve
    c "「啊」"
    c "「虽然不是什么很好的话题」"
    c "「但首先你的眼神很坚定。」"
    c "「尽管不知道有什么理由，」"
    c "「但你是认真的对吧。」"
    c "「刚刚嘲笑你的那些家伙都没好好思考过，」"
    c "「他们所说所讲的才是低劣玩笑。」"
    hide seo_01 with  dissolve
    b "「………………」"
    "少女直勾勾地望着这边，"
    "好像在判断我是不是值得信任...."
    window hide
    "短暂的沉默，"
    "草莓派终于端了上来，我们便开始分头朵颐。"
    "松脆的糕底，纯润而不粘牙的草莓馅。"
    " 嗯，真不愧是珍品啊。"
    hide seo_01 with  dissolve
    c "「――――那个」"
    show seo_01 at right with dissolve
    b "「怎么了？」"
    "我停下刀叉，注视着她。"
    show seo_02 at right with  dissolve
    c "「其实呢，我」"
    hide seo_02 at right with dissolve
    b "「啊啊，我知道哦。你想说你能看见未来对吧？」"
    show seo_01 at right with dissolve
    c "「―――――诶？」"
    hide seo_01 with  dissolve
    "她吃惊的张大了嘴巴。"
    "……嘛，只想着会不会是这样，就说出来了而已，"
    "好像这次猜对了呢。"

    show fake_01 at left with  dissolve
    b "「那怎么称呼你才好呢？」"
    b "「还没有告诉我你的名字呢。」"
    b "「我叫远野志贵。」"
    hide fake_01 at left with  dissolve

    show seo_02 at right with dissolve
    c "「啊」"
    c "「是」"
    g "「我叫籁尾晶。」"
    hide seo_02  with  dissolve

    "少女——籁尾晶,红着脸回答了我，"
    "说中了之后好像相当有效果嘛。"
    window hide
    stop  music
    play music "audio/se23.ogg"
    scene black
    pause
    stop music
    show  one_b with  dissolve
    pause
    show  bg_59 with  dissolve
    play music "audio/se24.ogg"
    pause

    show  fake_01 at right with  dissolve
    a "「――――你，想说自己能看见未来吗？」"
    hide fake_01 with  dissolve

    "初次相遇的男子，理所当然般地说出了这样的话。"

    show seo_02 at right with dissolve
    b "「那，那个——为什么……？」"
    hide seo_02  with  dissolve

    "胆怯地将目光投向他。"
    "对方的脸上露出了亲切的笑容。"
    show  fake_01 at right with  dissolve
    a "「感觉的吧，或许已经习惯那一套东西了吧」"
    hide fake_01 with  dissolve
    "真是好温柔的语气"
    "这样说虽然不太好，但志贵先生给人的第一印象像是"
    "毛茸茸的小狗。"
    window hide
    show  fake_01 at right with  dissolve
    a "「―――那套东西是…？」"
    hide fake_01 with  dissolve
    show seo_02 at right with dissolve
    b "「是啊」"
    b "「不过被“你是之后要杀人的人吗？」"
    b "「这样说还是头一次啊。」"
    b "「真是吓了我一跳。」"
    hide seo_02  with  dissolve
    "他噗哧一下笑了出来"
    "或许是带着黑边眼镜的缘故"
    "笑起来像个孩子，这让我少许平静了一些"

    show seo_02 at right with dissolve
    b "「啊——」"
    hide seo_02  with  dissolve
    "　因为之前冒昧的话、些许有丝惭愧。"
    "　眼前的这个人既不觉得是好奇来搭讪的"
    "也不像是为了找软妹。"
    show seo_02 at right with dissolve
    b "「那个……吓到你了吗？」"
    hide seo_02  with  dissolve
    "他嗯地哼了一下，没有恶意地点了点头"
    show seo_02 at right with dissolve
    b "「对、对不起。」"
    b "「明明素未谋面」"
    b "「却说远野先生那个------」"
    hide seo_02  with  dissolve
    "……嗯？"
    "刚刚，远野的发音，感觉好像有些耳熟"
    "是什么来着的"
    show  fake_01 at right with  dissolve
    a "「没有必要道歉啊。」"
    a "「只是，我想听听你是怎么得出这个结论来的。」"
    a "「……那个，叫你小晶可以吗？」"
    hide fake_01 with  dissolve
    show seo_02 at right with dissolve
    b "「-----------」"
    hide seo_02  with  dissolve
    "默许地点了点头。"
    "有一点高兴，又有点害羞"
    "被除了父亲以外的男人这样叫，还是头一次。"

    show seo_02 at right with dissolve
    b "「那个，已经没时间了，我明了地说了吧。」"
    b "「可以的话请不要取笑我，也可以尽早说完。」"
    hide seo_02  with  dissolve

    show  fake_01 at right with  dissolve
    a "「嗯」"
    a "「简洁明了很好」"
    hide fake_01 with  dissolve

    show seo_03 at right with dissolve
    b "「-----那我就说了」"
    b "「如远野先生说的」"
    b "「我能看见人的未来，和在不久后将要发生的事件。」"
    b "「……那个…虽然这种事情只是偶尔才有……」"
    b "「就是伴随着剧烈的头晕目眩…」"
    b "「眼前一片模糊，影像陆续流入脑中」"
    b "「……不过那些流入的映像不能进行回忆，只是单单让我“知道”了事件」"
    hide seo_03  with  dissolve

    show  fake_02 at right with  dissolve
    a "「嗯?」"
    a "「也就说作为映像记录不下来」"
    a "「但作为情报却可以转化为记忆对吧」"
    a "「……我不是专家并不太了解」"
    a "「但未来与过去的区别，仅仅只在于尚未决定而已」"
    a "「即使将每份情报当做一部分组合起来」"
    a "「还是呈现不出画卷的整体面貌啊」"
    hide fake_02 with  dissolve
    "志贵先生叹了口气，抿了抿红茶"

    show seo_01 at right with dissolve
    b "「―――― 啊？」"
    hide seo_01  with  dissolve
    "怎、怎么搞的这个人，"
    "不像是普通的反应啊，也没当笑话听。"
    "这个太古怪了，这个人淡定的神情太古怪了。"
    show seo_01 at right with dissolve
    b "「那个，相信了我吗？」"
    hide seo_01  with  dissolve

    show  fake_01 at right with  dissolve
    a "「因为没有人会那样吹牛的吧。」"
    a "「说什么“我能看见未来”」"
    a "「吹这种牛的风险也太高了吧」"
    hide fake_01 with  dissolve
    "他淡淡地说道。"

    show seo_02 at right with dissolve
    b "「……是么，」"
    b "「确实，像远野先生说的一样」"
    b "「不会有人说那样蹩脚的谎话。」"
    hide seo_02  with  dissolve
    "他赞同地点了点了头。"
    "……怎么回事，"
    "在这个人的面前变得心生暗鬼了"
    "真是无聊至极的举动"
    show  fake_01 at right with  dissolve
    a "「那么？」"
    a "「小晶到现在为止碰上那样的事情会怎么处理呢？」"
    a "「那个未来视要比过去视方便多了吧」"
    a "「派到用场了吧？」"
    hide fake_01 with  dissolve
    "怪异的远野先生又用了奇怪的言辞。"
    show seo_02 at right with dissolve
    b "「那个——请问是怎么样呢？」"
    hide seo_02  with  dissolve
    show  fake_01 at right with  dissolve
    a "「我的意思呢，」"
    a "「比如，小晶看到了未来，」"
    a "「自己的朋友受伤了，于是就去帮助她之类的？」"
    hide fake_01 with  dissolve
    show seo_02 at right with dissolve
    b "「――――唉，」"
    b "「像这样的好事情确实发生过几次。」"
    b "「基本上都被对方说多管闲事了」"
    b "「但我预见的结局只要努力的话应该都可改变」"
    hide seo_02  with  dissolve
    "远野先生露出了一丝惊讶的表情"
    show  fake_02 at right with  dissolve
    a "「原来如此。」"
    hide fake_02 with  dissolve
    "他重重靠倒在了沙发上"
    #志贵模板#################################
    show  fake_01 at right with  dissolve
    a "「嗯。真是个好孩子，小晶啊。」"
    hide fake_01 with  dissolve
    #小晶##################################
    show seo_02 at right with dissolve
    b "「........」"
    b "「像这样的好事情确实发生过几次。」"
    b "「基本上都被对方说多管闲事了」"
    b "「但我预见的结局只要努力的话应该都可改变」"
    hide seo_02  with  dissolve
################################################
    "有点心跳加速的感觉。"
    "温柔无比的笑容再次浮现在他的脸上，真是、太........."
    window hide
    show  fake_01 at right with  dissolve
    a "「....这样来说」"
    a "「未来视这个东西虽然真的是很便利。」"
    a "「不过我觉得呢、通过未来视看到的未来是绝对没有办法改变的。」"
    a "「和装在箱子里的猫一样。」"
    a "「不最终确认它死了的话，那只猫是不会死的」"
    hide fake_01 with  dissolve
    show seo_03 at right with dissolve
    b "「........确实。」"
    b "「我最开始也是这么想的。」"
    b "「但有些地方不对。」"
    b "「如果说我看到的不是那个人的未来，」"
    b "「而只单单只是那个人的过去呢？我是这样想的。」"
    hide seo_03  with  dissolve
    show  fake_02 at right with  dissolve
    a "「――――？」"
    hide fake_02 with  dissolve
    "远野先生迷惑的把脑袋歪到一边，之后茅塞顿开似得点了点头。"
    show  fake_01 at right with  dissolve
    a "「哈哈。小晶很聪明啊，理科一定很好吧。」"
    hide fake_01 with  dissolve
    window hide
    show seo_02 at right with dissolve
    b "「没有那样的事，我连书都背不进。」"
    hide seo_02  with  dissolve
    #############################################
    show  fake_02 at right with  dissolve
    a "「是吗？」"
    a "「真是奇怪啊」"
    a "「也就说你那边大量使用到了（脑）容量咯。」"
    a "「人的背景——也就是经历啊记忆什么的」"
    a "「读取那种东西的人类，就是过去视」"
    a "「小晶这样的情况同样也是过去视，不过这种情况算是第二阶段了吧」"
    a "「就是计算读取到的过去，」"
    a "「然后如字面所说“预测”某人未来将要发生的事」"
    a "「不过和普通的未来视不同」"
    a "「小晶能通过自我的意志来改变未来。」"
    hide fake_02 with  dissolve
    ##############################
    show  fake_01 at right with  dissolve
    a "「……真是厉害啊」"
    a "「和我这样的废柴完全不同啊」"
    hide fake_01 with  dissolve
    ########################
    window hide
    show seo_02 at right with blinds
    b "「啊——嗯。」"
    b "「或许，我也是这样想的。」"
    hide seo_02  with  dissolve
    "不好，刚刚发现自己正痴痴地望着远野先生。"
    "……真是吓了一跳。"
    "自己也用了近一年才明白了这个，"
    "这个人却简简单单就说中了。"
    ###################################
    show  fake_01 at right with  dissolve
    a "「接着呢？」"
    a "「刚刚，大声说出那种的事情。」"
    a "「也不是什么都没有考虑到吧。」"
    hide fake_01 with  dissolve
    "远野先生叉起整块蛋糕送到嘴边。"
    show  fake_01 at right with  dissolve
    a "「小晶看到了走在自己前面的某人的未来。」"
    a "「而那个未来是反人道的，是无论如何都不能无视的。」"
    a "「但令人懊恼的是有那么多人，」"
    a "「小晶也没有办法判断刚刚的那个未来是谁的」"
    a "「没有办法只能厚着脸皮大声喊出来，」"
    a "「但冷漠的市民没有一个人愿意听一下。」"
    a "「这就是刚才事情的一个大致对吧？」"
    hide fake_01 with  dissolve
    ################################
    show seo_01 at right with dissolve
    b "「说是没有错，但是。」"
    b "「远野先生有听我说啊。」"
    hide seo_01  with  dissolve
    show  fake_02 at right with  dissolve
    a "「……嘛，我比较爱管闲事所以不能视而不见。」"
    a "「比起那个，我刚刚提到的，」"
    a "「被小晶看到未来的那个家伙，，」"
    a "「不管他是哪种，」"
    a "「都不会放着小晶你不管的。」"
    hide fake_02 with  dissolve
    "一改前面温馨的气氛，远野先生的脸上露出了可怕的表情。"
    #############################################
    show seo_01 at right with dissolve
    b "「那个........」"
    b "「不管哪种，哪种是什么意思……？」"
    hide seo_01  with  dissolve
    show  fake_02 at right with  dissolve
    a "「也就是有杀人经历的，和有没有杀人经历的啊。」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「.........」"
    hide seo_01  with  dissolve
    "心“咯噔”沉了下去。"
    "远野先生知道，"
    "我偶然间看到的某人未来，"
    "这种行为会导致怎样的后果。"
    ##############################
    show  fake_02 at right with  dissolve
    a "「是这样的吧？」"
    a "「你是这么说的。杀人是不行的。」"
    a "「没有做过的人不会觉得什么，」"
    a "「但如果是杀过人的家伙、就不可能把这话当耳边风的。」"
    a "「如果他行过凶了的话，就势必会跟着你过来。」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「.........!」"
    hide seo_01  with  dissolve
    "我匆忙环视了一下屋子"
    "……根本就不可能做出辨认"
    window hide
    show  fake_02 at right with  dissolve
    a "「是吧，反过来即使是还没有动手的家伙，也有点糟糕哦。」"
    a "「不可能马上忘记小晶刚刚的一番表演。」"
    a "「他大概会暂认为没有必要担心，」"
    a "「但是一旦犯下罪行之后就会想起你的话来，」"
    a "「急切地想要把你找出来，这种情况也是有可能的」"
    hide fake_02 with  dissolve
    "远野先生用冰凉的语气说道。"
    "一定在为我的轻率而感到为难了吧。"
    show seo_01 at right with dissolve
    b "「啊……我，我————」"
    hide seo_01  with  dissolve
    show  fake_02 at right with  dissolve
    a "「没有想到会这样吗？」"
    hide fake_02 with  dissolve
    "……唔唔。"
    "那种事情当然有想到啊。"
    "可是，"
    "看到了那么过份的事情，我……"
    show  fake_02 at right with  dissolve
    a "「……比起自己更加在意可能被杀死的别人吗」"
    a "「……真是的，」"
    a "「那个咱可做不到啊。」"
    hide fake_02 with  dissolve
    "没有说我，而是用了咱，他仰望着天花板。"
    #############
    show seo_01 at right with dissolve
    b "「远、远野先生，怎么.........」"
    hide seo_01  with  dissolve
    "一听到远野先生嘴巴里冒出的被杀死这个词，"
    "腰板就不由颤抖了起来。"
    "我真是个胆小鬼。"
    "在别人的未来里看到死亡，明明是很平常的事。"
    ###################
    show  fake_02 at right with  dissolve
    a "「没办法，」"
    hide fake_02 with  dissolve
    show  fake_01 at right with  dissolve
    a "「不嫌弃的话我来帮你好么？」"
    hide fake_01 with  dissolve
    #############################
    show seo_01 at right with dissolve
    b "「嗯……帮我，远野先生？」"
    hide seo_01  with  dissolve
    show  fake_02 at right with  dissolve
    a "「不要犯傻了啊。」"
    a "「人犯你打算一个人找吗，那个未来的杀人犯。」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「............」"
    hide seo_01  with  dissolve
    "…………好厉害。"
    "这个人，看起来很沉着，但是其实好可怕。"
    "和毛茸茸的狗崽大不一样。"
    "他摘掉眼镜的话一定会变成一头大灰狼的吧。"
    window hide
    show seo_01 at right with dissolve
    b "「那个…虽然这样说我很高兴，可是这是行不通的。」"
    b "「要找到连长相都不知道人，普通人是没有办法的。」"
    hide seo_01  with  dissolve
    show  fake_01 at right with  dissolve
    a "「―――所以啊，我不是普通人喔。」"
    a "「虽然没有小晶那样的眼睛，但是我的眼睛也很不一般啊。」"
    a "「而且能通过自己的意识控制，」"
    a "「对于找人是再理想不过了。」"
    hide fake_01 with  dissolve
    show seo_02 at right with dissolve
    b "「嗯？——骗人的吧，远野先生也是未来视？」"
    hide seo_02  with  dissolve
    show  fake_01 at right with  dissolve
    a "「那个啊。」"
    a "「我不是说了吗，」"
    a "「没有人会撒什么我能看见未来这样的谎话、对吧。」"
    a "「不过我可看不到小晶那样具体就是了。」"
    hide fake_01 with  dissolve
    "远野先生用手指咚地敲了一下眼镜的镜片。"
    show seo_01 at right with dissolve
    b "「............」"
    hide seo_01  with  dissolve
    "原来如此，怪不得能很快接受我所说的。"
    "拜托这个人的话，或许真的能找出那个“谁”"
    "我能看见的未来、大抵是一天之后的事情。"
    "本来已经放弃了希望，可是远野先生能伸出援手的话"
    "或许真的，能够改变那个未来。"
    show fake_01 at right with dissolve
    a "「决定了呐」"
    a "「这样的话我也有个请求，」"
    a "「叫我志贵怎么样呢？」"
    a "「难得自报姓名，」"
    a "「叫我远野先生好是见外啊。」"
    hide fake_01  with  dissolve
    show seo_03 at right with dissolve
    b "「啊、是。」"
    b "「志贵先生那么说的话。」"
    hide seo_03  with  dissolve
    "......啊"
    "“志贵”这个发音，瞬间解开了我最初的那个萦怀。"
    "がついた"
    show seo_01 at right with dissolve
    b "「那个————难道，志贵先生是远野前辈的哥哥吗？」"
    hide seo_01  with  dissolve
    show fake_01 at right with dissolve
    a "「诶------？」"
    hide fake_01  with  dissolve
    "他好像大吃了一惊，肩膀耷拉了下来。"
    show seo_01 at right with dissolve
    b "「远野前辈的话？-----等…等等」"
    hide seo_01  with  dissolve
    "志贵先生吃惊地看着我。"
    show fake_01 at right with dissolve
    a "「这么说你是浅上女子学院的------？？」"
    hide fake_01  with  dissolve
    show seo_03 at right with dissolve
    b "「是。」"
    b "「我是中学部二年级学生。」"
    b "「一直很受远野前辈的照顾。」"
    hide seo_03  with  dissolve
    show fake_01 at right with dissolve
    a "「不对呀，那个------秋叶不是高中部的吗？」"
    a "「小晶你是中学部的对吧。」"
    hide fake_01  with  dissolve
    show seo_03 at right with dissolve
    b "「确实是这样，不过我们学院的高中部和初中部是不分开的。」"
    b "「因为我和远野前辈都是学生会的干事，」"
    b "「所以开会的时候经常在一起。」"
    hide seo_03  with  dissolve
    b "「天啊」"
    "志贵学长用手捂住了脸。"
    "一段短暂的沉默后，"

    show fake_02 at right with dissolve
    a "「……我说，那个」"
    hide fake_02  with  dissolve
    show seo_01 at right with dissolve
    b "「唔、怎么了？」"
    hide  seo_01  with  dissolve
    show fake_01 at right with dissolve
    a "「拜托了、对秋叶那个家伙保密啊、」"
    a "「那个、」"
    a "「和你搭话的事情。」"
    a "「在大街上搭讪女生什么的，」"
    a "「万一被她知道了我真不知道该如何解释。」"
    hide fake_01  with  dissolve
    "志贵微笑地说着。"
    show seo_01 at right with dissolve
    b "「可以是可以啦，难道说志贵学长很怕秋叶前辈？」"
    hide  seo_01  with  dissolve
    "我脱口而出。"
    a "「嗯，嘛，那个，不能这么说的吧。」"
    "学长含糊其辞地回答了我。"
    show fake_01 at right with dissolve
    a "「比起那个，这里的奶油蛋糕不吃么？你喜欢木莓是吧～？」"
    hide fake_01  with  dissolve
    "怎么感觉像越後谷送小判给代官似的点个不停"
    scene black
    window hide
    hide black
    show bg_59  with dissolve
    pause
    show fake_01 at right with dissolve
    a "「我说，小晶看到的未来到底是什么样的啊？」"
    hide fake_01  with  dissolve
    show seo_01 at right with dissolve
    b "「嗯？....嗯，那个....唔咕（吞咽）」"
    hide  seo_01  with  dissolve
    show fake_01 at right with dissolve
    a "「啊啊，吃东西的时候不要说话。」"
    a "「不用在意我，小晶的吃相我很中意哦。」"
    hide fake_01  with  dissolve
    show seo_02 at right with dissolve
    b "「啊唔.....我....不要那样.....不要。」"
    hide  seo_02  with  dissolve
    show fake_01 at right with dissolve
    a "「嗯、是这样的啊。」"
    hide fake_01  with  dissolve
    "他竟然笑盈盈地说出那种的话。"
    "好为难、我该有什么样的反应呢。"
    "总之先用餐巾擦擦嘴，观察下他吧。"
    window hide
    show seo_01 at right with dissolve
    b "「……我看到的只是一些片段。」"
    b "「先是几个浑身是血的人，」"
    b "「最后登场的是一个拿着小刀、表情狰狞的人。」"
    b "「地点是在一个昏暗的地方，没有什么显著的特征。」"
    b "「只知道大家一个个地，在同一个地方被杀死。」"
    b "「大致就是这样的。」"
    hide  seo_01  with  dissolve
######################################################
    show fake_02 at right with dissolve
    a "「一个个吗？」"
    hide fake_02  with  dissolve
    show fake_01 at right with dissolve
    a "「那具体有几个人呢？」"
    hide fake_01  with  dissolve
###########################################
    show seo_01 at right with dissolve
    b "「……三个人。」"
    b "「第一个是和我差不多年纪的女孩子、」"
    b "「皮肤晒地黑黑的、脱色的头发、像这么长」"
    hide  seo_01  with  dissolve
    "志贵学长没多说，继续询问下一个。"
    show seo_01 at right with dissolve
    b "「第二个人，三十岁左右，比学长矮一个头。」"
    b "「微胖、蛮和善的样子。着装很特别、是黄色的工作服。」"
    hide  seo_01  with  dissolve
    show fake_02 at right with dissolve
    a "「啊，这个容易弄清。」"
    a "「这附近制服是黄色工作服的公司只有两家。」"
    hide fake_02  with  dissolve
    "他边答应着边继续询问第二个人的确切相貌"
    "像是更加明了的身体特征啦、给我的第一印象啦、"
    "直到最后怎么个浑身是血啦、诸如此类。"
    show fake_02 at right with dissolve
    a "「这样的话。」"
    a "「虽然线索少了点、但是可以试着寻找下。」"
    hide fake_02  with  dissolve
    show seo_01 at right with dissolve
    b "「咦……？」"
    b "「志贵学长要找寻第二个人吗？」"
    hide  seo_01  with  dissolve
    show fake_01 at right with dissolve
    a "「是啊、」"
    a "「比起没头没脑地搜查未知的杀人犯，」"
    a "「还是保护起将来的被害者比较现实。」"
    hide fake_01  with  dissolve
    show seo_01 at right with dissolve
    b "「话是这样没错、可是……」"
    hide  seo_01  with  dissolve
    show fake_01 at right with dissolve
    a "「好啦，接着告诉我第三个人的样子吧。」"
    a "「记忆还很清晰对吧。」"
    hide fake_01  with  dissolve
    window hide
    show seo_01 at right with dissolve
    b "「.......」"
    hide  seo_01  with  dissolve
    "虽然学长那么认为，但即使经过一段时间，"
    "我看到的，关于未来的记忆都会不模糊掉。"
    "因为，除去映像、"
    "单单作为词句的那部分记忆衰退的速度特别慢。"
    "原因不是很确切，但似乎和我对影像不太敏感的体质有关联。"
    "……总的说，自己对声音异常敏感。"
    "敏感到，如果是喜欢的声音、即使通过电话听筒的报纸推销员，"
    "也会让我心跳加速。这都是题外话了。"
    window hide
    show seo_01 at right with dissolve
    b "「那个，第三个女性的话、」"
    b "「那个人没有什么明显的特征，」"
    b "「就是头发长长的，那样」"
    hide  seo_01  with  dissolve
    show fake_02 at right with dissolve
    a "「……难办啊」"
    a "「。这样可就没办法查了」"
    hide fake_02  with  dissolve
    "志贵学长郁郁地沉思了起来。"
    show fake_02 at right with dissolve
    a "「这样烦恼也不是个办法。」"
    a "「那么那人是怎么被杀死的呢？」"
    hide fake_02  with  dissolve
    show seo_01 at right with dissolve
    b "「和之前的一样，」"
    b "「手脚什么的被刀具割了下来。」"
    b "「这次的这个女性是两只手。」"
    hide  seo_01  with  dissolve
    show fake_02 at right with dissolve
    a "「……唔嗯……第一个人浑身是血，」"
    a "「第二个人一只手一只脚，第三个人两只手。」"
    a "「要砍下人的手脚的话，一定是用锯子或者柴刀之类的。」"
    a "「……这…简直就是流窜杀人犯嘛。」"
    a "「躲在避人耳目的地方，那样慢慢地肢解尸体。」"
    hide fake_02  with  dissolve
    "志贵学长咕噜咕噜嘟囔着和温柔表情不相符的话语。"
#######################################################
    show fake_01 at right with dissolve
    a "「那最后出来的那个家伙呢？」"
    a "「就是拿着刀的那个，」"
    a "「那个人没有死吗？」"
    hide fake_01  with  dissolve
    "志贵学长咕噜咕噜嘟囔着和温柔表情不相符的话语。"
    show seo_02 at right with dissolve
    b "「―――嗯。」"
    b "「虽然只是拿着刀，但感觉十分恐怖。」"
    b "「就像是电影里出镜的杀人魔一样。」"
    hide  seo_02  with  dissolve
    show fake_02 at right with dissolve
    a "「……诶？」"
    a "「这到底是怎么回事。」"
    a "「他是副什么模样呢？」"
    hide fake_02  with  dissolve
    show seo_02 at right with dissolve
    b "「―――嗯。」"
    b "「虽然只是拿着刀，但感觉十分恐怖。」"
    b "「就像是电影里出镜的杀人魔一样。」"
    hide  seo_02  with  dissolve
    show seo_02 at right with dissolve
    b "「―――嗯。」"
    hide  seo_02  with  dissolve
    "瞟了学长一眼，我立刻低下头。"
    "……说不出口"
    "总觉的拿刀的那个人很像学长。"
    "只是那个人没有戴眼镜，"
    "而且比起志贵学长要年轻不少。"
    show seo_02 at right with dissolve
    b "「……记不太清了。只觉得，或许那个就是杀人犯吧。」"
    hide  seo_02  with  dissolve
    show fake_02 at right with dissolve
    a "「？」"
    a "「什么？事情结束后，杀人犯自己照镜子？」"
    hide fake_02  with  dissolve
    show seo_02 at right with dissolve
    b "「那个……我看不见那样日常的延展，」"
    b "「只能看见事件本身而已，但确实目睹了持刀男子的身影、」"
    b "「因为我不是当事人而是观察者啦。」"
    hide  seo_02  with  dissolve
    show fake_01 at right with dissolve
    a "「――这样啊。」"
    a "「这个…要早点说……嘛。」"
    a "「小晶记不清他的样子对吧？」"
    hide fake_01  with  dissolve
    "我点头示意。"
    "志贵学长舒了一口气。"
    show fake_02 at right with dissolve
    a "「这样的话只能一步步来了。」"
    a "「我现在在就去找第二个人。」"
    a "「小晶的话呢，最好不要轻举妄动。」"
    a "「不管怎么样，对手都是杀人犯。」"
    a "「很有可能那件事情后就一直尾随监视着你」"
    hide fake_02  with  dissolve
    show seo_01 at right with dissolve
    b "「!」"
    hide  seo_01  with  dissolve
    "我又不禁在店内张望了一下，"
    "……可这样根本就找不到什么可疑的家伙啊。"
    show fake_01 at right with dissolve
    a "「女孩子一个人出太危险。」"
    a "「外勤就交给我了。」"
    a "「小晶只要到家再回想一下今天看到的“未来”就可以？。」"
    hide fake_01  with  dissolve
    show seo_01 at right with dissolve
    b "「可是…要说危险，志贵学长不也一样么」"
    hide seo_01  with  dissolve
    show fake_01 at right with dissolve
    a "「不一样啊。」"
    a "「嘛，如果他真的尾行了过来，」"
    a "「把我错当成的你的朋友的话，就谈不上危险什么的了。」"
    a "「总之，我对自己的能力还是很有自信。你就不用担心了」"
    hide fake_01  with  dissolve
    "说完，学长站了起来。"
    window hide
    show fake_01 at right with dissolve
    a "「如果顺利的话，明天我联络你。」"
    a "「麻烦小晶把电话号码告诉我。，」"
    hide fake_01  with  dissolve
    show seo_01 at right with dissolve
    b "「———那个。其实我现在，正在旅行中」"
    hide seo_01  with  dissolve
    show fake_01 at right with dissolve
    a "「旅行？」"
    hide fake_01  with  dissolve
    "志贵学长很惊奇地瞪大了眼睛。"
    show seo_01 at right with dissolve
    b "「啊——那个，是这样子的。」"
    b "「虽然年末还有很期待的聚会，」"
    b "「但不凑巧今年学院宿舍在改建。」"
    b "「于是大家都只能各自回家了。」"
    b "「我的家离这里很远，」"
    b "「所以直到改建结束就只能一个人留在这里。。」"
    hide seo_01  with  dissolve
    show fake_01 at right with dissolve
    a "「一个人留在这里的话，住在朋友家里么？」"
    hide fake_01  with  dissolve
    show seo_01 at right with dissolve
    b "「不是，住在这里附加的一个旅馆里。」"
    b "「据说两个月前发生了大事故，所以住宿费惊人的便宜。」"
    b "「于是就计划住一周左右」"
    b "「于是大家都只能各自回家了。」"
    hide seo_01  with  dissolve
    show fake_01 at right with dissolve
    a "「——旅馆???———啊、那个旅馆啊!!!」"
    hide fake_01  with  dissolve
    "志贵学长脸色苍白地微微摇了摇头。"
    window hide
    show seo_03 at right with dissolve
    b "「我住在十一楼的二号房。」"
    b "「电话直接打到旅馆来就可以了。」"
    hide seo_03  with  dissolve
    show fake_01 at right with dissolve
    a "「我知道了。」"
    a "「如果有什么问题就打电话来找我。」"
    a "「帐已经结好了。小晶你不要急慢慢吃。」"
    hide fake_01  with  dissolve
    "……学长抽身走出了咖啡店。"
    show seo_01 at right with dissolve
    b "「……真是个奇怪的人啊」"
    hide seo_01  with  dissolve
    "我从窗口中目送着他慢慢离去。"
    stop music
    scene black with  dissolve
    show  bg_59 with blinds
    play sound "audio/se02.ogg"
    "突然的、那感觉又来了"
    show seo_01 at right with dissolve
    b "「啊——呼～」"
    hide seo_01  with  dissolve
    "糟糕了。"
    "一个月发生一次就是新记录了。"
    "尽然像这样一天里发生了两次，难道我又功力（异能）大进了。"
    window hide
    stop music
    stop sound
    scene black with  dissolve
    show  ima_14 with  dissolve
    play  sound "audio/se03.ogg"
    "漆黑的夜晚"
    "无人的建筑，一面巨大的墙壁"
    "这个是……学校的体育馆么"
    "那里，相对而立的两人。"
    "一个是志贵学长，另一个是持刀的少年。"
    "嘀咕了些什么后，两人不约而同地抽出利器迎向对方。"
    show  bg_59 with blinds
    play music "audio/se02.ogg"
    "―――接着，啊，是。"
    b "「志贵学长被刺…中了」"
    "自己也被自己的话吓了一跳。"
    "但没有错，刚刚看到的是“未来”"
    b "「志贵学长―――――――――！」"
    "我紧追着学长冲出了咖啡屋。"
    show  bg_60 with blinds
    play music "audio/se08.ogg"
    "可是已经看不到他的踪影了。"
    "不管怎么张望都寻不见学长披着外套的身影。"
    "一边想着该怎么办，一边无精打采的回到了饭店。"
    stop music
    show bg_19d with blinds
    play music "music/tmcd-0101_01.ogg"
    b "「――――咦？对啊！」"
    b "「往前辈家打个电话就好了啊！」"
    "回到旅馆的瞬间，我才想到这个理所当然的办法。"
    b "「那个，前辈家的电话号码是——」"
    "从联系册里找到了远野前辈的电话号码"
    "我们中学部的学生基本都有前辈家电话号码，"
    "但实际没有多少人会去打。"
    "　听说即使是高中部，"
    "会和前辈直接对话的也只有同寝室的羽居前辈和苍香前辈。"
    "没有人能辈一样既被大家信赖着像前辈一样既被大家信赖着，"
    "又同时被大家所敬畏着。"
    "“中学部的那些家伙真好，不用实际见面、"
    "只要舒坦地信赖她…”高中部的学姐们经常这么唠叨。"
    b "「呜―――――」"
    "这样想着想着，都有点害怕打电话了。"
    "但事关志贵学长的性命，可不是该退缩的时候。"
    "……对啊"
    "开学的时候，可以在大家的面前炫耀下，"
    "我认识了传说中远野学姐的哥哥。"
    play sound "audio/se09.ogg"
    h "「你好，这里是远野家。您是哪位？」"
    "咦??"
    "什么时候 无意识间拨通了电话"
    h "「啊，唔，咦——？」"
    "突然对面传来了声音。"
    h "「这里是远野家。请不要着急、镇定一下」"
    "　从电话里传来一种悠闲的声音。"
    b "「啊啊.......是,......我...我……镇定、镇定」"
    "做了下深呼吸。"
    b "「晚、晚上打搅您十分抱歉。」"
    b "「我、我叫籁尾晶」"
    b "「请问远野学姐在吗？」"
    h "「请稍等一下」"
    "礼貌地回应后"
    "只过了一会、"
    show aki_t09 at right with dissolve
    i "「电话已接手了。」"
    i "「我是远野」"
    hide aki_t09 with dissolve
    "从彼端传来了前辈"
    "熟悉而又陌生的声音"
    b "「啊，那个，前辈、晚上好！」"
    "……恨死了自己的紧张兮兮。"
    i "「……………………………………」"
    i "「………………………………………瀬尾？」"
    b "「啊、是！」"
    b "「是我、前辈！」"
    show aki_t09 at right with dissolve
    i "「这样啊。」"
    i "「你会打电话过来还真是有些意外」"
    hide aki_t09 with dissolve
    "前辈似乎很高兴地说着。"
    "……唔。"
    "用这种语调、之后一定会有什么阴谋。"
    "前辈有欺负弱小的不良癖好"
    "每次学生会开会、我都有受到款待。"
    "这个在高中部的学姐们看起来好像是一种疼爱"
    "但是每次前辈朝我一笑"
    "我整个人就背脊发凉。"
    window hide
    show aki_t09 at right with dissolve
    i "「那么有什么重要的事情吗？」"
    i "「恭贺新年的话还有些早呐」"
    hide aki_t09 with dissolve
    b "「咦、那个、不是那样的啦...那个、」"
    b "「那个………前辈、您家的志贵先生」"
    b "「回来了吗？」"
    play sound "audio/se12.ogg"
    "噼咔哩。"
    "怎么回事、话筒那头传出了、像要把话筒"
    "捏爆那样的声音。"
    show aki_t03a at right with dissolve
    i "「籁尾。」"
    i "「志贵学长什么的，到底是怎么回事.......」"
    hide aki_t03a with dissolve
    j "「我回来啦～～～」"
    "紧接着从里面传出了，疑似学长的声音。"
    b "「啊、志贵学长回来了吗！？」"
    b "「太好了、」"
    b "「赶上了！」"
    b "「前辈、让志贵学长听一下」"
    b "「行吗！？」"
    b "「有重要的事情」"
    b "「一定得告诉他！」"
    "出奇的顺利。"
    "前辈不知为何叹了口气、默默地把电话"
    "交给了学长。"
##############################################################################
    a "「啊，我是远野志贵，请问一下是哪位？…」"
    b "「..........」"
    "听到这个声音我就激动起来了。"
    "可能是因为通过电话、有些感觉不一样？"
    "或者是刚刚的见面都只是在梦中？"
    "总之，真的是----好棒、"
    "即使现在想起来也真是好美的声音。"
    "　比起影像我的体质对声音更加有感觉"
    "所以通过话筒传过来学长的声音、那个、保守地说"
    "至少也是时速１６０千米等级的高速直球。"
    window hide
    b "「啊，啊，啊，我是籁尾！」"
    a "「嗯？」"
    "不好…怎么气血翻腾起来了。"
    b "「那个，是这样的、漏说了一句话」"
    b "「请不要夜晚到处走动！」"
    b "「特别是体育馆周围」"
    b "「绝对不要去！」"
    b "「可以吗！」"
    a "「……嗯、可以可是可以啦。」"
    a "「那个体育馆周围说的是」"
    a "「我们学校......」"
    play sound "audio/se10.ogg"
    "啪。"
    b "「哈啊…哈啊…哈啊……紧张死我了」"
    "放下话筒、缓了口气。"
    "拖着两条腿翻倒在床上，又深深吸了一口气。"
    b "「……但…这就没事…了…吧……」"
    "志贵学长知道了的话、那样的未来就不会出现成真"
    "应该......."
    "但这次电话的事情该怎么办呢........会不会"
    "在年初的学生会里、被学姐穿小鞋什么的啊"
    "唔唔....."
    "年初好可怕啊……。"
##############################################################################
    stop music
    window hide
    scene black with  dissolve
    pause
    show  two with  dissolve
    pause
    hide two with  dissolve
    show bg_60 with  dissolve
    play  music "audio/se11.ogg"
    b "「-------哈啊」"
    "发现早报一角的一则报道，心情不禁阴郁了起来。"
    k "「“发现单身男性碎尸”」"
    k "「被害人中山皆人，在柱户物流任职……」"
    "柱户物流的话，听说是使用全身鲜亮的"
    "黄色制服。"
    "新闻里没有详细说明、但碎尸的话,也就是切碎手脚吧。"
    b "「…………麻烦啊」"
    "昨天和濑尾晶那个孩子分开后、我也想尽了办法"
    "但还是变成了这样。"
    b "「但是，竟然那么早就登报了……不知道小晶」"
    b "「看到了没有」"
    b "「读到了一定会很伤心吧」"
    b "「如果可以，真想亲口用温柔的话语告诉她」"
    b "「或许她会好受点。」"
    "............."
    b "「……第一个人还没有被发现么。」"
    b "「但第二个人死亡的早早确认」"
    "已经足够证明一切了吧。"
    play sound "audio/se14.ogg"
    "我将报纸丢入垃圾箱，径直迈向公共电话亭。"
    "拨通了饭店的电话，并转接到十一楼二号房。"
    b "「----啊、小晶？」"
    b "「我就在这里附近，」"
    b "「能出来一下吗？我想请你吃早饭」"
    window hide
    stop music
    scene black with  dissolve
    show bg_60 with  blinds
    play music "audio/se08.ogg"
    "濑尾晶很快就赶了过来。"
    "好像昨夜没有睡好，眼睛都有黑眼圈了。"
    show seo_03 at right with dissolve
    g "「早…早上好，志贵学长！」"
    hide seo_03 with dissolve
    "尽管这样她还是打起精神在向在我打招呼、稍稍"
    "欣慰了一点。"
    b "「来稍微走走吧。」"
    b "「邀你出来的是我、」"
    b "「所以等下请你吃好吃的吧」"
    show seo_03 at right with dissolve
    g "「啊--好，那就多谢款待了」"
    hide seo_03 with dissolve
    "大概昨天的蛋糕挺和胃口、她的眼神里"
    "充满了期待。"
    "那么，为了迎合这期待，今天来顿豪华的和食吧。"
    hide bg_60 with  dissolve
#####################################################
    scene black with  dissolve
    show bg_59 with  blinds
    play music "audio/se25.ogg"
    "吃完饭，我们又走进了昨天的那家咖啡屋。"
    "一坐到坐席上、小晶就说道："
    show seo_03 at right with dissolve
    g "「果然冬天就该吃火锅呢！」"
    hide seo_03 with dissolve
    "最早还讨厌来着的，后来不知不觉喜欢上了"
    "鮟鱇火锅。"
    b "「------」"
    "我要选个恰当的时机，一定要把早报上的新闻告诉她"
    "……但感觉突然来句，“你看见的未来成真了哦”----有点"
    "太残忍了。"
    "算了，现在先花些时间"
    "闲聊一下吧。"
    b "「小晶。稍稍听我说一下好吗？」"
    show seo_03 at right with dissolve
    g "「誒―――可以啊。」"
    g "「……我想说，那个。」"
    g "「志贵学长比我年长地多，所以」"
    g "「不用一句句来征求我」"
    hide seo_03 with dissolve
    b "「那样吗？」"
    b "「那我就说了啊、小晶对于自己的眼睛」"
    b "「怎么想的呢。」"
    b "「不觉得很碍事吗？」"
    "她呆然若失地望着我。"
    show seo_01 at right with dissolve
    g "「嗯，很多时候是会觉得很讨厌，但从来没认为它很碍事。」"
    g "「我呢，从小的时候」"
    g "「就接受了这个事实。」"
    g "「看到讨厌的东西当然会心情不好，」"
    g "「但对我来说，通过努力就可以改变让人厌恶的」"
    g "「未来啊」"
    g "「所以，一定要说的话，」"
    g "「感觉还是赚到了吧」"
    hide seo_01 with dissolve
    show  fake_02 at right with  dissolve
    b "「这样啊。」"
    b "「小晶把人的过去化作记忆来观察，」"
    b "「之后预测作为结果的未来。」"
    b "「说穿了，对小晶来说，那些过去只是计算未来的一个参数」"
    b "「为不可能将最近之外更遥远的过去作为映像」"
    b "「来进行捕捉。」"
    b "「……所以小晶你能不受过去的影响」"
    b "「而客观的观察未来」"
    hide fake_02 with  dissolve
    "这种是理想的。"
    "所谓的未来不过就是过去加现在再划个等号而已。"
    "换而言之，要了解他人的未来，就必须要熟知这个人的过去与现在。"
    "但要得出未来这个答案，自己的人生"
    "就需要有对等的深度。"
    "只是单单关注对方的过去和现在，"
    "会产生各种各样的不妥。"
    "比如看见的是被观察者的私人问题。"
    "比如观察人的人生观发生改变。"
    window hide
    show seo_02 at right with dissolve
    g "「志贵学长……？」"
    g "「你说的事不是太明白？」"
    hide seo_02 with dissolve
    show  fake_01 at right with  dissolve
    b "「嗯？」"
    b "「啊啊，没听懂么？」"
    b "「就是，试着思考下，」"
    b "「单纯过去视的情形。」"
    b "「小晶你可以便利地仅仅观察未来」"
    b "「但对于单纯的过去视那就麻烦了。」"
    b "「假设，小晶一直想」"
    b "「移居到外国。」"
    b "「但因为实际问题、」"
    b "「想要维持自己现在的环境而无法做到。」"
    b "「把持这样愿望的小晶，若是偶然.」"
    b "「……嘛，会和那个人的记忆交杂吧。」"
    b "「接着，过去视的拥有者就会产生模拟体验」"
    b "「一样的感觉，此后得出“什么嘛，并不是什么了不起的事情嘛”」"
    b "「这样的结论，坦然地移居国外」"
    hide fake_01 with  dissolve
    show seo_02 at right with dissolve
    g "「那个，家人、朋友什么的」"
    g "「全部都不管了么？」"
    hide seo_02 with dissolve
    show  fake_01 at right with  dissolve
    b "「嗯。」"
    b "「.一般我们都会这样蜗居在自己的环境里，」"
    b "「以便保护自己所处的环境。」"
    b "「　谁都想冒险。」"
    b "「而且同时」"
    b "「谁都可以做。」"
    b "「但只是不会去做，」"
    b "「所以没有做而已。」"
    b "「作出现在自我、这个环境的正是自己。、」"
    b "「自然而然」"
    b "「把对于自己来说这必然是非常适宜居住的环境」"
    b "「任谁都不想舍弃这样的环境，」"
    b "「转而去做困难重重的冒险对吧。」"
    hide fake_01 with  dissolve
    show  fake_01 at right with  dissolve
    b "「我们人类就是，把梦想、自由、浪漫等等的幻想作为目标，」"
    b "「在圆形的跑道上追逐之的生物。」"
    b "「你想、」"
    b "「就像脑袋前面挂着胡萝卜的马一样。」"
    b "「　但不知为何，有些人却越过障碍，」"
    b "「在这个轱辘般转个不停的圆形跑道里跳了出来」"
    b "「刚刚提到的过去视、和小晶你看到的杀人犯」"
    b "「都符合以上状况。」"
    b "「从群落里脱离出来的生物只有死亡一条路。」"
    b "「因为所有的生物都不可能单体繁殖对吧。」"
    b "「也并不是说」"
    b "「个体不能增加这样的问题。」"
    b "「本来―――增不增加就没什么意义。」"
    b "「可能从循环里脱出，再独自死去，」"
    b "「这样的生物才是美丽的」"
    hide fake_01 with  dissolve
    show seo_02 at right with dissolve
    g "「----------」"
    hide seo_02 with dissolve
    "小晶愣愣地没有做出反应。"
    "……话说得跑题了啊。"
    show  fake_01 at right with  dissolve
    b "「那个、说到杀人犯。」"
    b "「小晶还没有看过早报吧」"
    hide fake_01 with  dissolve
    show seo_02 at right with dissolve
    g "「嗯-----是、不好意思」"
    hide seo_02 with dissolve
    show  fake_01 at right with  dissolve
    b "「嗯。」"
    b "「报纸上登出了、昨天深夜发现了一具男性碎尸。」"
    b "「是小晶所说的以黄色工作服作为制服的公司的员工」"
    hide fake_01 with  dissolve
    show seo_01 at right with dissolve
    play sound "audio/se13.ogg"
    g "「!!!!!!!!!」"
    hide seo_01 with dissolve
    "“咔哒”一声桌子摇晃了一下，小晶噌地站了起来。"
    "她脸色通红，整个人颤颤抖动着"
    "似乎想说什么但没有说出口。"
    window hide
    show  fake_01 at right with  dissolve
    b "「....先坐下来。」"
    b "「因为并没有登头像照、所以还不能断定啦。」"
    b "「不谨慎地说，我觉得」"
    b "「因为并没有登头像照、所以还不能断定啦。」"
    b "「还是在观察下情况比较好，警察也不是傻子」"
    b "「犯人没有找到也就是说，」"
    b "「是“完全掩人耳目的事件”。」"
    b "「称的上是完美犯罪的案子」"
    hide fake_01 with  dissolve
    show  fake_01 at right with  dissolve
    b "「你呀、快坐下吧。」"
    b "「本来就不是小晶你的责任。」"
    b "「错的是那个杀人的家伙」"
    b "「你完全没有责任。」"
    b "「这点不要弄错了啊。」"
    b "「你听我说，知道但没有去阻止」"
    b "「如果这种都算犯罪的话」"
    b "「那在电视上看杀人事件新闻的大家不就都有罪了吗？」"
    hide fake_01 with  dissolve
    show seo_01 at right with dissolve
    g "「--------」"
    hide seo_01 with dissolve
    "小晶动也不动，沉默地站在那里。"
    "一会儿、又悄悄地坐回到位子上。"
    show  fake_01 at right with  dissolve
    b "「这就好。」"
    b "「如果你一直那样，我在想我还要不要」"
    b "「再来这家店」"
    hide fake_01 with  dissolve
    show seo_01 at right with dissolve
    g "「------可是」"
    g "「------学长刚刚」"
    g "「------说了很可怕的话呢」"
    hide seo_01 with dissolve
    show  fake_01 at right with  dissolve
    b "「嗯？」"
    b "「什么可怕的话？」"
    hide fake_01 with  dissolve
    show seo_01 at right with dissolve
    g "「------没什么」"
    g "「------学长说的是对的」"
    hide seo_01 with dissolve
    "小晶就那样低着头、喃喃自语的说着。"
    show seo_01 at right with dissolve
    g "「学长。」"
    g "「我看见的那个人为什么」"
    g "「要杀人呢」"
    hide seo_01 with dissolve
    show  fake_02 at right with  dissolve
    b "「不清楚。」"
    b "「我也不太能理解」"
    b "「要说的话、可能是性冲动什么的吧」"
    hide fake_02 with  dissolve
    show seo_02 at right with dissolve
    g "「―-性、性冲动、不会吧--」"
    hide seo_02 with dissolve
    "唰地一下、她脸红了起来。"
    "沮丧的心情还是遮掩不掉"
    "害羞的性格。"
    show  fake_02 at right with  dissolve
    b "「那只是可能吧！？」"
    b "「或许杀人犯」"
    b "「是为了帮助什么人、那个……不得已什么的……」"
    b "「情非得已的情况也是有可能的啊。」"
    b "「像那样」"
    b "「杀人不是出于本意………」"
    b "「是有可能性的吧。」"
    b "「理由可以有各式各样。」"
    b "「可是关系到生死的话，归根结底也就是性冲动。」"
    b "「人类之所以是人类。」"
    b "「就是因为会制造道具，」"
    b "「在别的方面的行为和动物无异。」"
    b "「对于动物来说」"
    b "「生死就是本能问题。」"
    b "「本来在杀与不杀的问题上」"
    b "「理性就起不了什么作用。」"
    b "「所有的人都是如此。」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    g "「-----------」"
    hide seo_01 with dissolve
    show  fake_01 at right with  dissolve
    b "「-----对不起。」"
    b "「有些说过了。」"
    b "「因为从前有这样相似的体验，」"
    b "「所以我对“死”比较淡漠。」"
    b "「但是小晶。」"
    b "「杀害他人的理由确实很可悲，但追根溯源，」"
    b "「想要改变现在这个自我的愿望才是起因。」"
    b "「比如、有一个恨之入骨的人。」"
    b "「只要他活着我就恨不能已」"
    b "「讨厌那样」"
    b "「觉得不快。」"
    b "「所以」"
    b "「为了让自己不再怨恨、而将他杀死。」"
    b "「看吧、这种场合的原因就是为了改变自己。」"
    hide fake_01 with  dissolve
    show seo_01 at right with dissolve
    g "「或许吧。」"
    g "「可那是借口。」"
    g "「-如果」"
    g "「要改变的话，」"
    g "「我觉得还是去寻找一个其他的方法比较好吧」"
    hide seo_01 with dissolve
    "我赞同地点了点头。"
    "小晶说的是理所当然的。"
    "只要一个人的自我改变手段没有走到死胡同"
    "自然就不会做出称得上是最终手段的“杀人”"
    show seo_02 at right with dissolve
    g "「……可是，果然，还是志贵学长说得对。」"
    g "「虽然不明白，但杀人者在杀人的那一时刻，」"
    g "「-打破了世界应有的姿态是吧。」"
    g "「要改变的话，」"
    g "「借用学长的话来说，是损害了大家」"
    g "「至今为止我努力打造的」"
    g "「“自我环境”」"
    hide seo_02 with dissolve
    "好高兴、终于让她释怀了。"
    "这个孩子真是聪明。"
    "如果是自己妹妹的话，一定会很溺爱她吧。"
    "这般妄想着"
    window hide
    stop music
###################################################################
    scene black with  dissolve
    show bg_60 with  blinds
    play music "audio/se08.ogg"
    "和昨天一样、我同濑尾晶辞别。"
    "她还是很害怕的样子、"
    "告诉我今天.不想踏出旅馆。"
    b "「接着」"
    b "「第三个人是没有特征的女性」"
    b "「这个」"
    b "「找起来是麻烦还是简单呢?」"
    "使劲挠了挠脑袋。"
    "只靠这点情报要找到实在很困难"
    "可是小晶也不可能一直蹲在旅馆里。"
    "要尽早回应她的期待才行。"
    window hide
    stop music
#########################################################################
    scene black with  dissolve
    show three with  blinds
    pause
    hide three with  blinds
    show ima_13b with dissolve
    play music "audio/se11.ogg"
    "“你听我说，知道但没有去阻止，如果这种都算犯罪的话!”"
    "“那在电视上看杀人事件新闻的大家，不就都有罪了吗”"
    "....听到这句话，我真觉得志贵学长真是个可怕的人。"
    "不、比起可怕，或许应该说是严厉吧。"
    "在新闻里听闻不认识的人被杀死，大部分人"
    "都会同情地说一句“好可怜啊”。"
    "可是"
    "隔天就忘得干干净净"
    "即使记住了如果仅仅付诸同情"
    "也只是过眼云烟而已"
    "什么都改变不了"
    "不管是过去还是未来，如果知晓了就该付诸行动，"
    "我觉得这个是志贵学长想要说的"
    "总之。"
    "看过新闻、单单注视着事件的我们"
    "知道却什么也不准备做"
    "一味呆在那里"
    "这种事情是没有"
    "任何意义的"
    window hide
    stop music
##############################################################
    scene black with  dissolve
    show bg_19b with  blinds
    "迷迷糊糊醒来，时针已经指向了正午。"
    show seo_01 at right with dissolve
    b "「..........」"
    hide seo_01 with dissolve
    "因为直到早上也没有能入眠、整个人还昏昏欲睡。"
    show seo_01 at right with dissolve
    b "「...还是看下报纸吧」"
    hide seo_01 with dissolve
    "揉了揉惺忪的睡眼，让服务员送来了报纸和早饭。"
    "把淡而无味的咖啡（志贵前辈以为我是红茶党，其实我是喜欢咖啡的啊）尝了口后、打开送来的报纸"
    play sound "audio/se14.ogg"
    show seo_01 at right with dissolve
    b "「..........!!!」"
    hide seo_01 with dissolve
    "果然，有第三人的报道。"
    "没有任何特色。"
    "就是某女性在自己家里"
    "被人杀害的内容。"
    "没有确证,不过，尽管如此―――可以确定一个事实"
    "她就是第三个被害者"
    window hide
    play sound "audio/se15.ogg"
    show seo_01 at right with dissolve
    b "「啊…电话响了」"
    hide seo_01 with dissolve
    "心不在焉地接起听筒。"
    play sound "audio/se09.ogg"
    "总台的人告之是远野学长的电话,并转接了过来。"
    show  fake_01 at right with  dissolve
    a "「啊啊——终于接通了。」"
    a "「早上好、小晶。」"
    a "「有些仓促、但你能出来下吗？」"
    hide fake_01 with  dissolve
    "和昨天一样，志贵学长提出了这样的要求。"
    stop music
##################################################
    scene black with  dissolve
    show bg_59 with  blinds
    play music "audio/se26.ogg"
    "到咖啡店的时候差不多已经下午四点了。"
    "学长像往常一样坐在那里，打完招呼后,我在他对面的沙发上坐了下来。"
    show  fake_02 at right with  dissolve
    a "「....你的脸色」"
    a "「应该看过那则新闻了吧」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「----是」"
    b "「志贵前辈果然也是那么想的吗？」"
    hide seo_01 with dissolve
    show  fake_02 at right with  dissolve
    a "「啊……不、该怎么说呢。」"
    a "「那样子看起来」"
    a "「简直就是另外一宗事件」"
    hide fake_02 with  dissolve
    "学长不悦地说着。"
    "到昨天为止还是很通达的学长，今天看起来显得很暴躁。"
    show seo_01 at right with dissolve
    b "「……学长生气了呐」"
    hide seo_01 with dissolve
    show  fake_02 at right with  dissolve
    a "「啊」"
    hide fake_02 with  dissolve
    "点了下头，他心情沉重地叹了口气。"
    show  fake_02 at right with  dissolve
    a "「真是的，报社那群人什么东西、那么小的一块消息。」"
    a "「一个人被杀了啊」"
    a "「只用了两行不到的说明。」"
    a "「被害者是谁？」"
    a "「怎么被杀的？」"
    a "「这样根本就无从得知」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「那个......」"
    b "「学长觉得它们之间没关联？」"
    hide seo_01 with dissolve
    show  fake_02 at right with  dissolve
    a "「嗯？」"
    a "「不、我不觉得那没有关联」"
    a "「小晶还不明白吧，......麻烦呐!」"
    a "「一定是」"
    a "「和昨天的杀人事件用了相同的手法」"
    a "「所以对消息进行了管制」"
    a "「这样的话不管怎么努力都无法搞到内情了」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「那个....学长」"
    b "「那接下来该怎么办呢？」"
    hide seo_01 with dissolve

    show  fake_02 at right with  dissolve
    a "「虽然被害者不会在出现了」"
    a "「可...........」"
    a "「这很有可能」"
    a "「小晶你是不是」"
    a "「很想抓住犯人吗？」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「嗯」"
    hide seo_01 with dissolve
    "我点了点头。"
    "并非出于正义感、只是不想让那个家伙逍遥法外"
    show  fake_02 at right with  dissolve
    a "「那样啊。.……可是很棘手啊」"
    a "「你想，小晶知道那个“拿小刀男子”外貌的情报」"
    a "「可我却不知道」"
    a "「就算你告诉我看到的情报」"
    a "「我也感受不到」"
    a "「我这边也算是黔驴技穷了」"
    hide fake_02 with  dissolve
    show seo_02 at right with dissolve
    b "「那个..........」"
    b "「................我想说」"
    b "「志贵学长，那个.........」"
    hide seo_02 with dissolve
    "说不出口、学长被拿刀少年刺中的这样的事情。"
    "原本应该是最有可能发生的未来"
    "会因为一些琐碎的事情而降低出现的几率吧"
    show  fake_01 at right with  dissolve
    a "「嗯？」"
    a "「想对我说什么？」"
    hide fake_01 with  dissolve
    show seo_02 at right with dissolve
    b "「那个..........」"
    b "「....我想到大街上去搜寻下」"
    b "「所以..........」"
    b "「.......觉得......觉得...和.....志贵前辈在一起胆子」"
    b "「.........会大一点.」"
    b "「那个..........」"
    b "「...虽然很任性的想法.......」"
    hide seo_02 with dissolve
    "原来如此、学长打了个响指。"
    show  fake_01 at right with  dissolve
    a "「就这么做好啦。」"
    a "「这样的话我又能帮上你的忙了」"
    hide fake_01 with  dissolve
    show seo_02 at right with dissolve
    b "「啊.......这么」"
    b "「....这么说的我是很高兴」"
    b "「但不可能找到的吧」"
    b "「满大街找人什么的」"
    b "「根本不可能成功的」"
    hide seo_02 with dissolve
    show  fake_01 at right with  dissolve
    a "「但也不能说一定没有希望啊」"
    a "「要知道积水成渊,铁杵成针」"
    a "「只要小晶你不放弃」"
    a "「事情就不会这么结束」"
    hide fake_01 with  dissolve
    "他愉快地说着，起身离开座位。"
    show  fake_01 at right with  dissolve
    a "「来、兵贵神速。」"
    a "「乘着街道上人流密集」"
    a "「去扫一扫吧」"
    hide fake_01 with  dissolve
    play sound "audio/se01.ogg"
    stop music
    window hide
#######################################################################
    scene black with  dissolve
    pause
    show ima_11b with blinds
    pause
    show bg_52 with  blinds
    pause
    play music "audio/se08.ogg"
    show seo_02 at right with dissolve
    b "「啊---------」"
    hide seo_02 with dissolve
    "偶然"
    "行车线对面的两个人，映入了我的眼帘"
    "一个好像是我们学校的老师，走在一起的是“他”。"
    "........虽然很远看不清。"
    "但可以确定就是“他”。"
    window hide
    show  fake_01 at right with  dissolve
    a "「.......嗯？」"
    a "「怎么了、小晶？」"
    hide fake_01 with  dissolve
    show seo_02 at right with dissolve
    b "「----学长，那个人----」"
    hide seo_02 with dissolve
    "手指指向“他”"
    "他的视线顺着我手指的指向，定格在了那里。"
    show seo_01 at right with dissolve
    b "「....带着眼镜...的，那个人....」"
    hide seo_01 with dissolve
    show  fake_02 at right with  dissolve
    a "「那个人怎么了？」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「刺中志贵学长的人，他是」"
    hide seo_01 with dissolve
    show  fake_02 at right with  dissolve
    a "「.......啊？」"
    hide fake_02 with  dissolve
    "同时。学长用诧异的表情看着我"
    show seo_01 at right with dissolve
    b "「....啊...」"
    hide seo_01 with dissolve
    "不，不好！本来想着要保持沉默的，"
    "不小心说漏嘴了，我真是的....！"
    show  fake_02 at right with  dissolve
    a "「..小晶」"
    a "「刺中我什么的，到底是怎么回事?」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「啊.....唔....那个是，怎么说....我，看到了。」"
    b "「学长和那个人正面相遇、被他用小刀刺中了」"
    hide seo_01 with dissolve
    "啊，认同了，他一个劲地点着头。"
    show  fake_02 at right with  dissolve
    a "「........原来如此」"
    a "「......这种情况也是有可能的啊。」"
    a "「真是麻烦，」"
    a "「原本以为目睹过后能成为朋友的。」"
    a "「..小晶你的未来视实还真是含含糊糊啊」"
    hide fake_02 with  dissolve
    "说完、他用力捏住了我的肩膀"
    show  fake_01 at right with  dissolve
    a "「.....我知道谁是犯人了」"
    a "「.....他....是我的老师哦」"
    hide fake_01 with  dissolve
    show seo_01 at right with dissolve
    b "「.....!?」"
    hide seo_01 with dissolve
    show  fake_01 at right with  dissolve
    a "「....好了好了」"
    a "「...总之先离开这里。去一趟我上的学校吧!」"
    hide fake_01 with  dissolve
    "他拦下了一辆出租车。"
    show seo_01 at right with dissolve
    b "「.....!?」"
    hide seo_01 with dissolve
    play sound "audio/se17.ogg"
    "我跟着志贵学长、钻进了出租车。"
    ".......明明告诉他夜里的学校危险了。"
    "为什么还要去，到底在想什么啊。"
    stop music
    window hide
###########################################################
    scene black with  dissolve
    play sound "audio/se01.ogg"
    show bg_01c with  blinds
    play music "music/tmcd-0101_06.ogg"
    show seo_01 at right with dissolve
    b "「.....誒!?」"
    hide seo_01 with dissolve
    "一下车就感到头晕目眩。"
    "明明刚刚还怒气冲冲,看到正门上的校名"
    "一下子让我颈后起一阵鸡皮疙瘩"
    window hide
    show  fake_01 at right with  dissolve
    a "「来，就是这里」"
    hide fake_01 with  dissolve
    "他熟悉地走到校门口，接着打开了门锁（是荷包锁）。"
    play sound "audio/se18.ogg"
    show  fake_01 at right with  dissolve
    a "「来来，就是这里」"
    hide fake_01 with  dissolve
    "牵着我的手，两人走进了学校。"
    window hide
    show bg_03c with blinds
    play sound "audio/se01.ogg"
    show bg_61 with blinds
    play sound "audio/se02.ogg"
    show seo_01 at right with dissolve
    b "「.......不会吧」"
    hide seo_01 with dissolve
    "我没做梦吧。"
    "这个地方，我记得。"
    show seo_01 at right with dissolve
    b "「那个，志贵学长」"
    hide seo_01 with dissolve
    "我有些不安，想要和他搭话。"
    "可是他头也不回、牵着我的手继续走着。"
    show  fake_02 at right with  dissolve
    a "「什么？」"
    hide fake_02 with  dissolve
    "他冰冷地做了回答。"
    "被这样一说，自己就像被蒙骗了一样"
    "脑袋哄地一声炸开了"
    show seo_01 at right with dissolve
    b "「喂、前辈」"
    b "「喂可以听我说一句吗」"
    hide seo_01 with dissolve
    show  fake_02 at right with  dissolve
    a "「说啊!!!什么？」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「……那个，这里是高中对吧。」"
    b "「学长前面说」"
    b "「自己在这里上学？」"
    hide seo_01 with dissolve
    show  fake_02 at right with  dissolve
    a "「唔、是说过啊，很怪吗？」"
    hide fake_02 with  dissolve
    "------绝、绝对不正常。"
    "可学长、怎么------"
    show seo_01 at right with dissolve
    b "「……那个」"
    b "「志贵学长，比我大很多对吧」"
    hide seo_01 with dissolve
    show  fake_01 at right with  dissolve
    a "「啊?????」"
    a "「......今年....２２...岁了吧」"
    hide fake_01 with  dissolve
    show seo_01 at right with dissolve
    b "「啊，这样的啊。」"
    b "「学长是这里的老师对吧？」"
    hide seo_01 with dissolve
    show  fake_01 at right with  dissolve
    a "「.....不是啊」"
    a "「你觉得是这样？」"
    hide fake_01 with  dissolve
    "-----不。唔、绝对不是。"
    show seo_01 at right with dissolve
    b "「那个…您、那个……」"
    hide seo_01 with dissolve
    show  fake_02 at right with  dissolve
    a "「小晶。」"
    a "「我既不是这里的学生也不是这里的教师。」"
    a "「不过远野志贵是这里的学生哦」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「您说的.....是谁？」"
    hide seo_01 with dissolve
    show  fake_02 at right with  dissolve
    a "「不知道哦」"
    l "「但至少可以确定的是我不是远野志贵本人」"
    hide fake_02 with  dissolve
    window hide
    "说完他回过头。"
    "展现在视线里的是一副面具般，无机质的阴森脸庞。"
    "-------要死，撤回...撤回...大撤回。"
    "什么毛茸茸的狗崽、大灰狼，乱七八糟的。"
    "这个人、怎么看都和螳螂一个模子-----!!!"
    window hide
    stop music
#############################################
    scene black with  dissolve
    play sound "audio/se02.ogg"
    show bg_61 with  blinds
    play music "music/tmcd-0101_04.ogg"
    b "「啊――――」"
    "被抓住一只手,我努力想要挣扎着逃开。"
    "可他死也不放手，另一只手不知不觉"
    "已经握起了明晃晃的小刀。"
    "这个凶器不是在五金店里能够买到的东西，好像是史密斯（美国最大的手枪军械制造商）和什么的厉害刀具"
    b "「那个，为，为什么-------」"
    "声音都颤抖了。"
    "身体一动也不能动。"
    "虽然明白，大声叫喊、踢他一脚什么的都好"
    "但身体根本不听使唤。"
    "如果那刀子再往腹部靠一点，我就死定了。"
    "现在终于能理解。电影里那些被枪指着脑袋的人的心情了"
    show  fake_02 at right with  dissolve
    l "「为什么？啊啊，到底为什么呢。」"
    l "「今天我本来想是和想你告别的，」"
    l "「可是如果这样下去、我就要被志贵君刺中了。」"
    l "「作为连接我和志贵君的你，如果不抹消」"
    l "「的话那可是很麻烦的？」"
    hide fake_02 with  dissolve
    "他的手越握越紧了。"
    "不慌不乱地一点点靠了过来。"
    b "「唔-----」"
    "挣扎的尝试没有任何效果。"
    show  fake_02 at right with  dissolve
    l "「真是的。」"
    l "「我不是说了吗，要对远野秋叶保密的呢」"
    l "「果然和女孩子做的口头约定不能相信」"
    hide fake_02 with  dissolve
    b "「啊-----」"
    "被他猛地一拉，拽到身边。....这，这个人，真的是-----"
    "好可.....怕-----"
    show  fake_02 at right with  dissolve
    l "「不要那副表情啊。」"
    l "「会变成这样你也有」"
    l "「一半的责任咧。」"
    l "「呐，我不是说了吗。」"
    l "「杀人什么的被这样一叫」"
    l "「刚刚行凶完的人是不可能放着你不管的」"
    hide fake_02 with  dissolve
    b "「可....可是、那个时候....还没有...发生----」"
    show  fake_02 at right with  dissolve
    l "「那是第二个和第三个人哦。」"
    l "「第一个女人，在遇到小晶一个多钟头之前」"
    l "「就被我“拆掉”了。」"
    l "「就因为听了你说的话有些挂心」"
    l "「我想我无论如何也要做掉另外两个人。」"
    l "「所以啦，我找到了你说的目标，」"
    l "「当天就杀了他。」"
    l "「并不是你预测中了」"
    l "「而是我实现了你的预测」"
    l "「....不过.....这也应该算是一种未来视吧！」"
    hide fake_02 with  dissolve
    "又一用力。"
    "身体被强拽了过去，撞到了他的胸口。"
    show  fake_02 at right with  dissolve
    l "「你啊、不要乱动哦。」"
    l "「刀子就顶着你的脖子哦？」"
    l "「动一动可就不得了咯。」"
    l "「颈动脉喷出大量的血可不太好处理啊」"
    hide fake_02 with  dissolve
    b "「咕-----」"
    "脖子不禁向后仰去。一股刺痛，皮肤好像被划开了一条口子"
    show  fake_02 at right with  dissolve
    l "「啊-----本来想后面再说的。」"
    l "「对了对了」"
    l "「有一点要讲清楚」"
    l "「我没有骗你哦」"
    l "「我确实相信你能够看见未来，因为我真的也有特别眼睛。」"
    l "「我呢，看过你和其他人的过去」"
    l "「可能是看得不够准确。」"
    l "「共感这样的」"
    l "「就像.....」"
    l "「呐....」"
    l "「靠着这个知道了远野志贵的事情」"
    hide fake_02 with  dissolve
    show seo_01 at right with dissolve
    b "「....啊..痛.......」"
    hide seo_01 with dissolve
    "啊―――被他拧着手臂，压倒在墙上―――"
    show  fake_02 at right with  dissolve
    l "「一个月前不久。在和小晶相遇的同一条路上，」"
    l "「我偶然碰到了远野志贵」"
    l "「所有的起因就是因为看了他的过去。」"
    l "「他过去的经历实在是惊人」"
    l "「让我一时间都只能瘫在家里。」"
    l "「小晶」"
    l "「知道你所住的那家旅馆发生的事情吧」"
    l "「他是」"
    l "「那里唯一活着走出来的人类」"
    hide fake_02 with  dissolve
    "他淡淡的说道"
    show  fake_02 at right with  dissolve
    l "「所以说啊。」"
    l "「那真是命中注定的相会。」"
    l "「多亏了他我知道让简单的变革成为可能的方法。」"
    l "「因为他一切都美好了。」"
    l "「原本无意义的世界」"
    l "「现在看起来―――充满意义」"
    hide fake_02 with  dissolve
    "刀尖慢慢从我的喉咙滑落到胸口"
    show  fake_02 at right with  dissolve
    l "「再见了」"
    l "「如果你遇到的不是我而是真正的远野志贵」"
    l "「也就不会有这样的未来了」"
    hide fake_02 with  dissolve
    "刀刃一转"
    "明明都已命悬一线、目光的焦点却无法离开那把刀"
    "刀就要这样简简单单地插入我的胸膛了么"
    show  fake_02 at right with  dissolve
    l "「即使是远野志贵本人」"
    l "「结局也不会改变」"
    l "「因为那个家伙和我一样都是异常者---！」"
    hide fake_02 with  dissolve
    stop music
    window hide
    play sound "audio/se05.ogg"
    "“哐当”，发出了清脆的响声。"
    show  shiki_02 at right with  dissolve
    m "「-----我说」"
    m "「可以不要说那种危险的话吗」"
    hide shiki_02 with  dissolve
    "这个似曾相识的声音。"
    show  fake_02 at right with  dissolve
    l "「!!!!!!」"
    hide fake_02 with  dissolve
    "他捂住手，慌忙环视了一周。"
    "发现了自己手中的小刀已不知所终后，他立刻拼命的寻找了起来。"
    "然后。.在稍远一点的地方，站立着一个带着眼镜的少年。"
    "那握着小刀的少年怎么看都和我预见到的“他”一样----"
    show  fake_02 at right with  dissolve
    l "「啊-----唉？」"
    hide fake_02 with  dissolve
    "滑动着靠着墙壁，少年慢慢座倒在地上。"
    play music "music/tmcd-0101_08.ogg"
    show  shiki_02 at right with  dissolve
    a "「能提个问题吗？」"
    a "「你就是假冒我的人吗？」"
    hide shiki_02 with  dissolve
    show  fake_02 at right with  dissolve
    l "「--------」"
    hide fake_02 with  dissolve
    "凶手没有回答。"
    "拿小刀的少年....也就是真的志贵学长咯，我呆呆地望着少年。"
    show  shiki_02 at right with  dissolve
    m "「我晕，真是麻烦啊。」"
    m "「多亏了你的电话，这几天」"
    m "「我无时无刻都被秋叶监视着」"
    m "「被当做犯人一样对待的责任」"
    m "「你要怎么负呢？」"
    hide shiki_02 with  dissolve
    "学长叽咕叽咕地抱怨着。"
    "这个声音，是和远野前辈打电话时的声音，真的是～～好有质感～～的声线啊。"
    show  shiki_02 at right with  dissolve
    a "「哎」"
    a "「你接着打算怎么办呢？」"
    a "「乖乖地去自首、还是就这么继续下去」"
    a "「如果继续下去的话呢，我觉得刚刚在阴暗处」"
    a "「寂寞难耐的家伙可不会袖手旁观哦」"
    hide shiki_02 with  dissolve
    "……？他一声不吭。"
    "……这么一说、似乎不是志贵学长打掉了他手中的小刀"
    show  fake_02 at right with  dissolve
    l "「自首？开玩笑？」"
    hide fake_02 with  dissolve
    "他边说边捡起了地上的凶器。"
    "……他已经看不见我了。.除了志贵学长,他的眼中已空无一物。"
    show  fake_02 at right with  dissolve
    l "「这种话由你说出合适么？」"
    l "「分尸杀人比我多得多的“你”？」"
    hide fake_02 with  dissolve
    show  shiki_02 at right with  dissolve
    a "「没关系」"
    a "「我不记得到现在为止有杀过人」"
    a "「如果那就是你看到的也无所谓。」"
    hide shiki_02 with  dissolve
    "语毕。志贵学长向他迈出了一步。"
    show  fake_02 at right with  dissolve
    l "「等-----等下！」"
    l "「我和你不是同类吗？」"
    l "「活着也没什么意义」"
    l "「你应该察觉到了？」"
    l "「那种愚蠢的日常，只能不断奔跑。」"
    l "「所以要脱离出来。」"
    l "「这个方法是你教我的。」"
    l "「获得新生就必须死亡」"
    l "「但是死了的话就没有任何意义。」"
    l "「所以----」"
    l "「要活着推翻自己的价值观」"
    l "「只有杀人对吧？」"
    l "「第一个让我注意到这个的不是你吗！」"
    hide fake_02 with  dissolve
    show  shiki_02 at right with  dissolve
    a "「....哦。」"
    a "「你觉得活着很无聊啊」"
    hide shiki_02 with  dissolve
    show  fake_02 at right with  dissolve
    l "「当然！」"
    l "「重复着循环的每天哪里快乐了？」"
    l "「连明确的目的都没有，无意义地颓废地活着。」"
    l "「你看，不觉得这样很奇怪吗。」"
    l "「人类数百年前就这样毫无目的地重复地轮回着啊！？」"
    l "「连活着的意义都没有。」"
    l "「还不知不觉地不停消耗资源，比白痴还不如。」"
    l "「那种贪得无厌的动物」"
    l "「不该驱逐么！」"
    hide fake_02 with  dissolve
    show  shiki_02 at right with  dissolve
    a "「你到底在说什么。」"
    a "「根本无法沟通嘛」"
    hide shiki_02 with  dissolve
    "学长愤愤地丢下一句话。"
    show  shiki_02 at right with  dissolve
    a "「我说啊、我不想说什么废话。」"
    a "「但是，那么讨厌这个世界的话，自杀不就得了？」"
    a "「说什么杀人是好方法，你才是第一个嘛。」"
    a "「那个从什么虚假比赛里退出什么的」"
    hide shiki_02 with  dissolve
    show  fake_02 at right with  dissolve
    l "「唔----你说什么？」"
    hide fake_02 with  dissolve
    show  shiki_02 at right with  dissolve
    a "「你做不到是吧？」"
    a "「所以把脾气发泄给周围的人。」"
    a "「人生无趣？」"
    a "「人生无意义？」"
    a "「真是一副丑态。」"
    a "「生活无意义的只是你吧」"
    a "「因为都活了几十年了，却发现不了一件有意义的东西....!」"
    hide shiki_02 with  dissolve
    "又一步。"
    "志贵学长一手持刀步步紧靠。"
    show  shiki_02 at right with  dissolve
    a "「把自己的恶意归结给周遭，于是为了改变自己的价值观而杀人？」"
    a "「真是种侮辱」"
    a "「你那样的杀戮什么都得不到」"
    hide shiki_02 with  dissolve
    show  fake_02 at right with  dissolve
    l "「说什么——我哪里一副丑态了。」"
    l "「现在世界改变了啊」"
    l "「所以我才能有声有色地活着」"
    l "「像这样―――惊乍地颤抖着」"
    hide fake_02 with  dissolve
    show  shiki_02 at right with  dissolve
    a "「你那只不过是胆小鬼的举动而已」"
    a "「杀了人，感到害怕了么？」"
    a "「意识到本来明明就是快乐的」"
    a "「为即将回归到常世而感到不安了吧？」"
    a "「啊啊、够了」"
    a "「为什么我非要说那么无聊的话??」"
    a "「换句话说、既然你的世界不会改变!」"
    a "「那就落幕吧」"
    hide shiki_02 with  dissolve
    "学长摸索到眼镜"
    "安静地将其取下"
    show  shiki_03 at right with  dissolve
    a "「-----------------」"
    hide shiki_03 with  dissolve
    "我屏住了呼吸"
    "在漆黑的夜色中。志贵的眼睛，看上去像蓝色的灯火一样"
    "实在是------啊，好可怕，那种会必死无疑的感觉"
    show  fake_01 at right with  dissolve
    l "「等-----下」"
    hide fake_01 with  dissolve
    "他用注视着年长的恋人一般的表情、注视着学长的眼睛。"
    show  fake_01 at right with  dissolve
    l "「我知道了」"
    l "「你说的我很认同」"
    l "「但我所犯的罪行，要活着才能去偿还」"
    l "「所以.....」"
    hide fake_01 with  dissolve
    "他好像在求饶似得"
    show  shiki_03 at right with  dissolve
    a "「如果要改过自新的话还可以商量」"
    hide shiki_03 with  dissolve
    "志贵学长停下了脚步。他阴阴一笑，握起了匕首。"
    show  shiki_03 at right with  dissolve
    a "「这样的话------」"
    a "「可是、我被你说是杀人鬼？」"
    a "「那么-----杀人鬼给罪犯以改过自新的机会」"
    a "「这可不是世间的一般道德啊」"
    hide shiki_03 with  dissolve
    show  fake_01 at right with  dissolve
    l "「什-----么」"
    hide fake_01 with  dissolve
    play sound "audio/se20.ogg"
    "嗒”轻轻的一道踩踏声,学长窜到被攻击者的身侧，利刃一闪。"
    stop music
    scene black with  dissolve
    show ima_14 with  blinds
    play sound "audio/se03.ogg"
    "“咻”，轻轻一声。"
    play sound "audio/se04.ogg"
    "他(杀人魔)直直地倒向了地面"
    "学长如释重负般地深吸了一口气，然后戴上了眼镜。"
    show  shiki_02 at right with  dissolve
    a "「------」"
    hide shiki_02 with  dissolve
    "他——该说是、杀人犯，倒在地面动也不动。但感觉并没有死去"
    "只是昏过去了而已。确切的说。学长似乎用了什么招式,使对方失去了知觉。"
    stop music
    window hide
#############################################################
    scene black with  dissolve
    show bg_61 with  blinds
    play music "music/tmcd-0101_10.ogg"
    show  shiki_04 at right with  dissolve
    a "「小...晶？」"
    hide shiki_04 with  dissolve
    "掺杂着一些试探的语气。"
    "被那个声音叫出我的名字的时候，心跳突然加速了。"
    "这是——何等性感的声线。"
    show  shiki_04 at right with  dissolve
    a "「你就是濑尾晶吧？」"
    a "「从秋叶那里听说了」"
    hide shiki_04 with  dissolve
    "志贵学长把手伸向了瘫坐在地上的我"
    show seo_02 at right with  dissolve
    b  "「啊....哎、是、真是对不起！」"
    hide seo_02 with  dissolve
    "我慌慌张张地握住学长的手、站了起来。"
    "还没有从刚刚的冲击里缓过神、哆哆嗦嗦地站也站不好，只能紧紧的抱着他的手臂。"
    "......唔唔，真是丢死人了"
    show seo_02 at right with  dissolve
    b  "「唔....啊，唔---」"
    hide seo_02 with  dissolve
    "话也说不出来，只能不停晃动着脑袋。"
    "想说没有关系，又不想看躺在地上的家伙的脸，连是不是因为第一次被男生抱着也搞不清，总之脑袋里小鸟转个不停。"
    show  shiki_04 at right with  dissolve
    a "「对呀，还是出去吧!」"
    hide shiki_04 with  dissolve
    "好像察觉到我有些不适，他牵着我的手走离开了那里。"
    play sound "audio/se07.ogg"
    window hide
##########################################################
    scene black with  dissolve
    show bg_03c with  blinds
    show seo_02 at right with  dissolve
    b  "「那个人.....那个人，就这样丢着不管没事吗？」"
    hide seo_02 with  dissolve
    show  shiki_04 at right with  dissolve
    a "「之后就交给学校前辈来处理了」"
    hide shiki_04 with  dissolve
    "简单交代完，志贵学长朝校门走去"
    show bg_01c with  blinds
    "接着事件就这样简单地收场了。不管怎么说，这就是一直影响着我的事件。"
    "志贵学长什么都没有准备问，但我有很想知道的事情，就只问这一个吧。"
    show seo_02 at right with  dissolve
    b  "「请问，学长」"
    b  "「难道说你一直在找我吗？」"
    hide seo_02 with  dissolve
    "他点了点头"
    "......我越来越不明白了。"
    show seo_02 at right with  dissolve
    b  "「为什么？」"
    b  "「我只打过一个电话」"
    b  "「内容那么片面，像是恶作剧一样的电话」"
    b  "「为什么？」"
    hide seo_02 with  dissolve
    show  shiki_04 at right with  dissolve
    a "「啊，那确实是像个恶作剧电话呢」"
    a "「可是」"
    a "「小晶你的话，是拼死说出的吧？」"
    a "「总觉得不能放着不管，想自己问个清楚」"
    a "「......嘛」"
    a "「没想到会和从昨天起就查无踪影的杀人犯牵连上」"
    hide shiki_04 with  dissolve
    "他害羞地说完后又继续向前走去。"
    show  shiki_04 at right with  dissolve
    a "「接下来。我送你回家吧！」"
    a "「小晶是」"
    a "「住在临区的饭店的吧」"
    hide shiki_04 with  dissolve
    show seo_02 at right with  dissolve
    b  "「啊-------」"
    hide seo_02 with  dissolve
    "是的，就在他说那句话的时候。咕噜噜，可爱的（想如此这般坚信着）声音从肚子里发了出来。"
    show seo_02 at right with  dissolve
    b  "「-----！！！！」"
    b  "「我真是白，白痴白痴白痴白痴白痴啊！」"
    b  "「忘记还饿着肚子」"
    b  "「人就松弛了下来！」"
    hide seo_02 with  dissolve
    "学长......现出了十分困惑的表情."
    show  shiki_04 at right with  dissolve
    a "「好。我们先去吃晚饭吧」"
    a "「就当做是封口费请客啦」"
    hide shiki_04 with  dissolve
    "学长说出了让人愉悦的东西。"
    show  shiki_04 at right with  dissolve
    a "「啊......」"
    a "「等一下。」"
    a "「在此之前―----」"
    hide shiki_04 with  dissolve
    "他摸索了一下拿出了钱包，“呠”地打开了它。"
    "我好奇地偷偷瞟了一眼，真是让人瞠目结舌。"
    "...现在还在用蛙嘴式的小钱包，可怕！而且里面只放了一枚500圆的硬币，实在冲击力惊人。"
    show  shiki_04 at right with  dissolve
    a "「....速食荞麦面..喜欢...吗」"
    hide shiki_04 with  dissolve
    "像蚊子一样，他小声地说道。"
    show  shiki_04 at right with  dissolve
    a "「-----也是哈」"
    a "「再怎么说、女孩子都不会喜欢那个，对吧....」"
    hide shiki_04 with  dissolve
    show seo_02 at right with  dissolve
    b  "「-----！！！！」"
    b  "「那个......我」"
    hide seo_02 with  dissolve
    "绞尽脑汁要说些什么好呢。钱的话我带着，所以我来请客吧。这种话怎么无论如何也开不了口，想破脑袋也想不出什么好办法啊。"
    show seo_02 at right with  dissolve
    b  "「-我........我喜欢荞麦面！」"
    hide seo_02 with  dissolve
    "到底说出了什么不经大脑思考的话啊。"
    show seo_02 at right with  dissolve
    b  "「--------」"
    hide seo_02 with  dissolve
    "呀--------发觉自己脸红了。"
    "学长瞪大了眼睛，呆呆地看着我"
    show  shiki_04 at right with  dissolve
    a "「是吗?」"
    a "「那过来吧!!」"
    hide shiki_04 with  dissolve
    "他高兴地走到了前面。"
    show ima_22 with blinds
    show seo_02 at right with  dissolve
    b  "「---------！」"
    hide seo_02 with  dissolve
    "Lucky～！.　我忍住激动，跟了上去。"
    "....嘛，年终的夜晚。吃点荞麦面什么的，可能也不错嘛。"
    "咦？突然。.看着学长的背影，突然一阵眩晕袭来。"
    "迷迷糊糊中"
    "一瞬间，我和远野前辈、志贵学长还有些不认识的人们在一起-----幸福的幻视。"
    show  shiki_04 at right with  dissolve
    a "「小晶？」"
    hide shiki_04 with  dissolve
    show seo_02 at right with  dissolve
    b  "「啊，是-----我来了.....!」"
    hide seo_02 with  dissolve
    "回答着，我小跑追了上去。"
    "……原来如此。.多事之秋下会有这样的邂逅啊。"
    play sound "audio/se22.ogg"
    "跟在学长身后，朝着前方的背影，“嗙嗙”拍了拍手（開手、仪式动作）。"
    "接着，志贵学长"
    "今年好像给你添了好多麻烦"
    "但之后还是要请你多多关照啦"
    "在年终的夜晚，我许下了今年最后的祈愿。"
    scene black with  dissolve
    pause
    show fin with  blinds
    pause
    stop music
    window hide
    pause
    return

label yuecha:
    stop music
    show screen quick with  dissolve
    scene black with  dissolve
    "说明："
    "这段闲话公开了许多本篇中的秘密。"
    "只适合觉得月姬本篇「啊，月姬已经不需要再玩了」的人观看。"
    window hide
    hide screen quick with  dissolve
    scene black with dissolve
    pause
    scene tea with dissolve
    pause
    scene black with dissolve
    play music "music/tmcd-0101_03.ogg"
    show screen quick with  dissolve
    scene bg_59 with blinds
##################################################
    ##最左展示图像：
    show ark_t03 at center with dissolve:
        linear 0.5 xalign -0.3
###################################################
    m1 "「呐  ciel。"
    m1 "虽然觉得好像开始了，这是要干什么呢？」。"
###################################################
    ##最右展示图像：
    show cel_t01a at center with dissolve:
        xalign 1.2
####################################################
    y1 "「要说要干什么的话，好像是纪念完成的茶会哦。"
    y1 "可能因为考虑到预算就变成了这样的东西了"
    y1 "让我和你反省到现在为止的事情的，似乎是这样的。」"
    hide ark_t03 with dissolve
    show ark_t11 at center with dissolve:
        linear 0.5 xalign -0.3
    m1 "「唔哇，是这样啊。"
    m1 "……什么啊，早知道是这样就不来了。"
    m1 "说起来，为什么是我和ciel？我可不喜欢这个组合啊。」"
    hide cel_t01a  with dissolve
    show cel_t12 at center with dissolve:
        xalign 1.2
    y1 "「嗯，我也最讨厌你了来着，这组合是为什么呢？」"
    hide ark_t11 with dissolve
    show ark_t04 at center with dissolve:
        linear 0.5 xalign -0.3
    m1 "「嗯，你看啊，这和之前的知得留老师组合人员相同的吧？"
    m1 "ciel你待遇真好，连立绘都有"
    m1 "但是我的话就是那样了。"
    m1 "该说是这种待遇我觉得很过分呢？"
    m1 "还是该说我开始怀疑自己是不是第一女主了呢？什么的，总之我有各种不满。」"
    hide cel_t12 with dissolve
    show cel_t03 at center with dissolve:
        xalign 1.2
    y1 "「哈哈。"
    y1 "说起来那个组合，好像评价不错呢。"
    y1 "因为收集全要素的执念而接受了所有授课的人也是有的吧？」"
    hide ark_t04 with dissolve
    show ark_t01a at center with dissolve:
        linear 0.5 xalign -0.3
    m1 "「根本没有吧？"
    m1 "你看啊“心惊胆战的动物园其二”那里」"
    m1 "「连剧本担当（译者注：武内崇）都抱怨说不看攻略打不出来呢。」"
    hide cel_t03 with dissolve
    show cel_t08 at center with dissolve:
        xalign 1.2
    y1 "「……哈。"
    y1 "怎么觉得，作为游戏来说有破绽啊？」"
    hide ark_t01a with dissolve
    show ark_t03 at center with dissolve:
        linear 0.5 xalign -0.3
    m1 "「嗯，嘛反正也是和游戏本篇无关的组合，"
    m1 "这种程度的话还是可以接受的……"
    m1 "...那个，ciel好像有新的客人来了的样子。」"
    hide cel_t08
    show cel_t12 at center with dissolve:
        xalign 1.2
    y1 "「什么？"
    y1 "真是奇怪呢，明明说今天包给我的----」"
    window hide
    hide cel_t12 with fade
    hide ark_t03 with fade
    show aki_t15b with dissolve
    pause
    window show
    i"「----------额」"
    hide aki_t15b dissolve
    "「……………………………」"
    "「……………………………」"
    "「……………………………」"
    show ark_t04 at center with dissolve:
        linear 0.5 xalign -0.3
    m1 "「……………我说。"
    m1 "    这算什么啊，那个“额”的反应。」"
    show aki_t04b at center with dissolve:
        xalign 1.2
    i"「………………………」"
    hide ark_t04 with dissolve
    show ark_t16 at center with dissolve:
        linear 0.5 xalign -0.3
    m1 "「喂。"
    m1 "不要一副什么事都没有的样子坐下来啊。"
    m1 "特地连沙发都带来了，到底想干什么啊妹妹」"
    hide aki_t04b with dissolve
    show aki_t01b at center with dissolve:
        xalign 1.2
    i "「…………想干什么，这是我的台词吧。"
    i "我是因为今天开茶会就来了，为什么你们两个人在这里啊？"
    i "虽然这么说有些失礼，这种简陋的座位也配不上你们吧。"
    i "う？」"
    hide ark_t16 with dissolve
    show cel_t01a at center with dissolve:
        linear 0.5 xalign -0.3
    y1 "「―――――哈哈。"
    y1 "这就是那种情况吧。"
    y1 "因为只有我和Arcueid的话也没什么可讲的"
    y1 "就把有班长属性的秋叶当做主持人来确保对话的顺利进行，这样之类的。"
    y1 "这就是那种情况吧。」"
    hide cel_t01a with dissolve
    show ark_t30 at center with dissolve:
        linear 0.5 xalign -0.3
    m1 "「诶诶ー！"
    m1 "什么喵，那种东西听都没听说过啊！"
    m1 "妹妹什么的不是在本篇中出场最多吗！"
    m1 "连这种番外篇也要出场真是任性呢！」"
    hide aki_t01b with dissolve
    show aki_t03b at center with dissolve:
        xalign 1.2
    i "「Arcueid。"
    i "那个，可不可以不要叫我妹妹？"
    i "我虽然是远野志贵的妹妹，但是和你没有任何关系，只是陌生人而已。"
    i "因为这之后，不管发生什么都不会和你有血缘关系的」"
    m1 "「这样啊？"
    m1 "如果我和志贵结婚了，妹妹不就成了我的妹妹了么？」"
    hide aki_t03b with dissolve
    show aki_t15b at center with dissolve:
        xalign 1.2
    i"「什――――什么啊你那种蛮不讲理的说法！"
    hide aki_t15b with dissolve
    show aki_t06b at center with dissolve:
        xalign 1.2
    i "听好了，因为像你这种不明生物是不能和人类结婚的"
    i "所以不要老是粘着别人的哥哥了！"
    i "吸血鬼就像吸血鬼那样，在没人注意的到的地方咻咻的吸着老鼠的血就行了！」"
    hide ark_t30 with dissolve
    show ark_t06 at center with dissolve:
        linear 0.5 xalign -0.3
    m1 "「唔。"
    m1 "先说清楚，我可是不吸人血的，"
    m1 "相反妹妹的话才是需要定期的吸人血的吧，你才没法像人类那样生活呢？"
    m1 "说起来我们两个，某些方面是一样的呢。」"
    hide aki_t06b with dissolve
    show aki_t18b at center with dissolve:
        xalign 1.2
    i "「哈，怎么可能。"
    i "我只是把血液当做用餐的一环品尝而已。"
    i "只是稍微和普通人的趣味不同罢了，只是懂得其中不同的可爱的美食家罢了。"
    i "和根本不是人类的存在完全不一样，所以请不要产生同类意识。」"
    hide ark_t06 with dissolve
    show ark_t05d at center with dissolve:
        linear 0.5 xalign -0.3
    m1 "「―――诶。"
    m1 "那时候可不像你说的，不是相当享受吗？"
    m1 "头发通红的吸着血的妹妹，可比不专业的死徒内行多了。」"
    hide aki_t18b with dissolve
    show aki_t07b at center with dissolve:
        xalign 1.2
    i "「那，那是……那个，是哪里搞错了！"
    i "再说本来就是因为你到处追罗亚那个吸血鬼的亡灵，我和哥哥才会那么惨。"
    i "如果没有那种东西来添麻烦的话，我就会一直保持现在这个样子的。」"
    m1 "「呼呼，是这样吗？"
    m1 "嘛，既然妹妹都这么说了就当是这样吧。」"
    hide aki_t07b with dissolve
    show aki_t29 at center with dissolve:
        xalign 1.2
    i "「…………！"
    i "你，哪里有问题啊你这个小偷吸血鬼！」"
    hide ark_t05d with dissolve
    show cel_t01a at center with dissolve:
        linear 0.5 xalign -0.3
    y1 "「知道了知道了，冷静下来秋叶。"
    y1 "今天可不能吵架哦。"
    y1 "因为这里是大家喜欢的咖啡厅啊。」"
    hide aki_t29 with dissolve
    show aki_t05b  at center with dissolve:
        xalign 1.2
    i "「……我知道。"
    i "不需要劳驾前辈来说。」"
    y1 "「也是呢？"
    y1 "――――真是的，两个人是五十步笑百步所以不能不好好相处哦。"
    y1 "今天我们设定上相互不是敌对关系而是朋友关系呢。"
    y1 "嗯，所以说差不多该叫个蛋糕了。"
    y1 "不好意思，可以点餐吗？」"
    window hide
    hide cel_t01a with fade
    hide aki_t05b with fade
    pause
    show his_t01 at left with dissolve
    k2 "「让您久等了。」"
    show koha_t03b at right with dissolve
    k1 "「噢，不要客气尽管点吧！」"
    window hide
    hide his_t01 with dissolve
    hide koha_t03b with dissolve
    pause
    show ark_t13 at center with dissolve:
        linear 0.5 xalign -0.3
    window show
    m1 "「--------------」"
    hide ark_t13 with dissolve
    show cel_t07a  at center with dissolve:
        xalign 1.2
    y1 "「--------------」"
    hide cel_t07a with dissolve
    show aki_t15b at center with dissolve
    i "「--------------」"
    hide aki_t15b with dissolve
    window hide
    pause
    show aki_t03b at center with dissolve:
        linear 0.5 xalign -0.3
    window show
    i "「…………我说。"
    i "你们俩，在这种地方干什么呢？」"
    show koha_t03b at center with dissolve:
        xalign 1.2
    k1 "「诶嘿嘿。"
    k1 "想稍微挣点零用钱就来打工了。"
    k1 "但是这工作只有今天，只干一小时哦。」"
    hide koha_t03b with dissolve
    show his_t05 at right with dissolve
    k2 "「--------」"
    window hide
    hide his_t05 with dissolve
    hide aki_t03b with dissolve
    show cel_t08 at center with dissolve:
        linear 0.5 xalign -0.2
    window show
    y1 "「……真厉害。"
    y1 "以这种认真的工作来吸引并增加自己的粉丝量吗？"
    y1 "因为毫无破绽所以无法击破啊。"
    y1 "这种，该死的迷人魅力！"
    y1 "之类的。」"
    show ark_t06  at center with dissolve:
        xalign 1.2
    m1 "「…………同感。"
    m1 "我对你们能轻松面对对方发脾气稍稍"
    m1 "有些觉得感动呢。"
    m1 "果然是这样啊，为了粉丝的数量"
    m1 "不得不做到那种程度呢。」"
    hide cel_t08 with dissolve
    hide ark_t06 with dissolve
    window hide
    show aki_t11b at center with dissolve:
        linear 0.5 xalign -0.2
    i "「……好胆量呢，琥珀。"
    i "仅仅是在本篇还不满足，连这个番外篇里也要和我对着干吗？」"
    show koha_t03b  at center with dissolve:
        xalign 1.2
    k1 "「没有没有，没有那种事情。"
    k1 "我们俩只是普普通通的的服务员，"
    k1 "稍稍在后面听了听你们说话罢了，请不要太在意。」"
    i "「………………………」"
    hide aki_t11b with dissolve
    show his_t15 at center with dissolve:
        linear 0.5 xalign -0.1
    k2 "「（喂，姐姐……秋叶小姐都生气了"
    k2 "(是不是应该表现的老实一点比较好……)」"
    hide koha_t03b with dissolve
    show koha_t08 at center with dissolve:
        xalign 1.2
    k1 "「―――――――（咔）」"
    hide his_t15 with blinds
    k2 "「啊呜―――――！？」"
    hide koha_t08 with dissolve
    show koha_t03b  at center with dissolve:
        xalign 1.2
    k1 "「好的，那么请点餐吧！"
    k1 "总之推荐的似乎是是特大草莓派。」"
    show aki_t01b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「这样吗。"
    i "那么适当的拿点来吧，服务员。」"
    k1 "「好的，明白了。"
    k1 "那么我去去就来。」"
    window hide
    hide koha_t03b with blinds
    hide aki_t01b
    show cel_t09 at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    y1 "「……哇……琥珀把翡翠拖到厨房里去了呢。"
    y1 "感觉就像是恐怖电影一样。"
    y1 "熟食店，之类的」"
    show ark_t11  at center with dissolve:
        xalign 1.4
    m1 "「三菱铁丝？」"
    hide ark_t11 with dissolve
    y1 "「……好了。"
    y1 "说起来这里是那个咖啡厅呢。"
    y1 "秋叶，你知道吗？」"
    show aki_t18b  at center with dissolve:
        xalign 1.4
    i "「虽然只是听说过而已。"
    i "说起来前辈你和哥哥一起来过吗？」"
    show cel_t02 at center with dissolve:
        linear 0.5 xalign -0.1
    hide cel_t09 with dissolve
    y1 "「唔，他每次都推推拖拖的最后不了了之。"
    y1 "虽然这里是相当热的话题，却没能进入本篇呢。」"
    hide aki_t18b with dissolve
    show ark_t02  at center with dissolve:
        xalign 1.4
    m1 "「啊，那是没有办法的事哦。"
    m1 "这里啊，应该说并不是本来就在<<月姬>>的世界里的地方，"
    m1 "因为是像分界线一样的的地方。"
    m1 "所以说不能作为和某个世界紧密联系的正式的存在，"
    m1 "说起来普通的人并不能成为主角，"
    m1 "但这里是只有主角才能进入的。」"
    hide cel_t02 with dissolve
    show aki_t17b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「什么？」"
    hide ark_t02 with dissolve
    show ark_t16  at center with dissolve:
        xalign 1.4
    m1 "「所ー以ー说ー、志贵和式见面的话会变的很麻烦的吧。"
    m1 "远野志贵和浅上藤乃的话还没什么问题，"
    m1 "如果是志贵和式，我和橙子相遇的话因为会产生矛盾"
    m1 "在正式的时间轴上我们是进不去的。」"
    hide aki_t17b with fade
    hide ark_t16 with fade
    window hide
    show koha_t03b with blinds
    window show
    k1 "「上餐，让大家久等了！"
    k1 "……诶，这是怎么了？"
    k1 "怎么大家都一脸沉重的表情？」"
    window hide
    hide ark_t16 with dissolve
    hide koha_t03b with dissolve
    show aki_t01b at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    i "「嗯？"
    i "啊，稍稍有些呢，和你们俩没有关系。"
    i "怎么说你们也是副女主角，在本篇中也是可以进入这个咖啡厅的。」"
    show his_t07  at center with dissolve:
        xalign 1.2
    k2"「……………？」"
    hide aki_t01b with dissolve
    show aki_t04b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「好了好了，喝茶吧。"
    i "说起来翡翠。」"
    hide his_t07 with dissolve
    show his_t04  at center with dissolve:
        xalign 1.2
    k2 "「――――哦。"
    k2 "是什么事呢？秋叶小姐。」"
    hide aki_t04b with dissolve
    show aki_t16b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「琥珀有没有动什么手脚？"
    i "你看，就像是往茶里混奇怪的东西之类的……」"
    window hide
    scene ima_10 with dissolve
    scene bg_59 with blinds
    show aki_t04b with dissolve
    window show
    i "「――――那么。"
    i "吃的也差不多了我觉得该进入正题了。」"
    window hide
    hide aki_t04b with dissolve
    show ark_t03 at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    m1 "「那个什么反省会？"
    m1 "那个算了，我才没有什么好反省的。」"
    show cel_t07a  at center with dissolve:
        xalign 1.2
    y1 "「同意。"
    y1 "……嘛，虽然白天没能去消灭在街上旁若无人的徘徊的吸血鬼是挺值得反省的。」"
    hide ark_t03 with dissolve
    show aki_t04b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「前辈，这样说的话我也有要反省的事情，"
    i "这样的话就好好运用难得的后日谈的好处吧。"
    i "反正琥珀和翡翠也在认真听着呢，这里我觉得不应该是反省会而想办成感想会。」"
    hide cel_t07a with dissolve
    show his_t04  at center with dissolve:
        xalign 1.2
    k2 "「感想会是吗……？"
    k2 "非常对不起，我不是很明白秋叶小姐的想法……也就是要做民意调查？是这样吗？」"
    i "「民意调查，应该是各自把各自的疑问说出来一起讨论，这种形式吧。"
    i "就算是翡翠，"
    i "在本篇里不是也有过一两次歪着头说着“怎么回事？！”"
    i "的的时候么？？"
    i "就是解决这种疑问的哦。」"
    hide his_t04 with dissolve
    show ark_t01a  at center with dissolve:
        xalign 1.2
    m1 "「呐呐，那么如果不是疑问也行吗？"
    m1 "那样的话我也有几句想说的。」"
    i "「可以没关系。那么就从ciel前辈开始吧。」"
    window hide
    hide aki_t04b with dissolve
    hide ark_t01a with dissolve
    show cel_t08 at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    y1 "「从我开始吗……！？"
    y1 "唔嗯，我想想……虽然和本篇没什么关系"
    y1 "我想关于远野君的钱包问点问题。"
    y1 "远野君有的时候抱怨说都想去打工了"
    y1 "你给他每个月多少零花钱呢？」"
    show aki_t04b  at center with dissolve:
        xalign 1.2
    i"「我不给哦。」"
    y1"「诶？」"
    i "「哥哥才没有零花钱什么的呢。"
    i "在有间家的时候我不太清楚"
    i "回到本家之后就是这样的。"
    i "本来那种东西，没必要给吧？」"
    hide cel_t08 with dissolve
    show cel_t10a at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「没，没必要什么的―――难道说远野君，有银行卡之类的吗？」"
    hide aki_t04b with dissolve
    show koha_t03b  at center with dissolve:
        xalign 1.2
    k1 "「哈哈哈，是真的，ciel前辈"
    k1 "秋叶小姐不给志贵任何钱，不是这样说过了吗？」"
    hide cel_t10a with dissolve
    show cel_t09 at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「……那个，这样的话远野君平时都是怎么维持生活的？"
    y1 "没有零用钱的话，从学校回家路上的零食之类的，咖喱面包之类的怎么办啊？」"
    hide koha_t03b with dissolve
    show aki_t11b  at center with dissolve:
        xalign 1.2
    i "「那些是没有必要的。"
    i "想吃东西的话就吃必要的几顿，钱是没有必要的吧？」"
    hide cel_t09 with dissolve
    show cel_t08 at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「……哈？"
    y1 "但是，我觉得除此之外还会有好多想要"
    y1 "的东西的。」"
    hide aki_t11b  with dissolve
    show aki_t04b at center with dissolve:
        xalign 1.2
    i "「对啊。"
    i "所以说，那样的话就直接跟我说我去准备就行了。"
    i "如果哥哥真的需要的话明明不管是什么我都会去准备的"
    i "不知道为什么从没和我说过。"
    i "真是的，哥哥的无欲无求有点不正常呢。"
    i "你不这么觉得吗？琥珀。」"
    hide cel_t08 with dissolve
    show koha_t15 at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「嗯。"
    k1 "因为明明都怎么那样说了还拼命的去打工，"
    k1 "非常想去打工呢。」"
    hide aki_t04b with dissolve
    show his_t17 at center with dissolve:
        xalign 1.2
    k2 "「……姐姐，我觉得不是那个样子的……」"
###########################################################################
    window hide
    scene ima_10 with dissolve
    scene bg_59 with blinds
    show ark_t01a at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    m1 "「啊，那么接下来轮到我了呢。"
    m1 "要说在意的事的话"
    m1 "是那个哦。"
    m1 "怎么区分在那边的两个人呢？」"
    show his_t23 at center with dissolve:
        xalign 1.2
    k2 "「………………？」"
    hide his_t23 with dissolve
    show koha_t02b at center with dissolve:
        xalign 1.2
    k1 "「哈？"
    k1 "是说我和翡翠的事情吗？」"
    m1 "「嗯。"
    m1 "你们两个时不时―――――会相互装扮的吧？"
    m1 "仅靠外表分不出来所以不得不靠具体情况分析了"
    m1 "就没有什么方便的判断方法吗？"
    m1 "其实眼睛的颜色的区别也会消失，之类的」"
    hide koha_t02b with dissolve
    show cel_t01a at center with dissolve:
        xalign 1.2
    y1 "「啊，这个我也想问。"
    y1 "没有什么提示之类的东西吗？"
    hide ark_t01a with dissolve
    show aki_t02b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「说起来，这连我都不知道是怎么回事啊。"
    i "……嘛，虽然琥珀的话和普通标准不一样我是一直知道的"
    i "，居然连翡翠也……」"
    hide cel_t01a with dissolve
    show his_t21 at center with dissolve:
        xalign 1.2
    k2 "「啊…………………」"
    hide his_t21 with dissolve
    show koha_t17 at center with dissolve:
        xalign 1.2
    k1 "「不是这样的。"
    k1 "那是我一个人干的。"
    k1 "眼睛的颜色是使用颜色控制物的，"
    k1 "时间的话等翡翠因为药物睡着后，找准那段时间的。"
    k1 "和翡翠没有任何的关系。」"
    hide aki_t02b with dissolve
    show cel_t08 at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「把毒手伸向了自己的妹妹呢，琥珀.」"
    hide koha_t17 with dissolve
    show koha_t02b at center with dissolve:
        xalign 1.2
    k1 "「讨厌啦，这多不好听啊。"
    k1 "还没通翡翠线的好孩子看到了不是会产生误会吗？」"
    hide cel_t08 with dissolve
    show aki_t18b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「这既不是误会也不是舞会是毫无争议的事实啊」"
    hide koha_t02b with dissolve
    show koha_t08 at center with dissolve:
        xalign 1.2
    k1 "「啊，秋叶小姐好过分！"
    k1 "我会好好的告诉志贵了啦。"
    hide koha_t08 with dissolve
    show koha_t02b at center with dissolve:
        xalign 1.2
    k1 "虽然也有人注意到了"
    k1 "总之就是姐姐（姉さん）和姐姐（姉）的区别咯。"
    k1 "好孩子们，你们明白了吗？"
    k1 "二周目的话如果注意到那里去玩的话，意外的就都暴露了呢。」"
    hide aki_t18b  with dissolve
    show ark_t03 at center with dissolve:
        linear 0.5 xalign -0.1
    m1 "「诶，哪里哪里？……啊，真的。"
    m1 "这样啊，还以为一定是写错字了就没注意。」"
    hide koha_t02b with dissolve
    show his_t04 at center with dissolve:
        xalign 1.2
    k2 "「……嗯。"
    k2 "总之都到了连原画担当都说：那个称呼，叫姐姐（姉）的话是不是更好？”"
    k2 "的程度了。」"
    hide ark_t03 with dissolve
    show aki_t06b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「真是自作自受呢。"
    i "那家伙老是造点新的词出来，连正常的的文章别人都看不懂了」"
    hide his_t04 with dissolve
    show his_t18 at center with dissolve:
        xalign 1.2
    k2 "「――――不好意思。」"
    hide aki_t06b with dissolve
    show koha_t03b at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「嗯？"
    k1 "怎么了翡翠酱，突然露出那么令人害怕的神情。」"
    k2 "「关于那些新词，有些词语我无论如何都不会读。"
    k2 "(くら)眩(やみ)病(づき)月，(すけ)透る(つめ)爪(あと)跡，"
    k2 "(おり)檻(がみ)髪，这些我虽然会读，这个“硝る躯”怎么读"
    k2 "呢？」"
    hide koha_t03b with dissolve
    show ark_t08 at center with dissolve:
        linear 0.5 xalign -0.1
    m1 "「哈哈哈」"
    hide his_t18
    show cel_t04 at center with dissolve:
      xalign 1.2
    y1 "「嘿嘿嘿」"
    k2 "「？"
    k2 "两位知道怎么读吗？」"
    hide ark_t08 with dissolve
    show ark_t01a at center with dissolve:
        linear 0.5 xalign -0.1
############################################################################
    m1 "「啊，嗯。"
    m1 "说到这里呢。"
    m1 "我觉得那里的话就放过他比较好。"
    m1 "他本人好像也反省的相当厉害呢。」"
    hide cel_t04 with dissolve
    show cel_t01a at center with dissolve:
      xalign 1.2
    y1 "「好像在认真写解释呢。」"
    window hide
    hide ark_t01a with dissolve
    hide cel_t01a with dissolve
    pause
    show his_t18 with dissolve
    window show
    k2 "「……这不算是回答。"
    k2 "本来就是为了消除疑问才进行的交流，请无论如何回答我的问题。」"
    window hide
    hide his_t18 with dissolve
    show ark_t03 at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    m1 "「唔嗯……没有办法呢。"
    m1 "那个呢，读作“因为很燃啊”"
    m1 "就行了。」"
    show cel_t08 at center with dissolve:
      xalign 1.2
    y1 "「哦。"
    y1 "对于学过语言学的人来说用这种词是该吊死呢，还是该说只是新造的词呢？」"
    m1 "「你看，是说硝烟的硝字吧？"
    m1 "单词的意思什么的放在一边，已经给人深刻的印象了」"
    hide ark_t03 with dissolve
    show aki_t15b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「-------（说不出话来）」"
    hide cel_t08 with dissolve
    show koha_t02b at center with dissolve:
      xalign 1.2
    k1 "「哈哈。"
    k1 "与其做那种半吊子的事情，干脆用“好萌的身体”不就行了。"
    k1 "不是都受到翡翠酱的献身照料了吗？"
    k1 "用那个的话更好吧。"
    k1 "是吧翡翠酱？"
    k1 "能照料志贵你看起来很高兴呢。」"
    hide aki_t15b with dissolve
    show his_t02 at center with dissolve:
        linear 0.5 xalign -0.1
    k2 "「……………………」"
    pause
    window hide
    hide koha_t02b with fade
    hide his_t02 with fade
    show ark_t03 at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    m1 "「说起标题的话，虽然一开始想每一个都标上英文题目的。"
    m1 "ciel，你还记得吗？」"
    show cel_t01a at center with dissolve:
      xalign 1.2
    y1 "「记得啊。"
    y1 "确实是这样呢，"
    y1 "硝子の月 - Glass Moon"
    y1 "黒き獣Ⅰ - Six Six Six"
    y1 "朱の紅月 - Crimson Air"
    y1 "静夢 - cizumu"
    y1 "沈夢 - cizumu"
    y1 "之类的，这种感觉。」"
    hide ark_t03 with dissolve
    show koha_t15 at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「啊。"
    k1 "对了，“静（しずむ）夢”和“沈（しずむ）夢”在日语里读音一样呢！」"
    hide cel_t01a with dissolve
    show his_t20 at center with dissolve:
      xalign 1.2
    k2 "「……诶……我，沈……沈……」"
    hide koha_t15 with dissolve
    show koha_t03b at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「诶？"
    k1 "你在说什么呢翡翠酱？"
    k1 "你觉得沈梦该怎么读呢？」"
    hide his_t20 with dissolve
    show his_t21 at center with dissolve:
      xalign 1.2
    k2 "「………那个……沈（ちん）梦（む）……这样」"
    hide his_t21 with dissolve
    show aki_t03b at center with dissolve:
      xalign 1.2
    i "「琥珀，别欺负翡翠太过分。」"
    hide koha_t03b with dissolve
    show koha_t12 at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「知道了。"
    k1 "但是Arcueid和ciel对内部消息知道的很清楚呢。"
    k1 "为什么呢？」"
########
    hide aki_t03b with dissolve
    show ark_t01a at center with dissolve:
      xalign 1.2
    m1 "「因为，我和ciel是最早就在的。"
    m1 "虽然妹妹也挺早就在的，最早的一年半里，我们一直在和月姬打交道哦？」"
    hide koha_t12 with dissolve
    show cel_t12 at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「也是呢。"
    y1 "我们不管是月姬的酸甜苦辣都很清楚呢。"
    y1 "就说我的的结局吧，总计重写了两次，秋叶的结局重写了3次。"
    y1 "试玩版阶段的结局和完全版的结局完全不同呢。"
    y1 "特别是秋叶的测试版结局现在相当珍贵呢。"
    y1 "为什么远野君会OOOO的呢，因为很简单就由我来和大家口头说明吧。"
    y1 "那么，总之是这个样子的，"
    y1 "请有着世界上仅有十份的试玩版程序的人马上卸载掉，并且销毁掉CD。」"
    hide ark_t01a with dissolve
    show his_t01 at center with dissolve:
      xalign 1.2
    k2 "「……也就是说销毁证据呢，没错吧？」"
    hide cel_t12 with dissolve
    show koha_t15 at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「唔嗯，不小心看到大人的世界的阴暗面了。」"
    hide his_t01 with dissolve
    hide koha_t15 with dissolve
    window hide
    scene ima_10 with blinds
    scene bg_59 with blinds
    show aki_t04b with dissolve
    window show
    i "「咳咳。"
    i "那么接下来就轮到我了。"
    hide aki_t04b with dissolve
    show aki_t01b with dissolve
    i "虽然内容可能有些沉重，前辈为什么还呆在这条街上呢？」"
    hide aki_t01b with dissolve
    window hide
    show cel_t12 at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    y1 "「诶……？"
    y1 "啊，哈哈，那个，那是因为……这是为什么呢？」"
    show ark_t04 at center with dissolve:
      xalign 1.2
    m1 "「你这么一说确实是呢。"
    m1 "罗亚已经被消灭了，你留在这里的理由已经没有了。」"
    hide cel_t12 with dissolve
    show cel_t10a at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「理由什么的我有哦！"
    y1 "是这样的哦，吸血鬼潜伏过的地方的话"
    y1 "即使把那个吸血鬼消灭了之后也还是有调查的必要的。"
    y1 "吸血鬼会不断制造新的吸血鬼。"
    y1 "这么说你应该能听懂吧？"
    y1 "父母辈的吸血鬼如果死绝了的话"
    y1 "子女辈的吸血鬼大部分也会死绝。"
    y1 "但是被当做“后继人”的特别的“孩子”的话"
    y1 "即使父母死绝了也能幸存。"
    y1 "所以说，净化被吸血鬼污染的区域的话"
    y1 "不如说消灭掉父母辈的吸血鬼之后才真正开始。"
    y1 "我的话，那个……稍稍改了下文件"
    y1 "让自己去处理那件事情了……」"
    hide ark_t04 with dissolve
    show ark_t06 at center with dissolve:
      xalign 1.2
    m1 "「乱用职权吗？"
    m1 "真像你的作风呢，为了目的不择手段。」"
    hide cel_t10a with dissolve
    show cel_t12 at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「哼，你想说什么就说什么吧。"
    y1 "再说了不乱用一下还要职权有什么用？」"
    hide cel_t12 with dissolve
    show koha_t03b at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「啊，刚才你的发言有问题啊ciel。"
    k1 "对待工作要正确确干干净净，可不能表里不如一啊。」"
    hide ark_t06 with dissolve
    show aki_t16b at center with dissolve:
      xalign 1.2
    i "「是我幻听吧？"
    i "刚才，我好像听到和这句话最不相符的人"
    i "说了这句话。」"
    hide koha_t03b with dissolve
    hide aki_t16b with dissolve
    window hide
    scene ima_10 with blinds
    scene bg_59 with blinds
    show koha_t02b at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    k1 "「啊，我也有想问的问题，可以问吗？」"
    show aki_t04b at center with dissolve:
      xalign 1.2
    i "「请问吧。"
    i "这样的话干脆别站着了搬张凳子来怎么样？」"
    k1 "「不用不用，我和翡翠说到底只不过是在偷听的普通服务生而已」"
    hide koha_t02b with dissolve
    show his_t04 at center with dissolve:
        linear 0.5 xalign -0.1
    k2 "「…………………（刷）」"
    hide aki_t04b with dissolve
    show ark_t01a at center with dissolve:
      xalign 1.2
    m1 "「咦？　"
    m1 "要坐在我的旁边么？」"
    k2 "「……………………」"
    k2 "（点头）"
    hide ark_t01a with dissolve
    show koha_t16 at center with dissolve:
      xalign 1.2
    k1 "「啊，翡翠酱好过分！"
    k1 "我们俩不是明明说好了"
    k1 "这次好好服侍秋叶小姐的吗？"
    k1 "你居然背叛了！」"
    hide his_t04 with dissolve
    show aki_t18b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「……琥珀。"
    i "………………"
    i "关于冬comic体验版的组合。」"
    hide koha_t16 with dissolve
    show koha_t14 at center with dissolve:
      xalign 1.2
    k1 "「诶――――？」"
    i "「我说，冬comic体验版的组合。」"
    hide koha_t14 with dissolve
    show koha_t11 at center with dissolve:
      xalign 1.2
    k1 "「啊，唔―――――秋叶小姐，难道说……你看到了？」"
    hide aki_t18b with dissolve
    show aki_t04b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「放心吧。"
    i "Arcueid和ciel还没有看到呢。"
    i "嘛，琥珀如果表现好的话我也可以向Arcueid和前辈保密的？」"
    hide koha_t11 with dissolve
    show koha_t12 at center with dissolve:
      xalign 1.2
    k1 "「哈唔――――连那些都看到了呢……呜呜，我发誓之后会更加忠诚的。」"
    hide aki_t04b with dissolve
    show aki_t28 at center with dissolve:
        linear 0.5 xalign -0.1
    i "「你明白就好。"
    i "仆人就像个仆人，去扫扫窗户外的庭院"
    i "什么的就好了。"
    hide aki_t28 with dissolve
    show aki_t04b at center with dissolve:
        linear 0.5 xalign -0.1
    i "――――那么，你的疑问是什么呢？」"
    hide koha_t12 with dissolve
    show koha_t03b at center with dissolve:
      xalign 1.2
    k1 "「嗯。"
    k1 "是Arcueid和志贵关系很好的时候的事。"
    k1 "不是有5个死者来了吗？"
    k1 "那之后，究竟怎么样了呢？"
    k1 "虽然是Arcueid线第十天的事情。」"
    hide aki_t04b with dissolve
    show ark_t03 at center with dissolve:
        linear 0.5 xalign -0.1
    m1 "「诶？"
    m1 "咦，本篇里没有好好说明吗？」"
    hide koha_t03b with dissolve
    show his_t01 at center with dissolve:
      xalign 1.2
    k2 "「是的，没有。」"
    hide ark_t03 with dissolve
    show ark_t09 at center with dissolve:
        linear 0.5 xalign -0.1
    m1 "「这样么。"
    m1 "……嘛，过去的事就让它过去吧。"
    m1 "你说呢,ciel？」"
    hide his_t01 with dissolve
    show cel_t09 at center with dissolve:
      xalign 1.3
    y1 "「---------唔。"
    y1 "没关系，这又没什么。"
    y1 "反正我是很方便的万事屋啦。"
    y1 "嗯，事到如今再说点黑历史反而相当于表扬你呢。」"
    k2 "「……？"
    k2 "咦，这是ciel干的吗？」"
    hide ark_t09 with dissolve
    show ark_t09 at center with dissolve:
        linear 0.5 xalign -0.1
    m1 "「是啊。"
    m1 "第九天我一下子击溃死者后把他们的身体"
    m1 "保存了下来，在路灯上面用线控制。"
    m1 "巫术什么的对于你这个Ｒｏａ的女儿来说应该是相当简单呢」"
    hide cel_t09 with dissolve
    show cel_t12 at center with dissolve:
      xalign 1.3
    y1 "「……虽然不觉得简单，嘛，你大概对了百分之70吧。」"
    hide ark_t09 with dissolve
    show his_t23 at center with dissolve:
        linear 0.5 xalign -0.1
    k2 "「啊……说起来，那个Ｒｏａ称呼ciel为女儿，是这样来着……」"
    hide cel_t12 with dissolve
    show cel_t07a at center with dissolve:
      xalign 1.2
    y1 "「……那个的话，被选作Ｒｏａ的转生体的人们"
    y1 "是和Ｒｏａ没有仅仅没有血缘关系的子孙，也就是孩子了。"
    y1 "罗亚好像特别特别中意我，比起其他的转生体更加依恋我呢」"
    hide cel_t07a with dissolve
    show aki_t08b at center with dissolve:
      xalign 1.2
    i "「……这样啊。"
    i "前辈也有一段黑历史呢。」"
    hide his_t23 with dissolve
    hide aki_t08b with dissolve
    show koha_t15 at center with dissolve:
      xalign 1.2
    k1 "「啊，那个不错呢！"
    k1 "下次的番外篇就用那个吧。"
    k1 "巴黎的偏僻乡村被支配的女吸血鬼的倦怠和淫乱的日子！"
    k1 "掉入欲望的无底洞的少女的命运―"
    k1 "---下期月姬2，我不相信爱情ーーー！"
    k1 "这种怎么样！"
    k1 "吖，ciel好厉害！」"
    hide koha_t15 with dissolve
    show cel_t06a at center with dissolve:
      xalign 1.2
    y1 "「――――就，就算搞错的情况下也不可能有那种番外篇的！"
    y1 "祭典光盘上收录的10个番外篇，已经定下来了！」"

    show koha_t16 at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「切，没劲。」"
    hide cel_t06a with dissolve
    show his_t05 at center with dissolve:
      xalign 1.2
    k2 "「没劲。」"
    window hide
    scene ima_10 with blinds
    scene bg_59 with blinds
    show aki_t16b at center with dissolve:
        linear 0.5 xalign -0.1
    window show
####################################################################
    i "「接着。"
    i "这样的话虽然所有人的疑问都解决了，不觉得哪里有些不足吗？"
    i "Arcueid，其他还有什么漏掉的吗？」"
    show ark_t01a at center with dissolve:
      xalign 1.2
    m1 "「我想想，就比如说现在的状态。"
    m1 "虽然说这场景"
    m1 "是接在故事的后面的时间轴上的，那么这是谁的故事呢。"
    m1 "我也在，ciel也在，妹妹和女仆也在，我想是我或者ciel的结局吧。"
    hide aki_t16b with dissolve
    show aki_t01b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「……也是呢。"
    i "虽然不情愿这么说，我和翡翠他们的结局"
    i "的话，可不存在这么理想的“之后”。」"
    hide ark_t01a with dissolve
    hide aki_t01b with dissolve
    show cel_t03 at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「这也不是我的结局。"
    y1 "应该是Arcueid的goodend之后的事吧。"
    y1 "但是稍稍有些不同，我，Arcueid，Ｒｏａ和远野君战斗的时候"
    y1 "远野君也手法高明的体验了和秋叶酱，翡翠，琥珀的故事。"
    y1 "虽然重要的核心部分没体验。」"
    i "「……这样的话果然，Arcueid的结局"
    i "是月姬这个故事正式的结局，应该这样理解吧？」"
    hide cel_t03 with dissolve
    show ark_t08 at center with dissolve:
        linear 0.5 xalign -0.1
    m1 "「诶嘿嘿。」"

    show cel_t07a at center with dissolve:
      xalign 1.2
    y1 "「（……不服）嗯。"
    y1 "但是，这是“月姬”这个故事的正式结局。"
    y1 "远野志贵作为主人公他的结局是和秋叶在一起的。"
    y1 "本来的话和我和这边的阿姨吸血鬼是没什么关系的。」"
    hide ark_t08 with dissolve
    show aki_t11b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「……也就是说我或者翡翠，"
    i "琥珀之中的一个人的结局可能成为正式的结局吗……」"
    hide cel_t07a with dissolve
    show koha_t08 at center with dissolve:
      xalign 1.2
    k1 "「………………」"
    hide aki_t11b with dissolve
    show his_t01 at center with dissolve:
        linear 0.5 xalign -0.1
    k2 "「………………」"
    window hide
    pause
    hide koha_t08 with dissolve
    hide his_t01 with dissolve
    show ark_t01b at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    m1 "「……等等ciel。"
    m1 "你们3个，怎么感觉在沉默着相互瞪视。]"
    show cel_t04 at center with dissolve:
      xalign 1.2
    y1 "「是在观察是该佯攻还是该后手反击呢。"
    y1 "就别打扰他们了。"
    window hide
    scene ima_10 with blinds
    scene bg_59 with blinds
    show stk_t01 with blinds
    window show
    wy1 "「――――――来了，来了来了来了！」"
    window hide
    hide stk_t01 with fade
    show ark_t11 at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    m1 "「啊，是五月啊」"
    show stk_t01 at center with dissolve:
      xalign 1.2
    wy1 "「那个，我的待遇之后也没变过吗！？"
    wy1 "不管怎么样我觉得那样太过分了，你们说呢！」"
    hide ark_t11 with dissolve
    show cel_t08 at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「……唔嗯……据说弓塚线在构思阶段好像是有的"
    y1 "……剧本担当是这么说的。」"
    hide stk_t01 with dissolve
    show aki_t01b at center with dissolve:
      xalign 1.2
    i "「以“把月姬本篇有意图的无视的事件”为主轴的故事是吗？"
    i "但是很难呢。"
    i "放入祭典光盘的话有太长了。」"
    hide cel_t08 with dissolve
    show koha_t17 at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「这么说着，做完完全版后，又没有做“真·完全版”……」"
    hide aki_t01b with dissolve
    show his_t01 at center with dissolve:
      xalign 1.2
    k2 "「……很对不起，弓塚就只能保持做个配角了。」"
    window hide
    hide koha_t17 with dissolve
    hide his_t01 with dissolve
    show stk_t09 with dissolve
    window show
    wy1 "「过，过分，神啊你太过分了！"
    wy1 "我喜欢上了学校最笨的笨蛋，最后还在前半就死了！"
    wy1 "明明琥珀都有匆忙做出的剧本呢，只有我是这个样子！"
    wy1 "哇唔！」"
    window hide
    hide stk_t09 with fade
    show ark_t11 at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    m1 "「不是挺好么？五月你很幸福啊。"
    m1 "既然吸血鬼是主题而你是唯一很符合吸血鬼的人物啊。"
    m1 "五月，你是隐藏主角哦。」"
    show koha_t15 at center with dissolve:
      xalign 1.2
    k1 "「正因为是吸血鬼，一生都不能暴露到阳光下呢。」"
    hide ark_t11 with dissolve
    show cel_t05 at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「啊，正好。"
    y1 "给你个坐垫。」"
    window hide
    hide koha_t15 with dissolve
    hide cel_t05 with dissolve
    show stk_t12 with dissolve
    window show
    wy1 "「远野君这个大大大大大笨蛋！"
    wy1 "好吧，我一定会在夢現解体这一章里好好报仇的。！！」"
    window hide
    hide stk_t12 with blinds
    pause
    show cel_t07a at center with dissolve:
      xalign 1.2
    window show
    y1 "「弓塚离开了房间。"
    y1 "……对了，说到弓塚的话"
    y1 "秋叶。"
    y1 "歌月十夜，你知道了？」"
    show aki_t10b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「…………………」"
    hide cel_t07a with dissolve
    show cel_t08 at center with dissolve:
      xalign 1.2
    y1"「“那么，跟着我吧”这样。"
    y1"远野君对于年龄比他小的"
    y1"孩子（莲）要温柔三倍呢。」"
    hide cel_t08 with dissolve
    hide aki_t10b with dissolve
    show koha_t15 at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「反过来利用这一点采取行动吗！」"
    show aki_t05b at center with dissolve:
      xalign 1.2
    i "「……嘛，怎样都无所谓了。"
    i "我重新认识到了无意识的"
    i "善意就是罪恶。」"
    hide koha_t15 with dissolve
    show cel_t08 at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「嗯，完全同意。"
    y1 "这次远野君这回犯了相当重的罪了。"
    y1 "弓塚也肯定受不了他了。」"
    i "「嗯。"
    i "……真是的，也不分清楚对象就采取那种态度"
    i "一定是个纯真的孩子呢。"
    hide aki_t05b with dissolve
    show aki_t28 at center with dissolve:
      xalign 1.2
    i "……果然不把哥哥关到地下的禁闭室里"
    i "好好的反省一次不行呢………哼哼哼」"
    hide cel_t08 with dissolve
    hide aki_t28 with dissolve
    show his_t07 at center with dissolve:
      xalign 1.2
    k2 "「啊，秋叶小姐，请不要低声念叨那种令人害怕的东西」"
    show cel_t09 at center with dissolve:
        linear 0.5 xalign -0.1
    y1 "「那个，……秋叶，你不会是被什么附体了吧"
    y1 "感觉上，你后面渐渐出现了一个黑女巫……」"
    hide his_t07 with dissolve
    show koha_t03b at center with dissolve:
      xalign 1.2
    k1 "「不是不是，没有那回事啊。"
    k1 "秋叶小姐已经完全痊愈了。"
    k1 "这毫无问题肯定是秋叶小姐自己的性格啦。」"
    hide cel_t09 with dissolve
    show his_t17 at center with dissolve:
        linear 0.5 xalign -0.1
    k2 "「槙久大人的二重人格，遗传给了秋叶小姐……」"
    window hide
    scene ima_10 with blinds
    scene bg_59 with blinds
    show aki_t04b at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    i "「关于兴趣的话题。」"
    show ark_t06 at center with dissolve:
      xalign 1.2
    m1 "「好突然啊。」"
    hide aki_t04b with dissolve
    show aki_t08b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「是的。"
    i "我不说出来的话谁都不会说的吧？"
    i "姑且到了这里就问问这个吧。大家能说一首自己喜欢的歌吗？"
    i "但是限定日本音乐。"
    i "什么西洋音乐什么亚马逊部落音乐@"
    i "什么福音歌是禁止的。」"
    window hide
    hide ark_t06 with dissolve
    hide aki_t08b with dissolve
    show ark_t08 with dissolve
    window show
    m1 "「歌？"
    m1 "说到歌的话，应该是Nav Katze的crazy dream。」"
    hide ark_t08 with dissolve
    show cel_t08 with dissolve
    y1 "「……那个，地下室的旋律」"
    hide cel_t08 with dissolve
    show his_t02 with dissolve
    k2 "「我非常喜欢SOFT BALLET大人的parade。」"
    hide his_t02 with dissolve
    show koha_t03b with dissolve
    k1 "「喜欢cocco的柔和的忧伤的曲子。」"
    hide koha_t03b with dissolve
    show aki_t04b with dissolve
    i "「最近的话，我喜欢Swinging Popsicle的铁砂塔。」"
    window hide
    hide aki_t04b with dissolve
    show stk_t03 with blinds
    window show
    wy1 "「那个！"
    wy1 "我的话最喜欢文学风的原田知世的歌！」"
    window hide
    hide stk_t03 with blinds
    show cel_t11 at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    y1 "「唔哇，翡翠喜欢parade吗！"
    y1 "真好真好，SOFT BALLET真不错呢！"
    y1 "跟着被称作世界上最强的heavy voice辽先生的声音大声唱的话，"
    y1 "就像在教会的正中听赞美歌一样，给人一种那样的感觉！」"
    show his_t20 at center with dissolve:
      xalign 1.2
    k2 "「…………………………」"
    hide cel_t11
    show aki_t16b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「……说到parade……难道说，是那个？」"
    hide his_t20 with dissolve
    show koha_t11 at center with dissolve:
      xalign 1.2
    k1 "「是呢。"
    k1 "翡翠酱，每天早晨陶醉在那首曲子中醒来。"
    k1 "我有的时候在担心翡翠其实思维方式相当不得了呢。」"
    window hide
    scene ima_10 with blinds
    scene bg_59 with blinds
    show aki_t04b with dissolve
    window show
    i "「……嘛，似乎有很多问题但是每个人的问题都解决了吧？"
    i "接着，那么――――首曲子好像要作为每个人印象歌呢。」"
    hide aki_t04b with fade
    y1 "「诶诶ーーーーーーーーーーーーーーー！？」"
    show cel_t10a at center with dissolve:
      xalign 1.2
    y1 "「稍，稍微等一下，从没听说过这种事情！」"
    show aki_t04b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「咦，前辈。"
    i "有什么不方便吗？」"
    y1 "「肯，肯定有啊！"
    y1 "我的印象歌为什么是地下室的旋律啊！？"
    y1 "不是仅仅是'这里是哪里啊，另外我是谁'之类的歌词"
    y1 "拼接成的歌吗！」"
    hide aki_t04b with dissolve
    show aki_t08b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「真是好曲子呢，地下室的旋律。"
    i "有一种说法是，当時还是学生的剧本担当"
    i "在废墟一样的医院的等候室里看着歌词卡，"
    i "吓得半年没敢打开CD盒，到达了有这样的传说的程度呢。」"
    y1 "「啊，啊呜呜呜呜呜呜！"
    y1 "再这么说，再怎么说把它作为印象歌什么的，"
    y1 "那样不就像恐怖电影一样了吗！」"
    hide aki_t08b with dissolve
    show ark_t08  at center with dissolve:
        linear 0.5 xalign -0.1
    m1 "「“逃吧逃吧，逃吧逃吧，帮你开门吧？”」"
    hide cel_t10a with dissolve
    show cel_t06a at center with dissolve:
      xalign 1.2
    y1 "「就是这个！"
    y1 "不要接着唱了！」"
    m1 "「“大白天，一边颤抖？　哈"
    hide ark_t08 with dissolve
    show ark_t20 at center with dissolve:
        linear 0.5 xalign -0.1
    m1　"「哈ーーー！”」"
    hide ark_t20 with dissolve
    hide cel_t06a with dissolve
    y1 "「呀ーーーー！"
    y1 "神啊，这样太过分了ーーーー！」"
    window hide
    scene ima_10 with blinds
    scene bg_59 with blinds
    show ark_t01a at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    m1 "「啊，好痛快。"
    m1 "但是Nav Katze的crazy dream是女子组合"
    m1 "以吸血鬼为主题的可爱的歌哦。"
    m1 "因为剧本担当说这就像真正的月姬（Arcueid ）的印象歌"
    m1 "有兴趣的人试着听听看可能也没什么问题。」"
    show his_t01 at center with dissolve:
      xalign 1.2
    k2 "「OUT，这种小唱片。"
    k2 "两千元左右。"
    k2 "……说起来Arcueid，这种传教行为也能被允许？」"
    hide ark_t01a with dissolve
    show ark_t09 at center with dissolve:
        linear 0.5 xalign -0.1
    m1 "「okok，没问题！」"
    window hide
    scene ima_10 with blinds
    scene bg_59 with blinds
    show ark_t01a at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    m1 "「啊。"
    m1 "怎么觉得外面变暗了。」"
    show cel_t01a at center with dissolve:
      xalign 1.2
    y1 "「也是呢。"
    y1 "差不多也到了该结束的时候了吧。」"
    hide ark_t01a with dissolve
    show aki_t01b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「啊，是吗？"
    i "但是还有一个不得不问的事情。"
    i "那么真的是最后了，对于你们来说月姬本篇“最坏的人”是谁？」"
    window hide
    hide cel_t01a  with dissolve
    hide aki_t01b  with dissolve
    window show
    "「……………………………………」"
    "「……………………………………」"
    "「……………………………………」"
    "「……………………………………」"
    "「……………………………………」"
    show ark_t03 at center with dissolve:
        linear 0.5 xalign -0.1
    m1 "「ciel，没事你先说吧」"
    show cel_t12 at center with dissolve:
      xalign 1.2
    y1 "「你先请。"
    y1 "我在你后面说就行了。」"
    hide ark_t03 with dissolve
    show aki_t01b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「琥珀？"
    i "翡翠也不用先说吗？」"
    hide cel_t12 with dissolve
    show koha_t12 at center with dissolve:
      xalign 1.2
    k1 "「啊哈，感觉第一个说的话有些不好意思呢。」"
    hide aki_t01b with dissolve
    show his_t20 at center with dissolve:
        linear 0.5 xalign -0.1
    k2 "「…………………（咽口水声）」"
    window hide
    hide his_t20 with dissolve
    hide koha_t12 with dissolve
    show ark_t01a with dissolve
    window show
    m1 "「没办法呢。"
    m1 "这样的话大家一起说吧。"
    m1 "预ー备，」"
    hide ark_t01a with fade
    show ark_t03 with dissolve
    m1 "「嗯，可能是志贵。」"
    hide ark_t03 with fade
    show cel_t01a with dissolve
    y1 "「当然是远野君了。」"
    hide cel_t01a with fade
    show aki_t21b with dissolve
    i "「肯定是哥哥吧。」"
    hide aki_t21b with fade
    show his_t17 with dissolve
    k2 "「……真的很对不起，志贵少爷」"
    hide his_t17 with fade
    show koha_t15 with dissolve
    k1 "「只能想到志贵呢。」"
    window hide
    hide koha_t15
    show ark_t12 at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    m1 "「……咦。"
    m1 "大家都讨厌志贵吗？」"
    show cel_t02 at center with dissolve:
      xalign 1.2
    y1 "「唔嗯，虽然说不上讨厌。但是说到坏的话…"
    y1 "…爱之深恨之切，这种理由吧。」"
    hide ark_t12 with dissolve
    show aki_t16b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「我只是单纯的觉得哥哥是个坏人。"
    i "因为都是因为哥哥我才一直很痛苦。"
    i "也太不挑剔了。"
    i "哥哥是个坏人。」"
    hide cel_t02 with dissolve
    show his_t22 at center with dissolve:
      xalign 1.2
    k2 "「………………………」"
    hide aki_t16b with dissolve
    show koha_t03b at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「也是呢。"
    k1 "而且因为志贵老是喜欢H，这样结束之后不是非常累么？"
    k1 "我在想志贵怎么这个样子身体还这么好？」"
    hide his_t22 with dissolve
    show cel_t11 at center with dissolve:
      xalign 1.2
    y1 "「……赞成。"
    y1 "远野君，到底有多能干啊？」"
    hide koha_t03b with dissolve
    show ark_t14 at center with dissolve:
        linear 0.5 xalign -0.1
    m1 "「是这样吗……？"
    m1 "除了志贵以外，我不知道其他人"
    m1 "H的频率，不是特别清楚……」"
    hide cel_t11 with dissolve
    show his_t21 at center with dissolve:
      xalign 1.2
    k2 "「……………………（右边的好像也一样）」"
    hide ark_t14 with dissolve
    show aki_t16b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「……嘛，虽然和听到的比起来确实觉得相当厉害……"
    hide aki_t16b with dissolve
    show aki_t07b at center with dissolve:
        linear 0.5 xalign -0.1
    i "啊啊真是的，为什么会变着这种话题啊！"
    i "我们应该讲讲哥哥不成熟的地方！」"
    hide his_t21 with dissolve




    show cel_t12 at center with dissolve:
      xalign 1.2
    y1 "「嗯ー，这不也是远野君相当不成熟的地方吗？」"
    hide aki_t07b with dissolve
    show ark_t08 at center with dissolve:
        linear 0.5 xalign -0.1
    m1 "「嗯。"
    m1 "我也挺感兴趣的。"
    m1 "妹妹也别顽固了怎么样？"
    m1 "反正这个场合不拘身份的。」"
    hide ark_t08 with dissolve
    show aki_t16b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「―――――嘛，也是呢。"
    i "那个，就算是我也挺感兴趣的"
    i "嘛……虽然没忘坏的方面想。」"
    hide cel_t12 with dissolve
    show his_t13 at center with dissolve:
      xalign 1.2
    k2 "「怎么这样……秋叶小姐，在志贵少爷不在的场合里讨论这种事太过分了。」"
    hide his_t13 with dissolve
    show koha_t15 at center with dissolve:
      xalign 1.2
    k1 "「也是呢ー。"
    k1 "志贵不在这里挺遗憾的。"
    k1 "如果志贵在的话一定会很欢乐的。"
    k1 "你们看，不是有用剑刺钻入木桶里的乌贼的游戏吗？"
    k1 "和那个差不多从四面八方直直的刺向中间，"
    k1 "能让志貴很困扰呢。啊，真是遗憾呢。"
    k1 "志贵在的话会很有趣呢。」"
    hide aki_t16b with dissolve
    show aki_t24 at center with dissolve:
        linear 0.5 xalign -0.1
    i "「唔……。"
    hide aki_t24 with dissolve
    show aki_t25 at center with dissolve:
        linear 0.5 xalign -0.1
    i "琥，琥珀，这个，那个……你想出很厉害的东西了呢……」"
    window hide
    scene ima_10 with blinds
    scene bg_59 with blinds
    play sound "audio/se02.ogg"
    show ark_t03 at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    m1 "「嗯？"
    m1 "是什么，这个钟的声音。」"
    show koha_t02b at center with dissolve:
      xalign 1.2
    k1 "「啊，到了打烊的时间了。"
    k1 "大家今天真是好好的聊了一场呢ー。」"
    hide ark_t03 with dissolve
    show aki_t04b at center with dissolve:
        linear 0.5 xalign -0.1
    i "「……是呢。"
    i "一开始虽然还在想会变成怎样呢，"
    i "这样较过劲之后敌意也消失了，谈的很开心呢。」"
    hide koha_t02b with dissolve
    show cel_t04 at center with dissolve:
      xalign 1.2
    y1 "「我们三个人的话相互平衡的不错呢。"
    y1 "我今天也很开心。」"
    hide aki_t04b with dissolve
    show koha_t03b at center with dissolve:
        linear 0.5 xalign -0.1
    k1 "「呼呼，虽然今天也是相当危险的平衡呢」"
    hide cel_t04 with dissolve
    show his_t04 at center with dissolve:
      xalign 1.2
    k2 "「……姐姐，这是多余的话……」"
    window hide
    hide koha_t03b with dissolve
    hide his_t04 with dissolve
    show aki_t08b with dissolve
    window show
    i "「那么我先回去了。"
    i "后面的收拾就拜托你们两个二人了。」"
    window hide
    hide aki_t08b with blinds
    pause
    show cel_t04 with dissolve
    window show
    y1 "「我也准备走了呢。"
    y1 "差不多到巡逻的时间了。」"
    window hide
    hide cel_t04 with blinds
    pause
    show ark_t03 with dissolve
    window show
    y1 "「我也该走了呢。"
    y1 "感觉，过了相当长的时间了呢。」"
    window hide
    hide ark_t03 with dissolve
    pause
    show koha_t03b at center with dissolve:
        linear 0.5 xalign -0.1
    window show
    k1 "「好的。"
    k1 "Arcueid也路上小心。」"
    show ark_t01a at center with dissolve:
      xalign 1.2
    m1 "「那么再见咯。"
    m1 "啊，说起来我和翡翠今晚会见面吗？」"
    hide koha_t03b with dissolve
    show his_t17 at left with dissolve
    k2 "「……Arcueid大人。"
    k2 "那个，请不要频繁的潜伏进志贵"
    k2 "大人的房间里。」"
    m1 "「知道了知道了，开玩笑的。"
    m1 "那么两位再见！」"
    window hide
    hide ark_t01a with blinds
    pause
    show koha_t15 at center with dissolve:
      xalign 1.2
    window show
    k1 "「好的，那么再见了，来年再见！」"
    window hide
    hide his_t17 with blinds
    hide koha_t15 with blinds
    stop music
    stop sound
    pause
    scene bg_59 with dissolve
    scene fin with blinds
    pause
    hide screen quick with  dissolve
    return

label yuecha2:
    show screen quick with  dissolve
    scene black with  dissolve

    "testyuecha"
    "这是测试"
    "testyuecha"
    "这是测试"
    "testyuecha"
    "这是测试"
    "此故事已经结束了哦"
    window hide
    hide screen quick with  dissolve
    stop music
    return








































label mogu:
    show screen quick with  dissolve
    scene black with  dissolve
    scene black
    "这篇故事是在（月姬）半月版完成时写的东西"
    "因为设定上和本篇有较大不同，请完全当成外传来享受。"
    "另外，'为了享受这篇故事而浪费掉的时间和精力应该归还'"
    "这种意见是不予采纳的。"
    "那么请开始享受着构思零分，制作六十分的番外篇。"
    show kemo_t01 with  dissolve
    "三。"
    scene black
    show kemo_t04 with  dissolve
    "二。"
    scene black
    show kemo_t05 with  dissolve
    "一。"
    window hide
    show matu with  dissolve
    "要开始了哦。"
    window hide
    play  music "music/tmcd-0101_02.ogg" fadein 1.0 fadeout 2.0
    scene bg_40a with dissolve
    "-------被早晨的光线照醒。"
    a"「嗯………」"
    "怎么回事？不太寻常的，带着不好的预感睁开了眼睛。"
    "虽然可能是心理作用，但我觉得身体有点发热"
    "现在也是由于贫血而到了晕眩的程度。"
    a"「……尽管如此，这个房间的早晨还是一成不变呢。」"
    "把绝对不能说的东西一不小心说了出来。"
    "虽然这里每次都用同一个模式很对不起大家"
    "但因为除此之外早上能说的东西也没了"
    "所以希望大家能放过我。"
    a"「……真是没办法啊。虽然平时能说的东西倒是很多」"
    a"「但也不会专门去准备关于早晨阳光的东西。」"
    a "「只有一个套路的话不管怎么用语言修饰还是会有局限的---」"
    "就算是这样也要做点什么才算是主角吧，秋叶一定会这样生气的嘟哝。"
    "-------接着。"
    scene black with dissolve
    stop music
    play  music "music/tmcd-0101_03.ogg" fadein 1.0 fadeout 2.0
    "卡夏，卡夏，卡夏"
    "伴随着这样的声音,窗户上的百叶窗一下子掉了下来。"
    a"「-------怎么回事！」"
    "房间里一下子被黑暗包围。"
    "用手在黑暗中推了一下但窗户纹丝不动。"
    "……有种房间一下子变成了牢房的感觉。"
    "怎么一回事？。难道说这是以防犯罪的设备？"
    "……要说的话。不管怎么说，如果是秋叶的话很可能做这种程度的准备。"
    "而且那也不是防止犯罪的设施而是作为对Arcueid用设备。"
    "然后不用说，大肆起哄的一定是琥珀了。"
    a"「……但是为什么？早晨起来状态就不好，接下来又遇到这样的状况……」"
    "算了，对我来说算是在希望的地方结束了之前的话题。"
    show his_t01 with dissolve
    k2 "「不对。我认为那只是志贵少爷缺乏诗一样的感性」"
    hide his_t01 with dissolve
    scene black
    a"「翡、翡翠-------！」"
    show his_t01 with dissolve
    k2 "「在。早上好志贵少爷。」"
    hide his_t01 with dissolve
    a"「嗯……哦，早上好翡翠。那个，今天早上又是相当厉害的登场呢。」"
    hide his_t01 with dissolve
    show his_t08 at center with dissolve
    k2 "「……………………」"
    show his_t08 at center:
        linear 1.0 xalign 2.0
    pause
    scene black with dissolve
    "啊，逃走了。"
    a"「等等翡翠！衣服，我要换的衣服呢？」"
    "虽然都大喊了但是还是没有回答。"
    "翡翠以过山车的速度，嗖的一下子从房间里出去了"
    scene bg_40a with dissolve
    "啊，回到原点了。"
    stop music
    play  music "music/tmcd-0101_03.ogg"
    a"「……这下糟了。以前一旦穿着睡衣走到走廊里去的话」"
    a"「秋叶那家伙就会抱怨个不停的……」"
    "……嗯。"
    "这样的话在换的衣服送过来之前就睡吧。"
    "反正现在是暑假，没什么特别的、不得不早起的理由。"
    a"「！？」"
    "这，这，这……！"
    "这，这是怎么回事啊 -------"
    show koha_t06 with dissolve
    k1 "「啊拉，志贵少爷请快点起来出去哦。现在是扫除的时间咯。」"
    hide koha_t06 with dissolve
    "像这样。"
    "摆弄着扫帚，琥珀进入了房间。"
    "……总觉得，刚才的强震像是琥珀扫除时的余波。"
    show koha_t04 with dissolve
    k1 "「真是的，因为是假期就邋邋遢遢是不行的哦，志贵少爷！」"
    k1 "「早饭已经准备好了，请快点到餐厅去吧！」"
    hide koha_t04 with dissolve
    a"「……虽然我也想这么做，但是我没有换的衣服。」"
    a"「而且感觉翡翠从早上开始就很奇怪，把我叫醒之后就一下子跑掉了。」"
    show koha_t05 with dissolve
    k1 "「哦，是这个样子吗？」"
    k1 "「小翡翠，我还在想她什么时候会忍不下去呢，终于爆发了吗。」"
    hide koha_t05 with dissolve
    a"「……哈。爆发？」"
    show koha_t02 with dissolve
    k1 "「嗯。一定是因为昨天尝了志贵的饭的缘故。」"
    k1 "「因为志贵的饭里一直混着新的药,」"
    k1 "「昨晚在我不注意的时候，小翡翠就尝了一下。」"
    hide koha_t02 with dissolve
    a"「……哈？琥珀，你还没把往别人饭里混药的癖好改掉吗？」"
    show koha_t02 with dissolve
    k1 "「嗯，虽然我自己也明白，」"
    k1 "「但一不小心就把药混进去了呢。」"
    k1 "「虽然说志贵的耐药性很好但没什么效果也挺无聊的。」"
    hide koha_t02 with dissolve
    "琥珀还是那么天然。"
    show koha_t06 with dissolve
    k1 "「呀勒呀勒，要开始扫除了。」"
    k1 "「请到外面去。一个小时左右就结束了，在那之前请去吃饭吧。」"
    hide koha_t06 with dissolve
    "'快点快点'，琥珀一边这么说着一边拿扫帚来扎我的脸。"
    show koha_t06 with dissolve
    k1  "「-------」"
    hide koha_t06 with dissolve
    "受到说不出来的不好的预感的折磨，我离开了房间。"
    scene black with dissolve
########################################################
    scene bg_34a with dissolve
    "和往常一样，秋叶在起居室里。"
    show aki_t04a with dissolve
    h1"「早上好，哥哥。早饭的话已经准备好了」"
    hide aki_t04a with dissolve
    a"「嗯，知道了。总之我先去吃早饭了。」"
    show aki_t03a with dissolve
    h1"「真是的，要我说几遍你才明白」"
    h1"「哥哥身为远野家的长男，请稍微注意一下你的遣词-------」"
    hide aki_t03a with dissolve
    "-------这样。"
    "秋叶的训斥被咚塔塔塔的清脆的声音盖住。"
    "咚塔塔塔塔塔塔塔。"
    "似乎是什么人的脚步声，伴随着惊人的气势冲进了起居室。"
    a"「秋叶！」"
    a"「-------什」"
    show nero_t03 at left with dissolve
    hide nero_t03 at left with dissolve
    "出现的是穿着黑色大衣的神秘男子。"
    hide nero_t03 at left with dissolve
    show aki_t08a at right with dissolve
    #图像重叠################################
    h1"「什么啊，我还以为是谁呢,这不是叔父大人吗。」"
    h1"「发生什么事了吗？露出那种动摇的表情。」"
    hide aki_t08a at right with dissolve
    "-------噗！"
    a"「稍微等一下秋叶！ 叔父大人到底是谁啊！」"
    show aki_t04a at right with dissolve
    h1"「真是的哥哥，叔父大人就是叔父大人啊」"
    h1"「对不起，涅吕叔父大人。哥哥有的时候处在记忆丧失的状态。」"
    hide aki_t04a at right with dissolve
########################################
    show nero_t02c at left with dissolve
    j1"「嗯，没关系。因为这种琐事与我无关。」"
    hide nero_t02c at left with dissolve
    show nero_t03 at left with dissolve
    j1"「说起来秋叶。你知道我从昨晚开始期待布丁在哪吗？」"
    j1"「从不二家买的，一个７００日元的新式布丁。」"
    hide nero_t03 at left with dissolve
    show aki_t03b at left with dissolve
    h1"「哦。那个的话昨天晚上，哥哥就像熊猫吃竹叶一样刷刷的吃掉了哦。」"
    hide aki_t03b at left with dissolve
    a"「-------纳尼！」"
    a"「开，开，开什么玩笑秋叶！」"
    a"「我才不记得有那种事呢，首先比起西洋甜点来说我明明更喜欢东洋甜点……！」"
    show nero_t04 at left with dissolve
    play  music "music/tmcd-0101_04.ogg"
    j1"「哼哼哼哼哼哼哼哼哼！！！！！小子。」"
    j1"「我要揍你６６６回！」"
    hide nero_t04 at left with dissolve
    a"「啊啊啊啊啊，冤枉啊-------！」"
    scene black with dissolve
    stop music
#####################################
    scene bg_53 with dissolve
    play  music "music/tmcd-0101_03.ogg"
    "…………………………哈，哈，哈。"
    "总算是逃出来了。"
    "虽然逃出来了是很不错……"
    show roa_t03a at left with dissolve
    h "「-------你看见了！？」"
    hide roa_t03a at left with dissolve
    "……为什么"
    "一个已经奇怪到无法再奇怪的视觉系男子"
    "非法侵入到了屋子的庭院里。"
    a"「……喂。你是小偷吧？」"
    show roa_t03a at left with dissolve
    h "「你看见了！？看见了吧！」"
    hide roa_t03a at left with dissolve
    "……真是的呢。"
    "为什么会这样？偏偏在今天早上一个劲的碰到糟糕的事情。"
    a"「那么，看见的话指什么？」"
    show roa_t03a at left with dissolve
    l1"「你你你你！竟敢偷看我早晨的最重要的广播体操！」"
    l1"「你总是，总是妨碍我！」"
    l1"「不要比我还早到会场啊！不要比我先做完早操啊！」"
    l1"「不要比我收集更多的纪念章啊！」"
    l1"「啊真是的，不要随便就偷看我的头啊！」"
    hide roa_t03a at left with dissolve
    a"「…………………………」"
    "……干的不错啊。"
    "基本上对这种展开是没兴趣的，我啊。"
    a"「没偷看。」"
    a"「我没有偷看啊，」"
    a"「所以请你想怎么做体操就怎么做体操。」"
    a"「再见，我回去了。」"
    "请不要再粘着我了。"
    show roa_t04a at left with dissolve
    l1"「什么-------」"
    hide roa_t04a at left with dissolve
    "歪着头相当不满的视觉系男子。"
    "朝向那边。"
    show ark_t08 at left with dissolve
    m1"「你好！我来玩了哟，志贵--」"
    hide ark_t08 at left with dissolve
    "就这样，更加麻烦的家伙出现了。"
    a"「……Arcueid。虽然很不好意思，但现在不是干那种事的时候。」"
    show ark_t11 at left with dissolve
    m1 "「诶---」"
    hide ark_t11 at left with dissolve
    "尽管她露出相当不满的神情，总之现在我想一个人呆着。"
    a"「……很闲的话就去和她玩玩吧。你们不是难得的合得来吗？」"
    show ark_t11 at center with dissolve:
        linear 1.0 xalign 1.8
    show roa_t04a at center with dissolve:
        linear 1.0 xalign -0.8
    ##图像重叠###############################
    l1"「哎---」"
    hide roa_t04a with dissolve
    hide ark_t11  with dissolve
    a"「……感觉挺合得来的，你们俩。」"
    "说着说着，真的觉得晕眩了。"
    "本来站着不动就因为很热感觉不舒服了，这样子一来晕眩的快要死掉了。"
    "你看来了。马上说好的那个要来了。"
    a"「啊真是的，不管是广播体操还是民间舞蹈。」"
    a"「你想来什么就来什么！我回房间了别跟过来啊！」"
    a"「我回房间了别跟过来啊！」"
    show roa_t03a at left with dissolve
    l1"「喔哈哈哈哈，我也去了哦！」"
    hide roa_t03a at left with dissolve
    show ark_t08 at right with dissolve
    m1 "「什么，追上去了？　志贵真是受欢迎呢---。」"
    hide ark_t08 at right with dissolve
    "-------我说。"
    "为什么这个人也好，那个人也好都不听我说的话呢？"
    scene black with dissolve
    scene bg_54a with dissolve
    a"「……哈……哈……哈……」"
    "总之被他们两个人一搅合，我也到了体力的临界值了。"
    "回过头冷静想想的话，我今天从早上开始神智就不太清醒。"
    play music  "music/tmcd-0101_10.ogg"
    show kemo_t05 with dissolve
    n1"「终于注意到那个事实了哦？少年。」"
    hide kemo_t05 with dissolve
    a"「哇，你是什么东西！」"
    show kemo_t05 with dissolve
    n1"「这个哦？这是会说话的马。」"
    n1"「在一开始出现的那个谜一样的东西哦」"
    hide kemo_t05 with dissolve
    a "「……………………什么？」"
    "突然出现的谜样生物，果然说的话我完全搞不懂。"
    a"「那个……鹿神？」"
    show kemo_t05 with dissolve
    n1"「不是鹿神。」"
    hide kemo_t05 with dissolve
    "那个，除了鹿神以外看不出还能是别的什么了。"
    a"「那么，那个鹿神为什么要在别人的庭院里呆着啊？」"
    a"「是来搭救处在什么都不明白的状态的我的吗？」"
    show kemo_t05 with dissolve
    n1"「需要被救的是这边哦，笨蛋！」"
    hide kemo_t05 with dissolve
    "对方反而生气了。"
    "已经什么都搞不清楚了"
    show kemo_t05 with dissolve
    n1"「明明本来就因为夏日祭的准备忙的没时间了不是哦？」"
    n1"「觉得状况奇怪的话，在那时候就快点睁开眼睛哦！」"
    n1"「你这个笨蛋。」"
    hide kemo_t05 with dissolve
    a"「……？那个，这么说的话，这果然是梦吗？」"
    show kemo_t05 with dissolve
    n1"「当然了哦。在术语辞典上写着的哦。」"
    n1"「（术语）梦很方便的东西，这样。」"
    n1"「这种笨蛋一样的故事只有在梦里才能成立吧哦哦。」"
    hide kemo_t05 with dissolve
    "嘛，和我预想的差不多。"
    a"「这样啊。但是我想请教一下为什么会变成这个样子？」"
    show kemo_t05 with dissolve
    n1"「可以说因为你对夏天太期待了哦。」"
    n1"「呵呵呵，尝到了眩目的不合理的万花镜的滋味了哦」"
    n1"「你真是个幸福的家伙哦」"
    hide kemo_t05 with dissolve
    "嘻嘻嘻，这样笑着的鹿神"
    scene black with dissolve
    a"「-------啊」"
    show kemo_t05 with dissolve
    n1"「这样的话要快点回到早上哦。」"
    n1"「怎么样？」"
    n1"「哦---，这一次要为了明天能成功好好努力哦。」"
    hide kemo_t05 with dissolve
    "说着，鹿神转过身去。"
    a"「星期三的实验室！」"
    "真是的，这一次鹿神"
    "一边说着我完全搞不懂的东西，一边鼓励着我。"
    stop music
    a"「什-------么-------」"
    "骨碌骨碌像光棚滚动一样落下去。"
    "骨碌 骨碌。"
    "骨 碌 骨 碌。"
    "骨碌 骨碌。"
    "……呼呼，失去了知觉。"
    "但是说起来，睁开眼睛的话就要回到有一堆事情的早上了。"
    "啊，到什么时候能和XXX（请填入你喜欢的女主角的名字）"
    "一起去烟花大会约会呢？"
    "我………"
    scene white with dissolve
    scene bg_40a with dissolve
    play  music "music/tmcd-0101_02.ogg"
    "-------被早晨的光线照醒。"
    a"「嗯………」"
    "怎么回事？异常地，带着不好的预感睁开了眼睛。"
    "虽然可能是心理作用但我觉得身体有点发热，现在也是"
    "由于贫血而到了晕眩的程度。"
    a"「……啊，不知不觉已经早上了。」"
    "嘛，暑假的话就是这样的东西吧。"
    "也不用上学，每天的感觉差不多也是没有办法的。"
    a"-------接着。"
    "明天就是烟花大会了"
    "今天是去学校呢？还是留在家里呢？-------"
    scene black with  dissolve
    pause
    show fin with  blinds
    pause
    window hide
    pause
    window hide
    hide screen quick with  dissolve
    stop music
    return
label splashscreen:
    show screen my_scr
    $ renpy.movie_cutscene("audio/logo1.webm", loops=0, stop_music=True)
    #$ renpy.movie_cutscene("audio/logo1_psv.mp4", loops=0, stop_music=True)
    hide screen my_scr
    pause
    show gamestart4 with dissolve
    pause
    stop  music
    return
