def onModuleSelected(modulename):
  global tabWidget
  tabWidget.addTab(getattr(slicer.modules,
modulename.lower()).widgetRepresentation(), modulename)

import qt
import __main__

mainWidget = qt.QWidget()
mainWidget.objectName = "qSlicerAppMainWindow"
vlayout = qt.QVBoxLayout()
mainWidget.setLayout(vlayout)

layoutManager = slicer.qMRMLLayoutWidget()
layoutManager.setMRMLScene(slicer.mrmlScene)
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)
vlayout.addWidget(layoutManager)

hlayout = qt.QHBoxLayout()
vlayout.addLayout(hlayout)

loadDataButton = qt.QPushButton("Load Data")
hlayout.addWidget(loadDataButton)
loadDataButton.connect('clicked()', slicer.util.openAddVolumeDialog)

saveDataButton = qt.QPushButton("Save Data")
hlayout.addWidget(saveDataButton)
saveDataButton.connect('clicked()', slicer.util.openSaveDataDialog)

moduleSelector = slicer.qSlicerModuleSelectorToolBar()
moduleSelector.setModuleManager(slicer.app.moduleManager())
hlayout.addWidget(moduleSelector)
moduleSelector.connect('moduleSelected(QString)', onModuleSelected)

tabWidget = qt.QTabWidget()
vlayout.addWidget(tabWidget)

modules = ["Editor"]
for module in modules:
  onModuleSelected(module)

mainWidget.show()
__main__.mainWidget = mainWidget


