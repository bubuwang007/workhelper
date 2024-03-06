import re
from openpyxl.styles import Alignment,Font,Color

FONT_NORMAL = Font(name='宋体', size=11)
FONT_WARNING = Font(name='宋体', size=11, color=Color(rgb='FF0000'), bold=True)

ALIGNMENT_CENTER = Alignment(horizontal='center', vertical='center', wrapText=True)
ALIGNMENT_LEFT = Alignment(horizontal='left', vertical='center', wrapText=True)
ALIGNMENT_RIGHT = Alignment(horizontal='right', vertical='center', wrapText=True)

# NUMBER_FORMAT = {
#     'General',
#     '0',
#     '0.00',
#     '#,#',
#     '#,#.00',
#     '0%',
#     '0.00%',
#     '0.00E+00',
#     '# ?/?',
#     '# ??/??',
#     'mm-dd-yy',
#     'd-mmm-yy',
#     'd-mmm',
#     'mmm-yy',
#     'h:mm AM/PM',
#     'h:mm:ss AM/PM',
#     'h:mm',
#     'h:mm:ss',
#     'hh:mm:ss',
#     '@'
# }

def text_length(cell):
    """计算单元格内容长度

    计算方式为: 中文字符长度为1.7, 英文字符长度为1

    长度 = (中文字符数 * 1.7 + 英文字符数) * 字体大小 * 0.12

    Args:
        cell (Cell): 单元格

    Returns:
        float: 单元格内容长度

    """
    format = cell.number_format
    value = str(cell.value)
    size = cell.font.size
    if format == '@' or format == 'General':
        chinese_count = sum(1 for char in value if '\u4e00' <= char <= '\u9fff')
        english_count = len(value) - chinese_count
        ret = (english_count + chinese_count* 1.7) * size * 0.12
    elif re.match(r'0+\.0+', format):
        res = re.search(r'0+\.(0+)', format)
        if res is None:
            raise ValueError(f'Invalid value: {value}')
        ret = (len(res.group(1))+ len(str(int(float(value))))+1) * size *0.12
    else:
        chinese_count = sum(1 for char in value if '\u4e00' <= char <= '\u9fff')
        english_count = len(value) - chinese_count
        ret = (english_count + chinese_count* 1.7) * size * 0.12
    return ret

__all__ = ["FONT_NORMAL", "FONT_WARNING", "ALIGNMENT_CENTER", "ALIGNMENT_LEFT", "ALIGNMENT_RIGHT"]