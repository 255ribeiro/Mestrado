from __future__ import division

from Rhino.Geometry import Point3d, Line
import ghpythonlib.components as gh
import rhinoscriptsyntax as rs

#Cirando Listas vazias para os outputs
funicular=[]
PF=[]
raios=[]
resultante=[]
teste=[]



# Desenhando o poligono de forças
pAux = rs.coerce3dpoint(pto_inicial)
print "ponto inicial: ", pAux

polo = rs.coerce3dpoint(polo)
print "polo: ", polo
raios.append(Line(polo,pAux))

for v in vetores:
    vAux1 = rs.coerceline(v)
    vAux2 = pAux - v.PointAt(0)
    vAux3 = gh.Move(vAux1,vAux2)[0]
    pAux = vAux3.PointAt(1)
    PF.append(vAux3)
    r=Line(polo,pAux)
    raios.append(r)

r=Line(rs.coerce3dpoint(pto_inicial),pAux)

#testando PF ppara equilíbrio de translação
testePF=gh.Length(r)
if testePF == 0:
    print "Equilíbrio de Translação"
else:
    print "Módulo da resultante: ", testePF
    resultante.append(r)

#Desenhando o funicular

j = len(raios)

for i in range(j):
    r = rs.coerceline(raios[i])
    if i == 0:
        pAux = (rs.coerceline(vetores[0]).PointAt(.5))
        vAux1 = Line(r.PointAt(0),pAux)
        corda = gh.Move(r,vAux1)[0]
        corda = rs.coerceline(corda)
        funicular.append(corda)
        
    elif i < j-1:
        vAux1 = Line(r.PointAt(1),pAux)
        crdAux = gh.Move(r,vAux1)[0]
        crdAux = rs.coerceline(crdAux)
        pAux2 = pAux
        pAux = gh.LineXLine(crdAux,vetores[i])[-1]
        corda = Line(pAux2,pAux)
        funicular.append(corda)
        if not gh.CurveXCurve(crdAux,vetores[i])[-1]:
            print "teste"
            
            
    else:
        vAux1 = Line(r.PointAt(1),pAux)
        corda = gh.Move(r,vAux1)[0]
        corda = rs.coerceline(corda)
        funicular.append(corda)


