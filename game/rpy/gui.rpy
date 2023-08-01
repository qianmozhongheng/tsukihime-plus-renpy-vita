################################################################################
## 初始化
################################################################################
## “init offset”语句可使此文件中的初始化语句在任何其他文件中的“init”语句之前运
## 行。
init offset = -2
## 调用gui.init会将样式重置为合理的默认值，并设置游戏的宽度和高度（分辨率）。
init python:
    gui.init(640, 480)
################################################################################
## GUI配置变量
################################################################################
## 颜色 ##########################################################################
##
## 界面中文本的颜色。
## 整个界面中使用的强调色，用于标记和突出显示文本。
define gui.accent_color = u'#006666'
## 当既未选中也未悬停时用于文本按钮的颜色。
define gui.idle_color = u'#aaaaaa'
## 小颜色用于小文本，需要更亮/更暗才能达到相同的效果。
define gui.idle_small_color = u'#888888'
## 用于悬停的按钮和滑条的颜色。
define gui.hover_color = u'#006666'
## 用于选中但非焦点的文本按钮的颜色。当一个按钮为当前屏幕或设置选项值时，会处于
## 选中状态。
define gui.selected_color = u'#555555'
## 用于无法选择的文本按钮的颜色。
define gui.insensitive_color = u'#aaaaaa7f'
## 用于未填充的滑条部分的颜色。这些颜色不直接使用，但在重新生成条形图像文件时使
## 用。
define gui.muted_color = u'#66a3a3'
define gui.hover_muted_color = u'#99c1c1'
## 用于对话和菜单选择文本的颜色。
define gui.text_color = u'#404040'
define gui.interface_text_color = u'#404040'
## 字体和字体大小 #####################################################################
## 用于游戏内文本的字体。
define gui.text_font = "tl/test2.ttf"
## 用于角色名称的字体。
define gui.name_text_font = "tl/default.ttf"
## 用于游戏外文本的字体。
define gui.interface_text_font = "tl/test.ttf"
## 普通对话文本的大小。
define gui.text_size = 22
## 角色名称的大小。
define gui.name_text_size = 22
## 游戏用户界面中文本的大小。
define gui.interface_text_size = 20
## 游戏用户界面中标签的大小。
define gui.label_text_size = 22
## 通知屏幕上文本的大小。
define gui.notify_text_size = 22
## 游戏标题的大小。
define gui.title_text_size = 22
## 标题和游戏菜单 #####################################################################
## 用于标题菜单和游戏菜单的图像。
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"
## 对话 ##########################################################################
##
## 这些变量控制对话框一次一行显示在屏幕上的方式。
## 包含对话的文本框的高度。
define gui.textbox_height = 93
## 文本框在屏幕上的垂直位置。0.0 是顶部，0.5 是正中，1.0 是底部。
define gui.textbox_yalign = 1.0
## 叙述角色名称相对文本框的位置。可以是从左侧或顶部起的整数像素，或设为“0.5”来放
## 置到正中。
define gui.name_xpos = 120
define gui.name_ypos = 0
## 角色名称的水平对齐方式。0.0 为左侧对齐，0.5 为居中显示，而 1.0 为右侧对齐。
define gui.name_xalign = 0.0
## 包含角色名称的框的宽度，高度和边界尺寸，或设为“None”以自动调整其大小。
define gui.namebox_width = None
define gui.namebox_height = None
## 包含角色名称的框的边界尺寸，以左、上、右、下顺序排列。
define gui.namebox_borders = Borders(5, 5, 5, 5)
## 若为True，则名称框的背景将被平铺；若为False，则将缩放名称框的背景。
define gui.namebox_tile = False
## 对话框相对于文本框的位置。可以是相对于文本框从左侧或顶部起的整数像素，或设
## 为“0.5”来放置到正中。
define gui.dialogue_xpos = 134
define gui.dialogue_ypos = 25
## 对话文本的最大宽度（以像素为单位）。
define gui.dialogue_width = 372
## 对话文本的水平对齐方式。0.0 为左侧对齐，0.5 为居中显示，而 1.0 为右侧对齐。
define gui.dialogue_text_xalign = 0.0
## 按钮 ##########################################################################
##
## 这些变量以及 gui/button 中的图像文件控制着按钮显示方式。
## 按钮的宽度和高度像素数。如果为 None，则 Ren'Py 将计算大小。
define gui.button_width = None
define gui.button_height = None
## 按钮两侧的边框，按左、上、右、下的顺序排列。
define gui.button_borders = Borders(2, 2, 2, 2)
## 若为 True，则平铺背景图像。若为False，则背景图像将线性缩放。
define gui.button_tile = False
## 按钮使用的字体。
define gui.button_text_font = gui.interface_text_font
## 按钮所使用的文本大小。
define gui.button_text_size = gui.interface_text_size
## 按钮文本在各种状态下的颜色。
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
## 按钮文本的水平对齐方式。（0.0 为左侧对齐，0.5 为居中对齐，而 1.0 为右侧对
## 齐）。
define gui.button_text_xalign = 0.0
## 这些变量将覆盖不同类型按钮的设置。请参阅 gui 文档，了解可用的按钮种类以及每个
## 按钮的用途。
##
## 这些定制由默认界面使用：
define gui.radio_button_borders = Borders(9, 2, 2, 2)
define gui.check_button_borders = Borders(9, 2, 2, 2)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(5, 2, 5, 2)
define gui.quick_button_borders = Borders(5, 2, 5, 0)
define gui.quick_button_text_size = 7
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color
## 您还可以通过添加正确命名的变量来添加自己的自定义项。例如，您可以将以下几行取
## 消注释来设置导航按钮的宽度。
# define gui.navigation_button_width = 250
# 选项按钮 ########################################################################
##
## 用于游戏内菜单的选项按钮。
define gui.choice_button_width = 395
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(50, 3, 50, 3)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"
## 存档按钮 ########################################################################
##
## 存档按钮是一种特殊的按钮。它包含一个缩略图和描述该存档内容的文本。存档使用
## gui/button 中的图像文件，就像其他类型的按钮一样。
## 存档位按钮。
define gui.slot_button_width = 138
define gui.slot_button_height = 103
define gui.slot_button_borders = Borders(5, 5, 5, 5)
define gui.slot_button_text_size = 7
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color
## 存档所用缩略图的宽度和高度。
define config.thumbnail_width = 128
define config.thumbnail_height = 72
## 存档网格中的列数和行数。
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2
## 定位和间距 #######################################################################
##
## 这些变量控制各种用户界面元素的位置和间距。
## 导航按钮左侧相对于屏幕左侧的位置。
define gui.navigation_xpos = 20
## 快进指示器的垂直位置。
define gui.skip_ypos = 5
## 通知界面的垂直位置。
define gui.notify_ypos = 23
## 菜单选项之间的间距。
define gui.choice_spacing = 11
## 标题菜单和游戏菜单的导航部分中的按钮。
define gui.navigation_spacing = 2
## 控制设置项目之间的间隔量。
define gui.pref_spacing = 5
## 控制设置按钮之间的间距。
define gui.pref_button_spacing = 0
## 存档页面按钮之间的间距。
define gui.page_spacing = 0
## 存档按钮之间的间距。
define gui.slot_spacing = 5
## 标题菜单文本的位置。
define gui.main_menu_text_xalign = 1.0
## 框架 ##########################################################################
##
## 这些变量控制在不存在覆盖层或窗口时可以包含用户界面组件的框架的外观。
## 通用框架。
define gui.frame_borders = Borders(2, 2, 2, 2)
## 用作确认界面部分的框架。
define gui.confirm_frame_borders = Borders(20, 20, 20, 20)
## 用作快进界面部分的框架。
define gui.skip_frame_borders = Borders(8, 3, 25, 3)
## 用作通知界面部分的框架。
define gui.notify_frame_borders = Borders(8, 3, 20, 3)
## 框架背景是否应平铺？
define gui.frame_tile = False
## 条，滚动条和滑块 ####################################################################
## 这些语句控制条，滚动条和滑块的外观和大小。
## 默认的GUI仅使用滑块和垂直滚动条。所有其他栏仅在创建者编写的屏幕中使用。
## 水平条，滚动条和滑块的高度。垂直条，滚动条和滑块的宽度。
define gui.bar_size = 13
define gui.scrollbar_size = 6
define gui.slider_size = 13
## 如果条图应平铺，则为 True。 如果应该线性缩放，则为 False。
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False
## 水平边框。
define gui.bar_borders = Borders(2, 2, 2, 2)
define gui.scrollbar_borders = Borders(2, 2, 2, 2)
define gui.slider_borders = Borders(2, 2, 2, 2)
## 垂直边框。
define gui.vbar_borders = Borders(2, 2, 2, 2)
define gui.vscrollbar_borders = Borders(2, 2, 2, 2)
define gui.vslider_borders = Borders(2, 2, 2, 2)
## 如何处理 GUI 中不可滚动的滚动条。“hide”隐藏，“None”显示。
define gui.unscrollable = "hide"
## 历史 ##########################################################################
##
## 历史记录屏幕显示玩家已经阅读过的对话。
## Ren'Py 将保留的对话历史块数。
define config.history_length = 250
## 历史屏幕条目的高度，或设置为“None”以使高度变量自适应。
define gui.history_height = 70
## 所指定叙述角色的标签的坐标、宽度和对齐方式。
define gui.history_name_xpos = 78
define gui.history_name_ypos = 0
define gui.history_name_width = 78
define gui.history_name_xalign = 1.0
## 对话文本的坐标、宽度和对齐方式。
define gui.history_text_xpos = 85
define gui.history_text_ypos = 1
define gui.history_text_width = 370
define gui.history_text_xalign = 0.0
## NVL 模式 ######################################################################
##
## NVL 模式屏幕显示 NVL 模式的角色所产生的对话。
## NVL 模式背景窗口的背景边框。
define gui.nvl_borders = Borders(0, 5, 0, 10)
## Ren'Py 所显示的 NVL 模式条目的最大数量。如果要显示更多条目，则最早的条目将被
## 删除。
define gui.nvl_list_length = 6
## NVL 模式条目的高度。将此设置为 None 可使条目动态调整高度。
define gui.nvl_height = 58
## 当 gui.nvl_height 为 None 时，NVL 模式条目之间的间距，以及 NVL 模式条目和 NVL
## 模式菜单之间的间距。
define gui.nvl_spacing = 5
## 所指定叙述角色的标签的坐标、宽度和对齐方式。
define gui.nvl_name_xpos = 215
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 75
define gui.nvl_name_xalign = 1.0
## 对话文本的坐标、宽度和对齐方式。
define gui.nvl_text_xpos = 225
define gui.nvl_text_ypos = 4
define gui.nvl_text_width = 295
define gui.nvl_text_xalign = 0.0
## nvl_thought 文本（由 nvl_narrator 字符表示的文本）的位置，宽度和对齐方式。
define gui.nvl_thought_xpos = 120
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 390
define gui.nvl_thought_xalign = 0.0
## NVL menu_buttons 的位置。
define gui.nvl_button_xpos = 225
define gui.nvl_button_xalign = 0.0
## 本地化 #########################################################################
## 该变量控制允许在何时换行。默认值适用于大多数语言。可用的值请参见 https://
## www.renpy.org/doc/html/style_properties.html#style-property-language
define gui.language = "unicode"
################################################################################
## 移动设备
################################################################################
init python:
    ## 该变量增加快捷菜单按钮的尺寸来使它们在平板和手机上更容易按到。
    if renpy.variant("touch"):
        gui.quick_button_borders = Borders(20, 7, 20, 0)
    ## 该变量更改各个 GUI 元素的尺寸和间距来确保它们在手机上更容易识别。
    if renpy.variant("small"):
        ## 字体大小。
        gui.text_size = 15
        gui.name_text_size = 18
        gui.notify_text_size = 13
        gui.interface_text_size = 15
        gui.button_text_size = 15
        gui.label_text_size = 17
        ## 调整对话框的位置。
        gui.textbox_height = 120
        gui.name_xpos = 40
        gui.dialogue_xpos = 45
        gui.dialogue_width = 550
        ## 更改各元素的尺寸和间距。
        gui.slider_size = 18
        gui.choice_button_width = 620
        gui.choice_button_text_size = 15
        gui.navigation_spacing = 10
        gui.pref_button_spacing = 5
        gui.history_height = 95
        gui.history_text_width = 345
        gui.quick_button_text_size = 10
        ## 文件按钮布局。
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        ## NVL 模式。
        gui.nvl_height = 85
        gui.nvl_name_width = 153
        gui.nvl_name_xpos = 163
        gui.nvl_text_width = 458
        gui.nvl_text_xpos = 173
        gui.nvl_text_ypos = 3
        gui.nvl_thought_width = 620
        gui.nvl_thought_xpos = 10
        gui.nvl_button_width = 620
        gui.nvl_button_xpos = 10
