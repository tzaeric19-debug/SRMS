THEME_NAMES = ["Current", "Mono Blue", "Dusk"]

_THEME_TOKENS = {
    "Current": {
        "app_bg": "#081225",
        "surface": "rgba(15,23,42,0.96)",
        "surface_alt": "rgba(30,41,59,0.88)",
        "input_bg": "rgba(15,23,42,0.95)",
        "table_bg_0": "rgba(2,6,23,0.98)",
        "table_bg_1": "rgba(15,23,42,0.96)",
        "header_bg": "#17253c",
        "text": "#e2e8f0",
        "text_soft": "#dbeafe",
        "muted": "#94a3b8",
        "border": "rgba(59,130,246,0.24)",
        "primary": "#2563eb",
        "primary_2": "#3b82f6",
        "success": "#10b981",
        "danger": "#ef4444",
        "tooltip_bg": "#111827",
    },
    "Mono Blue": {
        "app_bg": "#f5f7fb",
        "surface": "rgba(3,7,18,0.96)",
        "surface_alt": "rgba(15,23,42,0.92)",
        "input_bg": "#ffffff",
        "table_bg_0": "rgba(2,6,23,0.98)",
        "table_bg_1": "rgba(17,24,39,0.96)",
        "header_bg": "#05070a",
        "text": "#111827",
        "text_soft": "#f8fafc",
        "muted": "#64748b",
        "border": "rgba(37,99,235,0.30)",
        "primary": "#2563eb",
        "primary_2": "#60a5fa",
        "success": "#0ea56f",
        "danger": "#dc2626",
        "tooltip_bg": "#030712",
    },
    "Dusk": {
        "app_bg": "#d8dbe2",
        "surface": "rgba(17,24,39,0.88)",
        "surface_alt": "rgba(31,41,55,0.76)",
        "input_bg": "rgba(248,250,252,0.92)",
        "table_bg_0": "rgba(17,24,39,0.98)",
        "table_bg_1": "rgba(31,41,55,0.94)",
        "header_bg": "#1f2937",
        "text": "#111827",
        "text_soft": "#f1f5f9",
        "muted": "#6b7280",
        "border": "rgba(59,130,246,0.28)",
        "primary": "#2563eb",
        "primary_2": "#38bdf8",
        "success": "#10b981",
        "danger": "#ef4444",
        "tooltip_bg": "#111827",
    },
}

_ALIASES = {
    "Dark": "Current",
    "Light": "Mono Blue",
    "Black & White": "Mono Blue",
    "Black White Blue": "Mono Blue",
}


def normalize_theme_name(theme_name):
    return _ALIASES.get(theme_name, theme_name if theme_name in _THEME_TOKENS else "Current")


def _build(tokens):
    return f"""
/* =========================================
   SRMS GLOBAL THEME
========================================= */

QWidget{{
    background:{tokens['app_bg']};
    color:{tokens['text']};
    font-family:Inter,Segoe UI,Arial;
    font-size:15px;
    font-weight:600;
}}

QLabel{{
    color:{tokens['text']};
    background:transparent;
    font-weight:650;
}}

QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox{{
    background:{tokens['input_bg']};
    border:1px solid {tokens['border']};
    border-radius:12px;
    padding:10px 14px;
    color:{tokens['text']};
    min-height:22px;
}}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus{{
    border:1px solid {tokens['primary_2']};
}}

QComboBox{{
    background:{tokens['input_bg']};
    border:1px solid {tokens['border']};
    border-radius:12px;
    padding:10px 14px;
    color:{tokens['text']};
    min-height:22px;
}}

QComboBox:hover{{
    border:1px solid {tokens['primary_2']};
}}

QComboBox::drop-down{{
    border:none;
    width:28px;
}}

QComboBox QAbstractItemView{{
    background:{tokens['table_bg_1']};
    color:#f8fafc;
    border:1px solid {tokens['border']};
    selection-background-color:{tokens['primary']};
    selection-color:white;
}}

QPushButton{{
    background:qlineargradient(
        x1:0,y1:0,x2:1,y2:1,
        stop:0 {tokens['primary_2']},
        stop:1 {tokens['primary']}
    );
    border:none;
    border-radius:14px;
    color:white;
    font-weight:850;
    padding:12px 16px;
    min-height:22px;
}}

QPushButton:hover{{
    background:qlineargradient(
        x1:0,y1:0,x2:1,y2:1,
        stop:0 #60a5fa,
        stop:1 {tokens['primary_2']}
    );
}}

QPushButton:pressed{{
    background:#1e40af;
}}

QTableWidget, QTableView, QListWidget, QTreeWidget{{
    background:qlineargradient(
        x1:0,y1:0,x2:1,y2:1,
        stop:0 {tokens['table_bg_0']},
        stop:1 {tokens['table_bg_1']}
    );
    color:#f8fafc;
    alternate-background-color:{tokens['surface_alt']};
    border:1px solid {tokens['border']};
    border-radius:16px;
    gridline-color:rgba(148,163,184,0.18);
    selection-background-color:{tokens['primary']};
    selection-color:white;
}}

QTableWidget::item, QTableView::item, QListWidget::item, QTreeWidget::item{{
    color:#f8fafc;
    padding:8px;
}}

QHeaderView::section{{
    background:{tokens['header_bg']};
    color:#ffffff;
    border:none;
    padding:10px;
    font-weight:900;
}}

QGroupBox, QFrame#GlassCard, QFrame#HeaderFrame, QFrame#QuickActionsPanel, QFrame#SchoolInfoPanel{{
    background:qlineargradient(
        x1:0,y1:0,x2:1,y2:1,
        stop:0 {tokens['surface']},
        stop:1 {tokens['surface_alt']}
    );
    border:1px solid rgba(148,163,184,0.28);
    border-radius:18px;
    color:{tokens['text_soft']};
}}

QGroupBox::title{{
    color:{tokens['primary_2']};
    font-weight:900;
    subcontrol-origin:margin;
    left:14px;
    padding:0 6px;
}}

QTabWidget::pane{{
    border:1px solid {tokens['border']};
    border-radius:12px;
}}

QTabBar::tab{{
    background:{tokens['surface_alt']};
    color:{tokens['text_soft']};
    padding:10px 16px;
    border-top-left-radius:10px;
    border-top-right-radius:10px;
    font-weight:800;
}}

QTabBar::tab:selected{{
    background:{tokens['primary']};
    color:white;
}}

QProgressBar{{
    background:{tokens['table_bg_1']};
    color:white;
    border:1px solid {tokens['border']};
    border-radius:10px;
    min-height:20px;
    text-align:center;
    font-weight:800;
}}

QProgressBar::chunk{{
    background:qlineargradient(
        x1:0,y1:0,x2:1,y2:0,
        stop:0 {tokens['primary_2']},
        stop:1 {tokens['primary']}
    );
    border-radius:9px;
}}

QScrollBar:vertical{{
    width:10px;
    background:transparent;
}}

QScrollBar::handle:vertical{{
    background:{tokens['primary']};
    border-radius:5px;
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical{{
    height:0;
}}

QScrollBar:horizontal{{
    height:10px;
    background:transparent;
}}

QScrollBar::handle:horizontal{{
    background:{tokens['primary']};
    border-radius:5px;
}}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal{{
    width:0;
}}

QMessageBox{{
    background:{tokens['surface']};
    color:{tokens['text_soft']};
}}

QToolTip{{
    background:{tokens['tooltip_bg']};
    color:white;
    border:1px solid {tokens['border']};
    padding:6px;
    border-radius:8px;
}}
"""


def get_theme(theme_name):
    """Return the stylesheet for the selected SRMS theme."""
    return _build(_THEME_TOKENS[normalize_theme_name(theme_name)])


# Backward-compatible constants used by older modules.
DARK_STYLE = get_theme("Current")
LIGHT_STYLE = get_theme("Mono Blue")
APP_STYLE = DARK_STYLE
