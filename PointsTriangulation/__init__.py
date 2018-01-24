# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PointsTriangulation
                                 A QGIS plugin
 Triangulation xyz points with structure lines to grid
                             -------------------
        begin                : 2018-01-24
        copyright            : (C) 2018 by uba_av/IMGG FEB RAS
        email                : uba_av@mail.ru
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PointsTriangulation class from file PointsTriangulation.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .PointsTriangulation import PointsTriangulation
    return PointsTriangulation(iface)
