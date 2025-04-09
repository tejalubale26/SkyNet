#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example script that allows control of the Crazyflie using keyboard input:
 * Move by using the arrow keys (left/right/forward/backwards)
 * Adjust the height with w/s (0.1 m for each keypress)
 * Yaw slowly using a/d (CCW/CW)
 * Yaw fast using z/x (CCW/CW)
"""
import logging
import math
import sys

import numpy as np


from vispy import scene
from vispy.scene import visuals
from vispy.scene.cameras import TurntableCamera

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.utils import uri_helper
from cflib.crazyflie.log import LogConfig

try:
    from sip import setapi
    setapi('QVariant', 2)
    setapi('QString', 2)
except ImportError:
    pass

from PyQt5 import QtCore, QtWidgets

logging.basicConfig(level=logging.INFO)

URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

if len(sys.argv) > 1:
    URI = sys.argv[1]

# Set the speed factor for moving and rotating
SPEED_FACTOR = 0.3


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, URI):
        QtWidgets.QMainWindow.__init__(self)

        self.resize(700, 500)
        self.setWindowTitle('Crazyflie Keyboard Control')

        self.canvas = Canvas(self.updateHover)
        self.canvas.create_native()
        self.canvas.native.setParent(self)

        self.setCentralWidget(self.canvas.native)

        cflib.crtp.init_drivers()
        self.cf = Crazyflie(ro_cache=None, rw_cache='cache')

        # Connect callbacks from the Crazyflie API
        self.cf.connected.add_callback(self.connected)
        self.cf.disconnected.add_callback(self.disconnected)

        # Connect to the Crazyflie
        self.cf.open_link(URI)

        self.hover = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'yaw': 0.0, 'height': 0.3}

        self.hoverTimer = QtCore.QTimer()
        self.hoverTimer.timeout.connect(self.sendHoverCommand)
        self.hoverTimer.setInterval(100)
        self.hoverTimer.start()

    def sendHoverCommand(self):
        self.cf.commander.send_hover_setpoint(
            self.hover['x'], self.hover['y'], self.hover['yaw'],
            self.hover['height'])

    def updateHover(self, k, v):
        if k != 'height':
            self.hover[k] = v * SPEED_FACTOR
        else:
            self.hover[k] += v

    def disconnected(self, URI):
        print('Disconnected')

    def connected(self, URI):
        print('We are now connected to {}'.format(URI))

        # The definition of the logconfig can be made before connecting
        lpos = LogConfig(name='Position', period_in_ms=100)
        lpos.add_variable('stateEstimate.x')
        lpos.add_variable('stateEstimate.y')
        lpos.add_variable('stateEstimate.z')

        try:
            self.cf.log.add_config(lpos)
            lpos.data_received_cb.add_callback(self.pos_data)
            lpos.start()
        except KeyError as e:
            print('Could not start log configuration,'
                  '{} not found in TOC'.format(str(e)))
        except AttributeError:
            print('Could not add Position log config, bad configuration.')


    def pos_data(self, timestamp, data, logconf):
        position = [
            data['stateEstimate.x'],
            data['stateEstimate.y'],
            data['stateEstimate.z']
        ]
        self.canvas.set_position(position)

    def closeEvent(self, event):
        if self.cf is not None:
            self.cf.close_link()


class Canvas(scene.SceneCanvas):
    def __init__(self, keyupdateCB):
        scene.SceneCanvas.__init__(self, keys=None)
        self.size = 800, 600
        self.unfreeze()
        self.view = self.central_widget.add_view()
        self.view.bgcolor = '#ffffff'
        self.view.camera = TurntableCamera(
            fov=10.0, distance=30.0, up='+z', center=(0.0, 0.0, 0.0))
        self.last_pos = [0, 0, 0]
        self.pos_markers = visuals.Markers()
        self.pos_data = np.array([0, 0, 0], ndmin=2)
        self.lines = []

        self.view.add(self.pos_markers)
        for i in range(6):
            line = visuals.Line()
            self.lines.append(line)
            self.view.add(line)

        self.keyCB = keyupdateCB

        self.freeze()

        scene.visuals.XYZAxis(parent=self.view.scene)

    def on_key_press(self, event):
        if not event.native.isAutoRepeat():
            if event.native.key() == QtCore.Qt.Key_Left:
                print('Strafing Left')
                self.keyCB('y', 1)
            if event.native.key() == QtCore.Qt.Key_Right:
                print('Strafing Right')
                self.keyCB('y', -1)
            if event.native.key() == QtCore.Qt.Key_Up:
                print('Strafing Forward')
                self.keyCB('x', 1)
            if event.native.key() == QtCore.Qt.Key_Down:
                print('Strafing Backward')
                self.keyCB('x', -1)
            if event.native.key() == QtCore.Qt.Key_A:
                print('Rotating Counter Clockwise Slowly')
                self.keyCB('yaw', -70)
            if event.native.key() == QtCore.Qt.Key_D:
                print('Rotating Clockwise Slowly')
                self.keyCB('yaw', 70)
            if event.native.key() == QtCore.Qt.Key_Z:
                print('Rotating Counter Clockwise Fast')
                self.keyCB('yaw', -200)
            if event.native.key() == QtCore.Qt.Key_X:
                print('Rotating Clockwise Fast')
                self.keyCB('yaw', 200)
            if event.native.key() == QtCore.Qt.Key_W:
                print('Increasing Height')
                self.keyCB('height', 0.1)
            if event.native.key() == QtCore.Qt.Key_S:
                print('Decreasing Height')
                self.keyCB('height', -0.1)

    def on_key_release(self, event):
        if not event.native.isAutoRepeat():
            if event.native.key() == QtCore.Qt.Key_Left:
                print('Left release')
                self.keyCB('y', 0)
            if event.native.key() == QtCore.Qt.Key_Right:
                print('Right release')
                self.keyCB('y', 0)
            if event.native.key() == QtCore.Qt.Key_Up:
                print('Forward release')
                self.keyCB('x', 0)
            if event.native.key() == QtCore.Qt.Key_Down:
                print('Backward release')
                self.keyCB('x', 0)
            if event.native.key() == QtCore.Qt.Key_A:
                print('A button release')
                self.keyCB('yaw', 0)
            if event.native.key() == QtCore.Qt.Key_D:
                print('D button release')
                self.keyCB('yaw', 0)
            if event.native.key() == QtCore.Qt.Key_W:
                print('W button release')
                self.keyCB('height', 0)
            if event.native.key() == QtCore.Qt.Key_S:
                print('S button release')
                self.keyCB('height', 0)
            if event.native.key() == QtCore.Qt.Key_Z:
                print('Z button release')
                self.keyCB('yaw', 0)
            if event.native.key() == QtCore.Qt.Key_X:
                print('X button release')
                self.keyCB('yaw', 0)

    def set_position(self, pos):
        self.last_pos = pos
        self.pos_data = np.append(self.pos_data, [pos], axis=0)
        self.pos_markers.set_data(self.pos_data, face_color='red', size=5)

if __name__ == '__main__':
    appQt = QtWidgets.QApplication(sys.argv)
    win = MainWindow(URI)
    win.show()
    appQt.exec_()
