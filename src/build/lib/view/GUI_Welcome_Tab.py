import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QMainWindow,
                             QAction, qApp,
                             QHBoxLayout, QVBoxLayout, QMessageBox,
                             QLineEdit, QTableWidget, QTableWidgetItem,
                             QGridLayout, QPlainTextEdit,
                             QDesktopWidget, QLabel, QRadioButton,
                             QGroupBox, QSizePolicy, QCheckBox, QFileDialog,
                             QTextEdit, QTextBrowser, QFrame)
from PyQt5.QtGui import QFont, QColor, QPixmap
from FilesNumberHandler import Files_Number_Handler
from GUI_FastaViewer import *
from Welcome_Tab_Logic import Welcome_Tab_Logic



class GUI_Welcome_Tab(QMainWindow):
    """Creates an welcome Tab for the user that contains importan information
    The information that is being shown on this tab is supposed to help
    the user understand the functionality of this programm

    Attributes
    ----------
    Output_Name : str
        a string that contains the ouput name of the final file

    Threads_Number : str
        a string that contains the threads for the final file

    ProteiFDR_Number : str
        a string that contains the protein fdr number

    mainwidget : QWidget
        a main QtWidget that contains all other widgets

    main_layout : QVBoxLayout
        a vertical layout that contains all other layouts

    Hboxlevel1 = QHBoxLayout
        a horizontal layout

    Welcome_Title_Label : QLabel
        a label that contains the  title

    Hline_Welcome : QLabel
        a label that contains a horizontal line for visual separation

    Tabs_Explination_Label : QLabel
        a label that contains an explenation of the tabs

    HLine_LFQ : QLabel
        a label that contains a horizontal line for visual separation

    proteomicsLFQ_Title_Label : QLabel
        a label that contains a title

    proteomicsLFQ_Load_Explination_Label : QLabel
        a label that contains an explenation of proteomicsLFQ

    proteomicsLFQ_Run_Explination_Label : QLabel
        a label that contains an explenation of the run button

    loadButton : QPushButton
        a QPushButton that is connected to a method

    hboxLoadBtn : QHBoxLayout
     a horizontal layout

     Threads : QLineEdit
        a QLineEdit where the user can write his input

    Threads_Label : QLabel
        a label that contains strings

    hbox2 : QHBoxLayout
        a horizontal layout

    ProteinFDR : QLineEdit
        a QLineEdit where the user can wirte his input

    ProteinFDR_Label : QLabel
        a label that contains strings

    hbox3 : QHBoxLayout
        a horizontal layout

    ExplenationLayout : QGridLayout
        a layout in the form of a matrix

    Explenation : QLabel
        a label containing an explenation

    FastaView : QLabel
        a label containg a title

    Spectrum : QLabel
        a label containg a title

    Spectrum_expl : QLabel
        a label that contains an explenation

    ExperimentalD : QLabel
        a label containg a title

    ExperimentalD_expl : QLabel
        a label that contains an explenation

    XmlV : QLabel
        a label that contains a title

    XmlV_expl : QLabel
        a label that contains an explenation

    Mztab : QLabel
        a label that contains a title

    Mztab_expl : QLabel
        a label that contains an explenation

    welcome_Title : str
        the title of the welcome tab as a string

    proteomicsLFQ_Title : str
        the title of the proteomicsLFQ section of the screen as a string

    proteomicsLFQ_Load_Explination : str
        the proteomicsLFQ explination as a string

    proteomicsLFQ_Run_Explination : str
        the explination of the run button as a string

    pixmap : QPixmap
        a picture that is loaded through a given path

    Picture : QLabel
        a label that contains a picture

    hboxExplenation : QHBoxLayout
        a horizontal layout

    hboxExplenation

    Methods
    -------
    initUI
        creates the layout of the window and sets the widgets

    get_Output_FileName
        gets the output filename that the user has given

    get_Threads
        gets the threads that the user has given

    get_ProteinFDR
        gets the prtein fdr number that the user has given
    """


    def __init__(self):


        super().__init__()
        self.resize(1280, 720)
        self.initUI()

    def initUI(self):
        #creating the Layout, QVBoxLayout with hboxlayout

        self.Output_Name = ''
        self.Threads_Number = ''
        self.ProteiFDR_Number = ''
        self.mainwidget = QWidget(self)
        self.main_layout = QVBoxLayout(self.mainwidget)
        self.Hboxlevel1 = QHBoxLayout()

        #Creating QLabel with welcome Text to display on first Tab

        self.Welcome_Title_Label = QLabel()
        self.Hline_Welcome = QLabel()
        self.Tabs_Explination_Label = QLabel()
        self.HLine_LFQ = QLabel()
        self.proteomicsLFQ_Title_Label = QLabel()
        self.proteomicsLFQ_Load_Explination_Label = QLabel()
        self.proteomicsLFQ_Run_Explination_Label = QLabel()



        self.OutputName = QLineEdit(self)
        self.OutputName_Label = QLabel(self)
        self.OutputName_Label.setText('Name for Output Files')
        self.hbox = QHBoxLayout()
        self.hbox.setSpacing(10)
        self.hbox.addWidget(self.OutputName)
        self.hbox.addWidget(self.OutputName_Label)
        self.hbox.addStretch(1)
        self.hbox.setContentsMargins(25, 2, 11, 2)

        self.loadButton = QtWidgets.QPushButton(self)
        self.loadButton.setText("Load Data")
        self.loadButton.setFixedWidth(140)

        self.hboxLoadBtn = QHBoxLayout()
        self.hboxLoadBtn.addWidget(self.loadButton)
        self.hboxLoadBtn.setContentsMargins(25, 2, 11, 2)
        self.hboxLoadBtn.addStretch(1)


        self.Threads = QLineEdit(self)
        self.Threads.setText('1')
        self.Threads_Label = QLabel(self)
        self.Threads_Label.setText('Threads')
        self.hbox2 = QHBoxLayout()
        self.hbox2.setSpacing(10)
        self.hbox2.addWidget(self.Threads)
        self.hbox2.addWidget(self.Threads_Label)
        self.hbox2.addStretch(1)
        self.hbox2.setContentsMargins(25, 2, 11, 2)

        self.ProteinFDR = QLineEdit(self)
        self.ProteinFDR.setText('0.3')
        self.ProteinFDR_Label = QLabel(self)
        self.ProteinFDR_Label.setText('Protein FDR')
        self.hbox3 = QHBoxLayout()
        self.hbox3.setSpacing(10)
        self.hbox3.addWidget(self.ProteinFDR)
        self.hbox3.addWidget(self.ProteinFDR_Label)
        self.hbox3.addStretch(1)
        self.hbox3.setContentsMargins(25, 2, 11, 2)



        self.ExplenationLayout = QGridLayout()
        normalFont = QFont("Sanserif",11)
        boldFont = QFont("Sanserif", 11, QFont.Bold)


        self.Explenation = QLabel()
        self.Explenation.setText('This Application offers the folowing Options:')
        self.Explenation.setFont(boldFont)

        self.FastaView = QLabel()
        self.FastaView.setText('Proteinsequence Viewer:')
        self.FastaView.setFont(boldFont)
        self.FastaView_expl = QLabel()
        self.FastaView_expl.setText('Displays all information of the loaded Fasta file.')
        self.FastaView_expl.setFont(normalFont)

        self.Spectrum = QLabel()
        self.Spectrum.setText('Spectrum Viewer:')
        self.Spectrum.setFont(boldFont)
        self.Spectrum_expl = QLabel()
        self.Spectrum_expl.setText('Displays the identified spectra.')
        self.Spectrum_expl.setFont(normalFont)

        self.ExperimentalD = QLabel()
        self.ExperimentalD.setText('Experimental Design:')
        self.ExperimentalD.setFont(boldFont)
        self.ExperimentalD_expl = QLabel()
        self.ExperimentalD_expl.setText('Display or create and edit the content of a provided experimental design')
        self.ExperimentalD_expl.setFont(normalFont)

        self.XmlV = QLabel()
        self.XmlV.setText('XML Viewer:')
        self.XmlV.setFont(boldFont)
        self.XmlV_expl = QLabel()
        self.XmlV_expl.setText('Display and edit a provided configuration file.')
        self.XmlV_expl.setFont(normalFont)

        self.Mztab = QLabel()
        self.Mztab.setText('PSM/Protein Viewer:')
        self.Mztab.setFont(boldFont)
        self.Mztab_expl = QLabel()
        self.Mztab_expl.setText('Displays the output mzTab file after successfully running the ProteomicsLFQ.')
        self.Mztab_expl.setFont(normalFont)

        self.ExplenationLayout.addWidget(self.Explenation,0,0)
        self.ExplenationLayout.addWidget(self.FastaView,1,0)
        self.ExplenationLayout.addWidget(self.FastaView_expl,2,0)
        self.ExplenationLayout.addWidget(self.Spectrum,3,0)
        self.ExplenationLayout.addWidget(self.Spectrum_expl,4,0)
        self.ExplenationLayout.addWidget(self.ExperimentalD,5,0)
        self.ExplenationLayout.addWidget(self.ExperimentalD_expl,6,0)
        self.ExplenationLayout.addWidget(self.XmlV,7,0)
        self.ExplenationLayout.addWidget(self.XmlV_expl,8,0)
        self.ExplenationLayout.addWidget(self.Mztab,9,0)
        self.ExplenationLayout.addWidget(self.Mztab_expl,10,0)
        self.ExplenationLayout.setContentsMargins(25, 11, 11, 11)


        welcome_Title = "OpenMS ProteomicsLFQ Application  "

        proteomicsLFQ_Title =   " ProteomicsLFQ "

        proteomicsLFQ_Load_Explination ="""Load a folder with your data containing at least mzML and idXML files.\nOther files can be also loaded automatically or manually via the different tools."""
        proteomicsLFQ_Run_Explination ="""Analyze your data with Run ProteomicsLFQ"""

        #assignt Strings to Label as Text

        self.Welcome_Title_Label.setText(welcome_Title)
        self.Hline_Welcome.setFrameStyle(QFrame.HLine | QFrame.Plain)
        self.Hline_Welcome.setLineWidth(2)
        self.Welcome_Title_Label.setLineWidth(2)
        self.proteomicsLFQ_Title_Label.setText(proteomicsLFQ_Title)
        self.HLine_LFQ.setFrameStyle(QFrame.HLine | QFrame.Plain)
        self.HLine_LFQ.setLineWidth(2)
        self.proteomicsLFQ_Load_Explination_Label.setText(proteomicsLFQ_Load_Explination)
        self.hboxLoadExp = QHBoxLayout()
        self.hboxLoadExp.addWidget(self.proteomicsLFQ_Load_Explination_Label)
        self.hboxLoadExp.setContentsMargins(25, 11, 11, 11)
        self.proteomicsLFQ_Run_Explination_Label.setText(proteomicsLFQ_Run_Explination)
        self.hboxRunExp = QHBoxLayout()
        self.hboxRunExp.addWidget(self.proteomicsLFQ_Run_Explination_Label)
        self.hboxRunExp.setContentsMargins(25, 11, 11, 11)

        # setting font for Labels

        self.Welcome_Title_Label.setFont(QFont("Sanserif",20))
        self.proteomicsLFQ_Title_Label.setFont(QFont("Sanserif",20))
        self.proteomicsLFQ_Load_Explination_Label.setFont(QFont("Sanserif",11))
        self.proteomicsLFQ_Run_Explination_Label.setFont(QFont("Sanserif",11))


        my_path = os.path.abspath(os.path.dirname(__file__))
        picture = os.path.join(my_path, "../Pictures/OpenMS2.png")
        self.pixmap = QPixmap(picture)
        self.newpixmap = self.pixmap.scaledToWidth(300)
        self.Picture = QLabel()
        self.Picture.setPixmap(self.newpixmap)
        self.hboxExplenation = QHBoxLayout()
        self.hboxExplenation.addLayout(self.ExplenationLayout)
        self.hboxExplenation.addStretch(1)
        self.hboxExplenation.addWidget(self.Picture)
        self.hboxExplenation.addStretch(1)


        #adding everything to Layouts

        self.main_layout.addWidget(self.Welcome_Title_Label)
        self.main_layout.addWidget(self.Hline_Welcome)
        self.main_layout.addLayout(self.hboxExplenation)
        self.main_layout.addWidget(self.proteomicsLFQ_Title_Label)
        self.main_layout.addWidget(self.HLine_LFQ)
        #self.main_layout.addWidget(self.proteomicsLFQ_Load_Explination_Label)
        self.main_layout.addLayout(self.hboxLoadExp)
        self.main_layout.addLayout(self.hboxLoadBtn)
        self.main_layout.addLayout(self.hbox)
        self.main_layout.addLayout(self.hbox2)
        self.main_layout.addLayout(self.hbox3)
        self.main_layout.addLayout(self.hboxRunExp)
        #self.main_layout.addWidget(self.proteomicsLFQ_Run_Explination_Label)
        self.Hboxlevel1.addStretch(1)
        self.main_layout.addLayout(self.Hboxlevel1)



        self.mainwidget.setLayout(self.main_layout)
        self.setCentralWidget(self.mainwidget)
        self.setWindowTitle('Welcome Screen')

        self.show()

    def get_Output_FileName(self, QLineEdit):
        """
        gets the output filename that the user has given

        Parameters
        ---------
        QLineEdit from which the text has to be saved

        Returns
        -------
        none
        """
        self.Output_Name = QLineEdit.text()

    def get_Threads(self, QLineEdit):
        """
        gets the output threads that the user has given

        Parameters
        ---------
        QLineEdit from which the text has to be saved

        Returns
        -------
        none
        """
        self.Threads_Number = QLineEdit.text()

    def get_ProteinFDR(self, QLineEdit):
        """
        gets the output number that the user has given

        Parameters
        ---------
        QLineEdit from which the text has to be saved

        Returns
        -------
        none
        """
        self.ProteiFDR_Number = QLineEdit.text()