﻿################################################################################
## 初始化
################################################################################

init offset = -1
define stopall = renpy.music.stop
init:
    $ button = 0
define stopall = renpy.music.stop
################################################################################
## 样式
################################################################################
style default:
    properties gui.text_properties()
    language gui.language
style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False
style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
style gui_text:
    properties gui.text_properties("interface")
style button:
    properties gui.button_properties("button")
style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
style prompt_text is gui_text:
    properties gui.text_properties("prompt")
style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
################################################################################
## 游戏内界面
screen my_scr:
    key "K_RETURN" action Hide("nonexistent_screen")
    key "K_KP_ENTER" action Hide("nonexistent_screen")
    key "K_SPACE" action Hide("nonexistent_screen")
    key "mousedown_4" action Hide("nonexistent_screen")
    key "K_PAGEUP" action Hide("nonexistent_screen")
    key "mousedown_5" action Hide("nonexistent_screen")
    key "mouseup_3" action Hide("nonexistent_screen")
    key "mouseup_1" action Hide("nonexistent_screen")
    # 只允许ESC键跳过视频
    key "K_ESCAPE" action Return("smth")
################################################################################
## 对话界面 ########################################################################
## 对话界面用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
## 此界面必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"
    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')
style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label
style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding
style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
## 输入界面 ########################################################################
## 此界面用于显示 renpy.input。“prompt”参数用于传递文本提示。
## 此界面必须创建一个 id 为“input”的输入可视控件来接受各种输入参数。
screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos
            text prompt style "input_prompt"
            input id "input"
style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")
style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
## 选择界面 ########################################################################
## 此界面用于显示由“menu”语句生成的游戏内选项。参数“items”是一个对象列表，每个对
## 象都有标题和操作字段。
screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action
## 若为 True，菜单内的叙述会使用旁白角色。若为 False，叙述会显示为菜单内的文字说
## 明。
define config.narrator_menu = True
style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text
style choice_vbox:
    xalign 0.5
    ypos 135
    yanchor 0.5
    spacing gui.choice_spacing
style choice_button is default:
    properties gui.button_properties("choice_button")
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
## 游戏内快捷菜单界面 ######################################################################
screen quick(before=stopall):
    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu
    frame:
        style "main_menu_frame"
    hbox:
        spacing 10
        xalign  0.00
        yalign  0.80
        imagebutton idle "gui/quick/game1.png" hover "gui/quick/game2.png"  action ShowMenu("preferences")

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_frame:
    xsize 140
    yfill True
style main_menu_vbox:
    xalign 1.0
    xoffset -10
    xmaximum 400
    yalign 1.0
    yoffset -10
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
style main_menu_title:
    properties gui.text_properties("title")
style main_menu_version:
    properties gui.text_properties("version")
## start菜单界面 ######################################################################
image green ="gui/ui/green.png"
image snow = SnowBlossom("green",count=40,border=10,xspeed=(-2,50),yspeed=(20,30),start=0, fast =True,horizontal=False)
screen start(before=stopall):
    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu
    add "gui/start.png"
    add "snow"
    ## 此空框可使标题菜单变暗。
    frame:
        style "main_menu_frame"
    vbox:
        spacing 10
        xalign  0.85
        yalign  0.55

        imagebutton idle "gui/ui/eyesalliance.png" hover "gui/ui/eyesalliance_hover.png" activate_sound "audio/click.ogg"  action [SetVariable("button",1),Jump("huanshi")]
        imagebutton idle "gui/ui/getcha.png" hover "gui/ui/getcha_hover.png" activate_sound "audio/click.ogg"  action [SetVariable("button",2),Jump("yuecha")]
        imagebutton idle "gui/ui/getcha2.png" hover "gui/ui/getcha2_hover.png" activate_sound "audio/click.ogg"  action [SetVariable("button",3),Jump("yuecha2")]
        imagebutton idle "gui/ui/kinoko.png" hover "gui/ui/kinoko_hover.png" activate_sound "audio/click.ogg" action [SetVariable("button",4),Jump("mogu")]
        imagebutton idle "gui/ui/fanhui.png" hover "gui/ui/fanhui_hover.png" activate_sound "audio/click.ogg" action MainMenu()

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_frame:
    xsize 140
    yfill True
style main_menu_vbox:
    xalign 1.0
    xoffset -10
    xmaximum 400
    yalign 1.0
    yoffset -10
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
style main_menu_title:
    properties gui.text_properties("title")
style main_menu_version:
    properties gui.text_properties("version")
### (1)标题和游戏菜单界面
################################################################################
## 0.壁纸界面 ########################################################################
transform getIn:
    xoffset -40
    yoffset 0
    alpha 0.0
    easein 0.35 xoffset 0 alpha 1.0
default thumb_index = 1
screen wallpaper:
    add Solid("#000")
    add "gui/bizhi.png"
    imagebutton idle "gui/ui/back.png" hover "gui/ui/back_hover.png" xcenter 0.5 ycenter 0.929  activate_sound "audio/click.ogg" action Hide("wallpaper")
    vbox at getIn:
        spacing 200
        xcenter 0.5
        ycenter 0.55
        grid 3 2 xspacing 50 yspacing 30:
             for i in range(thumb_index, thumb_index + 6):
                if i <= 24:
                    imagebutton:
                        idle "images/thumbnail/thumb{}.jpg".format(i)
                        hover "images/thumbnail/thumb{}.jpg".format(i)
                        action Show("wallpaper_fullscreen", bg="images/wallpaper/bg{}.jpg".format(i))
                else:
                    null
    hbox at getIn:
        if thumb_index > 1:
            imagebutton idle "gui/ui/pre.png" hover "gui/ui/pre_hover.png" xcenter 10.5 ycenter 8.72 activate_sound "audio/click.ogg" action SetVariable("thumb_index", thumb_index - 6)
        if thumb_index < 25:
            imagebutton idle "gui/ui/next.png" hover "gui/ui/next_hover.png" xcenter 10.53 ycenter 8.72 activate_sound "audio/click.ogg" action SetVariable("thumb_index", thumb_index + 6)
        else:
            null
screen wallpaper_fullscreen(bg):
    add Solid("#000")
    add bg at getIn
    imagebutton idle "gui/ui/back.png" hover "gui/ui/back_hover.png" xcenter 0.5 ycenter 0.929 activate_sound "audio/click.ogg" action Hide("wallpaper_fullscreen")

## 1.导航界面 ########################################################################
## navigation是一个包含了一些常用按钮和功能的screen，可以被main_menu和game_menu使用use语句来包含，
###这样可以复用界面资源1。navigation不会直接显示给玩家，而是作为main_menu和game_menu的一部分。
screen navigation():
    vbox:
        style_prefix "navigation"
        xpos 8
        yalign 0.5
        spacing 3
        if main_menu:
            textbutton _("开始游戏") activate_sound "audio/click.ogg" action Start()
        else:
            textbutton _("历史") activate_sound "audio/click.ogg" action ShowMenu("history")
            textbutton _("保存") activate_sound "audio/click.ogg" action ShowMenu("save")
            textbutton _("读取游戏") activate_sound "audio/click.ogg" action ShowMenu("load")
            textbutton _("设置") activate_sound "audio/click.ogg" action ShowMenu("preferences")
        if _in_replay:
            textbutton _("结束回放") activate_sound "audio/click.ogg" action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("标题界面") activate_sound "audio/click.ogg" action MainMenu()
            textbutton _("关于") activate_sound "audio/click.ogg" action ShowMenu("about")
        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            ## “帮助”对移动设备来说并非必需或相关。
            textbutton _("帮助") action ShowMenu("help")
        if renpy.variant("pc"):
            ## “退出”按钮在 iOS 上被禁止设置，在安卓和网页上也不是必需的。
            textbutton _("退出") action Quit(confirm=not main_menu)
style navigation_button is gui_button
style navigation_button_text is gui_button_text
style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
# 2.标题菜单界面 ######################################################################
## main_menu是在游戏启动时或者从game_menu中选择回到标题时显示的菜单，可以让玩家开始新游戏，继续旧游戏，设置选项等
#######################################################################################
image green ="gui/ui/green.png"
image snow = SnowBlossom("green",count=40,border=10,xspeed=(-2,50),yspeed=(20,30),start=0, fast =True,horizontal=False)
screen main_menu(before=stopall):
    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu
    add "gui/main_menu.png"
    add "snow"
    ## 此空框可使标题菜单变暗。
    frame:
        style "main_menu_frame"
    vbox:
        spacing 10
        xalign  0.09
        yalign  0.75
        imagebutton idle "gui/ui/start.png" hover "gui/ui/start_hover.png" activate_sound "audio/click.ogg" action Start()
        imagebutton idle "gui/ui/sezi.png" hover "gui/ui/sezi_hover.png" activate_sound "audio/click.ogg" action ShowMenu("preferences")
        imagebutton idle "gui/ui/guanyu.png" hover "gui/ui/guanyu_hover.png" activate_sound "audio/click.ogg" action ShowMenu("wallpaper")
        imagebutton idle "gui/ui/theend.png" hover "gui/ui/theend_hover.png"  action Quit()
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_frame:
    xsize 140
    yfill True
style main_menu_vbox:
    xalign 1.0
    xoffset -10
    xmaximum 400
    yalign 1.0
    yoffset -10
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
style main_menu_title:
    properties gui.text_properties("title")
style main_menu_version:
    properties gui.text_properties("version")
## 3.游戏菜单界面 ######################################################################
## game_menu是在游戏进行中按下Esc键或者右键弹出的菜单，可以让玩家选择返回游戏，回到标题，保存，加载等选项1
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此界面与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。
screen game_menu(title, scroll=None, yinitial=0.0, key="game_menu"):

    style_prefix "game_menu"
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude
    use navigation
    textbutton _("返回"):
        style "return_button"
        action Return()
    label title
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text
style return_button is navigation_button
style return_button_text is navigation_button_text
style game_menu_outer_frame:
    bottom_padding 15
    top_padding 60
    background "gui/overlay/game_menu.png"
style game_menu_navigation_frame:
    xsize 140
    yfill True
style game_menu_content_frame:
    left_margin 20
    right_margin 10
    top_margin 5
style game_menu_viewport:
    xsize 460
style game_menu_vscrollbar:
    unscrollable gui.unscrollable
style game_menu_side:
    spacing 5
style game_menu_label:
    xpos 25
    ysize 60
style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
style return_button:
    xpos 15
    yalign 1.0
    yoffset -15
## （2）关于界面 ########################################################################
## 此界面提供有关游戏和 Ren'Py 的制作人员和版权信息。
## 此界面没有什么特别之处，因此它也是如何制作自定义界面的一个例子。
##############################################################################
screen about():
    tag menu
    ## 此“use”语句将包含“game_menu”界面到此处。子级“vbox”将包含在“game_menu”界面
    ## 的“viewport”内。
    use game_menu(_("关于"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label "[config.name!t]"
            text _("版本 [config.version!t]\n")
            ## “gui.about”通常在 options.rpy 中设置。
            if gui.about:
                text "n"
            text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n")
            text _("感谢TYPEMOON吧以及群里的热心兄弟们对本项目的大力支持！")
            text _("")
            text _("程序：阡陌纵横")
            text _("文本：jjy830(章节“月茶”)")
            text _("         perplexe time(章节“月茶2”)")
            text _("                嗝儿    (章节“蘑菇试验场”)")
            text _("")
            text _("特别感谢---（天衣無缝，d好清酒，Mess alone，日向等群友提供测试以及技术支持，非常感谢！")
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text
style about_label_text:
    size gui.label_text_size
## （3）读取和保存界面 #####################################################################
## 这些界面负责让玩家保存游戏并能够再次读取。由于它们几乎完全一样，因此它们都是
## 以第三方界面“file_slots”来实现的。
screen save():
    tag menu
    use file_slots(_("保存"))
screen load():
    tag menu
    use file_slots(_("读取游戏"))
screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))
    use game_menu(title):
        fixed:
            ## 此语句确保输入控件在任意按钮执行前可以获取“enter”事件。
            order_reverse True
            ## 页面名称，可以通过单击按钮进行编辑。
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value
            ## 存档位网格。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)
            ## 用于访问其他页面的按钮。
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing 2
                ## “range(1, 10)”给出 1 到 9 之间的数字。
                for page in range(1, 5):
                    textbutton "[page]" activate_sound "audio/click.ogg" action FilePage(page)

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text
style page_label:
    xpadding 25
    ypadding 2
style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
style page_button:
    properties gui.button_properties("page_button")
style page_button_text:
    properties gui.button_text_properties("page_button")
style slot_button:
    properties gui.button_properties("slot_button")
style slot_button_text:
    properties gui.button_text_properties("slot_button")
## （4）设置界面 ########################################################################
## 设置界面允许玩家配置游戏以更好地适应自己的习惯。
screen preferences():
    tag menu
    use game_menu(_("设置"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "radio"
                    label _("回退操作区")
                    textbutton _("禁用") action Preference("rollback side", "disable")
                    textbutton _("屏幕左侧") action Preference("rollback side", "left")
                    textbutton _("屏幕右侧") action Preference("rollback side", "right")
                vbox:
                    style_prefix "check"
                    label _("快进")
                    textbutton _("未读文本") action Preference("skip", "toggle")
                    textbutton _("选项后继续") action Preference("after choices", "toggle")
                    textbutton _("忽略转场") action InvertSelected(Preference("transitions", "toggle"))
                ## 可以在此处添加类型为“radio_pref”或“check_pref”的其他“vbox”，
                ## 以添加其他创建者定义的首选项设置。
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("文字速度")
                    bar value Preference("text speed")
                    label _("自动前进时间")
                    bar value Preference("auto-forward time")
                vbox:
                    if config.has_music:
                        label _("音乐音量")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("音效音量")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("语音音量")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text
style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 1
style pref_label_text:
    yalign 1.0
style pref_vbox:
    xsize 113
style radio_vbox:
    spacing gui.pref_button_spacing
style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
style radio_button_text:
    properties gui.button_text_properties("radio_button")
style check_vbox:
    spacing gui.pref_button_spacing
style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
style check_button_text:
    properties gui.button_text_properties("check_button")
style slider_slider:
    xsize 175
style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 5
style slider_button_text:
    properties gui.button_text_properties("slider_button")
style slider_vbox:
    xsize 225


## （5）历史界面 ########################################################################
## 这是一个向玩家显示对话历史的界面。虽然此界面没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
screen history():
    tag menu
    predict False
    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"
        for h in _history_list:
            window:
                ## 此语句可确保如果“history_height”为“None”的话仍可正常显示条
                ## 目。
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                        ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
                        ## 人文本中。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
        if not _history_list:
            label _("尚无对话历史记录。")
## 此语句决定了允许在历史记录界面上显示哪些标签。
define gui.history_allow_tags = { "alt", "noalt" }
style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_text is gui_text
style history_label is gui_label
style history_label_text is gui_label_text
style history_window:
    xfill True
    ysize gui.history_height
style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
style history_label:
    xfill True
style history_label_text:
    xalign 0.5
### （6）帮助界面 ########################################################################
## 提供有关键盘和鼠标映射信息的界面。它使用其它界面
## （“keyboard_help”，“mouse_help“和”gamepad_help“）来显示实际的帮助内容。
screen help():
    tag menu
    default device = "keyboard"
    use game_menu(_("帮助"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 8
            hbox:
                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")
                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help
screen keyboard_help():
    hbox:
        label _("回车")
        text _("推进对话并激活界面。")
    hbox:
        label _("空格")
        text _("推进对话但不激活选项。")
    hbox:
        label _("方向键")
        text _("导航界面。")
    hbox:
        label _("Esc")
        text _("访问游戏菜单。")
    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")
    hbox:
        label _("Tab")
        text _("切换对话快进。")
    hbox:
        label _("Page Up")
        text _("回退至先前的对话。")
    hbox:
        label _("Page Down")
        text _("向前至之后的对话。")
    hbox:
        label "H"
        text _("隐藏用户界面。")


screen mouse_help():
    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")
    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")
    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")
    hbox:
        label _("鼠标滚轮上\n点击回退操作区")
        text _("回退至先前的对话。")
    hbox:
        label _("鼠标滚轮下")
        text _("向前至之后的对话。")
screen gamepad_help():
    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")
    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")
    hbox:
        label _("右肩键")
        text _("向前至之后的对话。")
    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")
    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")
    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")
        textbutton _("校准") action GamepadCalibrate()
style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text
style help_button:
    properties gui.button_properties("help_button")
    xmargin 4
style help_button_text:
    properties gui.button_text_properties("help_button")
style help_label:
    xsize 125
    right_padding 10
style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
################################################################################
## （7）其他界面
################################################################################
## 1.确认界面 ########################################################################
## 当 Ren'Py 需要询问玩家有关确定或取消的问题时，会调用确认界面。
transform getIn:
    xoffset -40
    yoffset 0
    alpha 0.0
    easein 0.35 xoffset 0 alpha 1.0
screen confirm(message, yes_action, no_action):
    ## 显示此界面时，确保其他界面无法输入。
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame at getIn:
        vbox:
            xalign .5
            yalign .5
            spacing 15
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 50
                textbutton _("确定") activate_sound "audio/click.ogg"  action yes_action
                textbutton _("取消") activate_sound "audio/click.ogg"  action no_action
    ## 右键点击退出并答复“no”（取消）。
    key "game_menu" action no_action
style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text
style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
style confirm_button:
    properties gui.button_properties("confirm_button")
style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
## 2.快进指示界面 ######################################################################
## “skip_indicator”界面用于指示快进正在进行中。
screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 3
            text _("正在快进")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"
## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat
style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text
style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding
style skip_text:
    size gui.notify_text_size
style skip_triangle:
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "tl/DejaVuSans.ttf"
## 3.通知界面 ########################################################################
## 通知界面用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!tq]"
    timer 3.25 action Hide('notify')
transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
style notify_frame is empty
style notify_text is gui_text
style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
style notify_text:
    properties gui.text_properties("notify")
################################################################################
##4. 移动设备界面
################################################################################
style pref_vbox:
    variant "medium"
    xsize 225
## 由于鼠标可能不存在，我们将快捷菜单替换为更容易触摸且按钮更少更大的版本。
screen quick_menu():
    variant "touch"
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()
style window:
    variant "small"
    background "gui/phone/textbox.png"
style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"
style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"
style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"
style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"
style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"
style game_menu_navigation_frame:
    variant "small"
    xsize 170
style game_menu_content_frame:
    variant "small"
    top_margin 0
style pref_vbox:
    variant "small"
    xsize 200
style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"
style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"
style slider_vbox:
    variant "small"
    xsize None
style slider_slider:
    variant "small"
    xsize 300
