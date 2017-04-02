#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plotly.plotly as py
from plotly.graph_objs import *

trace1 = {
  "x": ["-135000000",
                "-45000000",
                "-38000000",
                "-6000000",
                "-2500000",
                "-2000000",
                "-500000",
                "-300000",
                "-200000",
                "-70000",
                "-45000",
                "-30000",
                "-16000",
                "-13000",
                "-12000",
                "-5000",
                "-4250",
                "-2500",
                "-2000",
                "-1400",
                "-500",
                "-200",
                "0",
                "1000"],
  "y": ["0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0"],
  "hoverinfo": "none",
  "mode": "none",
  "name": "Col2",
  "showlegend": False,
  "type": "scatter",
  "uid": "d6088d"
}
data = Data([trace1])
layout = {
  "annotations": [
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "135亿年前<br>物质能量形成",
                "ay": -63,
                "arrowwidth": 1,
                "textangle": 0,
                "ax": -1,
                "y": 0,
                "x": -135000000,
                "font": {
                    "size": 8
                },
                "arrowcolor": "rgb(107, 95, 64)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "45亿年前<br>地球形成<br>",
                "align": "left",
                "ay": 60,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -45000000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "38亿年前<br>有机生物形成",
                "align": "left",
                "ay": -32,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -38000000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "600万年前<br>人类和黑猩猩<br>最后的共同祖先",
                "align": "center",
                "ay": -120,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -6000000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "250万年前<br>非洲人属开始演化<br>出现最早的石器<br>",
                "align": "center",
                "ay": 80,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -2500000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "200万年前<br>人类由非洲传播到欧亚大陆",
                "align": "center",
                "ay": -60,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -2000000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "50万年前<br>尼安德特人在欧洲和中东演化",
                "align": "center",
                "ay": -40,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -500000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "30万年前<br>日常用火",
                "align": "center",
                "ay": 83,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -300000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "20万年前<br>智人在东非演化",
                "align": "center",
                "ay": 40,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -200000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "7万年前<br>认知革命",
                "align": "left",
                "ay": -92,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -70000,
                "font": {
                    "color": "rgb(226, 126, 35)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "4.5万年前<br>智人抵达澳大利亚",
                "align": "center",
                "ay": 51,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -45000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "3万年前<br>尼安德特人绝种",
                "align": "center",
                "ay": -56,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -30000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "1.6万年前<br>智人抵达美洲",
                "align": "center",
                "ay": 61,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -16000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "1.3万年前<br>弗洛里斯人绝种",
                "align": "center",
                "ay": -44,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -13000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "1.2万年前<br>农业革命，驯化动植物<br>出现永久聚落",
                "align": "center",
                "ay": -88,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -12000,
                "font": {
                    "color": "rgb(226, 126, 35)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "5000年前<br>出现最早的王国，文字和金钱<br>多神教信仰",
                "align": "center",
                "ay": 47,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -5000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "4250年前<br>出现最早的帝国<br>萨尔贡大帝的阿卡德帝国",
                "align": "center",
                "ay": -49,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -4250,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "2500年前<br>出现最早的硬币，出现<br>波斯帝国 - 普世的政治秩序<br>印度佛教 - 普世的真理",
                "align": "center",
                "ay": 57,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -2500,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "2000年前<br>中国汉帝国，地中海罗马帝国。<br>基督教。",
                "align": "center",
                "ay": -81,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -2000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "1400年前<br>伊斯兰教",
                "align": "center",
                "ay": -35,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -1400,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "500年前<br>科学革命<br>欧洲人征服美洲和各大洋<br>资本主义兴起",
                "align": "center",
                "ay": 68,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": -500,
                "font": {
                    "color": "rgb(226, 126, 35)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "200年前<br>工业革命<br>家庭和社群被国家和市场取代<br>动植物大规模绝种",
                "align": "center",
                "ay": -75,
                "arrowwidth": 1,
                "ax": 1,
                "y": 0,
                "x": -200,
                "font": {
                    "color": "rgb(226, 126, 35)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "现在<br>人类去到地球以外<br>核武器威胁人类生存<br>生物趋向由智慧设计，而非自然选择",
                "align": "center",
                "ay": 55,
                "arrowwidth": 1,
                "ax": 69,
                "y": 0,
                "x": 0,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            },
            {
                "xref": "x",
                "arrowhead": 0,
                "yref": "y",
                "text": "未来<br>智慧设计成为生命的基本原则？<br>智人被超人类取代？",
                "align": "center",
                "ay": -99,
                "arrowwidth": 1,
                "ax": 0,
                "y": 0,
                "x": 1000,
                "font": {
                    "color": "rgb(60, 60, 60)",
                    "family": "\"Open Sans\", verdana, arial, sans-serif",
                    "size": 8
                },
                "arrowcolor": "rgb(60, 60, 60)",
                "showarrow": "true"
            }
        ],
  "autosize": True,
  "height": 450,
  "title": "人类简史",
  "width": 700,
  "xaxis": {
            "range": [
                -146092184.3687375,
                48697394.78957916
            ],
            "rangeslider": {
                "visible": "true",
                "range": [
                    -146092184.3687375,
                    48697394.78957916
                ],
                "autorange": "true"
            },
            "type": "linear",
            "autorange": "true",
            "title": "Click to enter X axis title"
        },
  "yaxis": {
            "range": [
                -1,
                1
            ],
            "type": "linear",
            "autorange": "true"
        }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
