from pygame.locals import *


BLACK = Color(0,0,0,name="black")
WHITE = Color(255,255,255,name="white")
RED = Color(255,0,0,name="red")
LIME = Color(0,255,0,name="lime")
BLUE = Color(0,0,255,name="blue")
YELLOW = Color(255,255,0,name="yellow")
CYAN = Color(0,255,255,name="cyan")
AQUA = Color(0,255,255,name="aqua")
MAGENTA = Color(255,0,255,name="magenta")
FUCHSIA = Color(255,0,255,name="fuchsia")
SILVER = Color(192,192,192,name="silver")
GRAY = Color(128,128,128,name="gray")
MAROON = Color(128,0,0,name="marron")
OLIVE = Color(128,128,0,name="olive")
GREEN = Color(0,128,0,name="green")
PURPLE = Color(128,0,128,name="purple")
TEAL = Color(0,128,128,name="teal")
NAVY = Color(0,0,128,name="navy")
DARK_RED = Color(139,0,0,name="darkRed")
BROWN = Color(165,42,42,name="brown")
FIREBRICK = Color(178,34,34,name="fireBrick")
CRIMSON = Color(220,20,60,name="crimson")
TOMATO = Color(255,99,71,name="tomato")
CORAL = Color(255,127,80,name="coral")
INDIAN_RED = Color(205,92,92,name="indianRed")
LIGHT_CORAL = Color(240,128,128,name="lightCoral")
DARK_SALMON = Color(233,150,122,name="darkSalmon")
SALMON = Color(250,128,114,name="salmon")
LIGHT_SALMON = Color(255,160,122,name="lightSalmon")
ORANGE_RED = Color(255,69,0,name="orangeRed")
DARK_ORANGE = Color(255,140,0,name="darkOrange")
ORANGE = Color(255,165,0,name="orange")
GOLD = Color(255,215,0,name="gold")
DARK_GOLDEN_ROD = Color(184,134,11,name="DARK_GOLDEN_ROD")
GOLDEN_ROD = Color(218,165,32,name="goldenRod")
PALE_GOLDEN_ROD = Color(238,232,170,name="PALE_GOLDEN_ROD")
DARK_KHAKI = Color(189,183,107,name="DARK_KHAKI")
KHAKI = Color(240,230,140,name="khaki")
YELLOW_GREEN = Color(154,205,50,name="yellowGreen")
DARK_OLIVE_GREEN = Color(85,107,47,name="DARK_OLIVE_GREEN")
OLIVE_DRAB = Color(107,142,35,name="oliveDrab")
LAWN_GREEN = Color(124,252,0,name="lawnGreen")
CHART_REUSE = Color(127,255,0,name="CHART_REUSE")
GREEN_YELLOW = Color(173,255,47,name="greenYellow")
DARK_GREEN = Color(0,100,0,name="darkGreen")
FOREST_GREEN = Color(34,139,34,name="forestGreen")
LIME_GREEN = Color(50,205,50,name="limeGreen")
LIGHT_GREEN = Color(144,238,144,name="lightGreen")
PALE_GREEN = Color(152,251,152,name="paleGreen")
DARK_SEA_GREEN = Color(143,188,143,name="DARK_SEA_GREEN")
MEDIUM_SPRING_GREEN = Color(0,250,154,name="MEDIUM_SPRING_GREEN")
SPRING_GREEN = Color(0,255,127,name="SPRING_GREEN")
SEA_GREEN = Color(46,139,87,name="SEA_GREEN")
MEDIUM_AQUA_MARINE = Color(102,205,170,name="MEDIUM_AQUA_MARINE")
MEDIUM_SEA_GREEN = Color(60,179,113,name="MEDIUM_SEA_GREEN")
LIGHT_SEA_GREEN = Color(32,178,170,name="LIGHT_SEA_GREEN")
DARK_SLATE_GRAY = Color(47,79,79,name="DARK_SLATE_GRAY")
DARK_CYAN = Color(0,139,139,name="DARK_CYAN")
LIGHT_CYAN = Color(224,255,255,name="LIGHT_CYAN")
DARK_TURQUOISE = Color(0,206,209,name="DARK_TURQUOISE")
TURQUOISE = Color(64,224,208,name="TURQUOISE")
MEDIUM_TURQUOISE = Color(72,209,204,name="MEDIUM_TURQUOISE")
PALE_TURQUOISE = Color(175,238,238,name="PALE_TURQUOISE")
AQUA_MARINE = Color(127,255,212,name="AQUA_MARINE")
POWDER_BLUE = Color(176,224,230,name="POWDER_BLUE")
CADET_BLUE = Color(95,158,160,name="CADET_BLUE")
STEEL_BLUE = Color(70,130,180,name="steelBlue")
CORN_FLOWER_BLUE = Color(100,149,237,name="black")
DEEP_SKY_BLUE = Color(0,191,255,name="deepSkyBlue")
DODGER_BLUE = Color(30,144,255,name="dodgerBlue")
LIGHT_BLUE = Color(173,216,230,name="lightBlue")
SKY_BLUE = Color(135,206,235,name="skyBlue")
LIGHT_SKY_BLUE = Color(135,206,250,name="black")
MIDNIGHT_BLUE = Color(25,25,112,name="black")
DARK_BLUE = Color(0,0,139,name="darkBlue")
MEDIUM_BLUE = Color(0,0,205,name="mediumBlue")
ROYAL_BLUE = Color(65,105,225,name="royalBlue")
BLUE_VIOLET = Color(138,43,226,name="blueViolet")
INDIGO = Color(75,0,130,name="indigo")
DARK_SLATE_BLUE = Color(72,61,139,name="black")
SLATE_BLUE = Color(106,90,205,name="slateBlue")
MEDIUM_SLATE_BLUE = Color(123,104,238,name="black")
MEDIUM_PURPLE = Color(147,112,219,name="black")
DARK_MAGENTA = Color(139,0,139,name="black")
DARK_VIOLET = Color(148,0,211,name="black")
DARK_ORCHID = Color(153,50,204,name="black")
MEDIUM_ORCHID = Color(186,85,211,name="black")
THISTLE = Color(216,191,216,name="thistle")
PLUM = Color(221,160,221,name="plum")
VIOLET = Color(238,130,238,name="violet")
ORCHID = Color(218,112,214,name="orchid")
MEDIUM_VIOLET_RED = Color(199,21,133,name="black")
PALE_VIOLET_RED = Color(219,112,147,name="black")
DEEP_PINK = Color(255,20,147,name="black")
HOT_PINK = Color(255,105,180,name="black")
LIGHT_PINK = Color(255,182,193,name="black")
PINK = Color(255,192,203,name="pink")
ANTIQUE_WHITE = Color(250,235,215,name="black")
BEIGE = Color(245,245,220,name="black")
BISQUE = Color(255,228,196,name="black")
BLANCHED_ALMOND = Color(255,235,205,name="black")
WHEAT = Color(245,222,179,name="black")
CORN_SILK = Color(255,248,220,name="black")
LEMON_CHIFFON = Color(255,250,205,name="black")
LIGHT_GOLDEN_ROD_YELLOW = Color(250,250,210,name="black")
LIGHT_YELLOW = Color(255,255,224,name="black")
SADDLE_BROWN = Color(139,69,19,name="black")
SIENNA = Color(160,82,45,name="sienna")
CHOCOLATE = Color(210,105,30,name="chocolate")
PERU = Color(205,133,63,name="peru")
SANDY_BROWN = Color(244,164,96,name="black")
BURLY_WOOD = Color(222,184,135,name="black")
TAN = Color(210,180,140,name="tan")
ROSY_BROWN = Color(188,143,143,name="black")
MOCCASIN = Color(255,228,181,name="moccasin")
NAVAJO_WHITE = Color(255,222,173,name="black")
PEACH_PUFF = Color(255,218,185,name="black")
MISTY_ROSE = Color(255,228,225,name="black")
LAVENDER_BLUSH = Color(255,240,245,name="black")
LINEN = Color(250,240,230,name="linen")
OLD_LACE = Color(253,245,230,name="black")
PAPAYA_WHIP = Color(255,239,213,name="PAPAYA_WHIP")
SEA_SHELL = Color(255,245,238,name="SEA_SHELL")
MINT_CREAM = Color(245,255,250,name="mintCream")
SLATE_GRAY = Color(112,128,144,name="slateGray")
LIGHT_SLATE_GRAY = Color(119,136,153,name="lightSlateGray")
LIGHT_STEEL_BLUE = Color(176,196,222,name="LIGHT_STEEL_BLUE")
LAVENDER = Color(230,230,250,name="lavender")
FLORAL_WHITE = Color(255,250,240,name="floralWhite")
ALICE_BLUE = Color(240,248,255,name="ALICE_BLUE")
GHOST_WHITE = Color(248,248,255,name="ghostWhite")
HONEYDEW = Color(240,255,240,name="honeydew")
IVORY = Color(255,255,240,name="ivory")
AZURE = Color(240,255,255,name="azure")
SNOW = Color(255,250,250,name="snow")
DIM_GRAY = Color(105,105,105,name="dimGray")
DIM_GREY = Color(105,105,105,name="dimGrey")
GREY = Color(128,128,128,name="grey")
DARK_GRAY = Color(169,169,169,name="darkGray")
DARK_GREY = Color(169,169,169,name="darkGrey")
LIGHT_GRAY = Color(211,211,211,name="lightGray")
LIGHT_GREY = Color(211,211,211,name="lightGrey")
GAINSBORO = Color(220,220,220,name="gainsboro")
WHITE_SMOKE = Color(245,245,245,name="whiteSmoke")
