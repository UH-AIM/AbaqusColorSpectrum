'''
This script creates several spectrums to better display the results like stress, strain, displacement, etc.
i.e. do not use rainbow, ever.
'''

from math import cos, sin, pi, sqrt, acos, tan, radians, degrees
import numpy as np
import getpass
import csv
import os

#load abaqus modules
from abaqus import *
from abaqusConstants import *
backwardCompatibility.setValues(includeDeprecated=True, reportDeprecated=False)
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
import mesh
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import regionToolset
import matplotlib as mpl
import matplotlib.pyplot as plt

def ABA_color():

    # see more color gradients here https://matplotlib.org/stable/tutorials/colors/colormaps.html
    colorViridis  = [mpl.colors.to_hex(x[0:3]).encode('ascii', 'ignore') for x in plt.get_cmap('viridis', 100).colors]
    colorPlasma   = [mpl.colors.to_hex(x[0:3]).encode('ascii', 'ignore') for x in plt.get_cmap('plasma',  100).colors]
    colorInferno  = [mpl.colors.to_hex(x[0:3]).encode('ascii', 'ignore') for x in plt.get_cmap('inferno', 100).colors]
    colorMagma    = [mpl.colors.to_hex(x[0:3]).encode('ascii', 'ignore') for x in plt.get_cmap('magma',   100).colors]
    colorCividis  = [mpl.colors.to_hex(x[0:3]).encode('ascii', 'ignore') for x in plt.get_cmap('cividis', 100).colors]
    # Batlow is not a part of matplotlib so I had to hard code it in
    colorBatlow = ('#011959', '#021A59', '#031C59', '#041D5A', '#051F5A', '#05205A', '#06225A', '#07235B', '#08255B', '#08265B', '#09285B', '#0A295C', '#0A2B5C', '#0B2C5C', '#0B2E5C', '#0C2F5D', '#0C305D', '#0C325D', '#0D335D', '#0D345D', '#0D355E', '#0E375E', '#0E385E', '#0E395E', '#0F3A5E', '#0F3B5F', '#0F3C5F', '#0F3D5F', '#103F5F', '#10405F', '#10415F', '#104260', '#114360', '#114460', '#114560', '#114660', '#124760', '#124761', '#124861', '#134961', '#134A61', '#134B61', '#144C61', '#144D61', '#144E61', '#154F61', '#155061', '#165162', '#165262', '#175362', '#175362', '#185462', '#185562', '#195662', '#195762', '#1A5862', '#1B5962', '#1B5A61', '#1C5A61', '#1D5B61', '#1E5C61', '#1F5D61', '#205E61', '#215E60', '#215F60', '#226060', '#246160', '#25615F', '#26625F', '#27635F', '#28645E', '#29645E', '#2A655D', '#2C665D', '#2D665C', '#2E675C', '#2F685B', '#31685B', '#32695A', '#336959', '#356A59', '#366B58', '#386B57', '#396C57', '#3A6C56', '#3C6D55', '#3D6D54', '#3F6E54', '#406E53', '#426F52', '#436F51', '#457050', '#46704F', '#48714F', '#4A714E', '#4B724D', '#4D724C', '#4E734B', '#50734A', '#517449', '#537449', '#547548', '#567547', '#587646', '#597645', '#5B7744', '#5C7743', '#5E7842', '#607841', '#617941', '#637940', '#657A3F', '#667A3E', '#687A3D', '#6A7B3C', '#6B7B3B', '#6D7C3A', '#6F7C3A', '#707D39', '#727D38', '#747E37', '#757E36', '#777F35', '#797F35', '#7B8034', '#7C8033', '#7E8132', '#808132', '#828231', '#848230', '#86832F', '#87832F', '#89842E', '#8B842E', '#8D852D', '#8F852D', '#91862C', '#93862C', '#95872B', '#97872B', '#99882B', '#9B882B', '#9D882B', '#9F892B', '#A1892B', '#A38A2B', '#A58A2B', '#A68B2C', '#A88B2C', '#AA8C2C', '#AC8C2D', '#AE8C2D', '#B08D2E', '#B28D2F', '#B48D30', '#B68E30', '#B88E31', '#BA8F32', '#BC8F33', '#BE8F34', '#C09035', '#C29037', '#C49038', '#C59139', '#C7913A', '#C9913C', '#CB923D', '#CD923E', '#CE9240', '#D09241', '#D29343', '#D49344', '#D59346', '#D79448', '#D99449', '#DA954B', '#DC954D', '#DE954E', '#DF9650', '#E19652', '#E29654', '#E49756', '#E59758', '#E7985A', '#E8985C', '#EA995E', '#EB9960', '#EC9A62', '#ED9A64', '#EF9B66', '#F09C68', '#F19C6B', '#F29D6D', '#F39D6F', '#F49E71', '#F59F74', '#F69F76', '#F6A078', '#F7A17B', '#F8A17D', '#F8A27F', '#F9A382', '#F9A484', '#FAA487', '#FAA589', '#FBA68B', '#FBA78E', '#FBA790', '#FCA892', '#FCA994', '#FCAA97', '#FCAA99', '#FCAB9B', '#FCAC9D', '#FDADA0', '#FDADA2', '#FDAEA4', '#FDAFA6', '#FDB0A8', '#FDB0AB', '#FDB1AD', '#FDB2AF', '#FDB3B1', '#FDB3B3', '#FDB4B5', '#FDB5B7', '#FDB5B9', '#FDB6BB', '#FCB7BE', '#FCB8C0', '#FCB8C2', '#FCB9C4', '#FCBAC6', '#FCBBC8', '#FCBBCA', '#FCBCCC', '#FCBDCF', '#FCBDD1', '#FCBED3', '#FCBFD5', '#FCC0D7', '#FCC1DA', '#FBC1DC', '#FBC2DE', '#FBC3E0', '#FBC4E3', '#FBC4E5', '#FBC5E7', '#FBC6E9', '#FBC7EC', '#FBC8EE', '#FAC8F0', '#FAC9F3', '#FACAF5', '#FACBF7', '#FACCFA')
    
    session.Spectrum(name='colorGradient-Batlow',  colors = colorBatlow )
    session.Spectrum(name='colorGradient-Viridis', colors = colorViridis)
    session.Spectrum(name='colorGradient-Plasma',  colors = colorPlasma )
    session.Spectrum(name='colorGradient-Inferno', colors = colorInferno)
    session.Spectrum(name='colorGradient-Magma',   colors = colorMagma  )
    session.Spectrum(name='colorGradient-Cividis', colors = colorCividis)
    
    # Demo displayment
    session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)

    vp=session.viewports['Viewport: 1']
    
    # Miscelleanous code to orient and show an ODB result
    # Locate the ODB file
    # You must point the name to an actual ODB file to open it
    #odb = session.openOdb(name='')
    #vp.setValues(displayedObject=odb)
    #
    #vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF, ))
    #
    #stepName = odb.steps.keys()
    #iFrame = odb.steps[stepName[1]].frames[-1]
    #    
    #vp.odbDisplay.contourOptions.setValues(spectrum='colorGradient-Viridis')
    #
    #vp.odbDisplay.commonOptions.setValues(visibleEdges=FEATURE)
    #
    #session.graphicsOptions.setValues(backgroundStyle=SOLID,  backgroundColor='#FFFFFF')
    #vp.view.setValues(session.views['Iso'])
    #vp.view.rotate(xAngle=-90, yAngle=0, zAngle=0, mode=MODEL)
    #
    #vp.odbDisplay.setPrimaryVariable(variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
    #
    #vp.viewportAnnotationOptions.setValues(
    #    legendFont = '-*-consolas-medium-r-normal-*-*-180-*-*-m-*-*-*',
    #    triadFont  = '-*-consolas-medium-r-normal-*-*-180-*-*-m-*-*-*', 
    #    titleFont  = '-*-consolas-medium-r-normal-*-*-180-*-*-m-*-*-*', 
    #    stateFont  = '-*-consolas-medium-r-normal-*-*-180-*-*-m-*-*-*')
    #
    #vp.viewportAnnotationOptions.setValues(triad=OFF,title=OFF, state=OFF, annotations=OFF, compass=OFF, legend=ON)

if __name__=="__main__":
	ABA_color()