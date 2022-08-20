#imports
import math
import shapefile
import copy

# functions
def getPointsList(filePath):
    '''read input shapefile and get xyz coordinate list'''
    r = shapefile.Reader(filePath[:filePath.find(".")])
    geoType = r.shapeType
    if not (geoType == 3 or geoType == 13):
        print("! input file has no suitable geometry")
        return
    
    features = []
    
    for fid in range(len(r.shapes())):
        pts = r.shape(fid).points
        heights = r.shape(fid).z
        feature = []

        for idx, pt in enumerate(pts):
            xyz = (*pt, heights[idx])
            feature.append(xyz)

        features.append(feature)
    
    return features


def transformCoord(feature):
    '''transform from XYZ coordinate system to distance-height coordinate system'''
    startXYZ = feature[0]
    startXY = [startXYZ[0], startXYZ[1]]
    startZ = startXYZ[2]

    newPtsList = []
    dist = 0
    newPtsList.append([0, 0])

    for idx in range(1, len(feature)):
        curXYZ = feature[idx]
        curXY = [curXYZ[0], curXYZ[1]]
        curZ = curXYZ[2]

        dist += getDist(startXY, curXY) # calculate accumulated distance
        height = curZ - startZ
        newPtsList.append([dist, height])
        startXY = curXY.copy()

    return newPtsList


def douglasPeucker(ptList, epsilon):
    '''Douglas-Peucker algorithm to select points that need to be modified with height'''
    '''
        This code block is inspired by the pseudocode on the Wikipedia page of Ramer-Douglas-Peucker algorithm.
        https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm
    '''
    # search for point with max distance to line and record the index
    dmax = 0
    index  = 0
    length = len(ptList)

    if length == 2:
        resList = copy.deepcopy(ptList)
        return resList
    
    for idx in range(1, length - 1):
        d = getDistOfPt2Line([ptList[0], ptList[length - 1]], ptList[idx])
        if d > dmax:
            dmax = d
            index = idx

    resList = []
    
    if dmax > epsilon:
        resList1 = douglasPeucker(ptList[:index + 1], epsilon)
        resList2 = douglasPeucker(ptList[index:], epsilon)

        resList = [*resList1, *(resList2[1:])]
    else:
        resList = copy.deepcopy(ptList)
        heightDiff = ptList[length - 1][1] - ptList[0][1]
        xDiff = ptList[length - 1][0] - ptList[0][0]
        h = ptList[0][1]
        for idx in range(1, length - 1):
            # do a linear interpolation of height
            dx = resList[idx][0] - resList[0][0]
            dh = heightDiff * (dx / xDiff)
            resList[idx][1] = h + dh

    return resList


def restorePtList(resList, feature):
    '''re-transform from distance-height coordinate system back to xyz coordinate system'''
    newFeature = []
    height = feature[0][2]
    for idx, xyz in enumerate(feature):
        newFeature.append([xyz[0], xyz[1], height + resList[idx][1]])

    return newFeature


def writeShp(newFeatures, outFile):
    w = shapefile.Writer(outFile[:outFile.find(".")], shapeType = shapefile.POLYLINEZ)
    w.field('FID', 'N')

    for idx, newFeature in enumerate(newFeatures):
        w.linez([newFeature])
        w.record(idx)
    
    w.close()
    return True


def getDist(pt1, pt2):
    '''calculate distance between two points'''
    return round(math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2), 4)


def getDistOfPt2Line(line, pt):
    '''calculate distance of a point to a line, line is a list of two tuples which represent the start and end point of a line'''
    startPt = line[0]
    endPt = line[1]

    k = (endPt[1] - startPt[1]) / (endPt[0] - startPt[0]) # k = (y2 - y1) / (x2 - x1)
    b = endPt[1] - k * endPt[0] # b = y1 - k * x1

    d = abs(k * pt[0] - pt[1] + b) / math.sqrt(k ** 2 + 1) # d = |k * x0 - y0 + b| / (k ^ 2 + 1) ^ (1/2)
    return d
