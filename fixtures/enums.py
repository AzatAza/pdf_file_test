from enum import Enum


class FirstCol(Enum):
    PN = 'PN'
    DESCRIPTION = 'DESCRIPTION'
    LOCATION = 'LOCATION'
    RECEIVER = 'RECEIVER#'
    EXP = 'EXP DATE'
    CERT = 'CERT SOURCE'
    REC = 'REC.DATE'
    BATCH = 'BATCH#'
    REMARK = 'REMARK'
    TAGGED = 'TAGGED BY'
    Qty = 'Qty'


class SecondCol(Enum):
    SN = 'SN'
    CONDITION = 'CONDITION'
    UOM = 'UOM'
    PO = 'PO'
    MFG = 'MFG'
    DOM = 'DOM'
    LOT = 'LOT#'
    NOTES = 'NOTES'
