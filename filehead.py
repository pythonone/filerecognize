# -*- coding:utf-8 -*-
#__author__='Kakarotto'
###
# 文章：Python通过文件头来判断文件类型
# 作者：http://aminby.net
###

import struct


# 支持文件类型
# 用16进制字符串的目的是可以知道文件头是多少字节
# 各种文件头的长度不一样，少半2字符，长则8字符
def typeList():
    return {
        "52617221": "EXT_RAR",
        "504B0304": "EXT_ZIP",
        "FFD8FF": "JPEG",
        "89504E47": "PNG",
        "47494638": "GIF",
        "49492A00": "TIFF",
        "424D": "Windows",
        "41433130": "CAD",
        "38425053": "Adobe",
        "7B5C727466": "Rich",
        "3C3F786D6C": "XML",
        "68746D6C3E": "HTML",
        "44656C69766572792D646174653A": "Email",
        "CFAD12FEC5FD746F": "Outlook",
        "2142444E": "Outlook",
        "D0CF11E0": "MS",
        "5374616E64617264204A": "MS",
        "FF575043": "WordPerfect",
        "252150532D41646F6265": "Postscript",
        "255044462D312E": "Adobe",
        "AC9EBD8F": "Quicken",
        "E3828596": "Windows",
        "504B0304": "ZIP",
        "52617221": "RAR",
        "57415645": "Wave",
        "41564920": "AVI",
        "2E7261FD": "Real",
        "2E524D46": "Real",
        "000001BA": "MPEG",
        "000001B3": "MPEG",
        "6D6F6F76": "Quicktime",
        "3026B2758E66CF11": "Windows",
        "4D546864": "MIDI"
    }


# 字节码转16进制字符串
def bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()


# 获取文件类型
def filetype(filename):
    binfile = open(filename, 'rb')  # 必需二制字读取
    tl = typeList()
    ftype = 'unknown'
    for hcode in tl.keys():
        numOfBytes = len(hcode) / 2  # 需要读多少字节
        binfile.seek(0)  # 每次读取都要回到文件头，不然会一直往后读取
        hbytes = struct.unpack_from("B" * numOfBytes, binfile.read(numOfBytes))  # 一个 "B"表示一个字节
        f_hcode = bytes2hex(hbytes)
        if f_hcode == hcode:
            ftype = tl[hcode]
            break
    binfile.close()
    return ftype,f_hcode


if __name__ == '__main__':
    ipath = 'D:\\迅雷下载\\insurance_policy'
    uipath = unicode(ipath, "utf8")
    print filetype(uipath)