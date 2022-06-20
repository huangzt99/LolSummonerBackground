import requests
import re
import time
import json
import base64
import sys
#根据英雄id，获取此英雄所有皮肤，id，供选择。后返回皮肤id
def get_skinId(heroId):
	url='https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'.format(heroId)
	res=requests.get(url)
	res.encoding="unicode_escape"
	skinidlist=re.findall('"skinId":"(.*?)".*?"name":"(.*?)"',res.text)
	for x in skinidlist:
		print(x)
	skinid=input("输入皮肤id")
	return skinid
	
#输入英雄名称，从英雄列表中找出目标英雄id
def get_heroId():
	hero=input("输入英雄称号")
	url='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
	res=requests.get(url)#获取英雄列表
	res.encoding="unicode_escape"
	heroId=re.findall('"heroId":"([0-9]+)","name":"{}"'.format(hero),res.text)#正则表达式找出英雄id，返回一个列表
	print(heroId[0])
	return heroId[0]

def send(url,aid,id):
	print(url,aid,id)
	requests.packages.urllib3.disable_warnings()
	header={'Content-Type': 'application/json',
		'authorization': 'Basic '+aid,#身份标识，base加密
		}
	data={
		"key":"backgroundSkinId","value":id
	}
	resskin=requests.post(url,headers=header,json=data,verify=False)#json格式提交，关闭ssl验证
	print(resskin)

def main():
	heroId=get_heroId()
	skinId=get_skinId(heroId)
	#读取本地文件夹中port，token，
	'''with open(r'D:\Games\英雄联盟\LeagueClient\lockfile','r') as file:
		allstr=file.read(-1)
		allstr=allstr.split(':')
		port=allstr[2]
		token=allstr[3]
	'''
	token='oZNlLMY6pCDkCr2TW7xPfg'
	port='57424'
	url='https://127.0.0.1:{}/lol-summoner/v1/current-summoner/summoner-profile'.format(port)
	aid="riot:"+token
	aid=base64.b64encode(aid.encode()).decode('ascii')
	send(url,aid,skinId)

if __name__ == '__main__':
	main()