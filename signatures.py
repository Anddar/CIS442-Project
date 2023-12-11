# Written By: Andrew Raposo
# Date: 2023-10-23
# Description: List of file signatures for the masquaraded file finder.

# Reference: This project was given by the University of Massachusetts Dartmouth for the course 
# CIS 442 - Digital Forensics taught by Professor Gohkan Kul.

file_signatures = {'wk1': [b'\x00\x00\x02\x00\x06\x04\x06\x00\x08\x00\x00\x00\x00\x00'],
 'wk3': [b'\x00\x00\x1a\x00\x00\x10\x04\x00\x00\x00\x00\x00'],
 'wk4': [b'\x00\x00\x1a\x00\x02\x10\x04\x00\x00\x00\x00\x00'],
 'wk5': [b'\x00\x00\x1a\x00\x02\x10\x04\x00\x00\x00\x00\x00'],
 '123': [b'\x00\x00\x1a\x00\x05\x10\x04'],
 'qxd': [b'\x00\x00IIXPR', b'\x00\x00MMXPR'],
 'psafe3': [b'PWS3'],
 'pcap': [b'\xd4\xc3\xb2\xa1', b'\xa1\xb2\xc3\xd4', b'M<\xb2\xa1', b'\xa1\xb2<M'],
 'pcapng': [b'\n\r\r\n'],
 'rpm': [b'\xed\xab\xee\xdb'],
 'sqlitedb': [b'SQLite format 3\x00'],
 'sqlite': [b'SQLite format 3\x00'],
 'db': [b'SQLite format 3\x00'],
 'bin': [b'SP01'],
 'wad': [b'IWAD'],
 'PIC': [b'\x00'],
 'PIF': [b'\x00'],
 'SEA': [b'\x00'],
 'YTR': [b'\x00'],
 'PDB': [b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'],
 'DBA': [b'\xbe\xba\xfe\xca', b'\x00\x01BD'],
 'TDA': [b'\x00\x01DT'],
 'TDF$': [b'TDF$'],
 'TDEF': [b'TDEF'],
 'ico': [b'\x00\x00\x01\x00'],
 'icns': [b'icns'],
 '3gp': [b'ftyp3g'],
 '3g2': [b'ftyp3g'],
 'heic': [b'ftypheic', b'ftypm'],
 'z': [b'\x1f\x9d', b'\x1f\xa0', b'\x1f\xa0'],
 'tar.z': [b'\x1f\x9d', b'\x1f\xa0', b'\x1f\xa0'],
 'lzh': [b'-hl0-', b'-hl5-'],
 'bac': [b'BACKMIKEDISK'],
 'idx': [b'INDX'],
 'plist': [b'bplist'],
 'bz2': [b'BZh'],
 'gif': [b'GIF87a', b'GIF89a'],
 'tif': [b'II*\x00', b'MM\x00*', b'MM\x00*'],
 'tiff': [b'II*\x00', b'MM\x00*', b'MM\x00*'],
 'cr2': [b'II*\x00\x10\x00\x00\x00CR'],
 'cin': [b'\x80*_\xd7'],
 'nui': [b'NURUIMG', b'NURUPAL'],
 'nup': [b'NURUIMG', b'NURUPAL'],
 'dpx': [b'SDPX', b'XPDS'],
 'exr': [b'v/1\x01'],
 'bpg': [b'BPG\xfb'],
 'jpg': [b'\xff\xd8\xff\xdb', b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01', b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01', b'\xff\xd8\xff\xee', b'\xff\xd8\xff\xee',
 'FFD8FFE1????457869660000',
 'FFD8FFE1????457869660000', b'\xff\xd8\xff\xe0'],
 'jpeg': [b'\xff\xd8\xff\xdb', b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01', b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01', b'\xff\xd8\xff\xee', b'\xff\xd8\xff\xee',
 'FFD8FFE1????457869660000',
 'FFD8FFE1????457869660000', b'\xff\xd8\xff\xe0'],
 'jp2': [b'\x00\x00\x00\x0cjP  \r\n\x87\n', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ'],
 'j2k': [b'\x00\x00\x00\x0cjP  \r\n\x87\n', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ'],
 'jpf': [b'\x00\x00\x00\x0cjP  \r\n\x87\n', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ'],
 'jpm': [b'\x00\x00\x00\x0cjP  \r\n\x87\n', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ'],
 'jpg2': [b'\x00\x00\x00\x0cjP  \r\n\x87\n', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ'],
 'j2c': [b'\x00\x00\x00\x0cjP  \r\n\x87\n', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ'],
 'jpc': [b'\x00\x00\x00\x0cjP  \r\n\x87\n', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ'],
 'jpx': [b'\x00\x00\x00\x0cjP  \r\n\x87\n', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ'],
 'mj2': [b'\x00\x00\x00\x0cjP  \r\n\x87\n', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ', b'\xffO\xffQ'],
 'qoi': [b'qoif'],
 'ilbm': ['464F524D????????494C424D',
 '464F524D????????38535658',
 '464F524D????????4143424D',
 '464F524D????????414E424D',
 '464F524D????????414E494D',
 '464F524D????????46415858',
 '464F524D????????46545854',
 '464F524D????????534D5553',
 '464F524D????????434D5553',
 '464F524D????????5955564E',
 '464F524D????????46414E54',
 '464F524D????????41494646'],
 'lbm': ['464F524D????????494C424D',
 '464F524D????????38535658',
 '464F524D????????4143424D',
 '464F524D????????414E424D',
 '464F524D????????414E494D',
 '464F524D????????46415858',
 '464F524D????????46545854',
 '464F524D????????534D5553',
 '464F524D????????434D5553',
 '464F524D????????5955564E',
 '464F524D????????46414E54',
 '464F524D????????41494646'],
 'ibm': ['464F524D????????494C424D',
 '464F524D????????38535658',
 '464F524D????????4143424D',
 '464F524D????????414E424D',
 '464F524D????????414E494D',
 '464F524D????????46415858',
 '464F524D????????46545854',
 '464F524D????????534D5553',
 '464F524D????????434D5553',
 '464F524D????????5955564E',
 '464F524D????????46414E54',
 '464F524D????????41494646'],
 'iff': ['464F524D????????494C424D',
 '464F524D????????38535658',
 '464F524D????????4143424D',
 '464F524D????????414E424D',
 '464F524D????????414E494D',
 '464F524D????????46415858',
 '464F524D????????46545854',
 '464F524D????????534D5553',
 '464F524D????????434D5553',
 '464F524D????????5955564E',
 '464F524D????????46414E54',
 '464F524D????????41494646'],
 '8svx': ['464F524D????????38535658',
 '464F524D????????41494646', b'.snd'],
 '8sv': ['464F524D????????38535658',
 '464F524D????????41494646', b'.snd'],
 'svx': ['464F524D????????38535658',
 '464F524D????????41494646', b'.snd'],
 'snd': ['464F524D????????38535658',
 '464F524D????????41494646', b'.snd'],
 'acbm': [b'464F524D????????4143424D'],
 'anbm': ['464F524D????????414E424D'],
 'anim': ['464F524D????????414E494D'],
 'faxx': ['464F524D????????46415858'],
 'fax': ['464F524D????????46415858'],
 'ftxt': ['464F524D????????46545854'],
 'smus': ['464F524D????????534D5553',
 '464F524D????????434D5553'],
 'smu': ['464F524D????????534D5553',
 '464F524D????????434D5553'],
 'mus': ['464F524D????????534D5553',
 '464F524D????????434D5553'],
 'cmus': ['464F524D????????434D5553'],
 'yuvn': ['464F524D????????5955564E'],
 'yuv': ['464F524D????????5955564E'],
 'aiff': ['464F524D????????41494646'],
 'aif': ['464F524D????????41494646'],
 'aifc': ['464F524D????????41494646'],
 'lz': [b'LZIP'],
 'cpio': [b'070707'],
 'exe': [b'MZ', b'ZM', b'RSVKDATA'],
 'dll': [b'MZ', b'ZM', b'RSVKDATA'],
 'mui': [b'MZ', b'ZM', b'RSVKDATA'],
 'sys': [b'MZ', b'ZM', b'RSVKDATA'],
 'scr': [b'MZ', b'ZM', b'RSVKDATA'],
 'cpl': [b'MZ', b'ZM', b'RSVKDATA'],
 'ocx': [b'MZ', b'ZM', b'RSVKDATA'],
 'ax': [b'MZ', b'ZM', b'RSVKDATA'],
 'iec': [b'MZ', b'ZM', b'RSVKDATA'],
 'ime': [b'MZ', b'ZM', b'RSVKDATA'],
 'rs': [b'MZ', b'ZM', b'RSVKDATA'],
 'tsp': [b'MZ', b'ZM', b'RSVKDATA'],
 'fon': [b'MZ', b'ZM', b'RSVKDATA'],
 'efi': [b'MZ', b'ZM', b'RSVKDATA'],
 'zip': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'aar': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'apk': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'docx': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'epub': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'ipa': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'jar': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'kmz': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'maff': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'msix': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'odp': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'ods': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'odt': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'pk3': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'pk4': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'pptx': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'usdz': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'vsdx': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'xlsx': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'xpi': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08', b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
 'rar': [b'Rar!\x1a\x07\x00', b'Rar!\x1a\x07\x01\x00'],
 'png': [b'\x89PNG\r\n\x1a\n', b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'],
 'com': [b'\xc9'],
 'class': [b'\xca\xfe\xba\xbe'],
 'txt': [b'\xef\xbb\xbf', b'\xff\xfe', b'\xff\xfe', b'\xfe\xff', b'\xfe\xff', b'\xff\xfe\x00\x00', b'\xff\xfe\x00\x00', b'\x00\x00\xfe\xff', b'\x00\x00\xfe\xff', b'\x0e\xfe\xff', b'\x0e\xfe\xff'],
 'ps': [b'%!PS'],
 'eps': [b'%!PS-Adobe-3.0 EPSF-3.0', b'%!PS-Adobe-3.1 EPSF-3.0', b'%!PS-Adobe-3.1 EPSF-3.0'],
 'epsf': [b'%!PS-Adobe-3.0 EPSF-3.0', b'%!PS-Adobe-3.1 EPSF-3.0', b'%!PS-Adobe-3.1 EPSF-3.0'],
 'chm': [b'ITSF\x03\x00\x00\x00`\x00\x00\x00'],
 'hlp': [b'?_'],
 'pdf': [b'%PDF-', b'\x25\x50\x44\x46\x2D'],
 'asf': [b'0&\xb2u\x8ef\xcf\x11\xa6\xd9\x00\xaa\x00b\xcel'],
 'wma': [b'0&\xb2u\x8ef\xcf\x11\xa6\xd9\x00\xaa\x00b\xcel'],
 'wmv': [b'0&\xb2u\x8ef\xcf\x11\xa6\xd9\x00\xaa\x00b\xcel'],
 'ogg': [b'OggS'],
 'oga': [b'OggS'],
 'ogv': [b'OggS'],
 'psd': [b'8BPS'],
 'wav': ['52494646????????57415645'],
 'avi': ['52494646????????41564920'],
 'mp3': [b'\xff\xfb', b'\xff\xf3', b'\xff\xf2', b'ID3'],
 'bmp': [b'BM'],
 'dib': [b'BM'],
 'iso': [b'CD001', b'EMU3'],
 'cdi': [b'CD001'],
 'mgw': [b'main.bs'],
 'nes': [b'NES', b'NES\x1a'],
 'd64': [b'\xa02A\xa0\xa0\xa0'],
 'g64': [b'GSR-1541'],
 'd81': [b'\xa03D\xa0\xa0'],
 't64': [b'C64 tape image file'],
 'crt': [b'C64 CARTRIDGE   ', b'-----BEGIN CERTIFICATE-----'],
 'fits': [b'SIMPLE  =                    T'],
 'flac': [b'fLaC'],
 'mid': [b'MThd'],
 'midi': [b'MThd'],
 'doc': [b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1', b'\rDOC'],
 'xls': [b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1', b'\rDOC'],
 'ppt': [b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1', b'\rDOC'],
 'msi': [b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1', b'\rDOC'],
 'msg': [b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1', b'\rDOC'],
 'dex': [b'dex\n035\x00'],
 'vmdk': [b'KDM', b'# Disk Descripto'],
 'crx': [b'Cr24'],
 'fh8': [b'AGD3'],
 'cwk': [b'\x05\x07\x00\x00BOBO\x05\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01', b'\x06\x07\xe1\x00BOBO\x06\x07\xe1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'],
 'toast': [b'ER\x02\x00\x00\x00', b'\x8bER\x02\x00\x00\x00'],
 'dmg': [b'koly'],
 'xar': [b'xar!'],
 'dat': [b'PMOCCMOC', b'regf'],
 'tar': [b'ustar\x0000', b'ustar  \x00'],
 'oar': ['\x4f\x41\x52'],
 'tox': [b'tox3'],
 'MLV': [b'MLVI'],
 '7z': [b"7z\xbc\xaf'\x1c"],
 'gz': [b'\x1f\x8b'],
 'tar.gz': [b'\x1f\x8b'],
 'xz': [b'\xfd7zXZ\x00'],
 'tar.xz': [b'\xfd7zXZ\x00'],
 'lz4': [b'\x04"M\x18'],
 'cab': [b'MSCF', b'ISc('],
 '??': [b"SZDD\x88\xf0'3"],
 'flif': [b'FLIF'],
 'mkv': [b'\x1aE\xdf\xa3'],
 'mka': [b'\x1aE\xdf\xa3'],
 'mks': [b'\x1aE\xdf\xa3'],
 'mk3d': [b'\x1aE\xdf\xa3'],
 'webm': [b'\x1aE\xdf\xa3'],
 'stg': [b'MIL '],
 'djvu': ['41542654464F524D????????444A56'],
 'djv': ['41542654464F524D????????444A56'],
 'der': [b'0\x82'],
 'pem': [b'-----BEGIN CERTIFICATE-----', b'-----BEGIN CERTIFICATE REQUEST-----', b'-----BEGIN PRIVATE KEY-----', b'-----BEGIN DSA PRIVATE KEY-----', b'-----BEGIN REA PRIVATE KEY-----'],
 'csr': [b'-----BEGIN CERTIFICATE REQUEST-----'],
 'key': [b'-----BEGIN PRIVATE KEY-----', b'-----BEGIN DSA PRIVATE KEY-----', b'-----BEGIN REA PRIVATE KEY-----'],
 'ppk': [b'PuTTY-User-Key-File-2:', b'PuTTY-User-Key-File-3:'],
 'pub': [b'-----BEGIN SSH2 KEY-----'],
 'dcm': [b'DICM'],
 'woff': [b'wOFF'],
 'woff2': [b'wOF2'],
 'xml': [b'<?xml ', b'<\x00?\x00x\x00m\x00l\x00 ', b'\x00<\x00?\x00x\x00m\x00l\x00 ', b'<\x00\x00\x00?\x00\x00\x00x\x00\x00\x00m\x00\x00\x00l\x00\x00\x00 \x00\x00\x00', b'\x00\x00\x00<\x00\x00\x00?\x00\x00\x00x\x00\x00\x00m\x00\x00\x00l\x00\x00\x00 ', b'Lo\xa7\x94\x93@'],
 'wasm': [b'\x00asm'],
 'lep': [b'\xcf\x84\x01'],
 'swf': [b'CWS', b'FWS'],
 'deb': [b'!<arch>\n'],
 'webp': ['52494646????????57454250'],
 'rtf': [b'{\\rtf1'],
 'ts': [b'G', b'\x00\x00\x01\xba', b'\x00\x00\x01\xba', b'\x00\x00\x01\xb3', b'\x00\x00\x01\xb3'],
 'tsv': [b'G', b'\x00\x00\x01\xba', b'\x00\x00\x01\xba', b'\x00\x00\x01\xb3', b'\x00\x00\x01\xb3'],
 'tsa': [b'G', b'\x00\x00\x01\xba', b'\x00\x00\x01\xba', b'\x00\x00\x01\xb3', b'\x00\x00\x01\xb3'],
 'mpg': [b'G', b'\x00\x00\x01\xba', b'\x00\x00\x01\xba', b'\x00\x00\x01\xb3', b'\x00\x00\x01\xb3'],
 'mpeg': [b'G', b'\x00\x00\x01\xba', b'\x00\x00\x01\xba', b'\x00\x00\x01\xb3', b'\x00\x00\x01\xb3'],
 'm2p': [b'\x00\x00\x01\xba'],
 'vob': [b'\x00\x00\x01\xba'],
 'mp4': [b'ftypisom', b'ftypMSNV', b'\x66\x74\x79\x70\x69\x73\x6F\x6D', b'\x66\x74\x79\x70\x4D\x53\x4E\x56'],
 'zlib': [b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01', b'x\x01'],
 'lzfse': [b'bvx2'],
 'orc': [b'ORC'],
 'avro': [b'Obj\x01'],
 'rc': [b'SEQ6'],
 'rbxl': [b'<roblox!'],
 'p25': [b'e\x87xV'],
 'obt': [b'e\x87xV'],
 'pcv': [b'UU\xaa\xaa'],
 'pbt': [b'xV4'],
 'pdt': [b'xV4'],
 'pea': [b'xV4'],
 'peb': [b'xV4'],
 'pet': [b'xV4'],
 'pgt': [b'xV4'],
 'pict': [b'xV4'],
 'pjt': [b'xV4'],
 'pkt': [b'xV4'],
 'pmt': [b'xV4'],
 'ez2': [b'EMX2'],
 'ez3': [b'EMU3'],
 'luac': [b'\x1bLua'],
 'alias': [b'book\x00\x00\x00\x00mark\x00\x00\x00\x00'],
 'Identifier': [b'[ZoneTransfer]'],
 'eml': [b'Received:'],
 'tde': [b' \x02\x01b\xa0\x1e\xab\x07\x02\x00\x00\x00'],
 'kdb': [b'7H\x03\x02\x00\x00\x00\x00X509KEY'],
 'pgp': ['85????03'],
 'zst': [b'(\xb5/\xfd'],
 'sml': [b':)\n'],
 'srt': [b'1\n00'],
 'vpk': [b'4\x12\xaaU'],
 'ace': [b'**ACE**'],
 'arj': [b'`\xea'],
 '??_': [b'KWAJ', b'SZDD'],
 'zoo': [b'ZOO'],
 'pbm': [b'P1\n', b'P4\n'],
 'pgm': [b'P2\n', b'P5\n'],
 'ppm': [b'P3\n', b'P6\n'],
 'wmf': [b'\xd7\xcd\xc6\x9a'],
 'xcf': [b'gimp xcf'],
 'xpm': [b'/* XPM */'],
 'aff': [b'AFF'],
 'Ex01': [b'EVF2'],
 'e01': [b'EVF'],
 'qcow': [b'QFI'],
 'ani': ['52494646????????41434F4E'],
 'cda': ['52494646????????43444441'],
 'qcp': ['52494646????????514C434D'],
 'dcr': ['52494658????????4647444D',
 '58464952????????4D444746'],
 'dir': ['52494658????????4D563933',
 '58464952????????3339564D',
 '58464952????????3339564D',
 '58464952????????3339564D'],
 'dxr': ['52494658????????4D563933',
 '58464952????????3339564D',
 '58464952????????3339564D',
 '58464952????????3339564D'],
 'drx': ['52494658????????4D563933',
 '58464952????????3339564D',
 '58464952????????3339564D',
 '58464952????????3339564D'],
 'flv': [b'FLV'],
 'vdi': [b'<<< Oracle VM VirtualBox Disk Image >>>'],
 'vhd': [b'connectix'],
 'vhdx': [b'vhdxfile'],
 'isz': [b'IsZ!'],
 'daa': [b'DAA'],
 'evt': [b'LfLe'],
 'evtx': [b'ElfFile'],
 'sdb': [b'sdbf'],
 'grp': [b'PMCC'],
 'icm': [b'KCMS'],
 'hiv': [b'regf'],
 'pst': [b'!BDN'],
 'drc': [b'DRACO'],
 'grib': [b'GRIB'],
 'grib2': [b'GRIB'],
 'blend': [b'BLENDER'],
 'jxl': [b'\x00\x00\x00\x0cJXL \r\n\x87\n', b'\xff\n'],
 'ttf': [b'\x00\x01\x00\x00\x00'],
 'tte': [b'\x00\x01\x00\x00\x00'],
 'dfont': [b'\x00\x01\x00\x00\x00'],
 'otf': [b'OTTO'],
 'wim': [b'MSWIM\x00\x00\x00\xd0\x00\x00\x00\x00'],
 'swm': [b'MSWIM\x00\x00\x00\xd0\x00\x00\x00\x00'],
 'esd': [b'MSWIM\x00\x00\x00\xd0\x00\x00\x00\x00'],
 'slob': [b'!-1SLOB\x1f'],
 'voc': [b'Creative Voice File\x1a\x1a\x00'],
 'au': [b'.snd'],
 'hazelrules': [b'HZLR\x00\x00\x00\x18'],
 'flp': [b'FLhd'],
 'flm': [b'10LF'],
 'mny': [b'\x00\x01\x00\x00MSISAM Database'],
 'accdb': [b'\x00\x01\x00\x00Standard ACE DB'],
 'mdb': [b'\x00\x01\x00\x00Standard Jet DB'],
 'drw': [b'\x01\xff\x02\x04\x03\x02'],
 'dss': [b'\x02dss', b'\x03dss'],
 'adx': [b'\x03\x00\x00\x00APPR'],
 'indd': [b'\x06\x06\xed\xf5\xd8\x1dF\xe5\xbd1\xef\xe7\xfet\xb7\x1d'],
 'mxf': [b'\x06\x0e+4\x02\x05\x01\x01\r\x01\x02\x01\x01\x02'],
 'skf': [b'\x07SKF'],
 'dtd': [b'\x07dt2ddtd'],
 'wallet': [b'\n\x16org.bitcoin.pr'],
 'nri': [b'\x0eNeroISO'],
 'wks': [b'\x0eWKS'],
 'sib': [b'\x0fSIBELIUS'],
 'dsp': [b'# Microsoft Developer Studio'],
 'amr': [b'#!AMR'],
 'sil': [b'#!SILK\n'],
 'hdr': [b'#?RADIANCE\n', b'ni1\x00'],
 'vbe': [b'#@~^'],
 'cdb': [b'\r\xf0\x1d\xc0'],
 'm3u': [b'#EXTM3U'],
 'm3u8': [b'#EXTM3U'],
 'm': [b'mdf\x00'],
 'pak': [b'KPKA'],
 'arc': [b'ARC'],
 'pl': [b'\xd0OPS'],
 'nii': [b'n+1\x00']
}