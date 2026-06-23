DARK_STYLE = """

/* =========================================
   GLOBAL
========================================= */

QWidget{
    background:#081225;
    color:#e2e8f0;
    font-family:Inter,Segoe UI,Arial;
    font-size:15px;
}

/* =========================================
   LABELS
========================================= */

QLabel{
    color:#dbeafe;
    background:transparent;
}

/* =========================================
   LINE EDIT
========================================= */

QLineEdit{
    background:rgba(15,23,42,0.95);
    border:1px solid #1e3a5f;
    border-radius:12px;
    padding:10px 14px;
    color:white;
    min-height:22px;
}

QLineEdit:focus{
    border:1px solid #3b82f6;
}

/* =========================================
   COMBO
========================================= */

QComboBox{
    background:rgba(15,23,42,0.95);
    border:1px solid #1e3a5f;
    border-radius:12px;
    padding:10px 14px;
    color:white;
    min-height:22px;
}

QComboBox:hover{
    border:1px solid #3b82f6;
}

QComboBox::drop-down{
    border:none;
    width:28px;
}

QComboBox QAbstractItemView{
    background:#0f172a;
    color:white;
    border:1px solid #334155;
    selection-background-color:#2563eb;
}

/* =========================================
   BUTTONS
========================================= */

QPushButton{
    background:qlineargradient(
        x1:0,y1:0,x2:1,y2:1,
        stop:0 #2563eb,
        stop:1 #1d4ed8
    );

    border:none;
    border-radius:14px;

    color:white;
    font-weight:600;

    padding:12px 16px;

    min-height:22px;
}

QPushButton:hover{
    background:qlineargradient(
        x1:0,y1:0,x2:1,y2:1,
        stop:0 #3b82f6,
        stop:1 #2563eb
    );
}

QPushButton:pressed{
    background:#1e40af;
}

/* =========================================
   TABLES
========================================= */

QTableWidget{
    background:#0b1427;
    border:1px solid #1e293b;
    border-radius:14px;

    color:white;
    gridline-color:#1e293b;

    selection-background-color:#2563eb;
}

QTableWidget::item{
    padding:8px;
}

QTableWidget::item:selected{
    background:#2563eb;
}

/* =========================================
   TABLE HEADERS
========================================= */

QHeaderView::section{
    background:#17253c;
    color:white;

    border:none;

    padding:10px;

    font-weight:700;
}

/* =========================================
   SCROLLBARS
========================================= */

QScrollBar:vertical{
    width:10px;
    background:transparent;
}

QScrollBar::handle:vertical{
    background:#2563eb;
    border-radius:5px;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical{
    height:0;
}

QScrollBar:horizontal{
    height:10px;
    background:transparent;
}

QScrollBar::handle:horizontal{
    background:#2563eb;
    border-radius:5px;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal{
    width:0;
}

/* =========================================
   MESSAGE BOX
========================================= */

QMessageBox{
    background:#0f172a;
}

/* =========================================
   TOOLTIP
========================================= */

QToolTip{
    background:#111827;
    color:white;
    border:1px solid #334155;
    padding:6px;
    border-radius:8px;
}

"""


LIGHT_STYLE = """

/* =========================================
   GLOBAL
========================================= */

QWidget{
    background:#f8fafc;
    color:#1e293b;
    font-family:Inter,Segoe UI,Arial;
    font-size:15px;
}

/* =========================================
   LABELS
========================================= */

QLabel{
    color:#1e293b;
    background:transparent;
}

/* =========================================
   LINE EDIT
========================================= */

QLineEdit{
    background:#ffffff;
    border:1px solid #cbd5e1;
    border-radius:12px;
    padding:10px 14px;
    color:#1e293b;
    min-height:22px;
}

QLineEdit:focus{
    border:1px solid #2563eb;
}

/* =========================================
   COMBO
========================================= */

QComboBox{
    background:#ffffff;
    border:1px solid #cbd5e1;
    border-radius:12px;
    padding:10px 14px;
    color:#1e293b;
    min-height:22px;
}

QComboBox:hover{
    border:1px solid #2563eb;
}

QComboBox::drop-down{
    border:none;
    width:28px;
}

QComboBox QAbstractItemView{
    background:#ffffff;
    color:#1e293b;
    border:1px solid #e2e8f0;
    selection-background-color:#dbeafe;
    selection-color:#1e40af;
}

/* =========================================
   BUTTONS
========================================= */

QPushButton{
    background:qlineargradient(
        x1:0,y1:0,x2:1,y2:1,
        stop:0 #2563eb,
        stop:1 #1d4ed8
    );

    border:none;
    border-radius:14px;

    color:white;
    font-weight:600;

    padding:12px 16px;

    min-height:22px;
}

QPushButton:hover{
    background:qlineargradient(
        x1:0,y1:0,x2:1,y2:1,
        stop:0 #3b82f6,
        stop:1 #2563eb
    );
}

QPushButton:pressed{
    background:#1e40af;
}

/* =========================================
   TABLES
========================================= */

QTableWidget{
    background:#ffffff;
    border:1px solid #e2e8f0;
    border-radius:14px;

    color:#1e293b;
    gridline-color:#e2e8f0;

    selection-background-color:#dbeafe;
    selection-color:#1e40af;
}

QTableWidget::item{
    padding:8px;
}

QTableWidget::item:selected{
    background:#dbeafe;
    color:#1e40af;
}

/* =========================================
   TABLE HEADERS
========================================= */

QHeaderView::section{
    background:#f1f5f9;
    color:#1e293b;

    border:none;

    padding:10px;

    font-weight:700;
}

/* =========================================
   SCROLLBARS
========================================= */

QScrollBar:vertical{
    width:10px;
    background:transparent;
}

QScrollBar::handle:vertical{
    background:#93c5fd;
    border-radius:5px;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical{
    height:0;
}

QScrollBar:horizontal{
    height:10px;
    background:transparent;
}

QScrollBar::handle:horizontal{
    background:#93c5fd;
    border-radius:5px;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal{
    width:0;
}

/* =========================================
   MESSAGE BOX
========================================= */

QMessageBox{
    background:#ffffff;
}

/* =========================================
   TOOLTIP
========================================= */

QToolTip{
    background:#ffffff;
    color:#1e293b;
    border:1px solid #e2e8f0;
    padding:6px;
    border-radius:8px;
}

"""

# Default to dark theme for backward compatibility
APP_STYLE = DARK_STYLE


def get_theme(theme_name):
    """Return the stylesheet for the given theme name."""
    if theme_name == "Light":
        return LIGHT_STYLE
    return DARK_STYLE
