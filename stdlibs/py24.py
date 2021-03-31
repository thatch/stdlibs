# Copyright 2021 John Reese
# Licensed under the MIT license

# Generated by stdlibs/fetch.py

module_names = frozenset(
    [
        "AL",
        "Audio_mac",
        "BaseHTTPServer",
        "Bastion",
        "CD",
        "CDIO",
        "CDROM",
        "CGIHTTPServer",
        "CL",
        "CL_old",
        "Canvas",
        "Carbon",
        "ColorPicker",
        "ConfigParser",
        "Cookie",
        "DEVICE",
        "DLFCN",
        "Dialog",
        "DocXMLRPCServer",
        "ERRNO",
        "EasyDialogs",
        "FILE",
        "FL",
        "FileDialog",
        "FixTk",
        "FrameWork",
        "GET",
        "GL",
        "GLWS",
        "HTMLParser",
        "IN",
        "IOCTL",
        "MacOS",
        "MimeWriter",
        "MiniAEFrame",
        "Nav",
        "OSATerminology",
        "Para",
        "PixMapWrapper",
        "Queue",
        "SOCKET",
        "STROPTS",
        "SUNAUDIODEV",
        "SV",
        "ScrolledText",
        "SimpleDialog",
        "SimpleHTTPServer",
        "SimpleXMLRPCServer",
        "SocketServer",
        "StringIO",
        "TYPES",
        "Tix",
        "Tkconstants",
        "Tkdnd",
        "Tkinter",
        "UserDict",
        "UserList",
        "UserString",
        "WAIT",
        "WASTEconst",
        "_AE",
        "_AH",
        "_App",
        "_CF",
        "_CG",
        "_CarbonEvt",
        "_Cm",
        "_Ctl",
        "_Dlg",
        "_Drag",
        "_Evt",
        "_File",
        "_Fm",
        "_Folder",
        "_Help",
        "_IBCarbon",
        "_Icn",
        "_LWPCookieJar",
        "_Launch",
        "_List",
        "_Menu",
        "_Mlte",
        "_MozillaCookieJar",
        "_OSA",
        "_Qd",
        "_Qdoffs",
        "_Qt",
        "_Res",
        "_Scrap",
        "_Snd",
        "_TE",
        "_Win",
        "__builtin__",
        "__future__",
        "__phello__",
        "_bisect",
        "_bsddb",
        "_codecs",
        "_codecs_cn",
        "_codecs_hk",
        "_codecs_iso2022",
        "_codecs_jp",
        "_codecs_kr",
        "_codecs_tw",
        "_csv",
        "_curses",
        "_curses_panel",
        "_emx_link",
        "_heapq",
        "_hotshot",
        "_locale",
        "_multibytecodec",
        "_random",
        "_socket",
        "_sre",
        "_ssl",
        "_strptime",
        "_subprocess",
        "_symtable",
        "_testcapi",
        "_threading_local",
        "_tkinter",
        "_weakref",
        "_winreg",
        "addpack",
        "aepack",
        "aetools",
        "aetypes",
        "aifc",
        "al",
        "anydbm",
        "applesingle",
        "appletrawmain",
        "appletrunner",
        "argvemulator",
        "array",
        "asynchat",
        "asyncore",
        "atexit",
        "audiodev",
        "audioop",
        "autoGIL",
        "base64",
        "bdb",
        "bgenlocations",
        "binascii",
        "binhex",
        "bisect",
        "bsddb",
        "bsddb185",
        "buildtools",
        "bundlebuilder",
        "bz2",
        "cPickle",
        "cStringIO",
        "calendar",
        "cd",
        "cddb",
        "cdplayer",
        "cfmfile",
        "cgi",
        "cgitb",
        "chunk",
        "cl",
        "cmath",
        "cmd",
        "cmp",
        "cmpcache",
        "code",
        "codecs",
        "codehack",
        "codeop",
        "collections",
        "colorsys",
        "commands",
        "compileall",
        "compiler",
        "cookielib",
        "copy",
        "copy_reg",
        "crypt",
        "csv",
        "curses",
        "datetime",
        "dbhash",
        "dbm",
        "decimal",
        "difflib",
        "dircache",
        "dircmp",
        "dis",
        "distutils",
        "dl",
        "doctest",
        "dumbdbm",
        "dummy_thread",
        "dummy_threading",
        "dump",
        "email",
        "encodings",
        "errno",
        "exceptions",
        "fcntl",
        "filecmp",
        "fileinput",
        "find",
        "findertools",
        "fl",
        "flp",
        "fm",
        "fmt",
        "fnmatch",
        "formatter",
        "fpectl",
        "fpetest",
        "fpformat",
        "ftplib",
        "gc",
        "gdbm",
        "gensuitemodule",
        "gestalt",
        "getopt",
        "getpass",
        "gettext",
        "gl",
        "glob",
        "gopherlib",
        "grep",
        "grp",
        "gzip",
        "heapq",
        "hmac",
        "hotshot",
        "htmlentitydefs",
        "htmllib",
        "httplib",
        "ic",
        "icglue",
        "icopen",
        "idlelib",
        "ihooks",
        "imageop",
        "imaplib",
        "imgfile",
        "imghdr",
        "imp",
        "imputil",
        "inspect",
        "itertools",
        "jpeg",
        "keyword",
        "linecache",
        "linuxaudiodev",
        "locale",
        "lockfile",
        "logging",
        "macerrors",
        "macfs",
        "macostools",
        "macpath",
        "macresource",
        "macurl2path",
        "mailbox",
        "mailcap",
        "markupbase",
        "marshal",
        "math",
        "md5",
        "mhlib",
        "mimetools",
        "mimetypes",
        "mimify",
        "mmap",
        "modulefinder",
        "msvcrt",
        "multifile",
        "mutex",
        "netrc",
        "new",
        "newdir",
        "ni",
        "nis",
        "nntplib",
        "nt",
        "ntpath",
        "nturl2path",
        "opcode",
        "operator",
        "optparse",
        "os",
        "os2",
        "os2emxpath",
        "ossaudiodev",
        "packmail",
        "panel",
        "panelparser",
        "parser",
        "pcre",
        "pdb",
        "pickle",
        "pickletools",
        "pimp",
        "pipes",
        "pkgutil",
        "platform",
        "plistlib",
        "poly",
        "popen2",
        "poplib",
        "posix",
        "posixfile",
        "posixpath",
        "pprint",
        "profile",
        "pstats",
        "pty",
        "pure",
        "pwd",
        "py_compile",
        "pyclbr",
        "pydoc",
        "pyexpat",
        "quopri",
        "rand",
        "random",
        "re",
        "readcd",
        "readline",
        "reconvert",
        "regex",
        "regex_syntax",
        "regsub",
        "repr",
        "resource",
        "rexec",
        "rfc822",
        "rgbimg",
        "riscosenviron",
        "riscospath",
        "rlcompleter",
        "robotparser",
        "rourl2path",
        "sched",
        "select",
        "sets",
        "sgi",
        "sgmllib",
        "sha",
        "shelve",
        "shlex",
        "shutil",
        "signal",
        "site",
        "smtpd",
        "smtplib",
        "sndhdr",
        "socket",
        "sre",
        "sre_compile",
        "sre_constants",
        "sre_parse",
        "stat",
        "statcache",
        "statvfs",
        "string",
        "stringold",
        "stringprep",
        "strop",
        "struct",
        "subprocess",
        "sunau",
        "sunaudio",
        "sunaudiodev",
        "sv",
        "symbol",
        "symtable",
        "sys",
        "syslog",
        "tabnanny",
        "tarfile",
        "tb",
        "telnetlib",
        "tempfile",
        "terminalcommand",
        "termios",
        "textwrap",
        "this",
        "thread",
        "threading",
        "time",
        "timeit",
        "timing",
        "tkColorChooser",
        "tkCommonDialog",
        "tkFileDialog",
        "tkFont",
        "tkMessageBox",
        "tkSimpleDialog",
        "toaiff",
        "token",
        "tokenize",
        "torgb",
        "trace",
        "traceback",
        "tty",
        "turtle",
        "types",
        "tzparse",
        "unicodedata",
        "unittest",
        "urllib",
        "urllib2",
        "urlparse",
        "user",
        "util",
        "uu",
        "videoreader",
        "warnings",
        "waste",
        "wave",
        "weakref",
        "webbrowser",
        "whatsound",
        "whichdb",
        "whrandom",
        "winsound",
        "xdrlib",
        "xml",
        "xmllib",
        "xmlrpclib",
        "xx",
        "xxsubtype",
        "zipfile",
        "zipimport",
        "zlib",
        "zmod",
    ]
)