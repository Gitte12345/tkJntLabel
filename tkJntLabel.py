# tkJntLabel.py

import maya.cmds as cmds
import maya.mel as mel
from functools import partial 

def cShrinkWin(windowToClose):
	cmds.window(windowToClose, e=1, h=20, w=180)

def tkJntLabel(*args):
	allJnts = cmds.ls(type='joint', l=1)
	for jnt in allJnts:
		label = jnt.split('|')[-1]
		cmds.setAttr(jnt + '.type', 18)
		cmds.setAttr(jnt + '.otherType', label, type = 'string')



def tkJntLabelUI(*args):
	ver = 0.1
	colSilverLight 		= [0.39, 0.46, 0.50];
	colSilverDark 		= [0.08, 0.09, 0.10];
	colSilverMid 		= [0.23, 0.28, 0.30];
	windowStartHeight = 50
	windowStartWidth = 450
	bh1 = 18
	if (cmds.window('win_tkJntLabel', exists=1)):
		cmds.deleteUI('win_tkJntLabel')
	myWindow = cmds.window('win_tkJntLabel', t='tkJntLabel ' + str(ver), s=1)

	cmds.frameLayout('flLabeling', l='Generate Labels', bgc=(colSilverMid[0], colSilverMid[1], colSilverMid[2]), 
		cll=1, cl=0, cc=partial(partial(cShrinkWin, "win_tkJntLabel")))

	cmds.columnLayout(adj=1, bgc=(colSilverMid[0], colSilverMid[1], colSilverMid[2]))
	cmds.rowColumnLayout(bgc=(colSilverDark[0], colSilverDark[1], colSilverDark[1]), nc=2, cw=[(1,180)])

	cmds.button(l='Add Labels To All Joints', c=partial(tkJntLabel), bgc=(colSilverLight[0], colSilverLight[1], colSilverLight[2]))
	# cmds.textField('tfAsset', h=bh1, ed=1)

	cmds.showWindow(myWindow)

tkJntLabelUI()
partial(cShrinkWin, "win_tkJntLabel")