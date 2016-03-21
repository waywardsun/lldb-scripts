## lldb-script

A collection of Python scripts for instrumenting LLDB.

### Scripts

[objc_msgSend.py](https://github.com/LifeForm-Labs/lldb-scripts/blob/master/objc_msgSend.py)
[xpc.py](https://github.com/LifeForm-Labs/lldb-scripts/blob/master/xpc.py)

### Example

#### .lldbinit
```
command script import objc_msgSend.py
objc_msgSend
```

#### Sample Output
```
replayd : 2015-12-14 19:32:59.596294 : ID : <RPRecordingManager: 0x125612a20>
replayd : 2015-12-14 19:33:24.290747 : malloc : 0x0000000125612a20: malloc(    80) -> 0x125612a20 RPRecordingManager.NSObject.isa
replayd : 2015-12-14 19:33:24.305204 : mem : 
0x125612a20: 0x0000a5a1000e112d
0x125612a28: 0x0000000000000001
0x125612a30: 0x000000012562d6c0
0x125612a38: 0x000000012560ac50
0x125612a40: 0x000000012560e8c0
0x125612a48: 0x0000000125612520
0x125612a50: 0x0000000125607080
0x125612a58: 0x00000001256378b0
0x125612a60: 0x000000012562def0
0x125612a68: 0x0000000000000000
replayd : 2015-12-14 19:33:24.308194 : SEL :0x1000d9c0b: "setMicrophoneRecording:"
```
