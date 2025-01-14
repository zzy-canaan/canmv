import uctypes
from mpp import video_def

# RGB Formats
PIXEL_FORMAT_RGB_444 = const(0)
PIXEL_FORMAT_RGB_555 = const(1)
PIXEL_FORMAT_RGB_565 = const(2)
PIXEL_FORMAT_RGB_888 = const(3)

PIXEL_FORMAT_BGR_444 = const(4)
PIXEL_FORMAT_BGR_555 = const(5)
PIXEL_FORMAT_BGR_565 = const(6)
PIXEL_FORMAT_BGR_888 = const(7)

PIXEL_FORMAT_ARGB_1555 = const(8)
PIXEL_FORMAT_ARGB_4444 = const(9)
PIXEL_FORMAT_ARGB_8565 = const(10)
PIXEL_FORMAT_ARGB_8888 = const(11)
PIXEL_FORMAT_ARGB_2BPP = const(12)

PIXEL_FORMAT_ABGR_1555 = const(13)
PIXEL_FORMAT_ABGR_4444 = const(14)
PIXEL_FORMAT_ABGR_8565 = const(15)
PIXEL_FORMAT_ABGR_8888 = const(16)

PIXEL_FORMAT_BGRA_8888 = const(17)

PIXEL_FORMAT_RGB_MONOCHROME_8BPP = const(18)

# RGB Bayer Formats
PIXEL_FORMAT_RGB_BAYER_8BPP = const(19)
PIXEL_FORMAT_RGB_BAYER_10BPP = const(20)
PIXEL_FORMAT_RGB_BAYER_12BPP = const(21)
PIXEL_FORMAT_RGB_BAYER_14BPP = const(22)
PIXEL_FORMAT_RGB_BAYER_16BPP = const(23)

# YUV Planar Formats
PIXEL_FORMAT_YVU_PLANAR_422 = const(24)
PIXEL_FORMAT_YVU_PLANAR_420 = const(25)
PIXEL_FORMAT_YVU_PLANAR_444 = const(26)

# YUV Semi-Planar Formats
PIXEL_FORMAT_YVU_SEMIPLANAR_422 = const(27)
PIXEL_FORMAT_YVU_SEMIPLANAR_420 = const(28)
PIXEL_FORMAT_YVU_SEMIPLANAR_444 = const(29)

PIXEL_FORMAT_YUV_SEMIPLANAR_422 = const(30)
PIXEL_FORMAT_YUV_SEMIPLANAR_420 = const(31)
PIXEL_FORMAT_YUV_SEMIPLANAR_444 = const(32)

# YUV Package Formats
PIXEL_FORMAT_YUYV_PACKAGE_422 = const(33)
PIXEL_FORMAT_YVYU_PACKAGE_422 = const(34)
PIXEL_FORMAT_UYVY_PACKAGE_422 = const(35)
PIXEL_FORMAT_VYUY_PACKAGE_422 = const(36)
PIXEL_FORMAT_YYUV_PACKAGE_422 = const(37)
PIXEL_FORMAT_YYVU_PACKAGE_422 = const(38)
PIXEL_FORMAT_UVYY_PACKAGE_422 = const(39)
PIXEL_FORMAT_VUYY_PACKAGE_422 = const(40)
PIXEL_FORMAT_VY1UY0_PACKAGE_422 = const(41)
PIXEL_FORMAT_YUV_PACKAGE_444 = const(42)

PIXEL_FORMAT_YUV_400 = const(43)
PIXEL_FORMAT_UV_420 = const(44)

# SVP Data Formats

# FIXME
# PIXEL_FORMAT_BGR_888_PLANAR = const(45)
# PIXEL_FORMAT_RGB_888_PLANAR = const(46)

PIXEL_FORMAT_BGR_888_PLANAR = const(46)
PIXEL_FORMAT_RGB_888_PLANAR = const(45)

PIXEL_FORMAT_HSV_888_PACKAGE = const(47)
PIXEL_FORMAT_HSV_888_PLANAR = const(48)
PIXEL_FORMAT_LAB_888_PACKAGE = const(49)
PIXEL_FORMAT_LAB_888_PLANAR = const(50)
PIXEL_FORMAT_S8C1 = const(51)
PIXEL_FORMAT_S8C2_PACKAGE = const(52)
PIXEL_FORMAT_S8C2_PLANAR = const(53)
PIXEL_FORMAT_S8C3_PLANAR = const(54)
PIXEL_FORMAT_S16C1 = const(55)
PIXEL_FORMAT_U8C1 = const(56)
PIXEL_FORMAT_U16C1 = const(57)
PIXEL_FORMAT_S32C1 = const(58)
PIXEL_FORMAT_U32C1 = const(59)
PIXEL_FORMAT_U64C1 = const(60)
PIXEL_FORMAT_S64C1 = const(61)

# LE Formats
PIXEL_FORMAT_RGB_565_LE = const(300)
PIXEL_FORMAT_BGR_565_LE = const(301)
PIXEL_FORMAT_BUTT = const(302)

PIXEL_FORMAT_GRAYSCALE = const(303)

VIDEO_FIELD_TOP = const(1)
VIDEO_FIELD_BOTTOM = const(2)
VIDEO_FIELD_INTERLACED = const(3)
VIDEO_FIELD_FRAME = const(4)
VIDEO_FIELD_BUTT = const(5)

VIDEO_FORMAT_LINEAR = const(0)
VIDEO_FORMAT_TILE_64x16 = const(1)
VIDEO_FORMAT_TILE_16x8 = const(2)
VIDEO_FORMAT_LINEAR_DISCRETE = const(3)
VIDEO_FORMAT_BUTT = const(4)

DYNAMIC_RANGE_SDR8 = const(0)
DYNAMIC_RANGE_SDR10 = const(1)
DYNAMIC_RANGE_HDR10 = const(2)
DYNAMIC_RANGE_HLG = const(3)
DYNAMIC_RANGE_SLF = const(4)
DYNAMIC_RANGE_XDR = const(5)
DYNAMIC_RANGE_BUTT = const(6)

COLOR_GAMUT_BT601 = const(0)
COLOR_GAMUT_BT709 = const(1)
COLOR_GAMUT_BT2020 = const(2)
COLOR_GAMUT_USER = const(3)
COLOR_GAMUT_BUTT = const(4)

COMPRESS_MODE_NONE = const(0)
COMPRESS_MODE_SEG = const(1)
COMPRESS_MODE_TILE = const(2)
COMPRESS_MODE_LINE = const(3)
COMPRESS_MODE_FRAME = const(4)
COMPRESS_MODE_BUTT = const(5)

def k_video_supplement(**kwargs):
    layout= uctypes.NATIVE
    buf = bytearray(uctypes.sizeof(video_def.k_video_supplement_desc), layout)
    s = uctypes.struct(uctypes.addressof(buf), video_def.k_video_supplement_desc, layout)
    video_def.k_video_supplement_parse(s, kwargs)
    return s

def k_video_frame(**kwargs):
    layout= uctypes.NATIVE
    buf = bytearray(uctypes.sizeof(video_def.k_video_frame_desc), layout)
    s = uctypes.struct(uctypes.addressof(buf), video_def.k_video_frame_desc, layout)
    video_def.k_video_frame_parse(s, kwargs)
    return s

def k_video_frame_info(**kwargs):
    layout= uctypes.NATIVE
    buf = bytearray(uctypes.sizeof(video_def.k_video_frame_info_desc), layout)
    s = uctypes.struct(uctypes.addressof(buf), video_def.k_video_frame_info_desc, layout)
    video_def.k_video_frame_info_parse(s, kwargs)
    return s

def vb_mgmt_dump_vicap_config(**kwargs):
    layout = uctypes.NATIVE
    buf = bytearray(uctypes.sizeof(video_def.vb_mgmt_dump_vicap_config_desc), layout)
    s = uctypes.struct(uctypes.addressof(buf), video_def.vb_mgmt_dump_vicap_config_desc, layout)
    video_def.vb_mgmt_dump_vicap_config_parse(s, kwargs)
    return s

def vb_mgmt_vicap_image(**kwargs):
    layout = uctypes.NATIVE
    buf = bytearray(uctypes.sizeof(video_def.vb_mgmt_vicap_image_desc), layout)
    s = uctypes.struct(uctypes.addressof(buf), video_def.vb_mgmt_vicap_image_desc, layout)
    video_def.vb_mgmt_vicap_image_parse(s, kwargs)
    return s

def is_vb_mgmt_vicap_image(obj):
    if isinstance(obj, uctypes.struct):
        return uctypes.sizeof(video_def.vb_mgmt_vicap_image_desc) == uctypes.sizeof(obj)
    return False
